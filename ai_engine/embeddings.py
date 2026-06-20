from hashlib import md5

def create_embedding(text):

    hash_value = md5(
        text.encode()
    ).hexdigest()

    embedding = [
        ord(char) % 10
        for char in hash_value[:64]
    ]

    return embedding