# Imports
import hashlib
from utils import *
from main import ROUNDS, BLOCK_SIZE


def encrypt(plaintext, key):
    # ASCII -> Binário
    plaintext_bits = string_to_bits(plaintext)
    # Separa em blocos do tamanho de BLOCK_SIZE
    plaintext_blocks = split_to_blocks(plaintext_bits, BLOCK_SIZE)

    # Gerando chave de 512 Bits
    key = generate_key(key)
    # Gerando sub chaves, 16 (Número de rodadas) blocos de 32 bits da chave de 512 bits
    sub_keys = split_to_blocks(key, int(BLOCK_SIZE / 2))

    ciphertext_blocks = []
    for plaintext_block in plaintext_blocks:
        # Pra cada bloco, faz ROUNDS rodadas
        for i in range(ROUNDS):
            plaintext_block = round(plaintext_block, sub_keys[i])
        # Quando acabam as rodadas, adiciona o texto cifrado aos blocos cifrados, invertendo as metades
        ciphertext_blocks.append(str(plaintext_block[32:]) + str(plaintext_block[:32]))
    # Juntando os blocos cifrados e convertendo pra hexadecimal
    return bits_to_hex("".join(ciphertext_blocks))


# A diferença entre os algoritmos de criptografar e descriptografar é a ordem das sub chaves
# Aqui, utilizamos a ordem inversa
def decrypt(ciphertext, key):
    ciphertext_bits = hex_to_bits(ciphertext)
    ciphertext_blocks = split_to_blocks(ciphertext_bits, BLOCK_SIZE)

    key = generate_key(key)
    sub_keys = split_to_blocks(key, int(BLOCK_SIZE / 2))

    plaintext_blocks = []
    for ciphertext_block in ciphertext_blocks:
        for i in range(ROUNDS, 0, -1):
            ciphertext_block = round(ciphertext_block, sub_keys[i - 1])
        plaintext_blocks.append(str(ciphertext_block[32:]) + str(ciphertext_block[:32]))
    return bits_to_string(split_to_blocks("".join(plaintext_blocks), 8))


# Lógica de cada rodada da cifra de Feistel
# Ou exclusivo da sub chave com a metade direita da string recebida, e então ou exclusivo do resultado disso com a metade esquerda.
def round(bits, sub_key):
    # Separa as metades da string
    left_bits = bits[:32]
    right_bits = bits[32:]
    # XOR da sub chave com a metade direita da string
    f_out = xor(sub_key, right_bits)
    # XOR f_out e a metade recebida
    left_xor_f_out = xor(left_bits, f_out)
    # Retorna as metades trocadas
    return right_bits + left_xor_f_out


# Ou exclusivo de duas strings binárias
def xor(first, second):
    return "".join([str(ord(a) ^ ord(b)) for a, b in zip(first, second)])


# Utilizan SHA-512 na chave especificada na execução, e retorna a representação binária da chave com hash
def generate_key(secret):
    hash = hashlib.sha512(str.encode(secret)).hexdigest()
    integer = int(hash, 16)
    bin_hash = format(integer, "0>42b").zfill(512)
    return bin_hash
