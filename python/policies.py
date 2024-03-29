import os
import subprocess
from os import getenv

# Get environment variables
resourceGroupName = os.getenv('resourceGroupName')
apimServiceName = os.getenv('apimServiceName')
product_id = os.getenv('product_id')

# Path to the policies.xml file
policy_file_path = './policies/policies.xml'

# Construct the command to update the product policy in APIM
command = [
    'az', 'apim', 'product', 'policy', 'update',
    '--resource-group', resourceGroupName,
    '--service-name', apimServiceName,
    '--product-id', product_id,
    '--xml-policy', policy_file_path,
    '--set', 'format=xml',
]

# Run the command
subprocess.run(command, check=True)