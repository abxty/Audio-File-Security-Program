import json
from hasher import hash_file

TRUSTED_HASH_DB = "trusted_hashes.json"

def load_trusted_hashes():
    try:
        with open(TRUSTED_HASH_DB, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_trusted_hashes(data):
    with open(TRUSTED_HASH_DB, "w") as f:
        json.dump(data, f, indent=4)

def register_trusted_file(filepath):
    trusted = load_trusted_hashes()
    file_hash = hash_file(filepath)
    trusted[filepath] = file_hash
    save_trusted_hashes(trusted)
    return file_hash

def verify_authenticity(filepath):
    trusted = load_trusted_hashes()
    current_hash = hash_file(filepath)

    trusted_hash = trusted.get(filepath)

    if not trusted_hash:
        return "UNTRUSTED", current_hash

    if current_hash == trusted_hash:
        return "AUTHENTIC", current_hash
    else:
        return "TAMPERED", current_hash