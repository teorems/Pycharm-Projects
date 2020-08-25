import random
import sqlite3
import sys

conn = sqlite3.connect('card.s3db')
c = conn.cursor()
# c.execute("DROP TABLE card")
c.execute("""CREATE TABLE IF NOT EXISTS card 
            (id INTEGER,number TEXT,pin TEXT,balance INTEGER DEFAULT 0);""")
database = {}


def create_card():
    balance = 0
    id_account = 1
    while id_account in database:
        id_account = id_account + 1
    card_n = "400000" + "%0.9d" % random.randint(0, 999999999)
    while card_n in database:
        card_n = "400000" + "%0.9d" % random.randint(0, 999999999)
    card_n = checksum(card_n)
    pin = "%0.4d" % random.randint(0, 9999)
    database[id_account] = card_n, pin, [balance]
    values = id_account, card_n, pin, balance
    c.execute("INSERT INTO card (id, number, pin, balance)  "
              "VALUES (?,?,?,?)", values)
    conn.commit()

    print("\nYour card has been created.\n"
          "Your card number:\n", card_n,
          "\nYour card PIN:\n", pin, sep="")
    print()
    # prints the data
    '''for row in c.execute('SELECT * FROM card ORDER BY number'):
        print(row)'''
    main_menu()


def checksum(card_n):
    int_card_n = [int(x) for x in card_n]
    for i in range(len(int_card_n)):
        if i % 2 == 0:
            int_card_n[i] = int_card_n[i] * 2

    for i in range(len(int_card_n)):
        if int_card_n[i] > 9:
            int_card_n[i] = int_card_n[i] - 9

    digits_sum = sum(int_card_n)
    check_sum = 0
    while digits_sum % 10 != 0:
        digits_sum += 1
        check_sum += 1
    else:
        card_n = card_n + str(check_sum)
        return card_n


def main_menu():
    choice = input("1. Create account\n2. Log into account\n0. Exit\n")
    if choice == "1":
        create_card()
    if choice == "2":
        card_n = input("\nEnter your card number:\n")
        pin = input("Your card PIN:\n")
        for k, v in database.items():
            if card_n in database[k] and database[k][1] == pin:
                print("\nYou have successfully logged in!\n")
                id_account = k
                balance = database[k][2][0]
                account_menu(id_account, card_n, balance)
                break
        else:
            print("\nSorry, wrong card number or PIN!\n")
            main_menu()
    if choice == 0:
        c.execute("DROP TABLE card")
        conn.commit()
        conn.close()
        print("Bye !")
        sys.exit()


def transfer(id_account, card_n, balance):
    dest_card = input("\nEnter card number:")
    if dest_card == card_n:
        print("\nYou can't transfer money to the same account!")
        account_menu(id_account, card_n, balance)
    elif checksum(dest_card[:-1]) != dest_card:
        print("\nProbably you made mistake in the card number. Please try again!")
        account_menu(id_account, card_n, balance)
    for k, v in database.items():
        if dest_card in v:
            id_dc = k
            break
    else:
        id_dc = None
        print("\nSuch a card does not exist")
        account_menu(id_account, card_n, balance)
    amount = int(input("Enter how much money you want to transfer:\n"))
    if amount > balance:
        print("Not enough money!\n")
        account_menu(id_account, card_n, balance)
    else:
        balance -= amount
        database[id_account][2][0] = balance
        database[id_dc][2][0] = balance
        c.execute("UPDATE card SET balance=? WHERE id = ?;", (balance, id_account))
        c.execute("UPDATE card SET balance=? WHERE id = ?;", (balance, id_dc))
        conn.commit()
        print("Success!")
        account_menu(id_account, card_n, balance)


def account_menu(id_account, card_n, balance):
    choice = input("1. Balance\n2. Add income\n3. Do transfer\n"
                   "4. Close account\n5. Log out\n0. Exit\n")
    if choice == "1":
        '''c.execute("SELECT id,balance FROM card WHERE id = ?", (id_account,))
        print(c.fetchone())'''
        print("\nBalance: ", balance)
        account_menu(id_account, card_n, balance)
    elif choice == "2":
        balance += int(input("\nEnter income:\n"))
        database[id_account][2][0] = balance
        c.execute("UPDATE card SET balance=? WHERE id = ?;", (balance, id_account))
        conn.commit()
        print("Income was added!")
        account_menu(id_account, card_n, balance)
    elif choice == "3":
        transfer(id_account, card_n, balance)
    elif choice == "4":
        c.execute("DELETE FROM card WHERE id = ?", (id_account,))
        conn.commit()
        print("\nThe account has been closed!\n ")
        main_menu()
    elif choice == "5":
        print("You have successfully logged out!\n")
        main_menu()
    elif choice == "0":
        conn.close()
        print("Bye !")
        sys.exit()
    else:
        account_menu(id_account, card_n, balance)


main_menu()
