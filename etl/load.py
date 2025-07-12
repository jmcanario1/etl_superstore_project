import pandas as pd
import logging

# Configure Logging
logger = logging.getLogger(__name__)

def load(data):
  """
  Loads the transformed data to a CSV file.
  """

  try:
    data.to_csv('data/processed/superstore_transformed.csv', index=False)
  
  except Exception as e:
    logger.error(f"Error loading data.")
    logger.error(e)
    return None