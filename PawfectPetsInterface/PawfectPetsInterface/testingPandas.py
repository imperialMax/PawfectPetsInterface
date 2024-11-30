import pyodbc
import re
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

def testRegEx():

    text = "User=JohnDoe;Password=mySecretPass;Server=localhost" 
    pattern = r"Password=[^;]+" 
    match = re.search(pattern, text) 
    if match: 
        print("Found password:", match.group()) 
    else: 
        print("Password not found")










    # text_to_search = """
    #     abcdefghijklmnopqrstuvwxyz
    #     ABCDEFGHIJKLMNOPQRSTUVWXYZ
    #     1234567890

    #     Ha HaHa

    #     MetaCharacters (Need to be escaped):
    #     . ^ $ * + ? {} []  | ()

    #     coreyms.com

    #     321-555-4321
    #     123.555.1234

    #     Mr. Schafer
    #     Mr Smith
    #     Ms Davis
    #     Mrs. Robinson
    #     Mr. T
    # """
    # sentence =  'start a sentence and bring it to an end'

    # pattern = re.compile(r"abc")

    # matches = pattern.finditer(text_to_search)

    # for match in matches:
    #     print(match)
