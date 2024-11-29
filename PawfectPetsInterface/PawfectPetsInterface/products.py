import pandas as pd
import pyodbc
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
class Products:
    def __init__(self, supplier_ID=None, product_name=None, product_cost=None):
        self.supplier_ID = supplier_ID
        self.product_name = product_name
        self.product_cost = product_cost

products = Products()

def InsertProducts():
    productInput = input("What is the name of the product?" + "\n")
    costInput = input("what is the cost of the product?" + "\n")
    supplierInput = input("what is the ID of the supplier?" + "\n")

    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO products (supplier_ID, product_name, product_cost) VALUES (?, ?, ?) """ 
    
    data = (supplierInput, productInput, costInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def SelectProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
    match uInput:
        case "1":
            print("Here are the results of your search:" + "\n")
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()

            select_Query =    """SELECT product_ID FROM products"""            

            cursor.execute(select_Query)
            product_ID = cursor.fetchall()


            select_Query =    """SELECT supplier_ID FROM products"""            

            cursor.execute(select_Query)
            supplier_ID = cursor.fetchall()

            select_Query =    """SELECT product_name FROM products"""            

            cursor.execute(select_Query)
            product_name = cursor.fetchall()

            select_Query =    """SELECT product_cost FROM products"""            

            cursor.execute(select_Query)
            product_cost = cursor.fetchall()


            data = {
                "product_ID": product_ID,
                "supplier_ID": supplier_ID,
                "product_name": product_name,
                "product_cost": product_cost
        
                }

            df = pd.DataFrame(data)
            print(df)

            cursor.close()
            conn.close()
        case "2":
            uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. supplier_ID" 
                   + "\n" + "2. product_name" 
                   + "\n" + "3. product_cost" + "\n")
            match uInput:
                case "1":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT supplier_ID FROM products"""            

                    cursor.execute(select_Query)
                    supplier_ID = cursor.fetchall()


                    data = {
                        "supplier_ID": supplier_ID,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()
                case "2":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT product_name FROM products"""            

                    cursor.execute(select_Query)
                    product_name = cursor.fetchall()


                    data = {
                        "product_name": product_name,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()
                case "3":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT product_cost FROM products"""            

                    cursor.execute(select_Query)
                    product_cost = cursor.fetchall()


                    data = {
                        "product_cost": product_cost,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()


def UpdateProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query =    """SELECT product_ID FROM products"""            

    cursor.execute(select_Query)
    product_ID = cursor.fetchall()


    select_Query =    """SELECT supplier_ID FROM products"""            

    cursor.execute(select_Query)
    supplier_ID = cursor.fetchall()

    select_Query =    """SELECT product_name FROM products"""            

    cursor.execute(select_Query)
    product_name = cursor.fetchall()

    select_Query =    """SELECT product_cost FROM products"""            

    cursor.execute(select_Query)
    product_cost = cursor.fetchall()


    data = {
        "product_ID": product_ID,
        "supplier_ID": supplier_ID,
        "product_name": product_name,
        "product_cost": product_cost
        
        }

    df = pd.DataFrame(data)

    print("Here is the contents of the table:" + "\n")
    print(df)
    product_ID = input("What is the ID number of the product you would like to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the row"
          + "\n")
    product_row = input("What is the ROW number of the product you would like to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the row"
          + "\n")
    uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
          + "\n" + "1. supplier_ID"
          + "\n" + "2. product_name" 
          + "\n" + "3. product_cost" + "\n")
    match uInput:
        case "1":
            product_row = int(product_row)
            current_supplier_ID = str(df.loc[product_row,"supplier_ID"])
            updatedValue = input("The supplier_name is currently " + current_supplier_ID
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            product_row = str(product_row)
            update_Query = """
                UPDATE products SET supplier_ID=? WHERE product_ID=?
            """

            data = (updatedValue,product_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "2":
            product_row = int(product_row)
            current_product_name = str(df.loc[product_row,"product_name"])
            updatedValue = input("The product_name is currently " + current_product_name
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            product_row = str(product_row)
            update_Query = """
                UPDATE products SET product_name=? WHERE product_ID=?
            """

            data = (updatedValue,product_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()        
        case "3":
            product_row = int(product_row)
            current_product_cost = str(df.loc[product_row,"product_cost"])
            updatedValue = input("The product_name is currently " + current_product_cost
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            product_row = str(product_row)
            update_Query = """
                UPDATE products SET product_cost=? WHERE product_ID=?
            """

            data = (updatedValue,product_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()        

def DeleteProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query =    """SELECT product_ID FROM products"""            

    cursor.execute(select_Query)
    product_ID = cursor.fetchall()


    select_Query =    """SELECT supplier_ID FROM products"""            

    cursor.execute(select_Query)
    supplier_ID = cursor.fetchall()

    select_Query =    """SELECT product_name FROM products"""            

    cursor.execute(select_Query)
    product_name = cursor.fetchall()

    select_Query =    """SELECT product_cost FROM products"""            

    cursor.execute(select_Query)
    product_cost = cursor.fetchall()


    data = {
        "product_ID": product_ID,
        "supplier_ID": supplier_ID,
        "product_name": product_name,
        "product_cost": product_cost
        
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
                DELETE FROM products
            """

            cursor.execute(delete_Query)
            conn.commit()
            cursor.close()
            conn.close()
        case "2":
            product_ID = input("What is the ID of the product that you want to delete?"
              + "\n" + "Select an option by entering the number appearing at the front of the products list:"
              + "\n")
            delete_Query = """
                    DELETE FROM products WHERE product_ID=?
                """

            data = (product_ID)

            cursor.execute(delete_Query,data)
            conn.commit()
            cursor.close()
            conn.close()