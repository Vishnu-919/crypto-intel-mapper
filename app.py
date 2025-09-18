import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

ETHERSCAN_API_KEY = "Enter your API Key"

@app.get("/ping")
async def ping():
    return {"message": "Crypto Intel Mapper API is up!"}

@app.get("/wallet/{address}")
async def get_wallet_transaction(address: str):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    data = response.json()

    if data["status"] != "1":
        raise HTTPException(status_code=404, detail="Wallet not found or no transactions")

    transactions = data["result"]

    return {
        "address": address,
        "transaction_count": len(transactions),
        "transactions": [
            {
                "blockNumber": tx["blockNumber"],
                "timeStamp": tx["timeStamp"],
                "hash": tx["hash"],
                "from": tx["from"],
                "to": tx["to"],
                "value": tx["value"],
                "gas": tx["gas"],
                "isError": tx["isError"]
            }
            for tx in transactions[:10]
        ]
    }
