# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:06:41 2019

@author: loren
"""


from flask import Flask, render_template, request, redirect, url_for
from functions_taskManager import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='GET':
        api_results = call_api()
        return render_template('index.html', api_results = api_results)
    elif request.method =='POST':
        task_status = form_data['status']
        ###make function to update DB for status. so call func here and then add func on functions py. 
        return None


@app.route('/api')
def api():
    tasks_to_show = retrieve_tasks()
    return tasks_to_show

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method =='GET':
        return render_template("index.html")
    elif request.method =='POST':
        form_data = request.form
        task_name = form_data['a-task']
        task_description = form_data['task-description']
        task_due_date = form_data['due-date']
        important = form_data['important']
        create_task(task_name, task_description, task_due_date, important)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
