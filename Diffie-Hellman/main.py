class DH_Endpoint(object):
    # Inicializa com os valores das chaves
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    # Gera chave parcial
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    # Gera chave completa
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    # Transforma o caractere em int, soma o valor da chave e o retorna para string
    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    # Descriptografa o texto criptografado pela função acima
    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


b_public = 104053
b_private = 101771
a_public = 100673
a_private = 103237
print("### Chaves públicas ###")
print(f"Chave pública de Bob: {b_public}")
print(f"Chave pública de Alice: {a_public}\n")

Bob = DH_Endpoint(b_public, a_public, b_private)
Alice = DH_Endpoint(b_public, a_public, a_private)

b_partial = Bob.generate_partial_key()
a_partial = Alice.generate_partial_key()
print("### Cálculo das chaves parciais ###")
print(f"Chave parcial de Bob: {b_partial}")
print(f"Chave parcial de Alice: {a_partial}\n")

b_full = Bob.generate_full_key(a_partial)
a_full = Alice.generate_full_key(b_partial)
print("### Cálculo das chaves completas ###")
print(f"Chave completa de Bob e Alice: {a_full}\n")

message = "Olá, Bob! Como vão as coisas? Faz um tempo que não nos encontramos..."
m_encrypted = Alice.encrypt_message(message)
print(f"Alice envia a mensagem '{message}', que é enviada pela rede da seguinte forma: '{m_encrypted}', até ser descriptografada na máquina de Bob, utilizando a chave completa.")

message = Bob.decrypt_message(m_encrypted)
