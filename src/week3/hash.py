import os.path

from Crypto.Hash import SHA256


FILE_1      = os.path.join(os.path.dirname(__file__), '../../tests/data/6 - 2 - Generic birthday attack (16 min).mp4')
FILE_1_URL  = "https://class.coursera.org/crypto-010/lecture/download.mp4?lecture_id=28"
FILE_1_HASH = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"

FILE_2      = os.path.join(os.path.dirname(__file__), '../../tests/data/6 - 1 - Introduction (11 min).mp4')
FILE_2_URL  = "https://class.coursera.org/crypto-010/lecture/download.mp4?lecture_id=27"
FILE_2_HASH = "5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949"


def read_blocks(file, block_size = 1024):
    while True:
        block = file.read(block_size)
        if not block:
            break
        yield block


def calculate_hash(blocks):
    current = 0
    for block in blocks:
        sha256 = SHA256.new()
        if current != 0:
            sha256.update(block + current)
        else:
            sha256.update(block)
        current = sha256.hexdigest().decode('hex')
    return current.encode('hex')


def main():
    file_1      = open(FILE_1, 'rb')
    file_1_hash = calculate_hash(reversed([block for block in read_blocks(file_1)]))

    print
    print "Expected Hash: ", FILE_1_HASH
    print "  Actual Hash: ", file_1_hash
    print "   Successful: ", FILE_1_HASH == file_1_hash

    file_2      = open(FILE_2, 'rb')
    file_2_hash = calculate_hash(reversed([block for block in read_blocks(file_2)]))

    print
    print "Expected Hash: ", FILE_2_HASH
    print "  Actual Hash: ", file_2_hash
    print "   Successful: ", FILE_2_HASH == file_2_hash



if __name__ == "__main__":
    main()
