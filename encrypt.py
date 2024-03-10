print('Welcome')
print("Rules: Don't open it")

message=input ('Enter message you want to encrypt:')
alphabet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = input("Enter a encrypt key of your Choice (at least 8 Numbers long): ")
encrypt =''

for i in message:
  position = alphabet.find(i)
  newposition = (position+int(key)) % len(alphabet)
  encrypt += alphabet[newposition]
output = (encrypt)

print ('Encrypted Message: '+ (output))
print ('Encryption Key: '+ (key))