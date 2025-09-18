# crypto-intel-mapper
FastAPI backend for Crypto Intel Mapper — fetches and displays the latest Ethereum wallet transactions using the Etherscan API. Simple, efficient, and perfect for blockchain analysis and investigation projects. Requires an Etherscan API key.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Crypto Intel Mapper - Backend

This is the backend API service for the Crypto Intel Mapper project, built with FastAPI.  
It allows tracking Ethereum wallet transactions using the Etherscan API.

## Features

- Ping endpoint to check service status
- Retrieve recent transactions of an Ethereum wallet
- Formats transaction timestamps for readability

## Prerequisites

- Python 3.9+
- Etherscan API key (free to generate at [https://etherscan.io/apis](https://etherscan.io/apis))

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/crypto-intel-mapper-backend.git
cd crypto-intel-mapper-backend

2.Install dependencies:
pip install -r requirements.txt

3.Set your Etherscan API key in app.py:
ETHERSCAN_API_KEY = "YOUR_API_KEY_HERE"

Running the server
Start the FastAPI server with Uvicorn:
uvicorn app:app --reload
The API will be available at http://127.0.0.1:8000
.
Example:
curl http://127.0.0.1:8000/wallet/0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe
