import math

from string import ascii_lowercase
from collections import Counter

alphabet = ascii_lowercase
letter_frequency = {
    "e": 12.702,
    "t": 9.056,
    "a": 8.167,
    "o": 7.507,
    "i": 6.966,
    "n": 6.749,
    "s": 6.327,
    "h": 6.094,
    "r": 5.987,
    "d": 4.253,
    "l": 4.025,
    "c": 2.782,
    "u": 2.758,
    "m": 2.406,
    "w": 2.360,
    "f": 2.228,
    "g": 2.015,
    "y": 1.974,
    "p": 1.929,
    "b": 1.492,
    "v": 0.978,
    "k": 0.772,
    "j": 0.153,
    "x": 0.150,
    "q": 0.095,
    "z": 0.074,
}


def cipher(text, key, decrypt):
    output = ""
    for char in text:
        if char not in alphabet:
            output += char
            continue

        index = alphabet.index(char.lower())

        if not decrypt:
            new_char = alphabet[(index + key) % len(alphabet)]
        else:
            new_char = alphabet[(index - key) % len(alphabet)]

        output += new_char.upper() if char.isupper() else new_char

    return output


def difference(text):
    counter = Counter(text)
    return sum(
        [
            abs(letter_frequency[letter] - counter.get(letter, 0) * 100 / len(text))
            for letter in alphabet
        ]
    ) / len(alphabet)


def break_cipher(cipher_text):
    lowest_difference = math.inf
    encryption_key = 0

    for key in range(1, len(alphabet)):
        current_plain_text = cipher(cipher_text, key, True)
        current_difference = difference(current_plain_text)

        if current_difference < lowest_difference:
            lowest_difference = current_difference
            encryption_key = key

    return encryption_key


if __name__ == "__main__":
    quote = "The quick brown fox jumps over the lazy dog"
    caesar_output = cipher(quote, 13, False)
    print("Caesar Cipher - Key: 13")
    print(f"'{quote}' -> '{caesar_output}'\n")
    
    cipher_quote = "Tli uymgo fvsar jsb nyqtw sziv xli pedc hsk"
    encryption_key = break_cipher(cipher_quote)
    print(f"Caesar Cipher - Cipher: '{cipher_quote}'")
    print(f"Key: {encryption_key}")
