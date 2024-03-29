import os
import subprocess
from os import getenv
from dotenv import load_dotenv

# Load the .env file
load_dotenv('python/.env')

# Get environment variables
clientId = os.getenv('clientId')
clientSecret = os.getenv('clientSecret')
resourceGroupName = os.getenv('resourceGroupName')
apimServiceName = os.getenv('apimServiceName')
tenantId = os.getenv('tenantId')
subscriptionId = os.getenv('subscriptionId')
product_id = os.getenv('PRODUCT_ID')
product_name = os.getenv('PRODUCT_NAME')

# Print the environment variables to debug
print(f"clientId: {clientId}")
print(f"clientSecret: {clientSecret}")
print(f"resourceGroupName: {resourceGroupName}")
print(f"apimServiceName: {apimServiceName}")
print(f"tenantId: {tenantId}")
print(f"subscriptionId: {subscriptionId}")
print(f"product_id: {product_id}")
print(f"product_name: {product_name}")

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