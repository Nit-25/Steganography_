import rsa

public_key,private_key = rsa.newkeys(1024)


with open("public_new.pem","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private_new.pem","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))


#with open("public.pem","rb") as f:
    #public_key = rsa.PublicKey.load_pkcs1(f.read())

#with open("private.pem","rb") as f:
    #private_key = rsa.PrivateKey.load_pkcs1(f.read())


message = "Hi"

encrypted_message = rsa.encrypt(message.encode(), public_key)


with open("encrypted_message","wb") as f:
    f.write(encrypted_message)

print(encrypted_message)
decrypt = rsa.decrypt(encrypted_message,private_key)
decrypted_message = decrypt.decode()
