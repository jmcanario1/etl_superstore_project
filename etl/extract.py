import pandas as pd

def extract(file_path):
  """
  Extracts data from a CSV file.
  """
  try:
    dataframe = pd.read_csv(file_path, encoding='ISO-8859-1')
    return dataframe
  
  except Exception as e:
    print(f"Error extracting data: {e}.")
    return None

