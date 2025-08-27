# Caesar Cipher

Welcome to the **Caesar Cipher** project by **sudo-shakyo**!  
A simple yet powerful implementation of the classic Caesar cipher in Python.

[View the code on GitHub](https://github.com/sudo-shakyo/ceaser-cipher)

---

##  Table of Contents
- [About](#about)  
- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Usage](#usage)  
- [Examples](#examples)  
- [Contributing](#contributing)  
- [License](#license)  
- [Author](#author)  

---

## About

The **Caesar Cipher** is a simple encryption technique where each letter in the plaintext is shifted by a fixed number of positions down the alphabet. For example I want to encrypt the string "shakyo", the ceaser-cipher project encrypts the string for me. Or if I want to decrpyt the string, I can simply call the decrypt function to decrypt the string.

---

## Features

- Encrypt plaintext by shifting letters by a user-defined "shift number"
- Decrypt ciphertext using the same "shift number"
- Works with English alphabet (both uppercase & lowercase) ["the output comes in lowercase tho"]
- Non-alphabet characters (e.g., numbers, punctuation) remain unchanged  

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system  
- Terminal or command-line access  

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sudo-shakyo/ceaser-cipher.git
   cd ceaser-cipher
2.  (optional) creating a virtal env
   ```bash
python3 -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```
3. Usage
run the file by the following command:
```bash
   python main.py
```
### Examples 
### Encryption
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
Hello, World
Type the shift number: 
3
Here is the encoded result: khoor zruog!
Type 'yes' if you want to go again. Otherwise, type 'no'.

### Decryption
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog!
Type the shift number: 
3
Here is the decoded result: hello world!
Type 'yes' if you want to go again. Otherwise, type 'no'.

### Author

sudo-shakyo

This project is maintained with care and curiosity—thanks for checking it out!


