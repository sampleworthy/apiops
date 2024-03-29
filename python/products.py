import os
import subprocess
from os import getenv, getcwd
from dotenv import load_dotenv


# Check if the script is run inside a folder named 'python'
if '/python' not in os.getcwd():
    raise Exception("This script must be run inside a folder named 'python'")

# Load the .env file
load_dotenv('python/.env')

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

# Get the product ID and product name from the .env file
product_id = getenv('PRODUCT_ID')
product_name = getenv('PRODUCT_NAME')

# Construct the command to create the product in APIM
command = [
    'az', 'apim', 'product', 'create',
    '--resource-group', resourceGroupName,
    '--service-name', apimServiceName,
    '--product-id', product_id,
    '--product-name', product_name,
]

# Run the command
subprocess.run(command, check=True)