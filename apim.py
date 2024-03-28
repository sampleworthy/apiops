import os
import subprocess
import sys
from os import getenv

# ENV VARS come from the pipeline
clientId = getenv('clientId')
clientSecret = getenv('clientSecret')
resourceGroupName = getenv('resourceGroupName')
apimServiceName = getenv('apimServiceName')
tenantId = getenv('tenantId')
subscriptionId = getenv('subscriptionId')
resource = "https://management.azure.com/.default"
azureApiVersion = "2021-08-01"
baseUrl = f"https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{apimServiceName}"

# Get the directory containing the API specifications
api_dir = 'apis'

# Get a list of all .yaml and .json files in the directory
api_files = [f for f in os.listdir(api_dir) if f.endswith('.yaml') or f.endswith('.json')]

# If no API files were found, exit the script
if not api_files:
    print("Didn't find any spec files, exiting")
    sys.exit(1)

# Loop over each API file
for api_file in api_files:
    # Construct the full path to the API file
    api_path = os.path.join(api_dir, api_file)

    # Extract the base name of the API file (without the .yaml extension)
    api_name = os.path.splitext(api_file)[0]

    # Construct the command to import the API into APIM
    command = [
        'az', 'apim', 'api', 'import',
        '--resource-group', resourceGroupName,
        '--service-name', apimServiceName,
        '--path', api_name,
        '--api-type', 'http',
        '--api-id', api_name,
        '--display-name', api_name,
        '--protocols', 'https',
        '--specification-format', 'OpenApi',
        '--specification-path', api_path,
    ]

    # Run the command
    subprocess.run(command, check=True)

    # Specify the product ID
    product_id = 'test-product'  # Replace with your actual product ID

    # Construct the command to add the API to the product
    command = [
        'az', 'apim', 'product', 'api', 'add',
        '--resource-group', resourceGroupName,
        '--service-name', apimServiceName,
        '--product-id', product_id,
        '--api-id', api_name,
    ]

    # Run the command
    subprocess.run(command, check=True)