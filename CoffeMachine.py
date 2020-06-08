class CoffeeMachine:

    def __init__(self):
        self.dollars = 550
        self.water = 400
        self.milk = 540
        self.cb = 120
        self.cups = 9
        self.things = ["water", "milk", "coffee beans", "cups", "money"]

    def menu(self):

        while True:
            action = input("\nWrite action(buy, fill, take, remaining, exit):\n>")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.state()
            elif action == "exit":
                break

    def state(self):
        print("\nThe coffee machine has:")
        for i, v in enumerate([self.water, self.milk, self.cb, self.cups, self.dollars]):
            print(f"{v} of {self.things[i]}")

    def buy(self):
        choice = input("What do you want to buy man? 1 - espresso, 2 - latte, 3 - cappuccino,:"
                       "back - to main menu: \n>")

        if choice == "1":
            self.water = self.water - 250
            self.cb = self.cb - 16
            self.dollars = self.dollars + 4
            self.cups = self.cups - 1
            if self.water < 0 or self.cb < 0 or self.cups < 0:
                if self.water < 0:
                    print("Sorry, not enough water.")
                elif self.cb < 0:
                    print("Sorry, not enough coffee")
                elif self.cups < 0:
                    print("Sorry, not enough cups")
                self.water = self.water + 250
                self.cb = self.cb + 16
                self.cups = self.cups + 1
                self.dollars = self.dollars - 4
            else:
                print("I can do that!")

        elif choice == "2":
            self.water = self.water - 350
            self.milk = self.milk - 75
            self.cb = self.cb - 20
            self.dollars = self.dollars + 7
            self.cups = self.cups - 1
            if self.water < 0 or self.cb < 0 or self.cups < 0:
                if self.water < 0:
                    print("Sorry, not enough water.")
                elif self.cb < 0:
                    print("Sorry, not enough coffee")
                elif self.cups < 0:
                    print("Sorry, not enough cups")
                self.water = self.water + 350
                self.milk = self.milk + 75
                self.cb = self.cb + 20
                self.cups = self.cups + 1
                self.dollars = self.dollars - 7
            else:
                print("I can do that!")
        elif choice == "3":
            self.water = self.water - 200
            self.milk = self.milk - 100
            self.cb = self.cb - 12
            self.dollars = self.dollars + 6
            self.cups = self.cups - 1
            if self.water < 0 or self.cb < 0 or self.cups < 0:
                if self.water < 0:
                    print("Sorry, not enough water.")
                elif self.cb < 0:
                    print("Sorry, not enough coffee")
                elif self.cups < 0:
                    print("Sorry, not enough cups")
                self.water = self.water + 200
                self.cb = self.cb + 12
                self.cups = self.cups + 1
                self.dollars = self.dollars - 6
            else:
                print("I can do that!")
        elif choice == "back":
            pass

    def fill(self):

        self.water = self.water + int(input("Write how many ml of water do you want to add:"))
        self.milk = self.milk + int(input("Write how many ml of milk do you want to add:"))
        self.cb = self.cb + int(input("Write how many g of coffee beans do you want to add:"))
        self.cups = self.cups + int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("Take everything!")

        self.dollars = 0


lavazza = CoffeeMachine()
lavazza.menu()
