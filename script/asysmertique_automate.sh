echo Write your message
read message 

echo $message > message.txt

echo Generate RSA : private
openssl genpkey -algorithm RSA -out cle_privee.pem

echo Generate RSA : public
openssl rsa -pubout -in cle_privee.pem -out cle_publique.pem 

echo Encrypt message 
openssl pkeyutl -encrypt -pubin -inkey cle_publique.pem -in message.txt -out message_chiffre_rsa.bin 

echo Decrypt message
openssl pkeyutl -decrypt -inkey cle_privee.pem -in message_chiffre_rsa.bin -out message_dechiffre.txt

clear

cat message_dechiffre.txt 

 