#!/usr/bin/python3
import hashlib
import xml.etree.ElementTree as ET
import sys
from bitcoinlib.keys import Key


def sha256_string(s):
    m = hashlib.sha256()
    m.update(s.encode('ascii'))
    return m.hexdigest()


def sha256_file(fp):
    m = hashlib.sha256()
    while True:
        chunk = fp.read(4096)
        if len(chunk) == 0:
            break
        m.update(chunk)
    return m.hexdigest()


def tree_travesal(root, verify_hash=None):
    current_hash = root.attrib['value']

    if verify_hash is not None and root.attrib['type'] == 'hash':
        if verify_hash != current_hash:
            raise ValueError("Hash mismatch for the inputted hash" % (verify_hash, current_hash))

    childrens = [x for x in root]
    N = len(childrens)
    if N == 0:
        return current_hash
    elif N != 2:
        raise ValueError("proof file has a node with more than 2 children")
    else:
        left_child = childrens[0]
        right_child = childrens[1]

        if left_child.tag == 'right' and right_child.tag == 'left':
            # just in case
            (left_child, right_child) = (right_child, left_child)
        assert left_child.tag == 'left'
        assert right_child.tag == 'right'

        left_hash = tree_travesal(left_child, verify_hash)
        right_hash = tree_travesal(right_child, verify_hash)
        test_hash = sha256_string(left_hash + right_hash)
        if test_hash != current_hash:
            raise ValueError("Hash mismatch found in proof file" % (test_hash, current_hash))

    return current_hash


def private_key_to_bitcoin_address(priv_key):
    k = Key(priv_key, is_private=True)
    return k.address(compressed=False)


def main():
    if len(sys.argv) != 3:
        print("%s (proof file) (file or hash to verify)" % sys.argv[0])
    else:
        try:
            with open(sys.argv[2], "rb") as fp:
                verify_hash = sha256_file(fp)
        except FileNotFoundError:
            verify_hash = sys.argv[2].lower()
            if len(verify_hash) != 64:
                raise ValueError("hash length is not of 64 bytes. Please input the hash as hexdecimal string")
        else:
            assert len(verify_hash) == 64

        tree = ET.parse(sys.argv[1])
        priv_key = tree_travesal(tree.getroot(), verify_hash)
        addr = private_key_to_bitcoin_address(priv_key)
        print("All hashes are correct")
        print("Bitcoin address: %s" % addr)
        print("https://www.blockchain.com/btc/address/%s" % addr)


if __name__ == "__main__":
    main()
