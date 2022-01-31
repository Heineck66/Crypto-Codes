import base64

b64 = "QUMxYWEzM2M0MmYyYTM3ZWU2ZTI5NTYxZDIyNDBiMjMwNzoxZTNmNzg1YmY5YWJjYzM2NzBkZjE2M2I4MzBjOGRkNA=="

result = base64.b64decode(b64)

print(result)
