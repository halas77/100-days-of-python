alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceasar(text, shift, direction):
    if direction == "encode":
        encrypt_word =''  
        for i in text:
            
            if i in alphabet:
                index_of_letter = alphabet.index(i)   
                encrypted_letter_index = index_of_letter + shift
                
                if encrypted_letter_index > len(alphabet):
                    out_range = encrypted_letter_index % len(alphabet)
                    encrypt_word += alphabet[out_range]
                elif encrypted_letter_index > len(alphabet):
                    out_range = encrypted_letter_index - len(alphabet)
                    encrypt_word += alphabet[out_range]  
                    
                else:
                    encrypt_word += alphabet[encrypted_letter_index]
            else:
                encrypt_word+=i
            
                
        print(f"The encrypted word is {encrypt_word}")
        
    elif direction == "decode":
        decrypt_word = ''
    
        for i in text:
            if i in alphabet:
                index_of_letter = alphabet.index(i)
                decrypted_letter_index = index_of_letter - shift
                
                if decrypted_letter_index < 0:
                    out_range = len(alphabet) - decrypted_letter_index
                    decrypt_word += alphabet[out_range]
                else:
                    decrypt_word += alphabet[decrypted_letter_index]
            else:
                decrypt_word +=i
                
        print(f"The Decrypted word is {decrypt_word}")
    
  
tester = True

while tester:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text= input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    ceasar(text=text, shift=shift, direction=direction)
    user = input("Do you wanna to continue Yes or No: ").lower()
    if user == "no":
        tester = False
        print("Good Bye!")
    
    

    
    
    

    
            
        
    

