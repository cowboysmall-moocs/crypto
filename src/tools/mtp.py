from collections import defaultdict


def find_key(cypher_texts, key_length):
    hits = [defaultdict(int) for _ in range(key_length)]
    key  = [0] * key_length

    for i in range(len(cypher_texts) - 1):
        for j in range(i + 1, len(cypher_texts)):

            count = 0
            for (x, y) in zip(cypher_texts[i][:key_length], cypher_texts[j][:key_length]):

                result = x ^ y
                if result in range(65, 91) + range(97, 123):

                    temp_key = y ^ 32
                    hits[count][temp_key] += 1
                    if key[count] not in hits[count] or hits[count][key[count]] < hits[count][temp_key]:
                        key[count] = temp_key

                    temp_key = x ^ 32
                    hits[count][temp_key] += 1
                    if key[count] not in hits[count] or hits[count][key[count]] < hits[count][temp_key]:
                        key[count] = temp_key

                count += 1

    return key

