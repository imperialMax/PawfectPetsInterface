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
            select_Query = ''' 
                SELECT * FROM customers
            '''
            cursor.execute(select_Query)
            result = cursor.fetchall()
            resultList = [result]
            print("Here are the results of your search:" + "\n")
            print(resultList)
            print("\n")
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
                    select_Query = ''' 
                        SELECT first_name FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "2":
                    select_Query = ''' 
                        SELECT last_name FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "3":
                    select_Query = ''' 
                        SELECT email FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "4":
                    select_Query = ''' 
                        SELECT address FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "5":
                    select_Query = ''' 
                        SELECT phone_number FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")



    cursor.close()
    conn.close()

def UpdateCustomers():
    
    customers = Customers()

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query = ''' 
        SELECT * FROM customers   
    '''
    cursor.execute(select_Query)
    result = cursor.fetchall()

    print("Here is the contents of the table:" + "\n")
    print(result)
    uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
          + "\n" + "1. first_name"
          + "\n" + "2. last_name" 
          + "\n" + "3. email"
          + "\n" + "address"
          + "\n" + "phone_number" + "\n")

    customer_ID = input("What is the ID of the customer that you want to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the customers list:"
          + "\n")
    match uInput:
        case "1":
            updatedValue = input("The first_name is currently " + customers.first_name + "." 
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            update_Query = """
                UPDATE customers SET first_name WHERE customer_ID VALUES (?,?) 
            """

            data = (updatedValue,customer_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()

def DeleteCustomers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query = ''' 
        SELECT * FROM customers   
    '''
    cursor.execute(select_Query)
    result = cursor.fetchall()
    resultList = [result]

    print("Here is the contents of the table:" + "\n")
    print(resultList)

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
            user_ID           = input("What is the ID of the customer that you want to delete?"
              + "\n" + "Select an option by entering the number appearing at the front of the suppliers list:"
              + "\n")
            delete_Query = """
                    DELETE FROM customers WHERE user_ID=?
                """

            data = (user_ID)

            cursor.execute(delete_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
