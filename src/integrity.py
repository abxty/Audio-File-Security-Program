from hasher import hash_file
import os

def get_file_info(filepath):
    return {
        "size": os.path.getsize(filepath),
        "hash": hash_file(filepath)
    }

def compare_files(original, modified):
    original_info = get_file_info(original)
    modified_info = get_file_info(modified)

    result = {
        "size_changed": original_info["size"] != modified_info["size"],
        "hash_changed": original_info["hash"] != modified_info["hash"],
        "original_hash": original_info["hash"],
        "modified_hash": modified_info["hash"]
    }

    return result