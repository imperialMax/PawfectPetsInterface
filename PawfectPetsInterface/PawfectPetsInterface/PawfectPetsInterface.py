import pyodbc
import suppliers as supp
import customers as cust
import products as prod
import testingPandas as pd
from argon2 import PasswordHasher
ph = PasswordHasher()
connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=LAPTOP-E8GVKM9S\SQLEXPRESS;"
    r"Database=ElysiumLuxuryDB;"
    r"Trusted_Connection=yes;"
    r"Column Encryption Setting=Enabled;"
    
)

# connection_string = (
#     r"Driver={ODBC Driver 17 for SQL Server};"
#     r"Server=10.221.64.20\SQLEXPRESS;"
#     r"Database=PawfectPetsDB;"
#     r"UID=MaxN;"
#     r"PWD=ysLDMKrLSUN9xSbH2PN7F8W1m0CDafK1jFaZGeUf10tHn4mMHz45mTs0Mk3vAwNoTAe5jDLEyvCOlD67X6dWyDKyHGdXJbIDcVBWNGmJMcA4ABn9JX3k9OWOQxuEXmp;"
#     r"Column Encryption Setting=Enabled;"
    
# )

global verifieduser 

verifieduser = False


def editSuppliers():
    supplierTransaction = input("Suppliers:" + "\n" +
                          "1. Select" + "\n" +
                          "2. Insert" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    match supplierTransaction:
        case "1":
            supp.SelectSuppliers()
        case "2":
            supp.InsertSuppliers()
        case "3":
            supp.UpdateSuppliers()
        case "4":
            supp.DeleteSuppliers()

def editProducts():
    productTransaction = input("Products:" + "\n" +
                          "1. Select" + "\n" +
                          "2. Insert" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    match productTransaction:
        case "1":
            prod.SelectProducts()
        case "2":
            prod.InsertProducts()
        case "3":
            prod.UpdateProducts()
        case "4":
            prod.DeleteProducts()

def editCustomers():
    customerTransaction = input("Customers:" + "\n" +
                          "1. Select" + "\n" +
                          "2. Insert" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    match customerTransaction:
        case "1":
            cust.SelectCustomers()
        case "2":
            cust.InsertCustomers()
        case "3":
            cust.UpdateCustomers()
        case "4":
            cust.DeleteCustomers()


def createUser():
    username = input("What will your username be?" + "\n")
    password = input("What will your password be?" + "\n")

    passwordHash = ph.hash(password)

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    insertQuery = """ INSERT INTO administrators (username, password) VALUES (?,?) """

    data = (username, passwordHash)

    cursor.execute(insertQuery, data)
    conn.commit()
    cursor.close()
    conn.close()
    
def verifyUser():
    global verifieduser
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        username = input("What is your username?" + "\n")
        password = input("What is your password?" + "\n")

        select_query = '''
            SELECT password FROM administrators WHERE username = ?
        '''

        cursor.execute(select_query, (username,))
        result = cursor.fetchone()

        if result:
            password_hash = result[0]
            if ph.verify(password_hash, password):
                
                verifieduser = True
                
            else:
                print("password is incorrect")
        else:
            print("username not found")
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        cursor.close()


while True:
    if verifieduser == True:
        break
    else:

        loginOrCreateAccount = input("Do you wish to login or create an account?" + "\n" + 
                                 "Please select an option by entering the corresponding number:" + "\n" +
                                 "1. Login" + "\n" +
                                 "2. Create Account" + "\n")

        match loginOrCreateAccount:
            case "1":
                verifyUser()
            case "2":
                createUser()
                createdaccount = True
            case "3":
                pd.testPandas()



while True:

    uInput = input("Welcome to the Pawfect Pets database" + "\n" +
                       "Please select an option by entering the corresponding number" + "\n" + 
                       "1. Edit Products" + "\n" +
                       "2. Edit Suppliers" + "\n" +
                       "3. Edit Customers" + "\n")
    match uInput:
        case "1":
            editProducts()
        case "2":
            editSuppliers()
        case "3":
            editCustomers()



