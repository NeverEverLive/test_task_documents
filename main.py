from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://nel:123@localhost:5432/document_test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# engine = create_engine('postgresql+psycopg2://nel:2578609HjK@localhost:5432/test')
db = SQLAlchemy(app)



if __name__ == "__main__":
    from api.views import view
    app.register_blueprint(view)
    app.run(debug=True)
    
    # Document.__table__.columns
    # Document.__table__.foreign_keys