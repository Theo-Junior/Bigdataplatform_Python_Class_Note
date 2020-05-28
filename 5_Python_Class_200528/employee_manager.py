import os
import cx_Oracle
import time
DB_ID = "system"
DB_PWD = "oracle"
DB_URL = "localhost/xe"
# region "주석 및 fold"
# endregion

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    #print(conn.version)
    return conn

def get_all_rows(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPLOYEE")
    for row in cursor:
        print(row)
    cursor.close()

def get_rows_key(conn, key):
    cursor = conn.cursor()
    str_sql = "SELECT * FROM EMPLOYE WHERE id = :id"
    cursor.execute(str_sql, {'id' : key})
    row = cursor.fetchall()
    print(row)
    cursor.close()

def insert_row(conn, id, name, email):
    cursor = conn.cursor()
    str_sql = "INSERT INTO EMPLOYE VALUES(:id, :name, :email)"
    cursor.execute(str_sql, \
        {'id': id, 'name' : name, 'email':email})
    conn.commit()
    cursor.close()

def update_row(conn, id, name, email):
    cursor = conn.cursor()
    str_sql = "UPDATE EMPLOYE SET name=:name, " + \
        "email=:email WHERE id=:id"
    cursor.execute(str_sql, \
        {'id': id, 'name' : name, \
            'email':email})
    conn.commit()
    cursor.close()

def delete_row(conn, id):
    cursor = conn.cursor()
    str_sql = "DELETE FROM EMPLOYE WHERE id=:id"
    cursor.execute(str_sql, \
        {'id': id })
    conn.commit()
    cursor.close()

while True:
    print("########부서관리#######")
    print(" 1. 전체               ")
    print(" 2. 검색               ")
    print(" 3. 추가               ")
    print(" 4. 수정               ")
    print(" 5. 삭제               ")
    print(" 6. 종료               ")
    print("#######################")
    num = input("번호를 입력해주세요.[1-6]: ")
    
    if num == "1":
        conn = get_conn()
        get_all_rows(conn)
        conn.close()
    elif num == "2":
        key = int(input("부서코드를 입력해주세요.: "))
        conn = get_conn()
        get_rows_key(conn, key)
        conn.close()
    elif num == "3":
        id = int(input("부서코드를 입력해주세요.: "))
        name = input("부서명을 입력해주세요.: ")
        email = int(input("위치코드를 입력해주세요.: "))
        conn = get_conn()
        insert_row(conn, id, name, email)
        conn.close()
    elif num == "4":
        id = int(input("부서코드를 입력해주세요.: "))
        name = input("부서명을 입력해주세요.: ")
        email = int(input("위치코드를 입력해주세요.: "))
        conn = get_conn()
        update_row(conn, id, name, email)
        conn.close()
    elif num == "5":
        id = int(input("부서코드를 입력해주세요.: "))
        conn = get_conn()
        delete_row(conn, id)
        conn.close()
    elif num == "6":
        print("종료되었습니다. 감사합니다. 안녕히 가십시요.")
        time.sleep(1)
        break
    else:
        os.system("cls")