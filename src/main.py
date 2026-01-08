#!/usr/bin/env python3
"""
Music File Integrity & Authenticity Tool
----------------------------------------
Interactive demo for file integrity verification.

Portfolio-ready: employers can immediately see detection of altered files.
"""

import hashlib
import json
import os

# Files for the demo
ORIGINAL_FILE = "sample.wav"
EXAMPLE_FILES = [ORIGINAL_FILE, "altered_sample.wav"]
HASH_DB_FILE = "hashes.json"

def compute_hash(file_path):
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

def load_hash_db():
    """Load existing hash database or create a new one."""
    if os.path.exists(HASH_DB_FILE):
        with open(HASH_DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hash_db(db):
    """Save the hash database to a JSON file."""
    with open(HASH_DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def ensure_original_hash(db):
    """Add the original file hash to the database if not already present."""
    if ORIGINAL_FILE not in db:
        h = compute_hash(ORIGINAL_FILE)
        if h:
            db[ORIGINAL_FILE] = h
            save_hash_db(db)
            print(f"[OK] Stored original hash for {ORIGINAL_FILE}: {h}")

def choose_file():
    """Prompt user to select a file."""
    print("Choose a file to test:")
    for i, f in enumerate(EXAMPLE_FILES, start=1):
        print(f"{i}. {f}")
    choice = input(f"Enter 1-{len(EXAMPLE_FILES)} [default 1]: ").strip()
    return EXAMPLE_FILES[1] if choice == "2" else EXAMPLE_FILES[0]

def verify_file_against_original(file_path, db):
    """Verify the selected file against the original file's hash."""
    original_hash = db.get(ORIGINAL_FILE)
    if not original_hash:
        print(f"[ERROR] Original hash not found. Please ensure {ORIGINAL_FILE} exists.")
        return
    current_hash = compute_hash(file_path)
    if current_hash == original_hash:
        print(f"[OK] {file_path} matches the original. No alterations detected.")
    else:
        print(f"[ALERT] {file_path} does NOT match the original! File may be altered.")
        print(f"Original hash: {original_hash}")
        print(f"Current hash:  {current_hash}")

def main():
    print("""
========================================
Music File Integrity & Authenticity Tool
========================================
""")
    db = load_hash_db()
    ensure_original_hash(db)

    file_path = choose_file()
    verify_file_against_original(file_path, db)

    print("\nDemo complete. Run again to test other files.")

if __name__ == "__main__":
    main()