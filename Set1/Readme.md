#Set 1 Challenges

## Base64 
###https://cryptopals.com/sets/1/challenges/1

This challenge is pretty straight forward, you need to convert the hex string into raw bytes, and then encode those bytes as a base64 encoded string. Looking at convhxtob64.py, I created a str2array

```python
def str2array(st):
   arr = []
   for index in range(0,len(st),2):
      arr.append(int(st[index:index+2],16))
   return arr
```

The function basically steps through the string two characters at a time, converts each set of characters into a hex byte, and then stores the byte into the array. There's also a function called fromhex that work with python 3:

```python
bytes.fromhex(hexvar)
```

However, I used python 2 for the first couple of challenges. Next, I think they really just wanted us to use something like

```python
import base64

base64.b64encode(hexval)
```

but I decided to try and implement a basic base64 encoder. I used the wikipedia page (https://en.wikipedia.org/wiki/Base64) to figure out how to start encoding. According to Wikipedia you take three bytes and split those three bytes into four 6-bit segments, then the values of the 6-bit segments and lookup the corresponding value in a table. To implement this, I basically created a loop that reads in 3 bytes at a time, then I use logical shifts to get the append them all together. After appending the values together, I use bit-masks and a logical and to seperate the four 6-bit segments and look up their values. Then I use a dictionary to see which character to print.

```python
index = 0
while index < len(hexval):
   temp1 = hexval[index] << 16
   index += 1
   temp2 = hexval[index] << 8
   index += 1
   temp3 = hexval[index]
   num = temp1 + temp2 + temp3
   output = output + dict[(num & 0xFC0000) >> 18]
   output = output + dict[(num & 0x3F000) >> 12]
   output = output + dict[(num & 0xFC0) >> 6]
   output = output + dict[(num & 0x3f)]
   index  += 1
```


## Fixed XOR
###https://cryptopals.com/sets/1/challenges/2


## Single-Byte XOR
###https://cryptopals.com/sets/1/challenges/3
