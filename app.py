import os
from flask import Flask, render_template,  request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI']='\
        'mysql://username:password@host:port/mydatabase' + os.path.join(basedir, 'database.db')'
app.config['SQLALCHEMY_TRACK_MODIFICATION']='False'

db = SQLAlchemy(app)

# ...

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    daily = db.Column(db.Text)
    weekly = db.Column(db.Text)
    monthly = db.Column(db.Text)

    def __repr__(self):
        return f'<Todo {self.name}>'

to_dos = [ ]
@app.route("/")
def index ():
              return render_template("index.html", to_dos=to_dos)

@app.route("/list/", methods = ("GET", "POST"))
def list():
         if request.method == 'POST':
              title = request.form['title']
              content = request.form['content']
              if not title:
                     flash('Enter which type of to do list!')
              elif not content:
                     flash('Content is required!')
              else:
                     to_dos.append({'title': title, 'content': content})
                     return redirect(url_for('index'))
         return render_template("to_do_list.html")