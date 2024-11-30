## CHECKED IT
import pyodbc
import pandas as pd
import re
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

def InsertProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        productInput = input("What is the name of the product?" + "\n")
        if re.match(r"^[a-zA-Z0-9 ]+$", productInput):
            pass
        else:
            print("Please only enter letters, numbers or spaces.")
            return

        costInput = input("what is the cost of the product?" + "\n")
        if re.match(r"^[0-9$]+$", costInput):
            pass
        else:
            print("Please only enter numbers or $.")
            return

        supplierInput = input("what is the ID of the supplier?" + "\n")
        if re.match(r"^[0-9]+$", supplierInput):
            pass
        else:
            print("Please only enter numbers")
            return

    
        insertQuery = """ INSERT INTO products (supplier_ID, product_name, product_cost) VALUES (?, ?, ?) """ 
    
        data = (supplierInput, productInput, costInput)

        cursor.execute(insertQuery,data)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def SelectProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                       + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
        if re.match(r"^[1-2 ]+$", uInput):
            pass
        elif re.match(r"^[03-9 ]+$", uInput):
            print("Please ensure you select an option that is available.")
            return
        else:
            print("Please only enter numbers")
            return

        match uInput:
            case "1":
                print("Here are the results of your search:" + "\n")

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

            case "2":
                uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                       + "\n" + "1. supplier_ID" 
                       + "\n" + "2. product_name" 
                       + "\n" + "3. product_cost" + "\n")
                if re.match(r"^[1-3 ]+$", uInput):
                    pass
                elif re.match(r"^[04-9]+$", uInput):
                    print("Please ensure you select an option that is available.")
                    return
                else:
                    print("Please only enter numbers.")
                    return

                match uInput:
                    case "1":

                        select_Query =    """SELECT supplier_ID FROM products"""            

                        cursor.execute(select_Query)
                        supplier_ID = cursor.fetchall()


                        data = {
                            "supplier_ID": supplier_ID,

                            }

                        df = pd.DataFrame(data)
                        print(df)
                        cursor.close()

                    case "2":

                        select_Query =    """SELECT product_name FROM products"""            

                        cursor.execute(select_Query)
                        product_name = cursor.fetchall()


                        data = {
                            "product_name": product_name,

                            }

                        df = pd.DataFrame(data)
                        print(df)

                        cursor.close()
                    case "3":

                        select_Query =    """SELECT product_cost FROM products"""            

                        cursor.execute(select_Query)
                        product_cost = cursor.fetchall()


                        data = {
                            "product_cost": product_cost,

                            }

                        df = pd.DataFrame(data)
                        print(df)

                        cursor.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def UpdateProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:

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
        if re.match(r"^[0-9]+$", product_ID):
            pass
        else:
            print("Please only enter numbers.")
            return

        product_row = input("What is the ROW number of the product you would like to edit?"
              + "\n" + "Select an option by entering the number appearing at the front of the row"
              + "\n")
        if re.match(r"^[0-9]+$", product_row):
            pass
        else:
            print("Please only enter numbers.")
            return

        uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
              + "\n" + "1. supplier_ID"
              + "\n" + "2. product_name" 
              + "\n" + "3. product_cost" + "\n")
        if re.match(r"^[1-3 ]+$", uInput):
            pass
        elif re.match(r"^[04-9]+$", uInput):
            print("Please ensure you select an option that is available.")
            return
        else:
            print("Please only enter numbers.")
            return

        match uInput:
            case "1":
                product_row = int(product_row)
                current_supplier_ID = str(df.loc[product_row,"supplier_ID"])
                updatedValue = input("The supplier_ID is currently " + current_supplier_ID
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[0-9]+$", updatedValue):
                    pass
                else:
                    print("Please only enter numbers.")
                    return

                product_row = str(product_row)
                update_Query = """
                    UPDATE products SET supplier_ID=? WHERE product_ID=?
                """

                data = (updatedValue,product_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()

            case "2":
                product_row = int(product_row)
                current_product_name = str(df.loc[product_row,"product_name"])
                updatedValue = input("The product_name is currently " + current_product_name
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[a-zA-Z0-9 ]+$", updatedValue):
                    pass
                else:
                    print("Please only enter letters, numbers or spaces.")
                    return

                product_row = str(product_row)
                update_Query = """
                    UPDATE products SET product_name=? WHERE product_ID=?
                """

                data = (updatedValue,product_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()
       
            case "3":
                product_row = int(product_row)
                current_product_cost = str(df.loc[product_row,"product_cost"])
                updatedValue = input("The product_cost is currently " + current_product_cost
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[0-9$]+$", updatedValue):
                    pass
                else:
                    print("Please only enter letters, numbers or spaces.")
                    return

                product_row = str(product_row)
                update_Query = """
                    UPDATE products SET product_cost=? WHERE product_ID=?
                """

                data = (updatedValue,product_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()

    except Exception as e:
        print(e)
    finally:
        conn.close()        

def DeleteProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:

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
        if re.match(r"^[1-2 ]+$", uInput):
            pass
        elif re.match(r"^[03-9]+$", uInput):
            print("Please ensure you select an option that is available.")
            return
        else:
            print("Please only enter numbers.")
            return


        match uInput:
            case "1":
                delete_Query = """
                    DELETE FROM products
                """

                cursor.execute(delete_Query)
                conn.commit()
                cursor.close()
            case "2":
                product_ID = input("What is the ID of the product that you want to delete?"
                  + "\n" + "Select an option by entering the number appearing at the front of the products list:"
                  + "\n")
                if re.match(r"^[1-3]+$", uInput):
                    pass
                elif re.match(r"^[04-9]+$", uInput):
                    print("Please ensure you select an option that is available.")
                    return
                else:
                    print("Please only enter numbers.")
                    return

                delete_Query = """
                        DELETE FROM products WHERE product_ID=?
                    """

                data = (product_ID)

                cursor.execute(delete_Query,data)
                conn.commit()
                cursor.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()