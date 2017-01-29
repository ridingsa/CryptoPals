freq = {'E':12.02,'T':9.10,'A':8.12,'O':7.68,'I':7.31,'N':6.95,'S':6.28,'R':6.02,'H':5.92,'D':4.32,'L':3.98,'U':2.88,'C':2.71,'M':2.61,'F':2.30,'Y':2.11,'W':2.09,'G':2.03,'P':1.82,'B':1.49,'V':1.11,'K':0.69,'X':0.17,'Q':0.11,'J':0.10,'Z':0.07}

#lineone = bytes.fromhex("0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032")

filehandle = open('60xor.txt', 'r')


def decryptline():
    linenum = 1
    temp = 0
    mysum = 0
    output = ""
    best = ""
    k1 = 0
    for line in filehandle:
        line = line.rstrip()
        line = bytes.fromhex(line)
        temp2 = findthebest(line)
        temp = temp2[0]
        output = temp2[1]
        linenum += 1
        if temp > mysum:
            mysum = temp
            best = output
            k1 = temp2[2]
    print("Key: " + str(k1) + "\nDecrypted string: " + best)        

def getOut(hexval,key):
      output = ''
      for i2 in range(0,len(hexval)):
         temp = hexval[i2] ^ key
         if (temp >= 0x00) and (temp <= 0x7D):
            output = output + chr(temp)
         else:
            return 0
      dic ={x:output.count(x) for x in output}
      return output        

def findthebest(s1):
    mysum = 0
    best = ''
    k1 = 0
    for i in range(0x00,0xFF):
       output = getOut(s1,i)
       if output != 0:
          output2 = output.upper()
          #print(output)
          dic ={x:output2.count(x) for x in output2}
          temp = 0
          for k in dic:
             if k in freq:
                temp = temp + freq[k]
          if temp > mysum:
             mysum = temp
             best = output
             k1 = i
                  
    return(mysum,best,k1)
    #print(best)

decryptline()

filehandle.close()



#findthebest(lineone)


