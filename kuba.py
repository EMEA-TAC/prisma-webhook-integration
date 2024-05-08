import requests
import json

# First, the creation part as you've previously done
create_url = "https://api2.eu.prismacloud.io/api/v1/tenant/1037390876936064000/integration"

create_payload = json.dumps({
    "description": "Test",
    "enabled": True,
    "integrationConfig": {
        "url": "https://webhook.site/a558c012-a538-4f35-b757-18ad66eac469",
        "authToken": "",
        "headers": [
            {"key": "Content-Type", "value": "application/json", "readOnly": True, "secure": False}
        ],
        "isCustomPayloadEnabled": False
    },
    "integrationType": "webhook",
    "name": "Kuba_automation_55"
})

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-redlock-auth': ''
}

response = requests.post(create_url, headers=headers, data=create_payload)
if response.status_code in [200, 201]:
    print("Integration created successfully.")
    print(response.text)
else:
    print(f"Failed to create integration. HTTP Status Code: {response.status_code}")
    print("Response:", response.text)

# Now, testing the integration
test_url = "https://api2.eu.prismacloud.io/api/v1/tenant/1037390876936064000/integration/test"

test_payload = create_payload  # Using the same payload for testing

test_response = requests.post(test_url, headers=headers, data=test_payload)
if test_response.status_code in [200, 201]:
    print("Integration test successful.")
    print(test_response.text)
else:
    print(f"Failed to test integration. HTTP Status Code: {test_response.status_code}")
    print("Response:", test_response.text)