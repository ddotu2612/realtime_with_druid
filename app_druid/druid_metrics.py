import requests

# Set up the base URL for the Druid Coordinator API
base_url = 'http://<druid_coordinator_host>:<druid_coordinator_port>/druid/v1/'

# Define the ingestion metrics endpoint
ingestion_metrics_endpoint = 'metrics/v1/ingest'

# Define the query metrics endpoint
query_metrics_endpoint = 'metrics/v1/query'

# Define the time range for the metrics
from_time = '2023-01-01T00:00:00Z'
to_time = '2023-02-01T00:00:00Z'

# Build the full URL for the ingestion metrics endpoint
ingestion_metrics_url = base_url + ingestion_metrics_endpoint + '?from=' + from_time + '&to=' + to_time

# Send a GET request to the ingestion metrics endpoint
ingestion_metrics_response = requests.get(ingestion_metrics_url)

# Check if the response is successful
if ingestion_metrics_response.status_code == 200:
    # Print the ingestion metrics
    print(ingestion_metrics_response.json())
else:
    # Print the error message
    print('Error retrieving ingestion metrics: ' + ingestion_metrics_response.text)

# Build the full URL for the query metrics endpoint
query_metrics_url = base_url + query_metrics_endpoint + '?dataSource=<data_source>&interval=' + from_time + '/' + to_time

# Send a GET request to the query metrics endpoint
query_metrics_response = requests.get(query_metrics_url)

# Check if the response is successful
if query_metrics_response.status_code == 200:
    # Print the query metrics
    print(query_metrics_response.json())
else:
    # Print the error message
    print('Error retrieving query metrics: ' + query_metrics_response.text)
