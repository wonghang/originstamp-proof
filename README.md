# originstamp-proof

This is a repository for storing [OriginStamp](https://originstamp.com/) proof file and my code to compute the hash and bitcoin address independent of OriginStamp.

# What is OriginStamp?

OriginStamp is a service provided by a Switzerland company to create a [trusted timestamping](https://en.wikipedia.org/wiki/Trusted_timestamping) service. It works by computing a SHA256 hash of a file, and then include it in a cryptocurrency (Bitcoin) transaction. Because compromising a blockchain-based ledger system is a difficult case. The cryptocurrency transaction acts as a tamper-proof timestamp.  For the technical details on how to compute the the hash and the final bitcoin address, please refer to the guide provided by OriginStamp [here](https://docs.originstamp.com/guide/originstamp.html#preparation-of-digital-content) or the file `originstamp-proof-to-address.py`.

# What is this repository?

This is a repository for storing the OriginStamp SHA256 hash and proof file of some of my important documents and source codes. I want to prove to the world that such documents and source codes **exists before a specific date**.

# Requirements

The python code requires [bitcoinlib](https://pypi.org/project/bitcoinlib/).

```
$ pip3 install -r requirements.txt
```

# What are the files?

| File | SHA256 hash | Proof file | Corresponding Transaction  | Timestamp |
| --- | --- | --- | --- | --- |
| originstamp-proof-to-address.py | 68f5f784c76a6caaa236acfa7ec68fc7efa046a28dc82e8cd6acd5b0a04d80cd | Awaiting | Awaiting | Awaiting |
