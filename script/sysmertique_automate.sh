echo Write your message
read message 

echo $message > message.txt


echo Encrypt message 
openssl enc -aes-256-cbc -in message.txt -out message_chiffre_aes.bin

echo Decrypt message
openssl enc -d -aes-256-cbc -in message_chiffre_aes.bin -out message_dechiffre.txt

clear

cat message_dechiffre.txt 