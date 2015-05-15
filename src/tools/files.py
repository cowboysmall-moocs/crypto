

def read_lines(file_path):
    lines = []

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)

    return lines


def read_blocks(file_path, block_size = 1024):
    blocks = []

    with open(file_path) as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            blocks.append(block)

    return blocks


