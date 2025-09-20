"""
anchor.py - Call anchor(hash, ref) on an existing ProofOfProvenance contract.

Prereqs:
- .env with RPC_URL, PRIVATE_KEY, CONTRACT_ADDRESS
- ABI file: services/web3_anchor/ProofOfProvenance.abi.json

Usage example:
  python services/web3_anchor/anchor.py 16a69b60...0fce "local://demo_shipments.csv#v=hash-policy-1"
"""
import os, sys, json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

load_dotenv()

if len(sys.argv) < 3:
    print("Usage: python services/web3_anchor/anchor.py <hex_hash> <ref>")
    raise SystemExit(2)

HEX_HASH = sys.argv[1]
REF = sys.argv[2]

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

if not RPC_URL or not PRIVATE_KEY or not CONTRACT_ADDRESS:
    raise SystemExit("Set RPC_URL, PRIVATE_KEY, CONTRACT_ADDRESS in .env")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
acct = Account.from_key(PRIVATE_KEY)

abi_path = os.path.join(os.path.dirname(__file__), "ProofOfProvenance.abi.json")
abi = json.loads(open(abi_path, "r", encoding="utf-8").read())
contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=abi)

# Convert hash hex -> bytes32
if len(HEX_HASH) != 64:
    raise SystemExit("hex hash must be 64 hex chars (sha256)")
hash_bytes32 = bytes.fromhex(HEX_HASH)

tx = contract.functions.anchor(hash_bytes32, REF).build_transaction({
    "from": acct.address,
    "nonce": w3.eth.get_transaction_count(acct.address),
    "maxFeePerGas": w3.to_wei("2", "gwei"),
    "maxPriorityFeePerGas": w3.to_wei("1", "gwei"),
    "chainId": w3.eth.chain_id
})
signed = acct.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
print("Sent anchor tx:", tx_hash.hex())
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Mined in block:", receipt.blockNumber)
print("Gas used:", receipt.gasUsed)
