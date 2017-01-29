def str2array(st):
   arr = []
   for index in range(0,len(st)):
      arr.append(ord(st[index]))
   return arr

def getOut(hexval,key):
   output = ''
   for i2 in range(0,len(hexval)):
      output = output + "%0.2X" % (hexval[i2] ^ key[i2 % len(key)])
   return output  

s1 = str2array("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
key = str2array('ICE')
print(getOut(s1,key))
