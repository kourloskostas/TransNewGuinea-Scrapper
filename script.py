from six.moves import urllib
from bs4 import BeautifulSoup
import validators
import requests
      
link = 'http://transnewguinea.org/word/?page='
base = 'http://transnewguinea.org'


filepath = "extracted_data.csv"
#Open File 
f = open(filepath, "w")

p = 1

while True:
      
      lin = link + str(p)
      print lin
      rek = requests.get(lin).text

      soup = BeautifulSoup(rek,features="lxml")

      table = soup.find('table', {"class" : "table table-bordered table-condensed"})

      if table:
                  
            # Find all wordlinks
            for row in table.findAll("tr"):
                  cell = row.find("td")
                  if (cell):
                        burl = cell.find_all('a')
                        for url in burl:
                              wordlink = base + url['href']
                              rek = requests.get(wordlink).text
                              soup = BeautifulSoup(rek,features="lxml")
                              
                              i = 1
                              # For all pages
                              while True:
                                    
                                    page = wordlink + '?page=' + str(i)
                                    rek = requests.get(page).text
                                    soup = BeautifulSoup(rek,features="lxml")
                                    transtable = soup.find('table', {"class" : "table table-bordered table-condensed"})

                                    if transtable:

                                          
                                          # Find all wordlinks
                                          for transrow in transtable.findAll("tr"):
                                                transcell = transrow.find('td' , {"class" : 'entry'})
                                                if (transcell):
                                                      ff = transcell.text

                                                      data = ff.encode('utf-8')

                                                      f.write(data + '\n')
                                                     
                                          
                                          i += 1
                                    else:
                                          break
      p +=1


f.close()

