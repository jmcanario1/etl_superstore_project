import logging
import os
import sqlite3
from etl import extract, transform, load

# Configure Logging
logger = logging.getLogger(__name__)

# Configure Database Connection
conn = sqlite3.connect('data/processed/elt_superstore.db')

def main():
  # Setting up logging to file
  logging.basicConfig(
    filename='log/etl_pipeline.log',
    level=logging.INFO,
    format='[%(asctime)s] - %(name)s - %(levelname)s: %(message)s'
  )

  logger.info('Started ETL Pipeline')

  extracted_data = extract('data/raw/superstore.csv')

  if extracted_data is not None:
    logger.info('Extraction complete')
    transformed_data = transform(extracted_data)

  if transformed_data is not None:
    logger.info('Transformation complete')
    load(transformed_data, conn)

  if os.path.exists('data/processed/superstore_processed.csv'):
    logger.info('Loading complete')

if __name__ == "__main__":
  main()