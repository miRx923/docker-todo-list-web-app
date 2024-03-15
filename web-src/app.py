""" Main file executing the app and defining Flask routes """

from flask import Flask, render_template, request, redirect, url_for
import os
import database_operations as dbop


# Creating the app instance of Flask class
app = Flask(__name__, 
            template_folder=os.path.abspath('web-src'), # Setting the folder path with HTML files
            static_folder=os.path.abspath('web-src')) # Setting the folder path with CSS files


# Route to display todo list
@app.route('/')
def index():
    dbop.db_init()
    todo_list_var = dbop.db_fetch()

    # Render the todo.html web page
    return render_template('todo.html', todo_list=todo_list_var)


# Route to add a new task
@app.route('/add_task', methods=['POST'])
def add_task_route():
    new_task = request.form['new_task']
    dbop.add_task(new_task)

    # Refresh the main web page
    return redirect(url_for('index'))


# Route to delete a task
@app.route('/delete_task', methods=['POST'])
def delete_task_route():
    task = request.form['task']
    dbop.delete_task(task)

    # Refresh the main web page
    return redirect(url_for('index'))


# Route to toggle task completion
@app.route('/toggle_completion/<task>', methods=['GET'])
def toggle_completion_route(task):
    dbop.toggle_completion(task)

    # Refresh the main web page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
