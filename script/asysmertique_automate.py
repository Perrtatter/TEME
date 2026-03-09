# import module
import os


# write message
message = input("(+) Write your message : ") 

with open("message.txt","w+") as message_file:
    message_file.write(message)

# generate private rsa
print("(*) Generate RSA : private")
os.system("openssl genpkey -algorithm RSA -out private.pem")

# generate public rsa
print("(*) Generate RSA : public")
os.system("openssl rsa -pubout -in private.pem -out public.pem")

# encrypt message
print("(*) Encrypt message")
os.system("openssl pkeyutl -encrypt -pubin -inkey public.pem -in message.txt -out message_chiffre_rsa.bin")

# decrypt message
print("(*) Decrypt message")
os.system("openssl pkeyutl -decrypt -inkey private.pem -in message_chiffre_rsa.bin -out message_dechiffre.txt")

# clear terminal
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# read message
with open("message_dechiffre.txt","r+") as message_file:
    message = message_file.read()
    print(message)

 