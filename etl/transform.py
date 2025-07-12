import pandas as pd
import logging

# Configure Logging
logger = logging.getLogger(__name__)

def transform(data):
  """
  Transforms the extracted data.
  Creates new dataframes with additional data.
  """

  if data.isnull().values.any():
    logger.warning("Data contains null values. Dropping rows with nulls.")

    rows_before = len(data)
    data = data.dropna()
    rows_after = len(data)

    logger.warning(F"Rows dropped: {rows_before - rows_after}.")

  try:
    data.loc[:, 'Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    data.loc[:, 'Ship Date'] = pd.to_datetime(data['Ship Date'], errors='coerce')

    data = data[data['Order Date'] < data['Ship Date']].copy()

    data.loc[:, 'Shipping Time'] = data['Ship Date'] - data['Order Date']

    data.loc[:, 'Profit'] = round(data['Profit'], 2)

    data.loc[:, 'Profit Level'] = ((data['Profit']/data['Sales'])*100).apply(
      lambda x: 'High' if x > 20 else 'Medium' if x > 10 else 'Low' if x >= 0 else 'Negative'
    )

  except Exception as e:
    logger.error(f"Error transforming data.")
    logger.error(e)
    return None

  return data