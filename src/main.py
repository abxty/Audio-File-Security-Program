import sys
from integrity import compare_files
from authenticity import register_trusted_file, verify_authenticity

def print_usage():
    print(\"\"\"\nMusic File Integrity & Authenticity Tool\n
Usage:
  python main.py register <file>
  python main.py verify <file>
  python main.py compare <original> <modified>
\"\"\")

def main():
    if len(sys.argv) < 3:
        print_usage()
        return

    command = sys.argv[1]

    if command == "register":
        filepath = sys.argv[2]
        file_hash = register_trusted_file(filepath)
        print(f\"File registered as trusted.\\nHash: {file_hash}\")

    elif command == "verify":
        filepath = sys.argv[2]
        status, file_hash = verify_authenticity(filepath)
        print(f\"Status: {status}\\nCurrent hash: {file_hash}\")

    elif command == "compare" and len(sys.argv) == 4:
        original = sys.argv[2]
        modified = sys.argv[3]
        result = compare_files(original, modified)

        print(\"Integrity comparison:\")
        print(f\"Size changed: {result['size_changed']}\")
        print(f\"Hash changed: {result['hash_changed']}\")
        print(f\"Original hash: {result['original_hash']}\")
        print(f\"Modified hash: {result['modified_hash']}\")
    else:
        print_usage()

if __name__ == \"__main__\":
    main()