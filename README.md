# Music File Integrity & Authenticity Tool

A Python-based command-line tool that analyses audio files to demonstrate
cryptographic file integrity, tampering detection, and authenticity verification.

## Features
- SHA-256 file hashing
- Tamper detection via hash comparison
- Trusted file registration
- Authenticity verification workflow

## Usage
Register a trusted file:
python main.py register song.mp3

Verify authenticity:
python main.py verify song.mp3

Compare two files:
python main.py compare original.mp3 modified.mp3