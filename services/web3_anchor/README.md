# web3.py Anchor Scripts

Two scripts to interact with the ProofOfProvenance contract on a testnet.

## Files
- `ProofOfProvenance.abi.json` – minimal ABI for anchor/getters.
- `deploy.py` – deploy the contract (requires compiled bytecode).
- `anchor.py` – call `anchor(bytes32 hash, string ref)` on an existing contract.

## Setup
1. Create `.env` in this folder using `.env.example`:
   ```
   RPC_URL=https://sepolia.infura.io/v3/<your-project-id>
   PRIVATE_KEY=0x<your-private-key>
   CONTRACT_ADDRESS=0x<existing-contract-address>   # if you skip deploy
   ```
2. Install deps (already in your env): `web3`, `eth-account`, `python-dotenv`.

## Use
- Deploy (optional): compile Solidity, paste BYTECODE in `deploy.py`, then run:
  ```bash
  python services/web3_anchor/deploy.py
  ```
- Anchor a dataset hash:
  ```bash
  python services/web3_anchor/anchor.py <hex_hash> "local://demo_shipments.csv#v=hash-policy-1"
  ```

**Security:** never commit real PRIVATE_KEY. Use `.env` only locally.
