from modules.commands import execute, conn, cursor


def main():
    while True:
        command_input = input("--> ").strip().split()
        if command_input[0] == "exit":
            verify = input("Do you really want to exit (Y|N) :")
            if verify[0].strip().lower() == 'y':
                break
        execute(command_input)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS contact_info (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name char(30), Address char(50), Phone char(25), Email char(40))')
    print('Write "help" to show a list of commands')
    main()


