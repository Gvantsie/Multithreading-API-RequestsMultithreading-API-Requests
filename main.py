import requests
import json
from concurrent.futures import ThreadPoolExecutor


def fetch_product_data(product_id):
    url = f'https://dummyjson.com/products/{product_id}'
    print(f"Fetching data for product {product_id}...")
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Successfully fetched data for product {product_id}")
        return response.json()
    else:
        print(f"Failed to fetch data for product {product_id}. Status code: {response.status_code}")
        return None


def main():
    num_of_products = 100
    file_name = 'Data.json'

    print("Starting...")
    with ThreadPoolExecutor() as thread:
        results = list(thread.map(fetch_product_data, range(1, num_of_products + 1)))
    print("completed.")

    successful_results = []
    for response in results:
        if response is None:
            successful_results.append(response)

    file = open(file_name, 'w')
    file.write('[')
    for ind in range(0, len(successful_results)):
        json.dump(successful_results[ind], file)
        if ind != len(successful_results)-1:
            file.write(',\n')
    file.write(']')
    file.close()

    print(f"Everything fetched and saved to {file_name}")


main()
