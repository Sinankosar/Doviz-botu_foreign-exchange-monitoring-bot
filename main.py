import requests
from bs4 import BeautifulSoup
import time
import mysql.connector

is_on = True
connection = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "mysql123",
    database ="doviz_db"
    
)

cursor = connection.cursor()

url_doviz = "https://bigpara.hurriyet.com.tr/doviz/"


data = requests.get(url_doviz)
soup = BeautifulSoup(data.text,"html.parser")


table_of_all_them = soup.find("div",class_ = "tableBox srbstPysDvz").find_all("div")[1]
while is_on:
    for row in table_of_all_them.find_all("ul"):
        doviz_adi = row.find_all("li")[0].text
        alis = row.find_all("li")[2].text
        satis = row.find_all("li")[3].text
        degisim = row.find_all("li")[4].text
        saat = row.find_all("li")[5].text
        sql = "INSERT INTO data_table(DovizAdi,Alis,Satis,Degisim,Saat) VALUES(%s,%s,%s,%s,%s)"
        values = (doviz_adi,alis,satis,degisim,saat)
        cursor.execute(sql,values)
        connection.commit()
        
    print("Veriler kaydedildi.\nSQL tablosu güncellendi.")
    time.sleep(500)
    
  








    