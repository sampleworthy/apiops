# apiops
# apim.py

The `apim.py` script is a Python program used for managing APIs in Azure API Management (APIM) service.

The script performs the following tasks:

1. **Environment Variables**: It retrieves necessary information from environment variables. This includes the client ID, client secret, resource group name, APIM service name, tenant ID, subscription ID, and other Azure-related details.

2. **API Specifications**: It locates the directory containing the API specifications (in this case, a directory named 'apis') and identifies all `.yaml `, `json` files within it. These files are assumed to be OpenAPI specification files for the APIs to be imported.

3. **API Import**: For each API specification file found, the script constructs and executes a command to import the API into the APIM service. This is done using the Azure CLI (`az` command). The API's name, path, type, ID, display name, protocols, specification format, and specification path are all set during this import process.

4. **Product Association**: After each API is imported, the script adds the API to a specified product in the APIM service. The product is identified by its ID, which should be replaced in the script with the actual product ID.

The script is designed to be run from a command line and requires the Azure CLI to be installed and configured with appropriate access permissions. It also requires that the APIM service and the product already exist in the Azure subscription.