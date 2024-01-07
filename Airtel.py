
import requests

# Replace these values with your Airtel developer credentials
client_id = "your_client_id"
client_secret = "your_client_secret"
callback_url = "your_callback_url"

# Airtel Money API endpoint for payment initiation
endpoint = "https://api-sandbox.airtel.in/merchant/v1/payments"

# Replace these values with your specific payment details
amount = "10.00"
currency = "INR"
msisdn = "recipient_phone_number"

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {base64_encoded_credentials}',  # base64 encoded "client_id:client_secret"
}

data = {
    'amount': amount,
    'currency': currency,
    'msisdn': msisdn,
    'callbackUrl': callback_url,
    'orderInfo': 'Payment for your order',
}

try:
    response = requests.post(endpoint, json=data, headers=headers)

    if response.status_code == 200:
        print("Payment initiated successfully")
        print(response.json())  # You may want to inspect the response for transaction details
    else:
        print(f"Failed to initiate payment. Response: {response.text}")

except Exception as e:
    print(f"Error: {str(e)}")
