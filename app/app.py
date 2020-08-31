from flask import Flask, render_template, request, redirect, url_for
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from models import db, Note


app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        note = Note(request.form['title'], request.form['content'])
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/')
def index():
    note = Note.query.all()
    return render_template('index.html', note=note)


@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    note = Note.query.get(id)
    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', note=note)


@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
