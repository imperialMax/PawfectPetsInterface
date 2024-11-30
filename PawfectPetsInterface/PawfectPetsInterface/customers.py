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



def InsertCustomers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:


        firstNameInput = input("What is the customer's first name?" + "\n")
        if re.match(r"^[a-zA-Z ]+$", firstNameInput):
            pass
        else:
            print("Please only enter letters or spaces.")
            return

        lastNameInput = input("What is the customer's last name?" + "\n")
        if re.match(r"^[a-zA-Z ]+$", lastNameInput):
            pass
        else:
            print("Please only enter letters or spaces.")
            return

        emailInput = input("What is the customer's email?" + "\n")
        if re.match(r"^[a-zA-Z@.0-9 ]+$", emailInput):
            pass
        else:
            print("Please only enter letters, numbers, spaces, @ or .")
            return

        addressInput  = input("What is the customer's address?" + "\n")
        if re.match(r"^[a-zA-Z0-9 ]+$", addressInput):
            pass
        else:
            print("Please only enter letters, spaces or numbers.")
            return

        phoneNumberInput  = input("What is the customer's phone number?" + "\n")
        if re.match(r"^[0-9 ]+$", phoneNumberInput):
            pass
        else:
            print("Please only enter numbers.")
            return



        insertQuery = """ INSERT INTO customers (first_name, last_name, email, address, phone_number) VALUES (?, ?, ?, ?, ?) """

        data = (firstNameInput, lastNameInput, emailInput, addressInput, phoneNumberInput)

        cursor.execute(insertQuery,data)
        conn.commit()
        cursor.close()
    except Exception as e:
        print(e)

    finally:
        conn.close()

def SelectCustomers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:

        uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                       + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
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
                print("Here are the results of your search:" + "\n")

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

            case "2":
                uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                       + "\n" + "1. first_name" 
                       + "\n" + "2. last_name" 
                       + "\n" + "3. email"
                       + "\n" + "4. address"
                       + "\n" + "5. phone_number"
                       + "\n")
                if re.match(r"^[1-5 ]+$", uInput):
                    pass
                elif re.match(r"^[06-9]+$", uInput):
                    print("Please ensure you select an option that is available.")
                    return
                else:
                    print("Please only enter numbers.")
                    return

                match uInput:
                    case "1":

                        select_Query =    """SELECT first_name FROM customers"""            

                        cursor.execute(select_Query)
                        first_name = cursor.fetchall()


                        data = {
                            "first_name": first_name,

                            }

                        df = pd.DataFrame(data)
                        print(df)

                        cursor.close()

                    case "2":

                        select_Query =    """SELECT last_name FROM customers"""            

                        cursor.execute(select_Query)
                        last_name = cursor.fetchall()


                        data = {
                            "last_name": last_name,

                            }

                        df = pd.DataFrame(data)
                        print(df)

                        cursor.close()

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

                    case "4":


                        select_Query =    """SELECT address FROM customers"""            

                        cursor.execute(select_Query)
                        address = cursor.fetchall()


                        data = {
                            "address": address,

                            }

                        df = pd.DataFrame(data)
                        print(df)

                        cursor.close()

                    case "5":

                        select_Query =    """SELECT phone_number FROM customers"""            

                        cursor.execute(select_Query)
                        phone_number = cursor.fetchall()


                        data = {
                            "phone_number": phone_number,

                            }

                        df = pd.DataFrame(data)
                        print(df)

                        cursor.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def UpdateCustomers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:

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
        if re.match(r"^[0-9]+$", customer_ID):
            pass
        else:
            print("Please only enter numbers.")
            return

        customer_row = input("What is the ROW number of the customer you would like to edit?"
              + "\n" + "Select an option by entering the number appearing at the front of the row"
              + "\n")
        if re.match(r"^[0-9]+$", customer_row):
            pass
        else:
            print("Please only enter numbers.")
            return


        uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
              + "\n" + "1. first_name"
              + "\n" + "2. last_name" 
              + "\n" + "3. email"
              + "\n" + "4. address"
              + "\n" + "5. phone_number" + "\n")
        if re.match(r"^[1-5 ]+$", uInput):
            pass
        elif re.match(r"^[06-9]+$", uInput):
            print("Please ensure you select an option that is available.")
            return
        else:
            print("Please only enter numbers.")
            return


        match uInput:
            case "1":
                customer_row = int(customer_row)
                current_first_name = str(df.loc[customer_row,"first_name"])
                updatedValue = input("The first_name is currently " + current_first_name
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[a-zA-Z ]+$", updatedValue):
                    pass
                else:
                    print("Please only enter letters or spaces.")
                    return

                customer_row = str(customer_row)
                update_Query = """
                    UPDATE customers SET first_name=? WHERE customer_ID=?
                """

                data = (updatedValue,customer_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()

            case "2":
                customer_row = int(customer_row)
                current_last_name = str(df.loc[customer_row,"last_name"])
                updatedValue = input("The last_name is currently " + current_last_name
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[a-zA-Z ]+$", updatedValue):
                    pass
                else:
                    print("Please only enter letters or spaces.")
                    return

                customer_row = str(customer_row)
                update_Query = """
                    UPDATE customers SET last_name=? WHERE customer_ID=?
                """

                data = (updatedValue,customer_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()

            case "3":
                customer_row = int(customer_row)
                current_email = str(df.loc[customer_row,"email"])
                updatedValue = input("The email is currently " + current_email
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[a-zA-Z0-9.@ ]+$", updatedValue):
                    pass
                else:
                    print("Please only enter letters, numbers, spaces, @ or .")
                    return

                customer_row = str(customer_row)
                update_Query = """
                    UPDATE customers SET email=? WHERE customer_ID=?
                """

                data = (updatedValue,customer_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()

            case "4":
                customer_row = int(customer_row)
                current_address = str(df.loc[customer_row,"address"])
                updatedValue = input("The addesss is currently " + current_address
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[a-zA-Z0-9 ]+$", updatedValue):
                    pass
                else:
                    print("Please only enter letters, numbers or spaces.")
                    return

                customer_row = str(customer_row)
                update_Query = """
                    UPDATE customers SET address=? WHERE customer_ID=?
                """

                data = (updatedValue,customer_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()

            case "5":
                customer_row = int(customer_row)
                current_phone_number = str(df.loc[customer_row,"phone_number"])
                updatedValue = input("The phone_number is currently " + current_phone_number
                                     + "\n" + "What should the updated value be?" 
                                     + "\n")
                if re.match(r"^[0-9 ]+$", updatedValue):
                    pass
                else:
                    print("Please only enter numbers.")
                    return

                customer_row = str(customer_row)
                update_Query = """
                    UPDATE customers SET phone_number=? WHERE customer_ID=?
                """

                data = (updatedValue,customer_ID)

                cursor.execute(update_Query,data)
                conn.commit()
                cursor.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def DeleteCustomers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:

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
                    DELETE FROM customers
                """

                cursor.execute(delete_Query)
                conn.commit()
                cursor.close()

            case "2":
                user_ID     = input("What is the ID of the customer that you want to delete?"
                  + "\n" + "Select an option by entering the number appearing at the front of the suppliers list:"
                  + "\n")
                if re.match(r"^[0-9]+$", uInput):
                    pass
                else:
                    print("Please only enter numbers.")
                    return

                delete_Query = """
                        DELETE FROM customers WHERE customer_ID=?
                    """

                data = (user_ID)

                cursor.execute(delete_Query,data)
                conn.commit()
                cursor.close()

    except Exception as e:
        print(e)
    finally:
        conn.close()
