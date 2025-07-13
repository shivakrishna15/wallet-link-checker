# Wallet Link Checker

[![Open In Colab] https://colab.research.google.com/drive/1xRA89L9gfuHJwR63ITzsb4sDrjc7Jkha?usp=sharing]

This notebook checks if two EVM wallets are directly linked by on-chain ETH transfers using the Etherscan V2 multichain API.

- Replace the wallet addresses and API key below.
- Click "Run" to fetch results.

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
