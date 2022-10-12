import math
from main import BLOCK_SIZE

# Lê um arquivo
def read_file(path):
    with open(path, "r") as file:
        return file.read()


# Escreve um arquivo
def write_file(path, data):
    with open(path, "w") as outfile:
        outfile.write(data)


# ASCII -> Binário
def string_to_bits(string):
    str = "".join("{:08b}".format(ord(c)) for c in string)
    return str.ljust(BLOCK_SIZE * math.ceil(len(str) / BLOCK_SIZE), "0")


# Binário -> ASCII
def bits_to_string(bytes):
    return "".join([chr(int(x, 2)) for x in bytes])


# Hexadecimal -> Binário
def hex_to_bits(hex):
    return bin(int(hex, 16))[2:]


# Binário -> Hexadecimal
def bits_to_hex(bits):
    return hex(int(bits, 2))


# Separa uma string binária em blocos do tamanho de BLOCK_SIZE
def split_to_blocks(bits, block_size):
    return [bits[i : i + block_size] for i in range(0, len(bits), block_size)]
