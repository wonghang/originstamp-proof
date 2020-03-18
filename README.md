# originstamp-proof

It is a repository of storing the [OriginStamp](https://originstamp.com/) SHA256 hash and corresponding proof files of some of my important documents and source codes. There is also a python code `originstamp-proof-to-address.py` to **compute everything independent of OriginStamp**. Just in case OriginStamp goes bankrupt or disappears, a backup of all Bitcoin-transactions  (and other cryptocurrency transactions) should be available somewhere on the Internet to prove the timestamp.

I want to prove to the world that such documents and source codes **exist before a specific date**. The reason for the proof is a complex legal and personal matters which I will not disclose unless a tragic event happens.

# What is OriginStamp?

OriginStamp is a service provided by a Switzerland company to create a [trusted timestamping](https://en.wikipedia.org/wiki/Trusted_timestamping) service. It works by computing a SHA256 hash of a file, and then include it in a cryptocurrency transaction. Because compromising a blockchain-based ledger system is difficult. The cryptocurrency transaction acts as a tamper-proof timestamp.  For the technical details on how to compute the the hash and the final bitcoin address, please refer to the guide provided by OriginStamp [here](https://docs.originstamp.com/guide/originstamp.html#preparation-of-digital-content) or the file `originstamp-proof-to-address.py`.

Please note that OriginStamp supports several cryptocurrency and I only implemented Bitcoin in `originstamp-proof-to-address.py`. Other cryptocurrency proof file are in the subdirectories.

# Requirements

The python code requires [bitcoinlib](https://pypi.org/project/bitcoinlib/).

```
$ pip3 install -r requirements.txt
```

# Usage

The basic usage is

```
$ python3 originstamp-proof-to-address.py (proof file) (file or hash to verify)
```

Unless a tragic event happen, the original documents and the source codes will not be available to the public. Only their SHA256 are open.
But, as an example to show what it is going on, the file `originstamp-proof-to-address.py` itself is timestamped as an example:

```
$ python3 originstamp-proof-to-address.py originstamp-proof-to-address.py.xml originstamp-proof-to-address.py
All hashes are correct
Bitcoin address: 1CPjACYh4ZfK4rQNM9PRCS8GJdHKXX2QG7
https://www.blockchain.com/btc/address/1CPjACYh4ZfK4rQNM9PRCS8GJdHKXX2QG7
$ 
```

# What are the files?

## SHA256 hash

| File | SHA256 hash | Bitcoin address
| --- | --- |  --- |
| originstamp-proof-to-address.py | 68f5f784c76a6caaa236acfa7ec68fc7efa046a28dc82e8cd6acd5b0a04d80cd | 1CPjACYh4ZfK4rQNM9PRCS8GJdHKXX2QG7 |

## Corresponding Transaction (Bitcoin only)

| File | Transaction | Timestamp (UTC) |
| --- | --- | --- | 
| originstamp-proof-to-address.py | [9665d28ab70f9d9b75bcb014348331b44c907c91a225f316205d390b1890ff3e](https://www.blockchain.com/btc/tx/9665d28ab70f9d9b75bcb014348331b44c907c91a225f316205d390b1890ff3e) | 2020-03-18 00:00  |
