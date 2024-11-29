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
class Customers:
    def __init__(self, first_name=None, last_name=None, email=None, address=None, phone_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone_number = phone_number


def InsertCustomers():

    customers = Customers()

    customers.first_name = input("What is the customer's first name?" + "\n")
    customers.last_name = input("What is the customer's last name?" + "\n")
    customers.email = input("What is the customer's email?" + "\n")
    customers.address  = input("What is the customer's address?" + "\n")
    customers.phone_number  = input("What is the customer's phone number?" + "\n")


    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    insertQuery = """ INSERT INTO customers (first_name, last_name, email, address, phone_number) VALUES (?, ?, ?, ?, ?) """

    data = (customers.first_name, customers.last_name, customers.email, customers.address, customers.phone_number)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def SelectCustomers():

    customers = Customers()

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
    match uInput:
        case "1":
            print("Here are the results of your search:" + "\n")
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()

            select_Query =    """SELECT customer_ID FROM customers"""            

            cursor.execute(select_Query)
            customer_ID = cursor.fetchall()


            select_Query =    """SELECT first_name FROM customers"""            

            cursor.execute(select_Query)
            first_name = cursor.fetchall()

            select_Query =    """SELECT last_name FROM customers"""            

            cursor.execute(select_Query)
            last_name = cursor.fetchall()

            select_Query =    """SELECT email FROM customers"""            

            cursor.execute(select_Query)
            email = cursor.fetchall()

            select_Query =    """SELECT address FROM customers"""            

            cursor.execute(select_Query)
            address = cursor.fetchall()

            select_Query =    """SELECT phone_number FROM customers"""            

            cursor.execute(select_Query)
            phone_number = cursor.fetchall()


            data = {
                "product_ID": customer_ID,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "address": address,
                "phone_number": phone_number
        
                }

            df = pd.DataFrame(data)
            print(df)

            cursor.close()
            conn.close()
        case "2":
            uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. first_name" 
                   + "\n" + "2. last_name" 
                   + "\n" + "3. email"
                   + "\n" + "4. address"
                   + "\n" + "5. phone_number"
                   + "\n")
            match uInput:
                case "1":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT first_name FROM customers"""            

                    cursor.execute(select_Query)
                    first_name = cursor.fetchall()


                    data = {
                        "first_name": first_name,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()
                case "2":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT last_name FROM customers"""            

                    cursor.execute(select_Query)
                    last_name = cursor.fetchall()


                    data = {
                        "last_name": last_name,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()
                case "3":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT email FROM customers"""            

                    cursor.execute(select_Query)
                    email = cursor.fetchall()


                    data = {
                        "email": email,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()
                case "4":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT address FROM customers"""            

                    cursor.execute(select_Query)
                    address = cursor.fetchall()


                    data = {
                        "address": address,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()
                case "5":
                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    select_Query =    """SELECT phone_number FROM customers"""            

                    cursor.execute(select_Query)
                    phone_number = cursor.fetchall()


                    data = {
                        "phone_number": phone_number,

                        }

                    df = pd.DataFrame(data)
                    print(df)

                    cursor.close()
                    conn.close()


def UpdateCustomers():
    
    customers = Customers()

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query =    """SELECT customer_ID FROM customers"""            

    cursor.execute(select_Query)
    customer_ID = cursor.fetchall()


    select_Query =    """SELECT first_name FROM customers"""            

    cursor.execute(select_Query)
    first_name = cursor.fetchall()

    select_Query =    """SELECT last_name FROM customers"""            

    cursor.execute(select_Query)
    last_name = cursor.fetchall()

    select_Query =    """SELECT email FROM customers"""            

    cursor.execute(select_Query)
    email = cursor.fetchall()

    select_Query =    """SELECT address FROM customers"""            

    cursor.execute(select_Query)
    address = cursor.fetchall()

    select_Query =    """SELECT phone_number FROM customers"""            

    cursor.execute(select_Query)
    phone_number = cursor.fetchall()


    data = {
        "customer_ID": customer_ID,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "address": address,
        "phone_number": phone_number,
        
        }

    df = pd.DataFrame(data)

    print("Here is the contents of the table:" + "\n")
    print(df)
    customer_ID = input("What is the ID number of the customer you would like to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the row"
          + "\n")
    customer_row = input("What is the ROW number of the customer you would like to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the row"
          + "\n")

    uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
          + "\n" + "1. first_name"
          + "\n" + "2. last_name" 
          + "\n" + "3. email"
          + "\n" + "4. address"
          + "\n" + "5. phone_number" + "\n")

    match uInput:
        case "1":
            customer_row = int(customer_row)
            current_first_name = str(df.loc[customer_row,"first_name"])
            updatedValue = input("The first_name is currently " + current_first_name
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            customer_row = str(customer_row)
            update_Query = """
                UPDATE customers SET first_name=? WHERE customer_ID=?
            """

            data = (updatedValue,customer_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "2":
            customer_row = int(customer_row)
            current_last_name = str(df.loc[customer_row,"last_name"])
            updatedValue = input("The last_name is currently " + current_last_name
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            customer_row = str(customer_row)
            update_Query = """
                UPDATE customers SET last_name=? WHERE customer_ID=?
            """

            data = (updatedValue,customer_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "3":
            customer_row = int(customer_row)
            current_email = str(df.loc[customer_row,"email"])
            updatedValue = input("The email is currently " + current_email
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            customer_row = str(customer_row)
            update_Query = """
                UPDATE customers SET email=? WHERE customer_ID=?
            """

            data = (updatedValue,customer_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "4":
            customer_row = int(customer_row)
            current_address = str(df.loc[customer_row,"address"])
            updatedValue = input("The addesss is currently " + current_address
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            customer_row = str(customer_row)
            update_Query = """
                UPDATE customers SET address=? WHERE customer_ID=?
            """

            data = (updatedValue,customer_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "5":
            customer_row = int(customer_row)
            current_phone_number = str(df.loc[customer_row,"phone_number"])
            updatedValue = input("The phone_number is currently " + current_phone_number
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            customer_row = str(customer_row)
            update_Query = """
                UPDATE customers SET phone_number=? WHERE customer_ID=?
            """

            data = (updatedValue,customer_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()

def DeleteCustomers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query =    """SELECT customer_ID FROM customers"""            

    cursor.execute(select_Query)
    customer_ID = cursor.fetchall()


    select_Query =    """SELECT first_name FROM customers"""            

    cursor.execute(select_Query)
    first_name = cursor.fetchall()

    select_Query =    """SELECT last_name FROM customers"""            

    cursor.execute(select_Query)
    last_name = cursor.fetchall()

    select_Query =    """SELECT email FROM customers"""            

    cursor.execute(select_Query)
    email = cursor.fetchall()

    select_Query =    """SELECT address FROM customers"""            

    cursor.execute(select_Query)
    address = cursor.fetchall()

    select_Query =    """SELECT phone_number FROM customers"""            

    cursor.execute(select_Query)
    phone_number = cursor.fetchall()



    data = {
        "customer_ID": customer_ID,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "address": address,
        "phone_number": phone_number
        
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
                DELETE FROM customers
            """

            cursor.execute(delete_Query)
            conn.commit()
            cursor.close()
            conn.close()
        case "2":
            user_ID     = input("What is the ID of the customer that you want to delete?"
              + "\n" + "Select an option by entering the number appearing at the front of the suppliers list:"
              + "\n")
            delete_Query = """
                    DELETE FROM customers WHERE customer_ID=?
                """

            data = (user_ID)

            cursor.execute(delete_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
