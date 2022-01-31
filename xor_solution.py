key1_b = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
k2_k3_b = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_r_b = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

flag = bytes([_a ^ _b ^ _c for _a, _b, _c in zip(key1_b, k2_k3_b, flag_r_b)])
print(flag)
