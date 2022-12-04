expences = []
expence_type = []

def show_expenses(month):
    for expence_amount, expense_type, expense_month in expences:
        if expense_month == month:
            print(f'{expence_amount}  - {expense_type}')


def add_expense(month):
    print()
    expense_amount = int(input("Podaj kwotę: "))
    expense_type = input("Podaj typ wydatku: ")
    expense = [expense_amount, expense_type, month]
    expences.append(expense)


def show_stats(month):
    # Suma poszczególnych zmiennych w tablicy w określonej lokacji
    total_amount_this_month = sum(
        expense_amount for expense_amount, _, expense_month in expences if expense_month == month)
    # Suma wszystkich wydatków
    total_amount_all = sum(expense_amount for expense_amount, _, _ in expences)

    number_of_expenses_this_month= sum(1 for _, _, expense_month in expences if expense_month == month)
    avarage_expenses_this_month = total_amount_this_month / number_of_expenses_this_month
    avarage_expenses_all = total_amount_all / len(expences)
    print()
    print("Statystyki")
    print("Wszystkie wydatki w tym miesiącu: ", total_amount_this_month)
    print("Średni wydatek w tym miesiącu", avarage_expenses_this_month)
    print("Wszystkie wydatki: ", total_amount_all)
    print("Średni wydatek: ", avarage_expenses_all)

def save_tasks_to_file():
    file = open("tasks.txt", "w")
    for expence_amount, expense_type, expense_month in expences:
        file.write(f'{expence_amount}  - {expense_type}')
        file.close()
#
while True:
    print()
    month = int(input("Wybierz miesiąc: "))

    if month == 0:
        break
    while True:
        print("0. Powrót do wyboru miesiąca: ")
        print("1. Wyświetl wszystkie wydatki:")
        print("2. Dodaj wydatek")
        print("3. Statystyki: ")
        print("4. Zapisz do pliku")
        choice = int(input("Wynierz opcję: "))

        if choice == 0:
            # ta metoda wychodzi z tej pętli i wraca do poprzedniej
            break

        if choice == 1:
            print("Wszystkie wydatki")
            show_expenses(month)

        if choice == 2:
            print("dodaj wydatek")
            print("Dodaj typ wydatku")
            add_expense(month)

        if choice == 3:
            show_stats(month)

        if choice == 4:
            save_tasks_to_file()
