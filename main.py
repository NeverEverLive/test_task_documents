from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://nel:123@localhost:5432/document_test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


if __name__ == "__main__":
    from api.views import document_view, right_view
    app.register_blueprint(document_view.documents)
    app.register_blueprint(right_view.rights)
    app.run(debug=True)
