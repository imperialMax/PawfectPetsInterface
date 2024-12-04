## CHECKED IT
import pyodbc
import pandas as pd
import re
import os
import suppliers as supp
import customers as cust
import products as prod
import testingPandas as tpd
from dotenv import load_dotenv
from argon2 import PasswordHasher
ph = PasswordHasher()
# load_dotenv()

UID = os.getenv('USER_ID')
print(UID)
PWD = os.getenv('PASS_WORD')

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
#     f"UID={UID};"
#     f"PWD={PWD};"
#     r"Column Encryption Setting=Enabled;"
    
# )
pd.set_option('display.expand_frame_repr', False)
global verifieduser 
global adminUser
global basicUser

verifieduser = False
adminUser = False
basicUser = True


def editSuppliers():
    supplierTransaction = input("Suppliers:" + "\n" +
                          "1. Insert" + "\n" +
                          "2. Select" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    if re.match(r"^[1-4 ]+$", supplierTransaction):
        pass
    elif re.match(r"^[05-9]+$", supplierTransaction):
        print("Please ensure you select an option that is available.")
    else:
        print("Please only enter numbers.")

    match supplierTransaction:
        case "1":
            try:
                supp.InsertSuppliers()
            except Exception as e:
                print(e)
        case "2":
            try:
                supp.SelectSuppliers()
            except Exception as e:
                print(e)
        case "3":
            try:
                supp.UpdateSuppliers()
            except Exception as e:
                print(e)
        case "4":
            try:
                supp.DeleteSuppliers()
            except Exception as e:
                print(e)

def editProducts():
    productTransaction = input("Products:" + "\n" +
                          "1. Insert" + "\n" +
                          "2. Select" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    if re.match(r"^[1-4 ]+$", productTransaction):
        pass
    elif re.match(r"^[05-9]+$", productTransaction):
        print("Please ensure you select an option that is available.")
    else:
        print("Please only enter numbers.")

    match productTransaction:
        case "1":
            try:
                prod.InsertProducts()
            except Exception as e:
                print(e)
        case "2":
            try:
                prod.SelectProducts()
            except Exception as e:
                print(e)
        case "3":
            try:
                prod.UpdateProducts()
            except Exception as e:
                print(e)
        case "4":
            try:
                prod.DeleteProducts()
            except Exception as e:
                print(e)

def editCustomers():
    customerTransaction = input("Customers:" + "\n" +
                          "1. Insert" + "\n" +
                          "2. Select" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    if re.match(r"^[1-4 ]+$", customerTransaction):
        pass
    elif re.match(r"^[05-9]+$", customerTransaction):
        print("Please ensure you select an option that is available.")
    else:
        print("Please only enter numbers.")

    match customerTransaction:
        case "1":
            try:
                cust.InsertCustomers()
            except Exception as e:
                print(e)

        case "2":
            try:
                cust.SelectCustomers()
            except Exception as e:
                print(e)

        case "3":
            try:
                cust.UpdateCustomers()
            except Exception as e:
                print(e)
        case "4":
            try:
                cust.DeleteCustomers()
            except Exception as e:
                print(e)


def createUser():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        username = input("What will your username be?" + "\n")
        if re.match(r"^[a-zA-Z0-9 ]+$", username):
            pass
        else:
            print("Please only enter letters, numbers or spaces")
            return

        password = input("What will your password be?" + "\n")
        if re.match(r"^[a-zA-Z0-9 !@#$%^&*,.]+$", password):
            pass
        else:
            print("Please only enter letters, numbers, spaces, !, @, #, $, %, ^, &, *, , and .")
            return

        passwordHash = ph.hash(password)

        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        insertQuery = """ INSERT INTO users (username, password) VALUES (?,?) """

        data = (username, passwordHash)

        cursor.execute(insertQuery, data)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def createAdministrator():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        username = input("What will your username be?" + "\n")
        if re.match(r"^[a-zA-Z0-9 ]+$", username):
            pass
        else:
            print("Please only enter letters, numbers or spaces")
            return

        password = input("What will your password be?" + "\n")
        if re.match(r"^[a-zA-Z0-9 !@#$%^&*,.]+$", password):
            pass
        else:
            print("Please only enter letters, numbers, spaces, !, @, #, $, %, ^, &, *, , and .")
            return

        passwordHash = ph.hash(password)

        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        insertQuery = """ INSERT INTO administrators (username, password) VALUES (?,?) """

        data = (username, passwordHash)

        cursor.execute(insertQuery, data)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()

    
def verifyUser():
    global verifieduser
    global adminUser
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        username = input("What is your username?" + "\n")
        if re.match(r"^[a-zA-Z0-9 ]+$", username):
            pass
        else:
            print("Please only enter letters, numbers or spaces.")
            return

        password = input("What is your password?" + "\n")
        if re.match(r"^[a-zA-Z0-9 !@#$%^&*,.]+$", password):
            pass
        else:
            print("Please only enter letters, numbers, spaces, !, @, #, $, %, ^, &, *, , and .")
            return
        select_query = '''
            SELECT password FROM users WHERE username = ?
        '''

        cursor.execute(select_query, (username,))
        result = cursor.fetchone()

        if result:
            password_hash = result[0]
            if ph.verify(password_hash, password):
                verifieduser = True

                
            else:
                print("The password is incorrect.")

        else:
                select_query = '''
                    SELECT password FROM administrators WHERE username = ?
                '''
                cursor.execute(select_query, (username,))
                result = cursor.fetchone()
                password_hash = result[0]
                if result:
                    if ph.verify(password_hash, password):
                        verifieduser = True
                        adminUser = True

                    else:
                        print("The password is incorrect.")
                else:
                    print("The username is incorrect.")
    except Exception as e:
        print(e)
    finally:
        cursor.close()


while True:
    if verifieduser == True:
        break
    else:
        tpd.testEnv()
        uInput = input("Do you wish to login or create an account?" + "\n" + 
                                 "Please select an option by entering the corresponding number:" + "\n" +
                                 "1. Login" + "\n" +
                                 "2. Create Account" + "\n")
        if re.match(r"^[1-2 ]+$", uInput):
            pass
        elif re.match(r"^[03-9]+$", uInput):
            print("Please ensure you select an option that is available.")
        else:
            print("Please only enter numbers.")


        match uInput:
            case "1":
                try:
                    verifyUser()
                except Exception as e:
                    print(e)
            case "2":
                try:
                    createUser()
                    createdaccount = True
                except Exception as e:
                    print(e)


if adminUser == True:

    while True:

        uInput = input("Welcome to the Pawfect Pets database" + "\n" +
                           "Please select an option by entering the corresponding number" + "\n" + 
                           "1. Edit Products" + "\n" +
                           "2. Edit Suppliers" + "\n" +
                           "3. Edit Customers" + "\n" +
                           "4. Add Administrator" + "\n")
        if re.match(r"^[1-3 ]+$", uInput):
            pass
        elif re.match(r"^[05-9]+$", uInput):
            print("Please ensure you select an option that is available.")
            pass
        else:
            print("Please only enter numbers.")
            pass

        match uInput:
            case "1":
                editProducts()
            case "2":
                editSuppliers()
            case "3":
                editCustomers()
            case "4":
                createAdministrator()

elif basicUser == True:

        while True:

            uInput = input("Welcome to the Pawfect Pets database" + "\n" +
                               "Please select an option by entering the corresponding number" + "\n" + 
                               "1. View Products" + "\n" +
                               "2. View Suppliers" + "\n" +
                               "3. View Customers" + "\n"
                               "4. Add User" + "\n")
            if re.match(r"^[1-4 ]+$", uInput):
                pass
            elif re.match(r"^[05-9]+$", uInput):
                print("Please ensure you select an option that is available.")
                pass
            else:
                print("Please only enter numbers.")
                pass

            match uInput:
                case "1":
                    prod.SelectProducts()
                case "2":
                    supp.SelectSuppliers()
                case "3":
                    cust.SecureSelectCustomers()
                case "4":
                    createUser()

else:
    print("how did you get in")




