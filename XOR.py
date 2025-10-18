import base64
cipher_for_B64 = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
cipher_bytes = base64.b64decode(cipher_for_B64)
key = "secure".encode()
text = bytes([cipher_bytes[i] ^ key[i % len(key)] for i in range(len(cipher_bytes))])
print("Decrypted message:", text.decode())