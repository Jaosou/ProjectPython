import csv
from mysql import connector

def wri_csv(list_order_total):
    with open("data_projrct.csv","a+",encoding="UTF-8",newline='') as f :
        writ_csv = csv.writer(f)
        for i in list_order_total :
            writ_csv.writerow(i)

def connec_base(list_order_total):
    db = connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Jaosou*2003',
        database='data_computer'
    )

    cursor = db.cursor()
    sql = '''
        INSERT INTO order_data ( Order_datatitle, Order_price, datetime_order)
        VALUE(%s ,%s ,%s)
    '''
    cursor.executemany(sql, list_order_total)
    db.commit()
    print(f"Insert data {str(cursor.rowcount)} row\n")

