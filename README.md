# Wallet Link Checker

🧠 Check if two Ethereum-based wallets are linked by direct on-chain transactions.

This script uses the Etherscan Multichain API to fetch transactions from one wallet and filter those sent to another.

## Features
- Supports Base chain (Chain ID 8453)
- Easy to modify
- Works with any EVM-compatible chain via Etherscan's V2 API

## Requirements
- Python 3
- `requests` library

## Usage
Edit the `wallet1`, `wallet2`, and `api_key` in `check_link.py`, then run:

```bash
python check_link.py
