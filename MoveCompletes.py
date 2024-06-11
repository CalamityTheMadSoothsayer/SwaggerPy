import requests # pip install requests
from MCjson import Payload # takes InventoryType, Barcode and LocationId
from colors import Color

def doMoveComplete(api_url, payload):
    try:
        # Send the POST request to the API
        response = requests.post(api_url, json=payload, verify=False)

        # Check status of the request
        if 200 <= response.status_code < 300:
            # Notify user of successful post
            return True, response.status_code, response.text
        else:
            return False, response.status_code, response.text
    except Exception as e:
        # Notify user of error
        return False, 0, str(e), ''
    
if __name__ == "__main__":
    print(Color.RED, "DO NOT RUN THIS SCRIPT DIRECTLY.", Color.RESET)