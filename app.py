from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import settings

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
db.create_all()


if __name__ == "__main__":
    from api.views import document_view, right_view
    app.register_blueprint(document_view.documents)
    app.register_blueprint(right_view.rights)
    app.run(debug=True, host='0.0.0.0')
