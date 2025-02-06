# Git-like Implementation

This project provides a simple implementation of some core Git operations using Python. The functionality includes initializing a Git repository, hashing files to create Git objects, and displaying the content of Git objects.

## Features

1. **git init** - Initializes a basic Git repository structure.
2. **git hash-object -w <file-path>** - Hashes a file and stores it as a Git object.
3. **git cat-file -p <object-hash>** - Displays the content of a Git object in a human-readable format.

## Requirements

- Python 3.x
- Basic understanding of Git and its internal object model.

## How It Works

### 1. **`git init`**

This command initializes the necessary directories and files for a basic Git repository. It creates the following structure:

.git/ 
	├── objects/ # Store Git objects (blobs, trees, commits) 
	├── refs/ # References for branches (e.g., HEAD, main) 
	└── HEAD # Points to the current branch reference (default: refs/heads/main)


When you run the `init` command, it will create the `.git` directory with the basic repository structure and write a reference to the `main` branch in the `.git/HEAD` file.

#### Example:

```bash
$ python main.py init
Initialized git directory
```

### 2. **`git hash-object -w <file-path>`**

This command simulates the creation of a Git object for a file. It computes the SHA-1 hash of a file, creates a corresponding `blob` object, and stores it in the `.git/objects` directory.

Git objects are stored in a compressed format. The object data consists of:
- A header: `blob <file-size>\0` (Git object header format).
- The file's content.

The object is stored in a directory structure based on the first two characters of the SHA-1 hash.

#### Example:

```bash
$ echo "Hello, Git! This is the content of myfile.txt." > myfile.txt 
$ python git_like.py hash-object -w myfile.txt
e1eaf4ecb3ad905e11824c74ed6999b54d9a9b8f
```

### 3. **`git cat-file -p <object-hash>`**

This command retrieves the content of a Git object (typically a `blob` object) and displays it in a human-readable format.

If the object is a text file, it will print the file content. If it's binary data, the function will display the object in hex format.

#### Example:

```bash
$ python git_like.py cat-file -p e1eaf4ecb3ad905e11824c74ed6999b54d9a9b8f
Hello, Git! This is the content of myfile.txt.
```
