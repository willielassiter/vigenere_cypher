#! /usr/bin/env python3

"""

    just an innocent change

"""

trace = False
debug = False

Encrypt = 1
Decrypt = -1

def shift_letter(character, offset):
    
    if trace or debug: print(f"shift_letter('{character}', {offset})")

    if not character.isalpha():

        if debug: print(f"'{character}'' is non-alphabetic")
    
        return character

    if character.isupper ():
        base = ord('A')
    else:
        base = ord('a')

    character_value = ord(character)
    character_value -= base
    index = (character_value + offset) % 26

    if trace or debug: print(f"shift_letter returning '{chr (base + index)}'")

    return chr (base + index)


def vigenère_codec(message, key, direction):

    if trace or debug: print(f"vigenère_codec('{key}', '{message}', {direction})")

    key = key.lower()
    keyLength = len (key)
    keyIndex = 0

    shifted_characters = ""

    for character in message:

        if not character.isalpha():
            shifted_characters += character

            if debug: print(f"skipping non-alphabetic: '{character}'")

            continue

        key_offset = ord(key[keyIndex]) - ord('a')

        shift_amount = key_offset * direction

        shifted_characters += shift_letter (character, shift_amount)

        keyIndex = (keyIndex + 1) % keyLength

    if trace or debug: print(f"vigenère_codec returning {shifted_characters}")

    return shifted_characters


test_message = "Dfc aruw fsti gr vjtwhr wznj? Vmph otis! Cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
# original_message = "Dfc aruw!"

decoded = vigenère_codec (test_message, "FRIENDS", Decrypt)
print (decoded)

encoded_message = vigenère_codec (decoded, "friends", Encrypt)
print (encoded_message)

if encoded_message != test_message:
    print ("\nprogram failed")
else:
    print ("\nprogram succeeded")
