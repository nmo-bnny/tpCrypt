from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


# Having trouble decrypting traffic use the valid examples to see how it's supposed to work
# You should see a ipping request that has been decrypted


# A valid Key is shown below
# 1276313602298947

print("AES Key:")
Key = input().replace("\n", "")
bKey = Key.encode('utf-8').strip()


# A valid IV is shown below
# 3229721559440934

print("AES IV:")
Iv = input().replace("\n", "")
bIv = Iv.encode('utf-8').strip()


# A valid encrypted payload is shown below.
# +HC+d77Dc16VCJAGGIs3qb7V1kjRLP62ovdCZMSbNx69WUdmEVf5258rGcOjgDmH



print("Encrypted Payload:")
encryptedPayload = input().replace("\n", "")

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
