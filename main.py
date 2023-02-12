from fastapi import FastAPI
import asyncio
import random
import pandas as pd
import nest_asyncio
import numpy as np

app = FastAPI()
nest_asyncio.apply()


@app.get('/')
async def root():
    user_data = get_user_details(10)
    return user_data


async def get_names(number: int) -> tuple:
    first_names: list = ['Olivia', 'Emma', 'Charlotte', 'Amelia', 'Ava', 'Sophia',
                         'Isabella', 'Mia', 'Evelyn', 'Harper', 'Luna', 'Camila',
                         'Gianna', 'Elizabeth', 'Eleanor', 'Ella', 'Abigail', 'Sofia',
                         'John', 'Richard', 'Alex', 'Harvey', 'Mark', 'Brian',
                         'Charles', 'Edward', 'Geoffrey', 'Steven', 'Carl', 'Allan']

    last_names: list = ['Doe', 'Lopez', 'Lee', 'Granger', 'Smith', 'Amani', 'Knight',
                        'Rogers', 'Romanov', 'Perez', 'White', 'Brown', 'King',
                        'Johnson', 'Miller', 'Lee', 'Davis', 'Smith', 'Wilson', 'Knight',
                        'Alvarez', 'Moore', 'Thomas', 'Jackson', 'Imani', 'Zane']

    names_list: list = []
    email_list: list = []
    for i in range(number):
        num1 = random.randint(0, len(first_names) - 1)
        num2 = random.randint(0, len(last_names) - 1)
        email_list.append(f"{first_names[num1]}{random.randint(0, 100)}@mail.com")
        names_list.append(f'{first_names[num1]} {last_names[num2]}')

    return names_list, email_list


def get_phone_number(number_of_people: int):
    numbers = np.random.randint(999, size=number_of_people)
    new_numbers = []
    for number in numbers:
        new_numbers.append(f"+XXX+{number}+{number}X")
    return new_numbers


def get_loan_details(number_of_people: int):
    columns = ['OLB', 'Installments', 'Arrears']
    balanced_df = pd.DataFrame(columns=columns)
    outstanding_balance = np.random.randint(9999, size=number_of_people)
    installments = np.random.randint(15, size=number_of_people)
    arrears = [int(np.random.rand(1) * num) for num in outstanding_balance]

    balanced_df['OLB'] = outstanding_balance
    balanced_df['Installments'] = installments
    balanced_df['Arrears'] = arrears

    return balanced_df


def get_user_details(number_of_people: int):
    loop = asyncio.get_event_loop()
    task_list = get_names(number_of_people)
    details = loop.run_until_complete(asyncio.gather(task_list))
    table_columns = ['Full names', 'Email', 'Phone number']
    user_data_df = pd.DataFrame(columns=table_columns)
    loan_data_df = get_loan_details(number_of_people)

    user_data_df["Full names"] = details[0][0]
    user_data_df["Email"] = details[0][1]
    user_data_df["Phone number"] = get_phone_number(number_of_people)
    data_df = user_data_df.join(loan_data_df)

    return data_df.to_json(orient="records")
