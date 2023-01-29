from colorama import Fore, Style

help_str = """
Commands:
    create <Name> <Address> <Phone> <Email>
    delete <ID>
    update <old name to be changed> <data to be changed: name|address|phone|email>
    find <data to be found: name|address|phone|email> <data to search>
    exit
You can also type help <command> to get a little more info
""" + Fore.RED + """NOTE: Name field must be written in one word.
NOTE: The command must be run on same order it is shown.
NOTE: Commands are case sensitive""" + Style.RESET_ALL
create_str = """Command:
    create <name> <address> <phone> <email>
For example to add a contact:
    create Honza Praha +420 honzapraha@420.com
""" + Fore.RED + "NOTE: All of the details must be separated by spaces" + Style.RESET_ALL

delete_str = """Command:
    delete <ID>
""" + Fore.RED + "NOTE: You must enter the exact ID." + Style.RESET_ALL

update_str = """Command:
    update <data to be changed: name|address|phone|email> <old name to be changed>
Example to change phone number of a contact:
    update phone <Name>
""" + Fore.RED + """NOTE: Here name is used as an identifier to identify which contact you need to change.
There will be issues if you have two contact with same exact name.""" + Style.RESET_ALL

find_str = """Command:
    find <data to be found: name|address|phone|email> <data to search>
Example:
    find email abc@domain.com"""

exit_str = """This will commit recent changes to the database and will stop the program."""

help_strings = {
    "create": create_str,
    "delete": delete_str,
    "update": update_str,
    "find": find_str,
    "exit": exit_str,
    "help": help_str
}


def help_command(command=None):
    if command is None:
        command = "help"

    try:
        print(help_strings[command])
    except KeyError:
        print("This command doesn't exist")
