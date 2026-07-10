# tpCrypt
Tool for decrypting AES-CBC traffic.

# Dependecies
pycryptodome

# Files
tpCrypt.py - tool used to decrypt AES encrypted data <br />
tpCryptExample - displays an encrypted packet decrypted to show how it is supposed to look like

# How To Use
python3 tpCrypt.py <br />
python3 tpCryptExample.py

# Troubleshooting
tpCrypt requires cryptodome to install using pip run <br />
pip install pycryptodome

tpCrypt decodes in base64 as it is common encoding used in text based transmission, if you attempt to decrypt using another format the tool will fail.
