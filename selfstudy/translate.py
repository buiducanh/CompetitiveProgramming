def translate(crypt, decrypt):
    res = []
    for i in crypt:
        if i in decrypt:
            res.append(decrypt[i].lower())
        else:
            res.append(i)
    return "".join(res)
inp = open("crypt.in", "r")
crypt = ""
decrypt = {}
idx = True
for line in inp:
    if line.strip() == "PLEASEEND":
        print "DECRYPTING -----------=======>"
        print translate(crypt, decrypt)
        print "====------ DONE --------===="
        idx = True
        crypt = ""
        decrypt = {}
    else:
        if idx:
            idx = False
            crypt = line.rstrip()
            print line.rstrip()
        else:
            key, value = line.rstrip().split(" ")
            for i in xrange(len(key)):
                decrypt[key[i]] = value[i]
            print key, value

# decrypt = {}
# for count in xraknge(5):
#     for i in xrange(26):
#         key = chr(ord('a') + i)
#         for j in xrange(26):
#             value = chr(ord('a') + j)
#             if not value in decrypt.values:
#                 decrypt[key] = value
