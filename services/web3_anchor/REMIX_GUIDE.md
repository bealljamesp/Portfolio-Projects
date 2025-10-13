# Remix Compile Guide — ProofOfProvenance.sol

This guide shows how to compile `ProofOfProvenance.sol` in the browser and use the outputs with your scripts.

## 1) Open Remix
- Go to https://remix.ethereum.org
- In the **File Explorer**, create folders: `contracts/` and add your `ProofOfProvenance.sol` source (from `Blockchain/common/contracts/ProofOfProvenance.sol`).

## 2) Compile
- Click the **Solidity compiler** tab (left sidebar).
- Select a compatible compiler version (e.g., 0.8.x that matches your pragma).
- Press **Compile ProofOfProvenance.sol**.
- After success, open the compilation **artifacts**:
  - ABI: `artifacts/.../ProofOfProvenance.json` → copy the `"abi"` array and save as `services/web3_anchor/ProofOfProvenance.abi.json` (it already exists with a minimal ABI).
  - Bytecode: in the same JSON, copy the `"bytecode"` string.

## 3) Use with scripts
- **Deploy**: paste the bytecode into `services/web3_anchor/deploy.py` (the `BYTECODE = "0x..."` line), then:
  ```bash
  python services/web3_anchor/deploy.py
  ```
  Note the **contract address** printed at the end.
- **Anchor** using an existing contract:
  1) Put these in `services/web3_anchor/.env`:
     ```
     RPC_URL=https://sepolia.infura.io/v3/<your-project-id>
     PRIVATE_KEY=0x<your-test-wallet-private-key>
     CONTRACT_ADDRESS=0x<deployed-or-existing-address>
     ```
  2) Run:
     ```bash
     python services/web3_anchor/anchor.py <64-hex-hash> "local://Blockchain/common/notebooks/demo_shipments.csv#v=hash-policy-1"
     ```

## 4) Verify via API (on-chain mode)
- Start the API with on-chain mode:
  ```bash
  # PowerShell:
  $env:VERIFY_MODE="onchain"
  $env:RPC_URL="https://sepolia.infura.io/v3/<project-id>"
  $env:CONTRACT_ADDRESS="0x<contract>"
  python -m uvicorn services.verify_api.main:app --host 127.0.0.1 --port 8000
  ```
- Call verify:
  ```bash
  curl "http://127.0.0.1:8000/verify?hash=<64-hex>&ref=local://Blockchain/common/notebooks/demo_shipments.csv#v=hash-policy-1"
  ```
  Add `&strict=false` to ignore ref mismatches and only check existence.

**Security Note:** Never commit real private keys. Keep `.env` local and in `.gitignore`.
