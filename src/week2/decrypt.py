from Crypto.Cipher import AES
from Crypto.Util import Counter


'''

Decrypted Messages:

1: Basic CBC mode encryption needs padding.\x08\x08\x08\x08\x08\x08\x08\x08
2: Our implementation uses rand. IV\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10
3: CTR mode lets you build a stream cipher from a block cipher.
4: Always avoid the two time pad!

'''
def main():
    print
    print  "AES Demo"
    print


    key_1         = "140b41b22a29beb4061bda66b6747e14".decode('hex')
    cypher_text_1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode('hex')
    cypher_text_2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253".decode('hex')

    print AES.new(key_1, AES.MODE_CBC, cypher_text_1[:16]).decrypt(cypher_text_1[16:])
    print AES.new(key_1, AES.MODE_CBC, cypher_text_2[:16]).decrypt(cypher_text_2[16:])
    print


    key_2         = "36f18357be4dbd77f050515c73fcf9f2".decode('hex')
    cypher_text_3 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329".decode('hex')
    cypher_text_4 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451".decode('hex')

    counter_1 = Counter.new(128, initial_value = long(cypher_text_3[:16].encode('hex'), 16))
    counter_2 = Counter.new(128, initial_value = long(cypher_text_4[:16].encode('hex'), 16))

    print AES.new(key_2, AES.MODE_CTR, counter = counter_1).decrypt(cypher_text_3[16:])
    print AES.new(key_2, AES.MODE_CTR, counter = counter_2).decrypt(cypher_text_4[16:])
    print


if __name__ == "__main__":
    main()
