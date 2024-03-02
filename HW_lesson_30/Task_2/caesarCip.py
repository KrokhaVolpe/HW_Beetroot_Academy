# caesar_cipher
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?. "

def encrypt_caesar_cipher(message, key):
    
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = (symbol_index + int(key)) % len(SYMBOLS)
            translated += SYMBOLS[translated_index]
        else:
            translated += symbol

    return translated

def decrypt_caesar_cipher(message, key):
    
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = (symbol_index - int(key)) % len(SYMBOLS)
            translated += SYMBOLS[translated_index]
        else:
            translated += symbol

    return translated



#print(encrypt_caesar_cipher("Hello", 2))
#print(decrypt_caesar_cipher("Hello", 2))

    
 
