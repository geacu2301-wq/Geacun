def caesar_cipher(bai4, shift, direction):
    with open(bai4, 'r') as file:
        text = file.read()
    result = ""
    for c in text:
        if 'A' <= c <= 'Z':
            if direction == "right":
                new_char = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= c <= 'z':
            if direction == "right":
                new_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif '0' <= c <= '9':  
            new_char = c
        else:
            new_char = c
        result += new_char
    with open("ciphertext.txt", 'w') as file:
        file.write(result)
    return result