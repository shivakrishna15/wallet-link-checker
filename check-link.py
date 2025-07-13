import requests
from datetime import datetime

# === 🧾 User Inputs ===
wallet1 = "0xSenderAddressHere".lower()     # Replace with sender address
wallet2 = "0xRecipientAddressHere".lower()  # Replace with recipient address
api_key = "YourWorkingEtherscanKeyHere"     # Replace with your Etherscan multichain API key

# === 🌐 API Parameters ===
url = "https://api.etherscan.io/v2/api"
params = {
    "chainid": 8453,  # Base chain ID (change for other chains if needed)
    "module": "account",
    "action": "txlist",
    "address": wallet1,
    "startblock": 0,
    "endblock": 99999999,
    "sort": "asc",
    "apikey": api_key
}

# === 🚀 Fetch Transactions ===
print(f"📡 Fetching transactions from {wallet1} on Base network...")
resp = requests.get(url, params=params)
data = resp.json()

# === 🔍 Filter by recipient wallet2 ===
if data.get("status") == "1" and isinstance(data.get("result"), list):
    all_txs = data["result"]
    filtered = [tx for tx in all_txs if tx.get("to", "").lower() == wallet2]

    print(f"\n✅ Found {len(filtered)} transactions from {wallet1} → {wallet2}:\n")
    for tx in filtered:
        timestamp = datetime.utcfromtimestamp(int(tx["timeStamp"])).strftime('%Y-%m-%d %H:%M:%S UTC')
        print(f"🔗 TxHash:     {tx['hash']}")
        print(f"⛓️  Block:     {tx['blockNumber']} | Time: {timestamp}")
        print(f"💰 Value:     {int(tx['value']) / 1e18:.6f} ETH")
        print(f"⛽ Gas Used:  {tx['gasUsed']}\n")
else:
    print("❌ Error fetching transactions:")
    print(f"Message: {data.get('message')}")
    print(f"Details: {data.get('result')}")
