import hashlib

def hash_file(filepath, algorithm="sha256", chunk_size=4096):
    hasher = hashlib.new(algorithm)

    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)

    return hasher.hexdigest()