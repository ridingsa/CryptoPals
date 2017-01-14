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

However, I used python 2 for the first couple of challenges. 
