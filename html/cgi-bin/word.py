#!/usr/bin/python3

import cgi
print("Content-Type: text/html\n")
form = cgi.FieldStorage()
drow = form.getvalue("word").lower()
lendrow=len(drow)
ldrow=list(drow)
ldrow.sort()
words=open("./words","r")
print("<ul>")
for word in words:
   lenword=len(word)-1
   if(lenword>2 and lendrow>=lenword):
      word=word.lower()
      lword=list(word)
      lword=lword[:-1]
      lword.sort()
      i = 0
      j = 0
      anomaly = 0
      while (i<lenword and j<lendrow):
            if(ldrow[j]!=lword[i]):
               anomaly = 1
               j+=1
            else:
               anomaly = 0
               i+=1
               j+=1
               if(j == lendrow and i < lenword):
                   anomaly = 1
      if(anomaly == 0):
         print("<li>")
         #print(i,j,ldrow, lword)
         print(word.upper())
         print("</li>")
      #if(anomaly == 1):
         #print(i,j,ldrow, lword)
words.close()
print("</ul>")

