from venv import create
from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://nel:2578609HjK@localhost:5432/test'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

# engine = create_engine('postgresql+psycopg2://nel:2578609HjK@localhost:5432/test')
db = SQLAlchemy(app)

@app.route('/')
def dummy_request():
    return {"message": "Hello world"}


if __name__ == "__main__":
    app.run(debug=True)
