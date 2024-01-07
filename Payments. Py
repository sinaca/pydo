
import requests

# Replace these values with your MTN developer credentials
api_key = "your_api_key"
subscription_key = "your_subscription_key"
callback_url = "your_callback_url"

# MTN Mobile Money API endpoint for payment initiation
endpoint = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"

# Replace these values with your specific payment details
amount = "10.00"
currency = "USD"
msisdn = "recipient_phone_number"

headers = {
    'Authorization': f'Bearer {api_key}',
    'X-Reference-Id': 'your_unique_reference_id',
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
}

data = {
    'amount': amount,
    'currency': currency,
    'externalId': 'your_external_id',
    'payer': {
        'partyIdType': 'MSISDN',
        'partyId': msisdn,
    },
    'payerMessage': 'Payment for your order',
    'payeeNote': 'Thank you for shopping with us',
}

try:
    response = requests.post(endpoint, json=data, headers=headers)

    if response.status_code == 202:
        print("Payment initiated successfully")
    else:
        print(f"Failed to initiate payment. Response: {response.text}")

except Exception as e:
    print(f"Error: {str(e)}")
