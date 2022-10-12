#!/bin/bash

echo "input_text.txt:"
cat ./input_text.txt

echo "

>>> CRIPTOGRAFANDO O ARQUIVO 'input_text.txt' UTILIZANDO A CHAVE 'W8NCj4W4BW'"
python3 main.py -e -k W8NCj4W4BW input_text.txt output_ciphertext.txt

echo "output_ciphertext.txt:"
cat ./output_ciphertext.txt

echo "

>>> DESCRIPTOGRAFANDO O ARQUIVO 'output_ciphertext.txt' GERADO ANTERIORMENTE UTILIZANDO A CHAVE 'W8NCj4W4BW'"
python3 main.py -d -k W8NCj4W4BW output_ciphertext.txt output_plaintext.txt

echo "output_plaintext.txt:"
cat ./output_plaintext.txt