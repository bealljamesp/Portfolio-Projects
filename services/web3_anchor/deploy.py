"""
deploy.py - Deploy ProofOfProvenance.sol to a testnet (e.g., Sepolia).

Prereqs:
- .env with RPC_URL and PRIVATE_KEY set (see .env.example)
- Contract compiled to bytecode (this script includes a minimal placeholder and expects you to paste bytecode)

NOTE: For learning purposes, you can skip deploy and use an existing address + ABI with anchor.py.
"""
import os, json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if not RPC_URL or not PRIVATE_KEY:
    raise SystemExit("Set RPC_URL and PRIVATE_KEY in .env")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
acct = Account.from_key(PRIVATE_KEY)

# Load ABI
abi_path = os.path.join(os.path.dirname(__file__), "ProofOfProvenance.abi.json")
abi = json.loads(open(abi_path, "r", encoding="utf-8").read())

# !!! You must compile the Solidity contract and paste the 'bytecode' string here or load from file.
BYTECODE = "0x"  # placeholder

if BYTECODE == "0x":
    raise SystemExit("Please compile ProofOfProvenance.sol and paste BYTECODE before deploying.")

contract = w3.eth.contract(abi=abi, bytecode=BYTECODE)
tx = contract.constructor().build_transaction({
    "from": acct.address,
    "nonce": w3.eth.get_transaction_count(acct.address),
    "maxFeePerGas": w3.to_wei("2", "gwei"),
    "maxPriorityFeePerGas": w3.to_wei("1", "gwei"),
    "chainId": w3.eth.chain_id
})
signed = acct.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
print("Deploying... tx:", tx_hash.hex())
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed at:", receipt.contractAddress)
