from solana.rpc.api import Client
from solders.keypair import Keypair
import requests
import json

# Convert your HEX format private key to bytes
# Replace 'YOUR_HEX_PRIVATE_KEY_HERE' with your actual HEX private key
hex_private_key = 'your_wallet_private_key_HEX'
secret_key = bytes.fromhex(hex_private_key)

# Initialize the Keypair with the secret key
owner = Keypair.from_bytes(secret_key)

# Connect to the Solana devnet for testing
client = Client("https://api.devnet.solana.com")

# Token mint addresses
SOL_MINT = "So11111111111111111111111111111111111111112"  # SOL
USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"  # USDC

# Swap configuration
amount = 0.01  # Amount of SOL to swap
slippage = 0.5  # Slippage tolerance in percentage

def swap_sol_to_usdc():
    try:
        # Compute the swap through Raydium's API
        response = requests.get(
            f"https://api.raydium.io/swap/compute?inputMint={SOL_MINT}&outputMint={USDC_MINT}&amount={int(amount * 1e9)}&slippage={slippage * 100}"
        )
        swap_data = json.loads(response.text)

        # Here we would normally construct and send a transaction, but since we're learning and don't have full transaction logic:
        print("This is where we would typically construct and send a transaction to Solana for the swap.")
        print(f"Swap details from Raydium API: {swap_data}")

        # For educational purposes, let's check the balance of our wallet
        # Corrected balance check
        balance_response = client.get_balance(owner.pubkey())
        balance = balance_response['result']['value']
        print(f"Your current SOL balance on devnet: {balance / 1e9} SOL")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    swap_sol_to_usdc()
