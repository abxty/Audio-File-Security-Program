# Music Integrity & Authenticity Tool

A Python-based project that helps users check the integrity and authenticity of their music files. This tool can detect if files have been tampered with and verify the authenticity of tracks using simple cryptographic methods. It is designed as a command-line application, demonstrating file handling, hashing, and authenticity verification in Python.

## Features

- Verify if a music file has been altered or corrupted
- Generate and check cryptographic hashes for file integrity
- Track and authenticate multiple files efficiently
- CLI-based interface for quick and easy use
- Designed with Python for flexibility and future expansion

## Technologies Used

- Python 3
- hashlib for hashing and file integrity checks
- argparse for command-line interface
- Optional: additional modules for audio metadata handling

## Installation

1. Clone the repository:
git clone https://github.com/YOURUSERNAME/Music-Integrity-Tool.git

2. Navigate to the project folder:
cd Music-Integrity-Tool

3. Create a virtual environment:
python -m venv venv

4. Activate the environment:
Windows: venv\Scripts\activate  
macOS/Linux: source venv/bin/activate

5. Install dependencies:
pip install -r requirements.txt

## Usage

- Open a terminal in the project folder
- Run the main program:
python main.py [options] <file or folder>
- Use options to:
  - Generate a hash for a file
  - Check the integrity of an existing file
  - Verify authenticity against a stored hash database
- Follow CLI prompts for file selection and verification

## Learning Outcomes

- File integrity and tampering detection
- Working with cryptographic hashes in Python
- Command-line interface design
- Handling real-world file data and metadata
- Understanding practical applications of security in media files

## Future Improvements

- Add support for batch file verification and directories
- Integrate audio metadata checks for deeper authenticity validation
- Expand to GUI for a more user-friendly experience
- Explore more advanced cryptographic methods

## Author

Samuel George Loots  
Year 2 Computer Science Student · Cardiff University

[GitHub Repository](https://github.com/YOURUSERNAME/Music-Integrity-Tool)
