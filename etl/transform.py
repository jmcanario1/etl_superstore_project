import pandas as pd

def transform(data):
  """
  Transforms the extracted data.
  """

  if data.isnull().values.any():
    data = data.dropna()

  try:
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    data['Ship Date'] = pd.to_datetime(data['Ship Date'], errors='coerce')

    data = data[data['Order Date'] < data['Ship Date']].copy()

    data['Shipping Time'] = data['Ship Date'] - data['Order Date']

    data['Profit'] = round(data['Profit'], 2)

    data['Profit Level'] = ((data['Profit']/data['Sales'])*100).apply(
      lambda x: 'High' if x > 20 else 'Medium' if x > 10 else 'Low' if x >= 0 else 'Negative'
    )



  except Exception as e:
    print(f"Error transforming data: {e}.")
    return None

  return data