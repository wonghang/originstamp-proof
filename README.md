# originstamp-proof

It is a repository of storing the [OriginStamp](https://originstamp.com/) SHA256 hash and corresponding proof files of some of my important documents and source codes. There is also a python code `originstamp-proof-to-address.py` to **compute everything independent of OriginStamp**. Just in case OriginStamp goes bankrupt or disappears, a backup of all Bitcoin-transactions  (and other cryptocurrency transactions) should be available somewhere on the Internet to prove the timestamp.

I want to prove to the world that such documents and source codes **exist before a specific date**. The reason for the proof is a complex legal and personal matter which I will not disclose now.

# What is OriginStamp?

OriginStamp is a service provided by a Switzerland company to create a [trusted timestamping](https://en.wikipedia.org/wiki/Trusted_timestamping) service. It works by computing a SHA256 hash of a file and then use [Merkle Tree](https://en.wikipedia.org/wiki/Merkle_tree) to include it in a cryptocurrency transaction. Because compromising a blockchain-based ledger system is virtually impossible. The cryptocurrency transaction acts as a tamper-proof timestamp.  For the technical details on computing the hash and the final bitcoin address, please refer to the guide provided by OriginStamp [here](https://docs.originstamp.com/guide/originstamp.html#preparation-of-digital-content) or the file `originstamp-proof-to-address.py`.

Please note that OriginStamp supports several cryptocurrencies, and I only implemented Bitcoin in `originstamp-proof-to-address.py`. Other cryptocurrency-proof files are in the subdirectories.

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

Unless **an unwanted event** happens, the original documents and the source codes will not be available to the public. Only their SHA256 (and proof files) are open.
But, as an example to show what is going on, the file `originstamp-proof-to-address.py` itself is timestamped as an example:

```
$ python3 originstamp-proof-to-address.py originstamp-proof-to-address.py.xml originstamp-proof-to-address.py
All hashes are correct
Bitcoin address: 1CPjACYh4ZfK4rQNM9PRCS8GJdHKXX2QG7
https://www.blockchain.com/btc/address/1CPjACYh4ZfK4rQNM9PRCS8GJdHKXX2QG7
$ 
```

If I release those files to the public, one can compute all the hashes and Bitcoin addresses using a bash script as follow:

```bash
for i in /path/to/those/files/*
do
  python3 originstamp-proof-to-address.py $(echo $i | sed 's/^.*\/\(.*\)$/\1/').xml $i
done
```

and you should see the following output:

```
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
All hashes are correct
Bitcoin address: 139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU
```

The code `originstamp-proof-to-address.py` is open source here, therefore the integrity of my code is self-evident. One can also check the integrity from [OriginStamp](https://originstamp.com/).

# What are the files?

## SHA256 hash

| File | SHA256 hash | Bitcoin address
| --- | --- |  --- |
| originstamp-proof-to-address.py | 68f5f784c76a6caaa236acfa7ec68fc7efa046a28dc82e8cd6acd5b0a04d80cd | [1CPjACYh4ZfK4rQNM9PRCS8GJdHKXX2QG7](https://www.blockchain.com/btc/address/1CPjACYh4ZfK4rQNM9PRCS8GJdHKXX2QG7) |
| 0cc7adf.py | 0cc7adf4e66ea431326c62320548efa688a28e252f1d1907fedab419179f3b57 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 3a9582b.cu | 3a9582b71f8d55aafe351bdaa75f162b1f26a0186f2d921d53da0d45a7ff8c26 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 4fa1122.bib | 4fa1122cf54e3adccc3116dde49604f764c4ccc192aecec2eee3b918245d0955 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 5f4c789.mp4 | 5f4c7899f10da078f70b9766bd95f17def41b52d3a1a5983eb25ad888c4a798a | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 6b74576.cu | 6b74576399d0c4783cf01ec1141511989583a9d5882474fa0879ffd742e92432 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 7d79fa7.py | 7d79fa7dea881f242dcc651b82806b88ba14d7a57ffe32c54069442c0d097842 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 9b6702b.py | 9b6702b36d843231b51488e919fac0549298521b926a3e3cbcbf65c2ccb3e7da | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 11e6bf3.cu | 11e6bf3132f146d4486aa5e9f48ac0071d4b4e42fc2f5a8c55764123935a4cd0 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 15bee49.cu | 15bee49c1c7cbb895c8b05c22e5349113bea7fded0121539dc3a3d140f3ac97f | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 022a805.tex | 022a80562714d28a11ad5403bca48c3d64217fa04d82a68128c5fa381d69d1c5 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 724fc30.cu | 724fc30f2df7aee30afbe3efb6f69aee9ff978560ad0333a2e36c5f7f14195bb | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 02418a7.py | 02418a7ca35a944e616baace0c8e924b690205cfee225677f865a4c86cd7cd27 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 7708f54.py | 7708f548486c5b041f2ab4e63d29bdc795cb3af67fbc0fce135ec25ef39fc28d | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 53471f7.mp4 | 53471f756aef98650d5f5a2da09624a435345881a9719340d434f2cff03f0b30 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 053801b.patch | 053801b07c1c522f952be9229e539539d83392de598f7110e15894af308333f4 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| 5787759.cu | 5787759c55c59c89bb49caaa6e4bd1e6e948e26e88576d61b819b1ed08031e52 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| a7d1f16.bash | a7d1f1622a253a6ce81956556d4c6c5825da3c6174c56e85d776c01aa45e59c2 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| a150d4d.cu | a150d4d8606c9e23d0c3a92dbfac74ab551e41c9a585a0a4af5820743d4ed5f4 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| a17601c.cu | a17601c458859834e187e51fb928b0dd8cb1ff4a93d16d59a70ece043019427a | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| b98e226.py | b98e22663b3874b0bc3a720f7557585ec55a7ec25c60e233b3804e3154ddb96c | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| ca62966.cu | ca62966c78799830abcda14744899bbae0095727422379aca776a2143246261c | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| d11805c.mp4 | d11805c0275a8a425a1ac7456c3af2ed5b6919b660bb9dfe6b6be95635702181 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| da8f3f5.mp4 | da8f3f584f3f4b557b9979b9fefe2a33fdb5f345fcf74f6cd7d8fa617c537d84 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| dd86049.cu | dd8604920e88bd593bd8530112410ee5773c51127f77ccab504b9df69bcbca02 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| ea8ad56.cu | ea8ad56f87e6add24deb449f1dfd00c1298ca387cb532b5ce85be9f5f185d542 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| ee6c712.py | ee6c712cf206a12b1ddfeec3fadc1630712e4031fbce7c2a1f53db978860d7d2 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| f48ba61.py | f48ba619802dcdca0beefa0d662e459127a891cc83d8a9d8fb73fddc60983312 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| f335444.cu | f3354445f7e66ca2aa4352d55245ab0bca0c94cce6e4d8a5d988c0b2a99a20b0 | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| original-name.txt | 74d9144c88500436ce48b1229da42143b969f85fa35f8c7ccc7d9419c243652c | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |
| trunk-11337.tar.gz | e01bfd0d1c80b0a82b05878b39146401385f0984a246a81f039641f18475575e | [139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU](https://www.blockchain.com/btc/address/139DGkJExFW29LAmG1MjyNuuAyMQD2BRTU) |


## Corresponding Transaction (Bitcoin only)

| File | Transaction | Timestamp (UTC) |
| --- | --- | --- | 
| originstamp-proof-to-address.py | [9665d28ab70f9d9b75bcb014348331b44c907c91a225f316205d390b1890ff3e](https://www.blockchain.com/btc/tx/9665d28ab70f9d9b75bcb014348331b44c907c91a225f316205d390b1890ff3e) | 2020-03-18 00:00  |
| 0cc7adf.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 3a9582b.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 4fa1122.bib | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 5f4c789.mp4 | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 6b74576.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 7d79fa7.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 9b6702b.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 11e6bf3.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 15bee49.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 022a805.tex | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 724fc30.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 02418a7.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 7708f54.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 53471f7.mp4 | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 053801b.patch | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| 5787759.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| a7d1f16.bash | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| a150d4d.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| a17601c.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| b98e226.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| ca62966.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| d11805c.mp4 | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| da8f3f5.mp4 | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| dd86049.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| ea8ad56.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| ee6c712.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| f48ba61.py | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| f335444.cu | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| original-name.txt | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
| trunk-11337.tar.gz | [2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9](https://www.blockchain.com/btc/tx/2f26f595fab74519c94fb4044f7fe036c9bf2eac5b655f70f89e23e435e106c9) | 2020-04-01 00:00 |
