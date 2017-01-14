from optparse import OptionParser
import sys
import operator

def str2array(st):
   arr = []
   for index in range(0,len(st),2):
      arr.append(int(st[index:index+2],16))
   return arr

dict = {0:'A',16:'Q',32:'g',48:'w',1:'B',17:'R',33:'h',49:'x',2:'C',18:'S',34:'i',50:'y',3:'D',19:'T',35:'j',51:'z',4:'E',20:'U',36:'k',52:'0',5:'F',21:'V',37:'l',53:'1',6:'G',22:'W',38:'m',54:'2',7:'H',23:'X',39:'n',55:'3',8:'I',24:'Y',40:'o',56:'4',9:'J',25:'Z',41:'p',57:'5',10:'K',26:'a',42:'q',58:'6',11:'L',27:'b',43:'r',59:'7',12:'M',28:'c',44:'s',60:'8',13:'N',29:'d',45:'t',61:'9',14:'O',30:'e',46:'u',62:'+',15:'P',31:'f',47:'v',63:'/'}

parser = OptionParser()
parser.add_option("-x", "--hex", dest="hexval", help="hex to XOR", metavar="HEX")
(options, args) = parser.parse_args()

hexval = str2array(options.hexval)

if (len(hexval) % 3) != 0:
   print "[-] ERROR: Needs padding"
   add = len(hexval) % 3
   for i in range(0,add):
      hexval.append(0x00)

output = ''
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

print output
