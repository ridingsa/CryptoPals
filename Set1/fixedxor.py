from optparse import OptionParser
import sys

def str2array(st):
   arr = []
   for index in range(0,len(st),2):
      arr.append(int(st[index:index+2],16))
   return arr

def compare(key, xor):
   output = ''
   index = 0
   while index < len(key):
      output = output + "%0.2X" %  (key[index] ^ xor[index])
      index += 1
   return output

parser = OptionParser()
parser.add_option("-x", "--hex", dest="hexval", help="hex to XOR", metavar="HEX")
parser.add_option("-k", "--key", dest="key", help="key", metavar="KEY")
(options, args) = parser.parse_args()

if len(options.key) == len(options.hexval):
   key = str2array(options.key)
   hexval = str2array(options.hexval)
   print compare(key,hexval)
else:
   print "[-] ERROR: Fixed XOR only uses two Hex Strings of the Same Length, your strings are not the same length"
   sys.exit()

