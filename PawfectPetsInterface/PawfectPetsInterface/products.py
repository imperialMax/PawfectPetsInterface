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
    
    data = (supplierInput, 
            productInput, costInput)

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
            select_Query = ''' 
                SELECT * FROM products
            '''
            cursor.execute(select_Query)
            result = cursor.fetchall()
            resultList = [result]
            print("Here are the results of your search:" + "\n")
            print(resultList)
            print("\n")
        case "2":
            uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. supplier_ID" 
                   + "\n" + "2. product_name" 
                   + "\n" + "3. product_cost")
            match uInput:
                case "1":
                    select_Query = ''' 
                        SELECT supplier_ID FROM products
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "2":
                    select_Query = ''' 
                        SELECT product_name FROM products
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "3":
                    select_Query = ''' 
                        SELECT product_cost FROM products
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")

    cursor.close()
    conn.close()

def UpdateProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query = ''' 
        SELECT * FROM products    
    '''
    cursor.execute(select_Query)
    result = cursor.fetchall()
    resultList = [result]

    print("Here is the contents of the table:" + "\n")
    print(resultList)

    uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
          + "\n" + "1. supplier_ID"
          + "\n" + "2. product_name" 
          + "\n" + "3. product_cost")
    product_ID = input("What is the ID of the product that you want to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the supplier's list:"
          + "\n")
    match uInput:
        case "1":
            updatedValue = input("The supplier_ID is currently " + products.supplier_ID + "." 
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            update_Query = """
                UPDATE products SET supplier_ID WHERE product_ID VALUES (?,?) 
            """

            data = (updatedValue,product_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "2":
            updatedValue = input("The product_name is currently " + products.product_name + "." 
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            update_Query = """
                UPDATE products SET product_name WHERE product_ID VALUES (?,?) 
            """

            data = (updatedValue,product_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
        case "3":
            updatedValue = input("The product_cost is currently " + products.product_cost + "." 
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            update_Query = """
                UPDATE products SET product_cost WHERE product_ID VALUES (?,?) 
            """

            data = (updatedValue,product_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()

def DeleteProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query = ''' 
        SELECT * FROM products     
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