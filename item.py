import mysql.connector

def new_item(name):
    # connects to the database
    connection = mysql.connector.connect(user=open('username.txt').readline(), database='inventorium')
    cursor = connection.cursor()

    add_item = (
            "INSERT INTO items "
            "(itemname, cost, quantity, description)"
            "VALUES (%(itemname)s, %(cost)s, %(quantity)s, %(description)s)"
            )
    # ensures that the name is shorter than twenty characters, then commits the new object's data to the database
    if len(name) < 20:

        item_data = {'itemname': name,
             'cost': input("Cost of item: "),
             'quantity': input("Quantity in stock: "),
             'description': input("Description: ")
                    }

        cursor.execute(add_item, item_data)
        connection.commit()

    if len(name) > 20:
        print("Please enter a name shorter than 20 characters.")

    cursor.close()
    connection.close()

def change_item(id, changing_input_type):
    changing_input = input("New {}: ").format(changing_input_type)

    # connects to database
    connection = mysql.connector.connect(user=open('username.txt').readline(), database='inventorium')
    cursor = connection.cursor()

    # updates the description field and commits it to the database
    modify_item = ("UPDATE items SET "
                    "{} = '{}'"
                    " WHERE id = '{}';"
                ).format(changing_input_type, changing_input, id)

    cursor.execute(modify_item)
    connection.commit()

    cursor.close()
    connection.close()