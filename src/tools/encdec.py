from Crypto.Cipher import AES
from Crypto.Util import Counter


def aes_decrypt(key, cypher_text, counter_mode = False):
    if counter_mode:
        ctr = Counter.new(128, initial_value = long(cypher_text[:16].encode('hex'), 16))
        aes = AES.new(key, AES.MODE_CTR, counter = ctr)
    else:
        aes = AES.new(key, AES.MODE_CBC, cypher_text[:16])

    return aes.decrypt(cypher_text[16:])

