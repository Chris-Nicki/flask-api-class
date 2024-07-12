from app.schemas import ma
from marshmallow import fields, validate

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False) # is is autogenerate
    name = fields.String(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))

# Create instance of that
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

