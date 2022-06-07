from main import db
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Document(db.Model):
    __tablename__ = 'Documents'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    inserted_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    rights = relationship("Right", cascade="all, delete")

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        attrs = list(self.__dict__.keys())
        if isinstance(other, Document):
            for attr in attrs:
                if getattr(self, attr) != getattr(other, attr):
                    return False
        return True

    @classmethod
    def get_all(cls):
        return cls.query.order_by(Document.id).all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    #validate functions if need


class Right(db.Model):
    __tablename__ = 'Rights'

    id = db.Column(db.Integer(), primary_key=True)
    document_id = db.Column(db.Integer(), db.ForeignKey('Documents.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    rights_from = db.Column(db.DateTime(timezone=True), nullable=False)
    rights_to = db.Column(db.DateTime(timezone=True), nullable=False)
    inserted_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.query.order_by(Right.id).all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
