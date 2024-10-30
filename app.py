from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#sample data storage
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_item = request.form.get('todo')
    if todo_item:
        todos.append(todo_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

