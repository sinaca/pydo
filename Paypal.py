
import paypalrestsdk
from paypalrestsdk import Payment

# Set your PayPal credentials
paypalrestsdk.configure({
  "mode": "sandbox",  # Change to "live" for production
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
})

# Create a payment
payment = Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "paypal"
  },
  "redirect_urls": {
    "return_url": "YOUR_RETURN_URL",
    "cancel_url": "YOUR_CANCEL_URL"
  },
  "transactions": [{
    "item_list": {
      "items": [{
        "name": "Item Name",
        "sku": "Item SKU",
        "price": "10.00",
        "currency": "USD",
        "quantity": 1
      }]
    },
    "amount": {
      "total": "10.00",
      "currency": "USD"
    },
    "description": "Payment for Item Name"
  }]
})

# Create payment and return the approval_url
if payment.create():
  for link in payment.links:
    if link.method == "REDIRECT":
      redirect_url = link.href
      print("Redirect for approval: {}".format(redirect_url))
else:
  print("Error while creating payment:", payment.error)
