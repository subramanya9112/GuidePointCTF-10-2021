f = open('GOFASTER.txt', 'r')
for line in f:
    text = bytes.fromhex(line).decode("utf-8") 
    if "StormCTF" in text:
        print(text)
f.close()
