from fastapi import FastAPI
import asyncio
import random
import pandas as pd
import nest_asyncio

app = FastAPI()
nest_asyncio.apply()


@app.get('/')
async def root():
    user_data = get_user_details(10)

    return user_data


async def get_names(number):
    first_names = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia',
                   'Isabella', 'Mia', 'Evelyn', 'Harper', 'Luna', 'Camila',
                   'Gianna', 'Elizabeth', 'Eleanor', 'Ella', 'Abigail', 'Sofia',
                   'John', 'Richard', 'Alex', 'Harvey', 'Mark', 'Brian',
                   'Charles', 'Edward', 'Geoffrey', 'Steven', 'Carl', 'Allan']

    last_names = ['Doe', 'Lopez', 'Lee', 'Granger', 'Smith', 'Amani', 'Knight',
                  'Rogers', 'Romanov', 'Perez', 'White', 'Brown', 'King',
                  'Johnson', 'Miller', 'Lee', 'Davis', 'Smith', 'Wilson', 'Knight',
                  'Alvarez', 'Moore', 'Thomas', 'Jackson', 'Imani', 'Zane']

    names_list = []
    email_list = []
    for i in range(number):
        num1 = random.randint(0, len(first_names) - 1)
        num2 = random.randint(0, len(last_names) - 1)
        email_list.append(f"{first_names[num1]}{random.randint(0, 100)}@mail.com")
        names_list.append(f'{first_names[num1]} {last_names[num2]}')

    return names_list, email_list


def get_user_details(number_of_people: int):
    loop = asyncio.get_event_loop()
    task_list = get_names(number_of_people)
    details = loop.run_until_complete(asyncio.gather(task_list))
    table_columns = ['Full names', 'Email', 'Phone number', 'Loan balance']

    user_data_df = pd.DataFrame(columns=table_columns)
    user_data_df["Full names"] = details[0][0]
    user_data_df["Email"] = details[0][1]

    return user_data_df.to_json(orient="records")
