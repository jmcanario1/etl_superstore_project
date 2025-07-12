import pandas as pd
import logging

# Configure Logging
logger = logging.getLogger(__name__)

def extract(file_path):
  """
  Extracts data from a CSV file.
  """

  try:
    dataframe = pd.read_csv(file_path, encoding='ISO-8859-1')
    return dataframe
  
  except Exception as e:
    logger.error(f"Error extracting data from {file_path}.")
    logger.error(e)
    return None

