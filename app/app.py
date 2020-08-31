from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    abort
)
from flask_restplus import (
    Api,
    Resource
)
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from models import db, Note


app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

api = Api(app=app)
name_space = api.namespace('api', description='Main APIs')


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


@name_space.route('')
class ApiNote(Resource):
    def get(self):
        note = Note.query.all()
        return jsonify(json_list=[i.serialize for i in note])

    def post(self):
        req_data = request.get_json()
        note = Note(req_data['title'], req_data['content'])
        db.session.add(note)
        db.session.commit()
        return jsonify({'id': note.id})


@name_space.route('/<id>')
@name_space.doc(params={'id': 'An ID'})
class ApiNoteId(Resource):
    def get(self, id):
        note = Note.query.get(id)
        if note:
            return jsonify(note.serialize)

        abort(status=404, description='Not exist ID(%s)' % id)

    def put(self, id):
        note = Note.query.get(id)
        req_data = request.get_json()
        if note:
            note.title = req_data['title']
            note.content = req_data['content']
            db.session.commit()
            return jsonify({'result': 'updated'})

        abort(status=404, description='Not exist ID(%s)' % id)

    def delete(self, id):
        note = Note.query.get(id)
        if note:
            db.session.delete(note)
            db.session.commit()
            return jsonify({'result': 'deleted'})

        abort(status=404, description='Not exist ID(%s)' % id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
