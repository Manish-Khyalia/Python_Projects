from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount) :
    encrypted_text = ""
    for letter in original_text :
        if letter in alphabet :
            encrypted_text += alphabet[(alphabet.index(letter)+shift_amount)%len(alphabet)]
        else :
            encrypted_text += letter

    print(f"The encrypted text is: {encrypted_text}")
def decrypt(original_text, shift_amount) :
    decrypted_text = ""
    for letter in original_text :
        if letter in alphabet :
            decrypted_text += alphabet[(alphabet.index(letter)-shift_amount)%len(alphabet)]
        else :
            decrypted_text += letter
    print(f"The decrypt text is: {decrypted_text}")
def caesar() :
    if direction == "encode" :
        encrypt(text,shift)
    elif direction == "decode" :
        decrypt(text,shift)
    else :
        print("You enter something else. Please enter only encode/decode.")


over = True
while over :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar()
    s = input("Type 'yes' if you want to go again. Otherwise, type  'no'.\n").lower()
    if s == "no" :
        over = False
        print("Goodbye")


