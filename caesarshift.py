#!/usr/bin/env python3
import string

text  = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

alphabet = string.ascii_lowercase

def caesarshift(s, a):
    result = []
    for ch in s:
        lower = ch.lower()
        if lower in alphabet:
            idx = alphabet.index(lower)
            new = alphabet[(idx - a) % 26]             
            result.append(new.upper() if ch.isupper() else new)
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    print("Brute-force Caesar (trying shifts 0..25):\n")
    for a in range(26):
        print(f"Shift {a:2d}: {caesarshift(text, a)}")