import cmd
import sqlconnector
import item

item_dict = dict()

class client(cmd.Cmd):
    def help_createitem(self):
        print("Creates a new item. Input after the command will be used as the item's name.")

    def help_changename(self):
        print("Changes the name of an item. Input after the command must be the item's ID.")

    def help_changedesc(self):
        print("Changes the description of an item. Input after the command must be the item's ID.")

    def help_changecost(self):
        print("Changes the cost of an item. Input after the command must be the item's ID.")

    def help_changequant(self):
        print("Changes the quantity of an item. Input after the command must be the item's ID.")

    # creates a new item using the name of the item, and saves it to the database
    # primary key is an auto-incrementing ID number
    def do_createitem(self, line):
        item.new_item(line)

    # changes the name of the item, with the line acting as the id; user is prompted for new name
    def do_changename(self, line):
        item.change_item(line, 'name')

    # changes the description of the item, with the line acting as the id; user is prompted for new description
    def do_changedesc(self, line):
        item.change_item(line, 'description')

    # changes the cost of the item, with the line acting as the id; user is prompted for new cost
    def do_changecost(self, line):
        item.change_item(line, 'cost')

    # changes the quantity of the item, with the line acting as the id; user is prompted for new quantity
    def do_changequant(self, line):
        item.change_item(line, 'quantity')

client().cmdloop()