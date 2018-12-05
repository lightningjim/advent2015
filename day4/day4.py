import hashlib

key = 'ckczppom'
index = 1

fiveZerosFound = False
sixZerosFound = False
fiveIndex = ''
sixIndex = ''
fiveMD5 = ''
sixMD5 = ''
while True:
	if fiveZerosFound and sixZerosFound:
		break
	md5 = hashlib.md5()
	test_seed = key + str(index) 
	md5.update(test_seed)
	md5hash = md5.hexdigest()
	# print md5hash
	if md5hash[:5] == "00000":
		if md5hash[:6] == "000000":
			sixZerosFound = True
			sixIndex = str(index)
			sixMD5 = md5hash
		else:
			if not fiveZerosFound:
				fiveZerosFound = True
				fiveIndex = str(index)
				fiveMD5 = md5hash
	index += 1

print "Answers for key seed " + key
print "5 0s: "+ fiveIndex + " | hash " + fiveMD5
print "6 0s: "+ sixIndex + " | hash " + sixMD5