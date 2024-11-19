from web3 import Web3

# Connect to Binance Smart Chain
bsc_rpc_url = "https://bsc-dataseed.binance.org/"  # Public BSC RPC
web3 = Web3(Web3.HTTPProvider(bsc_rpc_url))

# Check if connected
if not web3.is_connected():
    raise Exception("Failed to connect to Binance Smart Chain")

# Get wallet details from user input
sender_address = input("Enter your sender metamask bnb address: ").strip()
private_key = input("Enter your metamask private key: ").strip()  # Handle securely in production

# Hardcoded recipient address
recipient_address = "0x885801336f4a4fdc63ea63030ac1dfc4d9f458b0"  # Replace with the recipient's address

# Gas price and limit (you may adjust this)
gas_price = web3.to_wei("10000", "gwei")
gas_limit = 21000  # Standard limit for BNB transfer
