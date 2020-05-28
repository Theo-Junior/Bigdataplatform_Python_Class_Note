import requests
from bs4 import BeautifulSoup

import os
import cx_Oracle
import time
DB_ID = "system"
DB_PWD = "oracle"
DB_URL = "localhost/xe"

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    #print(conn.version)
    return conn

def get_all_rows(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MOVIES_RANKS")
    for row in cursor:
        print(row)
    cursor.close()

def insert_row(conn, no, title, link):
    cursor = conn.cursor()
    str_sql = "INSERT INTO MOVIES_RANKS VALUES(:no, :title, :link)"
    cursor.execute(str_sql, \
        {'no': no, 'title' : title, 'link':link})
    conn.commit()
    cursor.close()



conn = get_conn()



res = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
soup = BeautifulSoup(res.content, 'lxml')
rankings = soup.find_all('table', class_="list_ranking")
movies = rankings[0].find_all('div', class_='tit3')


count = 0
for movie in movies:
    count += 1
    m = movie.find('a')
    insert_row(conn, count, m.get_text(), m['href'])
    ##print(m.get_text(), m['href'])

get_all_rows(conn)
conn.close()