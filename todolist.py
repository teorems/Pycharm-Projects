from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, date, timedelta
from sqlalchemy.orm import sessionmaker

# create db
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

# create Base class
Base = declarative_base()


# table (Model class)
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# create table in db
Base.metadata.create_all(engine)
# create session object to manage db
Session = sessionmaker(bind=engine)
session = Session()


def menu():
    print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")


def today_tasks():
    today = datetime.today()
    rows = session.query(Table).filter(Table.deadline == today.date()).all()
    print("Today:")
    if len(rows) == 0:
        print('Nothing to do!')
    else:
        for each in rows:
            print(each.task)
    print()


def week_tasks():
    week_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    for key in week_days.keys():
        day = (datetime.today() + timedelta(days=key)).date()
        rows = session.query(Table).filter(Table.deadline == day).all()
        print(f'{week_days[day.weekday()]} {day.day} {day.strftime("%b")}:')
        if len(rows) != 0:
            for each in rows:
                print(f'{rows.index(each) + 1}. {each.task}')
        else:
            print('Nothing to do!')
        print()


def all_tasks():
    rows = session.query(Table).order_by(Table.deadline).all()
    print('All tasks:')
    for task in rows:
        print(f'{rows.index(task) + 1}. {task.task}. {task.deadline.day} {task.deadline.strftime("%b")}')
    print()


def add_task():
    print('Enter task')
    task = input().strip()
    print('Enter deadline')
    deadline = datetime.strptime(input().strip(), '%Y-%m-%d').date()
    new_row = Table(task=task, deadline=deadline)
    session.add(new_row)
    session.commit()
    print('The task has been added!')
    print()


def delete_task():
    alltasks = session.query(Table).order_by(Table.deadline)
    print("Choose the number of the task you want to delete:")
    for i, v in enumerate(alltasks, start=1):
        print(str(i) + ".", str(v) + ".", v.deadline.day, v.deadline.strftime('%b'))
    choice = int(input())
    to_delete = alltasks[choice - 1]
    session.delete(to_delete)
    session.commit()


def missed_tasks():
    print("Missed tasks:")
    today = date.today()
    past = session.query(Table).filter(Table.deadline < today).order_by(Table.deadline)
    for i, v in enumerate(past, start=1):
        print(str(i) + ".", str(v) + ".", v.deadline.day, v.deadline.strftime('%b'))
    print()


# main program
while True:
    menu()
    user_input = int(input())
    if user_input == 0:
        print()
        print('Bye!')
        exit()
    elif user_input == 1:
        print()
        today_tasks()
    elif user_input == 2:
        print()
        week_tasks()
    elif user_input == 3:
        print()
        all_tasks()
    elif user_input == 4:
        print()
        missed_tasks()
    elif user_input == 5:
        print()
        add_task()
    elif user_input == 6:
        print()
        delete_task()
