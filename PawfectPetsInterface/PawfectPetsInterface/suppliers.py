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
pd.set_option('display.expand_frame_repr', False)
class Suppliers:
    def __init__(self, supplier_name=None, supplier_email=None):
        self.supplier_name = supplier_name
        self.supplier_email = supplier_email

suppliers = Suppliers()

def InsertSuppliers():
    supplierInput = input("What is the name of the supplier?" + "\n")
    contactInput = input("What is the contact email of the supplier?" + "\n")  


    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO suppliers (supplier_name, supplier_email) VALUES (?,?) """ 
    
    data = (supplierInput, contactInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def SelectSuppliers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
    match uInput:
        case "1":
            print("Here are the results of your search:" + "\n")
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
        case "2":
            uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. supplier_name" + "\n" + "2. supplier_email" + "\n")
            match uInput:
                case "1":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT supplier_name FROM suppliers"""            

                    cursor.execute(select_Query)
                    supplier_name = cursor.fetchall()


                    data = {
                        "supplier_name": supplier_name,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()
                case "2":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT supplier_email FROM suppliers"""            

                    cursor.execute(select_Query)
                    supplier_email = cursor.fetchall()


                    data = {
                        "supplier_email": supplier_email
        
                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()

def UpdateSuppliers():
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

    print("Here is the contents of the table:" + "\n")
    print(df)
    supplier_ID = input("What is the ID number of the supplier you would like to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the row"
          + "\n")
    supplier_row = input("What is the ROW number of the supplier you would like to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the row"
          + "\n")
    uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
          + "\n" + "1. supplier_name"
          + "\n" + "2. supplier_email" + "\n")
    match uInput:
        case "1":
            supplier_row = int(supplier_row)
            current_name = str(df.loc[supplier_row,"supplier_name"])
            updatedValue = input("The supplier_name is currently " + current_name
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            supplier_row = str(supplier_row)
            update_Query = """
                UPDATE suppliers SET supplier_name=? WHERE supplier_ID=?
            """

            data = (updatedValue,supplier_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "2":
            supplier_row = int(supplier_row)
            current_email = str(df.loc[supplier_row,"supplier_email"])
            updatedValue = input("The supplier_email is currently " + current_email
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            supplier_row = str(supplier_row)
            update_Query = """
                UPDATE suppliers SET supplier_email=? WHERE supplier_ID=?
            """

            data = (updatedValue,supplier_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()

def DeleteSuppliers():
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

    print("Here is the contents of the table:" + "\n")
    print(df)

    uInput = input("\n" + "What would you like to delete?" + "\n" + "Select an option by entering the corresponding number:" 
          + "\n" + "1. All records"
          + "\n" + "2. One row" 
          + "\n")
    match uInput:
        case "1":
            delete_Query = """
                DELETE FROM suppliers
            """
            
            cursor.execute(delete_Query)
            conn.commit()
            cursor.close()
            conn.close()
        case "2":
            supplier_ID = input("What is the ID of the supplier that you want to delete?"
              + "\n" + "Select an option by entering the ID of the supplier:" #### i wanted row number but had to settle for id
              + "\n")
            delete_Query = """
                    DELETE FROM suppliers WHERE supplier_ID=?
                """

            data = (supplier_ID)

            cursor.execute(delete_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
