import os
import subprocess
from os import getenv

# Get environment variables
resourceGroupName = os.getenv('resourceGroupName')
apimServiceName = os.getenv('apimServiceName')
product_id = os.getenv('product_id')

# Path to the policies.xml file
policy_file_path = './policies/policies.xml'

# Construct the command to create the product policy in APIM
command = [
    'az', 'apim', 'product', 'policy', 'create',
    '--resource-group', resourceGroupName,
    '--service-name', apimServiceName,
    '--product-id', product_id,
    '--xml-policy', policy_file_path,
]

# Run the command
subprocess.run(command, check=True)