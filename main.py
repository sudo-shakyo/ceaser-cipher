alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):

    text_list = list(original_text)
    print(text_list)
    index_list = []
    shifted_index_list = []
    encrypted_list = []
    shifted_word = ""

    for letter in text_list:
        index = alphabet.index(letter)
        index_list.append(index)
    print(index_list)

    for i in index_list:
        i += shift_amount
        shifted_index_list.append(i%len(alphabet))
    print(shifted_index_list)

    for j in shifted_index_list:
        k = alphabet[j]
        encrypted_list.append(k)
    print(encrypted_list)

    for shifted_letters in encrypted_list:
        shifted_word += shifted_letters

    print(f"here is the encrypted word {shifted_word}")




def decrypt(encrypted_text, shift_amount):

    encrypted_text_list = list(encrypted_text)
    index_list = []
    decrypted_index_list = []
    decrypted_word = ""
    for letter in encrypted_text_list:
        index = alphabet.index(letter)
        index_list.append(index)
    print(index_list)

    for indices in index_list:
        indices -= shift_amount
        decrypted_index_list.append(indices % len(alphabet))
    print(decrypted_index_list)

    for shifted_indices in decrypted_index_list:
        letter = alphabet[shifted_indices]
        decrypted_word += letter

    print(f"the decrypted word is {decrypted_word}")

def caesar(direction_, coded_word, number_shift):
    if direction_ == "encode":
        encrypt(coded_word, number_shift)

    elif direction_ == "decode":
        decrypt(coded_word, number_shift)

    else:
        print("wrong parameters")

caesar(direction_ = direction, coded_word = text, number_shift = shift)
