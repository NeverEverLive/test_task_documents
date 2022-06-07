from marshmallow import Schema, fields


class DocumentSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    text = fields.String()
    inserted_at = fields.DateTime()
    updated_at = fields.DateTime()