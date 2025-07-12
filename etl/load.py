import pandas as pd
import logging
import os

# Configure Logging
logger = logging.getLogger(__name__)

def load(data, conn=None):
  """
  Loads the transformed data to a CSV file and to a Database file.
  """

  try:
    os.makedirs('data/processed', exist_ok=True)

    data.to_csv('data/processed/superstore_processed.csv', index=False)

    if conn is not None:
      data.to_sql('superstore', conn, if_exists='replace', index=False)
  
  except Exception as e:
    logger.error(f"Error loading data.")
    logger.error(e)
    return None