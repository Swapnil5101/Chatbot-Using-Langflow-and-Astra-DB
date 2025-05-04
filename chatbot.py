import requests

# NOTE: Replace '<Your Astra DB API key>' with actual API key

# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/f35bec75-e12b-4a0d-be84-dcd9cdf792d7/api/v1/run/80b253db-d1cd-424c-8ec6-fbe427225a5b"  

# Request payload configuration
payload = {
    "input_value": "hello world!",  # The input value to be processed by the flow
    "output_type": "chat",  # Specifies the expected output format
    "input_type": "chat"  # Specifies the input format
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "<Your Astra DB API key>"  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    