import os
from dotenv import load_dotenv
load_dotenv()



UID = os.getenv('USER_ID')

PWD = os.getenv('PASS_WORD')

def returnConnectionString():
    
    UID = os.getenv('USER_ID')
    
    PWD = os.getenv('PASS_WORD')


    connection_string = (
        r"Driver={ODBC Driver 17 for SQL Server};"
        r"Server=10.221.64.20\SQLEXPRESS;"
        r"Database=PawfectPetsDB;"
        f"UID={UID};"
        f"PWD={PWD};"
        r"Column Encryption Setting=Enabled;"
    
    )
    return connection_string
