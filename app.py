from flask import Flask, render_template,  request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

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
                     flash('Title is required!')
              elif not content:
                     flash('Content is required!')
              else:
                     to_dos.append({'title': title, 'content': content})
                     return redirect(url_for('index'))
         return render_template("to_do_list.html")