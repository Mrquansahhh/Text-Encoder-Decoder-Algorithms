"""
Assignment 3: Text Encoder / Decoder
Algorithms: Caesar Cipher, Vigenere Cipher, Atbash Cipher, Base64
Run with: python cipher.py
"""

import base64
import binascii


# ---------- Helper ----------
def shift_char(ch, shift):
    """Shift a letter by 'shift' places, keeping case. Non-letters unchanged."""
    if ch.isalpha() and ch.isascii():
        base = ord("A") if ch.isupper() else ord("a")
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch


# ---------- Algorithm 1: Caesar Cipher ----------
def caesar(text, key, decode=False):
    shift = -key if decode else key
    return "".join(shift_char(c, shift) for c in text)


# ---------- Algorithm 2: Vigenere Cipher ----------
def vigenere(text, keyword, decode=False):
    shifts = [ord(k.lower()) - ord("a") for k in keyword if k.isalpha()]
    if not shifts:
        raise ValueError("Keyword must contain at least one letter.")
    result = []
    i = 0
    for ch in text:
        if ch.isalpha() and ch.isascii():
            s = shifts[i % len(shifts)]
            result.append(shift_char(ch, -s if decode else s))
            i += 1
        else:
            result.append(ch)
    return "".join(result)


# ---------- Algorithm 3: Atbash Cipher ----------
def atbash(text):
    """Reverses the alphabet (A<->Z, B<->Y...). Same function encodes and decodes."""
    result = []
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr(base + 25 - (ord(ch) - base)))
        else:
            result.append(ch)
    return "".join(result)


# ---------- Algorithm 4: Base64 ----------
def base64_encode(text):
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def base64_decode(text):
    try:
        return base64.b64decode(text.encode("ascii"), validate=True).decode("utf-8")
    except (binascii.Error, UnicodeDecodeError, UnicodeEncodeError):
        raise ValueError("Invalid Base64 input.")


# ---------- User Interface ----------
def get_mode():
    while True:
        choice = input("Encode or Decode? (e/d): ").strip().lower()
        if choice in ("e", "d"):
            return choice == "d"
        print("Please enter 'e' or 'd'.")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def show_menu():
    print("\n===== TEXT ENCODER / DECODER =====")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Atbash Cipher")
    print("4. Base64")
    print("5. Exit")


def main():
    while True:
        show_menu()
        option = input("Choose an algorithm (1-5): ").strip()

        if option == "5":
            print("Goodbye!")
            break
        if option not in ("1", "2", "3", "4"):
            print("Invalid choice. Try again.")
            continue

        decode = get_mode()
        text = input("Enter your text: ")

        try:
            if option == "1":
                key = get_int("Enter shift key (number): ")
                result = caesar(text, key, decode)
            elif option == "2":
                keyword = input("Enter keyword (letters only): ")
                result = vigenere(text, keyword, decode)
            elif option == "3":
                result = atbash(text)
            else:
                result = base64_decode(text) if decode else base64_encode(text)

            print("\nResult:", result)
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()