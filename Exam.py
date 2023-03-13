import json
from datetime import datetime



class ExpenseTracker:
    def __init__(self):
        self.categories = []
        self.expenses = []

    #Додати категорію
    def add_category(self, category_name):
        for cat in self.categories:
            if cat['category'] == category_name:
                return f'Вже існує категорія - {category_name}'
        self.categories.append({'category':category_name})
        return f' Added category - {category_name}'


    #Видалити категорію
    def remove_category(self, category_name):
        for cat in self.categories:
            if cat['category'] == category_name:
                self.categories.remove(cat)
                return f'Remove category - {category_name}'
        return 'Not found'

    #Показати усі категорії
    def show_cat(self):
        str = ''
        print(f'{"Category":<20}')
        for cat in self.categories:
            str += f'{cat["category"]:<20}\n'
        return str

    #Додаьти витрати
    def add_expense(self, name, date, category, amount):
        for cat in self.categories:
            if cat['category'] == category:
                self.expenses.append({'name': name, 'date': date, 'category': category, 'amount': amount})
                return f'Added expenses - Name: {name}, date - {date}, category - {category}, amount - {amount}'
        return f'Not found cat - {category}'

    #Зберегти в файл
    def save_expenses(self, filename):
        with open(filename, 'w') as f:
            json.dump({'category': self.categories, 'expenses': self.expenses}, f) #дозволяє записати об'єкти Python у файл у форматі JSON
        return f'Saved to file - {filename}'

    #Загрузити з файлу
    def load_expenses(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)   #дозволяє прочитати JSON-файл та перетворити його у об'єкт Python.
            self.categories = data['category']
            self.expenses = data['expenses']
        return f'Load from file - {filename}'

    #Створити звітт
    def generate_report(self, start_date=None, end_date=None, category=None, name=None):
        filtered_expenses = self.expenses

        if start_date:
            startDateTime = datetime.strptime(start_date, '%d.%m.%Y') #перетворення рядка у об'єкт datetime
            filtered_expenses = [e for e in filtered_expenses if datetime.strptime(e['date'], '%d.%m.%Y') >= startDateTime]
        if end_date:
            endDateTime = datetime.strptime(end_date, '%d.%m.%Y')
            filtered_expenses = [e for e in filtered_expenses if datetime.strptime(e['date'], '%d.%m.%Y') <= endDateTime]
        if category:
            filtered_expenses = [e for e in filtered_expenses if e['category'] == category]
        if name:
            filtered_expenses = [e for e in filtered_expenses if e['name'] == name]

        if not filtered_expenses:
            print('No expenses found.')
            return

        print(f"{'Expense Name':<20} {'Date':<15} {'Category':<15} {'Amount':<10}") #Заголовок таблиці будуть вирівнюватися з лівого краю за шириною цифра
        for e in filtered_expenses:
            print(f"{e['name']:<20} {e['date']:<15} {e['category']:<15} {e['amount']:<10}")

        max_expense = max(filtered_expenses, key=lambda e: e['amount'])  #Функція ключа lambda e: e['amount'] повертає значення ключа 'amount' для кожного елемента 'e' у списку, за допомогою якого визначається максимальне значення.
        min_expense = min(filtered_expenses, key=lambda e: e['amount'])

        if category:
            category_expenses = [e for e in filtered_expenses if e['category'] == category]
            max_category_expense = max(category_expenses, key=lambda e: e['amount'])
            min_category_expense = min(category_expenses, key=lambda e: e['amount'])
            print(
                f"\nMaximum expense in {category} category: {max_category_expense['name']} ({max_category_expense['amount']})")
            print(
                f"Minimum expense in {category} category: {min_category_expense['name']} ({min_category_expense['amount']})")

        print(f"\nMaximum expense: {max_expense['name']} ({max_expense['amount']})")
        print(f"Minimum expense: {min_expense['name']} ({min_expense['amount']})")


tracker = ExpenseTracker()
tracker.add_category('Food')
tracker.add_category('Transportation')
tracker.add_category('Entertainment')

tracker.add_expense('Groceries', '01.03.2022', 'Food', 50.25)
tracker.add_expense('Gas', '28.02.2022', 'Transportation', 30.00)
tracker.add_expense('Movie ticket', '02.03.2022', 'Entertainment', 12.50)
tracker.add_expense('Dinner', '03.03.2022', 'Food', 35.75)

# tracker.save_expenses('expenses.json')
#
# tracker.load_expenses('expenses.json')

# tracker.generate_report() #Показує усі витрати
#
# tracker.generate_report(start_date='2022-03-01', end_date='2022-03-02') # Показує витрати в періоді часу
#
# tracker.generate_report(category='Food') # Показує витрати за категорією
#
# tracker.generate_report(name='Gas') # Показує витрати за назвою


def main():
    while True:
        var = input('1 - Add cat\n'
                    '2 - Remove cat\n'
                    '3 - Add expense\n'
                    '4 - Save to file\n'
                    '5 - load from file\n'
                    '6 - Show all cat\n'
                    '7 - Generate all report\n'
                    '8 - Generate report date\n'
                    '9 - Generate report name\n'
                    '10 - Generate report cat\n'
                    '--> ')
        match var:
            case '1':
                category_name1 = input('Category name: ')
                print(tracker.add_category(category_name1))
            case '2':
                category_name2 = input('Category name: ')
                print(tracker.remove_category(category_name2))
            case '3':
                try:
                    category_name3 = input('Category name: ')
                    name3 = input('Name: ')
                    data3 = input('Data(11.11.1111): ')
                    amount3 = float(input('Amount: '))
                    print(tracker.add_expense(name3, data3, category_name3, amount3))
                except:
                    print('Enter float amount!')
            case '4':
                print(tracker.save_expenses('expenses.json'))
            case '5':
                print(tracker.load_expenses('expenses.json'))
            case '6':
                print(tracker.show_cat())
            case '7':
                tracker.generate_report()
            case '8':
                start_data = input('Start data(11.11.1111): ')
                end_data = input('End data(11.11.1111): ')
                tracker.generate_report(start_date=start_data, end_date=end_data)
            case '9':
                name8 = input('Name: ')
                tracker.generate_report(name=name8)
            case '10':
                category_name9 = input('Category name: ')
                tracker.generate_report(category=category_name9)
            case _:
                break

if __name__ == '__main__':
    main()
