# import module
import os


# write message
message = input("(+) Write your message : ") 

with open("message.txt","w+") as message_file:
    message_file.write(message)


# encrypt message
print("(*) Encrypt message")
os.system("openssl enc -aes-256-cbc -in message.txt -out message_chiffre_aes.bin")

# decrypt message
print("(*) Decrypt message")
os.system("openssl enc -d -aes-256-cbc -in message_chiffre_aes.bin -out message_dechiffre.txt")

# clear terminal
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# read message
with open("message_dechiffre.txt","r+") as message_file:
    message = message_file.read()
    print(message)



 