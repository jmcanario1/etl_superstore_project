from etl import extract, transform, load

def main():
  extracted_data = extract('data/raw/superstore.csv')

  if extracted_data is not None:
    transformed_data = transform(extracted_data)

  if transformed_data is not None:
    load(transformed_data)



if __name__ == "__main__":
  main()