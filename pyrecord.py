import tkinter.messagebox
from datetime import date
from pycategory import Categories
categories = Categories()


class Record:
    """Represent a record."""
    
    def __init__(self, date, category, description, amount):
        """The attribute of a record."""
        self._category = category
        self._description = description
        self._amount = amount
        self._date = date 

    def __repr__(self):
        """Represent a record."""
        return(f'{self._date} {self._category} {self._description} {self._amount}')

    def get_category(self):
        """Get the record more convineince."""
        return self._category

    def get_description(self):
        """Get the record more convineince."""
        return self._description

    def get_amount(self):
        """Get the record more convineince."""
        return self._amount
    
    def get_date(self):
        return self._date
    

    category = property(lambda self: self.get_category())
    description = property(lambda self: self.get_description())
    amount = property(lambda self: self.get_amount())
    date = property(lambda self: self.get_date())


    
    
    
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        """Read from 'records.txt' or prompt for initial amount of money."""
        total_money = 0
        try:
            fh = open('records.txt')
            initial_money = int(fh.readline())
            temp = fh.readlines()
            records = []
            for i in range(len(temp)):
                temp[i] =temp[i].strip('\n').split()
                temp[i][3] = int(temp[i][3])
                records.append(Record(*temp[i]))
                total_money += records[i].amount
            fh.close()
        except:
            initial_money = 0
            total_money = 0
            records = []
        self._records = records
        self._initial_money = initial_money
        self._total_money = total_money + initial_money

    def __repr__(self):
        """Represent records"""
        return(f'{self._records}')

    def add(self, add_record):
        """Add a record if it is valid."""
        try:
            add_record = (' '.join(add_record.split()).split(' '))
            if len(add_record) not in [3, 4]:
                raise IndexError
            elif len(add_record) == 4:
                try:
                    date.fromisoformat(add_record[0])
                except:
                    tkinter.messagebox.showwarning(title = 'input Error', message = 'The format of date should be YYYY-MM-DD.\nFail to add a record.')
            elif len(add_record) == 3:
                add_record = [str(date.today())] + [*add_record]                
            category = add_record[1]
            add_record[3] = int(add_record[3])
            assert categories.is_category_valid(category)
        except IndexError:
            tkinter.messagebox.showwarning(title = 'input Error', message = 'The format of a record should be like this:\nYYYY-MM-DD(option) meal breakfast -50\nFail to add a record.')
        except ValueError:
            tkinter.messagebox.showwarning(title = 'input Error', message = 'Invalid value for money.\nFail to add a record.')
        except AssertionError:
            tkinter.messagebox.showwarning(title = 'input Error', message = 'The specified category is not in the category list.\nYou can check the category list on the left side.\nFail to add a record.')
        else:
            self._records.append(Record(*add_record))
            self._total_money += add_record[3]
            
    
    def view(self):
        """View records"""
        print("{0:<12} {1:<20} {2:<25} {3:<8}".format('Date','Category','Description','Amount'))
        print('============ ==================== ========================= ========')
        for i in range(len(self._records)):
            print (f'{self._records[i].date:<12s} {self._records[i].category:<20s} {self._records[i].description:<25s} {self._records[i].amount:<8d}')
        print('============ ==================== ========================= ========')
        print(f'Now you have {self._total_money} dollars.')


    def delete(self, delete_value):
        self._total_money -= self._records[delete_value].amount
        del self._records[delete_value]

    def find(self, find_cat_list):
        """Represent all records under an assigned category."""
        try:
            assert find_cat_list != []
            find_result = list(filter(lambda n: n.category in find_cat_list, self._records))
            find_result_money = sum(map(lambda n:n.amount, find_result))
            return find_result
        except AssertionError:
            tkinter.messagebox.showwarning(title = 'input Error', message = 'Your input is not in the category list!\nYou can check the category list on the left side.')
            

    def save(self):
        """Save records and into records.txt"""
        str_total_money = str(self._initial_money)
        str_records = self._records
        with open('records.txt', 'w') as memory:
            memory.write(str_total_money+'\n')
            for item in str_records:
                memory.write('%s\n' % item)