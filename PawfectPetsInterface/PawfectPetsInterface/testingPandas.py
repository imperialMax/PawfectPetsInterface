import pyodbc
import pandas as pd
from argon2 import PasswordHasher
ph = PasswordHasher()
connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=LAPTOP-E8GVKM9S\SQLEXPRESS;"
    r"Database=ElysiumLuxuryDB;"
    r"Trusted_Connection=yes;"
    r"Column Encryption Setting=Enabled;"
    
)

def testPandas():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query =    """SELECT supplier_ID FROM suppliers"""            

    cursor.execute(select_Query)
    supplier_ID = cursor.fetchall()


    select_Query =    """SELECT supplier_name FROM suppliers"""            

    cursor.execute(select_Query)
    supplier_name = cursor.fetchall()

    select_Query =    """SELECT supplier_email FROM suppliers"""            

    cursor.execute(select_Query)
    supplier_email = cursor.fetchall()


    data = {
        "supplier_ID": supplier_ID,
        "supplier_name": supplier_name,
        "supplier_email": supplier_email
        
        }

    df = pd.DataFrame(data)
    print(df)

    cursor.close()
    conn.close()
