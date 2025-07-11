import pandas as pd

def load(data):
  """
  Loads the transformed data to a CSV file.
  """

  try:
    data.to_csv('data/processed/superstore_transformed.csv', index=False)
  except Exception as e:
    print(f"Error loading data: {e}.")

    return None