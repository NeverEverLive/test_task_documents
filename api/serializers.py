from marshmallow import Schema, fields


class DocumentSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    text = fields.String()
    inserted_at = fields.DateTime()
    updated_at = fields.DateTime()


class RightSchema(Schema):
    id = fields.Integer()
    document_id = fields.Integer()
    name = fields.String()
    text = fields.String()
    rights_from = fields.DateTime()
    rights_to = fields.DateTime()
    inserted_at = fields.DateTime()
    updated_at = fields.DateTime()
