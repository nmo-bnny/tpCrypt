from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64



# A valid Key is shown below

print("\nAES Key:")
Key = "1276313602298947"
bKey = Key.encode('utf-8').strip()
print(Key)

# A valid IV is shown below

print("AES IV:")
Iv = "3229721559440934"
bIv = Iv.encode('utf-8').strip()
print(Iv)

# A valid encrypted payload is shown below.

print("Encrypted Payload:")
encryptedPayload = "+HC+d77Dc16VCJAGGIs3qb7V1kjRLP62ovdCZMSbNx69WUdmEVf5258rGcOjgDmH"
print(encryptedPayload)
difference = len(encryptedPayload) % 4

if difference >= 1:
    print("\nNot in correct format")
    print(f"--Off by {difference} remove newline characters")

else:
    bencryptedPayload = encryptedPayload.encode('utf-8')

    decodedBase64EncryptedPayload = base64.b64decode(encryptedPayload, validate=False)

     # Key and IV are required to decrypt payload(Byte Format)
    decryptAESType = AES.new(bKey, AES.MODE_CBC, bIv)

    payload = unpad(decryptAESType.decrypt(decodedBase64EncryptedPayload), AES.block_size)


    print("\n__Decrypted Payload__\n")
    print(payload)
    print("---\n")
