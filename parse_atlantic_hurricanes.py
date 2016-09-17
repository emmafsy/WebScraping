
# coding: utf-8



import sqlite3 as lite
import os
import sys
import re
import urllib2
from bs4 import BeautifulSoup
powers = {'billion': 10 ** 9, 'million': 10 ** 6}



conn = lite.connect('hurricanes.db')
cur = conn.cursor()
cur.execute("CREATE TABLE atlantic_hurricanes(year INTEGER, tropical_storms INTEGER, hurricanes INTEGER, major_hurricanes INTEGER, deaths INTEGER, damage FLOAT, notes STRING)")



page1 = urllib2.urlopen("file:///Users/emmafsy/Documents/ML/en.wikipedia.org/wiki/Atlantic_hurricane_season.html")
soup = BeautifulSoup(page1)




def f(num_str):
    
    match = re.search(r"([0-9\.]+)\s?(million|billion)", num_str)
    if match is not None:
        quantity = match.group(1)
        magnitude = match.group(2)
        return float(quantity) * powers[magnitude]



w_data = soup.find_all("table",{"class":"wikitable sortable"})
for item in w_data:
    rows = item.find_all("tr")
    for row in rows:
        tds = row.find_all("td")
        if len(tds)!=0:
            if len(tds)== 6:
                td1 = []
                for td in tds:
                    tdtext = re.sub('[\+,$~>]','',td.text)
                    tdtext = tdtext.replace(u'\xa0',u' ')
                    patterns = ["Unknown","Not known","None","Numerous"]
                    if tdtext in patterns:
                        td1.append(int(0))
                    elif re.search(r"([0-9\.]+)\s?(million|billion)", tdtext):
                        print tdtext
                        td1.append(f(tdtext))
                    else:
                        try:            
                            td1.append(int(tdtext))
                        except:
                            td1.append(tdtext)                     
                cur.execute("INSERT INTO atlantic_hurricanes VALUES(?,?,?,?,?,?,?)",
                            (td1[0],td1[1],td1[2],td1[3],td1[4],"N.A",td1[5]))
                
            elif len(tds)== 7:
                td2 = []
                for td in tds:
                    tdtext = re.sub('[\+,$~>]','',td.text)
                    tdtext = tdtext.replace(u'\xa0',u' ')
                    patterns = ["Unknown","Not known","None","Numerous"]
                    if tdtext in patterns:
                        td2.append(int(0))
                    elif re.search(r"([0-9\.]+)\s?(million|billion)", tdtext):
                        td2.append(f(tdtext))
                    else:
                        try:            
                            td2.append(int(tdtext))
                        except:
                            td2.append(tdtext)                     
                cur.execute("INSERT INTO atlantic_hurricanes VALUES(?,?,?,?,?,?,?)", 
                            (td2[0],td2[1],td2[2],td2[3],td2[4],"N.A",td2[5]+","+td2[6]))
                
            elif len(tds)== 8:
                td3 = []
                for td in tds:
                    tdtext = re.sub('[\+,$~>]','',td.text)
                    tdtext = tdtext.replace(u'\xa0',u' ')
                    patterns = ["Unknown","Not known","None","Numerous"]
                    if tdtext in patterns:
                        td3.append(int(0))
                    elif re.search(r"([0-9\.]+)\s?(million|billion)", tdtext):
                        td3.append(f(tdtext))
                    else:
                        try:            
                            td3.append(int(tdtext))
                        except:
                            td3.append(tdtext)                     
                cur.execute("INSERT INTO atlantic_hurricanes VALUES(?,?,?,?,?,?,?)", 
                            (td3[0],td3[1],td3[2],td3[3],td3[4],td3[5],td3[6]+","+td3[7]))
            
                
            elif len(tds)== 9:
                td4 = []
                for td in tds:
                    tdtext = re.sub('[\+,$~>]','',td.text)
                    tdtext = tdtext.replace(u'\xa0',u' ')
                    patterns = ["Unknown","Not known","None","Numerous"]
                    if tdtext in patterns:
                        td4.append(int(0))
                    elif re.search(r"([0-9\.]+)\s?(million|billion)", tdtext):
                        td4.append(f(tdtext))
                    else:
                        try:            
                            td4.append(int(tdtext))
                        except:
                            td4.append(tdtext)                     
                cur.execute("INSERT INTO atlantic_hurricanes VALUES(?,?,?,?,?,?,?)", 
                            (td4[0],td4[1],td4[2],td4[3],td4[4],td4[5],str(td4[6])+","+str(td4[7])+","+str(td4[8])))
                                      
            elif len(tds)== 10:
                td5 = []
                for td in tds:
                    tdtext = re.sub('[\+,$~>]','',td.text)
                    tdtext = tdtext.replace(u'\xa0',u' ')
                    patterns = ["Unknown","Not known","None","Numerous"]
                    if tdtext in patterns:
                        td5.append(int(0))
                    elif re.search(r"([0-9\.]+)\s?(million|billion)", tdtext):
                        td5.append(f(tdtext))
                    else:
                        try:            
                            td5.append(int(tdtext))
                        except:
                            td5.append(tdtext)                     
                cur.execute("INSERT INTO atlantic_hurricanes VALUES(?,?,?,?,?,?,?)", 
                            (td5[0],td5[2],td5[3],td5[4],td5[5],td5[6],str(td5[7])+","+str(td5[8])+","+str(td5[9])))
        
conn.commit()
conn.close()       
            
        
        

        

