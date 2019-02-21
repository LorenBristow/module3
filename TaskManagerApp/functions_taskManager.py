# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:01:06 2019

@author: loren
"""
import sqlite3
import datetime
import json
import requests

##### CREATE & CONNECT TO DATABASE #####
conn = sqlite3.connect("dbTaskManager.db")
c = conn.cursor() #harriet - put this un a func and call it, also close at end of everyt function.

##### USER RECORDS TABLE - Users are referred to as Unicorns. #####
def create_table_unicorns():
    c.execute("DROP TABLE unicorns")
    c.execute("CREATE TABLE IF NOT EXISTS unicorns(user_id TEXT PRIMARY KEY, username_or_email TEXT, password TEXT, date_user_registered NUMERIC, date_user_last_logged_in NUMERIC)")
create_table_unicorns()

##### TASK TABLE #####
def create_table_tasks():
    c.execute("CREATE TABLE IF NOT EXISTS tasks(task_id NUMERIC PRIMARY KEY, user_id TEXT, task_created_date NUMERIC, task_last_saved_date NUMERIC, task_name TEXT, task_description TEXT, task_status NUMERIC, task_due_date NUMERIC, important NUMERIC, category TEXT, priority TEXT )")
create_table_tasks()

##### CREATE USER #####
user_id = 1

def create_user(user_id):
    #user_registration_inputs() - retired userInputs.py
    #new or existing user piece to come
    #assuming new user - test create user to database
    username_or_email = 'loren'
    password_1 = '12'
    password_2 = '12'
    if password_1 == password_2:
            password = password_2
            #add logic that 1st creation only updates registered date & user_id is autocreated on this first time, thereafter only change login date.
            date_user_registered = datetime.datetime.now()
            date_user_last_logged_in = datetime.datetime.now()
            c.execute("INSERT INTO unicorns(user_id, username_or_email, password, date_user_registered, date_user_last_logged_in) VALUES (?, ?, ?, ?, ?)", (user_id, username_or_email, password, date_user_registered, date_user_last_logged_in))
            conn.commit()
    else:
        print("passwords don't match")
        #retry functionality to come user_id, username_or_email, password, date_user_registered, date_user_last_logged_in
    return user_id
create_user(user_id)

##### CREATE TASK #####
def create_task(task_name, task_description,task_due_date, important):
    with sqlite3.connect("dbTaskManager.db") as conn:
        c = conn.cursor()
        task_id = 1 # make dynamic later
        task_created_date = datetime.datetime.now()
        task_last_saved_date = datetime.datetime.now()
        #task_name = request.form['a-task']
        #task_description = 'blah blah' # make dynamic later
        task_status = False
        #task_due_date = datetime.datetime.now()
        #important = False
        category = 'category'
        priority = 'priority'
        c.execute("INSERT INTO tasks(task_id, user_id, task_created_date, task_last_saved_date, task_name, task_description, task_status, task_due_date, important, category, priority) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (task_id, user_id, task_created_date, task_last_saved_date, task_name, task_description, task_status, task_due_date, important, category, priority))
        conn.commit()

##### RETRIEVE TASKS #####
def retrieve_tasks():
    try:
        with sqlite3.connect("dbTaskManager.db") as conn:
            c = conn.cursor()
            unicorn_tasks = c.execute("SELECT * FROM tasks")
            unicorn_tasks_list = []
            for row in unicorn_tasks:
                unicorn_tasks_list.append({"task_name":row[4], "task_description":row[5], "task_status":row[6], "task_due_date":row[7], "important":row[8]},)
            return json.dumps(unicorn_tasks_list)
    except:
        return None

##### CALL API #####
def call_api():
    try:
        endpoint = 'http://127.0.0.1:5000/api'
        response = requests.get(endpoint)
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 400:
            print("error - bad request - 400")
        elif response.status_code == 500:
            print("error - internal server error - 500")
    except:
        return None

