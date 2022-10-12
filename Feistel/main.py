# Imports
import argparse
from feistel import *
from utils import *

# Constantes
BLOCK_SIZE = 64
ROUNDS = 16


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", action="store_true", help="criptografa o texto")
    group.add_argument("-d", "--decrypt", action="store_true", help="descriptografa o texto")
    
    parser.add_argument("-k", "--key", type=str, help="especifica a chave que será utilizada", required=True)
    parser.add_argument("input_file", help="arquivo onde está o texto a ser criptografado")
    parser.add_argument("output_file", help="arquivo onde o programa escreverá seu output")
    
    args = parser.parse_args()
    key = args.key.encode("UTF-8")

    input_text = read_file(args.input_file)
    if args.encrypt:
        ciphertext = encrypt(input_text, key.decode())
        output=ciphertext
    else:
        plaintext = decrypt(input_text, key.decode())
        output=plaintext

    write_file(args.output_file, output)
