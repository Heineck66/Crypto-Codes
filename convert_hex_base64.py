hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

import base64

fromhex = bytes.fromhex(hex_string)
print(fromhex)

result = base64.b64encode(fromhex)

print(result)
