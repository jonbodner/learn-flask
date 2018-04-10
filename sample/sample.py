import os

import pg8000
from flask import Flask, g, session, render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.environ['SAMPLE_DB'],
    PWD=os.environ['SAMPLE_DB_PWD'],
    USER=os.environ['SAMPLE_DB_USER'],
    HOST=os.environ['SAMPLE_DB_HOST'],
    SECRET_KEY=os.environ['SAMPLE_SECRET_KEY']
))

app.config.from_envvar('SAMPLE_SETTINGS', silent=True)


def connect_db():
    conn = pg8000.connect(app.config['USER'], host=app.config['HOST'], database=app.config['DATABASE'],
                          password=app.config['PWD'])
    return conn


def get_db():
    if not hasattr(g, 'postgres_db'):
        g.postgres_db = connect_db()
    return g.postgres_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'postgres_db'):
        g.postgres_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        content = f.read().split(';')
        for r in content:
            if len(r.strip()) != 0:
                print(r)
                db.cursor().execute(r)
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.route('/', methods=['GET'])
def main():
    if not session.get('logged_in'):
        return render_template('login_create.html')
    user = session.get('user')
    cur = get_db().cursor()
    cur.execute("select * from documents where user_id = ?", user.user_id)
    results = cur.fetchall()
    cur.close()
    return render_template('show_documents.html', results=results, user=user)


@app.route('/', methods=['POST'])
def login_create():
    pass
