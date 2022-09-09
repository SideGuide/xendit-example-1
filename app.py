from xendit import Xendit, Balance, BalanceAccountType

# This is a test api key
api_key = "xnd_development_P4qDfOss0OCpl8RtKrROHjaQYNCk9dN5lSfk+R1l9Wbe+rSiCwZ3jw=="

# Create the xendit instance utilizing the api key
xendit_instance = Xendit(api_key=api_key)
# Get the Invoice object from instance
Invoice = xendit_instance.Invoice

# Create a new invoice
invoice = Invoice.create(
    external_id="invoice-1593684000",
    amount=20000,
    payer_email="customer@domain.com",
    description="Invoice Demo #123",
)
print("Invoice created: {}".format(invoice))


