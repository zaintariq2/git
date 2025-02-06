
import sys
import os
import zlib
import hashlib


def init():
    os.mkdir(".git")
    os.mkdir(".git/objects")
    os.mkdir(".git/refs")
    with open(".git/HEAD", "w") as f:
        f.write("ref: refs/heads/main\n")
    print("Initialized git directory")

def cat_file(obj):

    with open(f".git/objects/{obj[:2]}/{obj[2:]}", "rb") as f:
        raw_data = zlib.decompress(f.read())

    header, content = raw_data.split(b"\0", maxsplit=1)
    try:
        print(content.decode('utf-8'), end="")
    except UnicodeDecodeError:
        print(f"Binary content: {content.hex()}")   # If it's not valid UTF-8, handle the binary content (for example, display as hex)

def hash_object(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    header = '{} {}'.format("blob", len(data)).encode("ascii")
    raw = header + b"\x00" + data

    sha = hashlib.sha1(raw).hexdigest()
    path = os.path.join(".git","objects",sha[:2],sha[2:])
    
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(zlib.compress(raw))
    print(sha, end="")


def main():
    
    print("Logs from your program will appear here!", file=sys.stderr)

    command = sys.argv[1]
    if command == "init":
        init()
    
    elif command == "cat-file" and sys.argv[2] == "-p":
        obj = sys.argv[3]
        cat_file(obj)    

    elif command == "hash-object" and sys.argv[2] == "-w":
    
        file_path = sys.argv[3]
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            sys.exit(1)
        
        hash_object(file_path)

    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
