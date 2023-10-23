def caesar_encrypt(text: str, offset: int = 1) -> str:
    result = ''

    for char in text:
        # Lowercase
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            index = (index + offset) % 26
            result += chr(index + ord('a'))
            continue

        # Uppercase
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            index = (index + offset) % 26
            result += chr(index + ord('A'))
            continue

        # Others
        result += char

    return result


def caesar_decrypt(text: str) -> list[tuple[str, int]]:
    result = []

    for i in range(1, 27):
        result.append((caesar_encrypt(text, 26 - i), 26 - i))

    return result

sentence = "J'apprends le langage python"
secret = caesar_encrypt(sentence, 3)

print("Message chiffré : " + secret)

possibilities = caesar_decrypt(secret)

print("Tentatives de déchiffrement :")
for possibility, offset in possibilities:
    print(f"Offset {offset}: {possibility}")
