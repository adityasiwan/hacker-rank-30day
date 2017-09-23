T = int(raw_input().strip())

for i in range(0, T):
	S = raw_input()
	even, odd = S[0::2], S[1::2]
	print(even + " " + odd)
