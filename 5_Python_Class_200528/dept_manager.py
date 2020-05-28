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
    cursor.execute("SELECT * FROM DEPT")
    for row in cursor:
        print(row)
    cursor.close()

def get_rows_key(conn, key):
    cursor = conn.cursor()
    str_sql = "SELECT * FROM DEPT WHERE DEPT_ID = :dept_id"
    cursor.execute(str_sql, {'dept_id' : key})
    row = cursor.fetchall()
    print(row)
    cursor.close()

def insert_row(conn, dept_id, dept_name, loc_id):
    cursor = conn.cursor()
    str_sql = "INSERT INTO DEPT VALUES(:dept_id, :dept_name, :loc_id)"
    cursor.execute(str_sql, \
        {'dept_id': dept_id, 'dept_name' : dept_name, 'loc_id':loc_id})
    conn.commit()
    cursor.close()

def update_row(conn, dept_id, dept_name, loc_id):
    cursor = conn.cursor()
    str_sql = "UPDATE DEPT SET dept_name=:dept_name, " + \
        "loc_id=:loc_id WHERE dept_id=:dept_id"
    cursor.execute(str_sql, \
        {'dept_id': dept_id, 'dept_name' : dept_name, \
            'loc_id':loc_id})
    conn.commit()
    cursor.close()

def delete_row(conn, dept_id):
    cursor = conn.cursor()
    str_sql = "DELETE FROM DEPT WHERE dept_id=:dept_id"
    cursor.execute(str_sql, \
        {'dept_id': dept_id })
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
        dept_id = int(input("부서코드를 입력해주세요.: "))
        dept_name = input("부서명을 입력해주세요.: ")
        loc_id = int(input("위치코드를 입력해주세요.: "))
        conn = get_conn()
        insert_row(conn, dept_id, dept_name, loc_id)
        conn.close()
    elif num == "4":
        dept_id = int(input("부서코드를 입력해주세요.: "))
        dept_name = input("부서명을 입력해주세요.: ")
        loc_id = int(input("위치코드를 입력해주세요.: "))
        conn = get_conn()
        update_row(conn, dept_id, dept_name, loc_id)
        conn.close()
    elif num == "5":
        dept_id = int(input("부서코드를 입력해주세요.: "))
        conn = get_conn()
        delete_row(conn, dept_id)
        conn.close()
    elif num == "6":
        print("종료되었습니다. 감사합니다. 안녕히 가십시요.")
        time.sleep(1)
        break
    else:
        os.system("cls")