# Multithreading-API-RequestsMultithreading-API-Requests

This Python script is designed to fetch product data from a dummy API endpoint and save the retrieved data into a JSON file.

Prerequisites
Python 3.x
Requests library (can be installed via pip install requests)

How to Use
Clone or download the script to your local machine.
Ensure you have Python installed on your system.
Install the Requests library if you haven't already (pip install requests).
Run the script using Python: python main.py.

Description
The script performs the following steps:

1. Defines a function fetch_product_data(productId) to fetch product data from the API endpoint. It takes a product ID as input and returns the JSON response if successful, otherwise returns None.

2. Defines the main() function to orchestrate the fetching process.It sets the number of products to fetch and the name of the output JSON file.
Utilizes ThreadPoolExecutor to concurrently fetch data for multiple products. Writes the fetched data to a JSON file named Data.json.
3. Executes the main() function to start the fetching process.

Notes
The fetch_product_data() function fetches data for a single product using a dummy API endpoint.
Concurrent fetching is achieved using ThreadPoolExecutor to improve efficiency.
The fetched data is saved to a JSON file named Data.json in the current directory.
Status updates are printed to the console during the execution of the script.
 >>>Gvantsa
