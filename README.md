```markdown
# 🔗 Solana Geyser gRPC Wallet Subscription (Python) 

It is written in **Python** and uses the official `.proto` files provided by GS Node to interact directly with Solana's `GeyserPlugin`.

---

## 🚀 Features

- ✅ Connects securely via gRPC using TLS (`secure_channel`)
- ✅ Subscribes to account-level updates for any wallet
- ✅ Uses auto-generated stubs from `.proto` files
- ✅ Fully configurable via CLI

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/Nerevaine/grpc-python.git
cd grpc-python
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Usage

### ✅ Check gRPC Connection

```bash
python slot.py \
  --rpc-fqdn "rpc" \
  --x-token ""
```

> Should return something like: `slot: 333889597`

---

### 📡 Subscribe to Wallet

```bash
python subscribe_wallet.py \
  --endpoint "rpc" \
  --wallet-pubkey "66ZC9U8y1uYaAxt4...Zohvi8ev6wBHsAxykh"
```

You will receive logs on the terminal when that wallet changes.

