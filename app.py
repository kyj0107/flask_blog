import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort
import pygal

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'

#function to open a connection to the database.db file
def get_db_connection():
    #get a database connection
    conn = sqlite3.connect('database.db')

    #allows name-based access to columns
    #rows from db connection can be used like python dictionaries
    conn.row_factory = sqlite3.Row

    #return connection object
    return conn

# use the app.route() decorator to create a Flask view function called index()
@app.route('/')
def index():
    #get a database connection
    conn = get_db_connection()

    #execute a query to get all posts from the database
    #use fetchall() to get all the rows (remember the final project from 3380?)

    query = 'SELECT * FROM posts'
    posts = conn.execute(query).fetchall()

    #close the connection
    conn.close()

    return render_template('index.html', posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    
    if request.method == "POST":
        #get the title and content
        title = request.form['title']
        content = request.form['content']

        #display an error if title or content is not submitted
        #otherwise connect to the database and add the post
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

#route to edit post
@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):


    return "<h1>Edit a Post Page<\h1>"

# route to delete a post
@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    
    
    return 


app.run(host="0.0.0.0", port=5001)