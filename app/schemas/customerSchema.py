from app.schemas import ma
from marshmallow import fields

# Define the Customer Schema
class CustomerSchema(ma.Schema):
    id = fields.Integer(required = False) # ID is auto generated
    first_name = fields.String(required = True)
    last_name = fields.String(required= True)
    username = fields.String(required= True)
    email = fields.String(required= True)
    password = fields.String(required= True)


# Create instances of the schema
# Input Schema
customer_input_schema = CustomerSchema()
customer_output_schema = CustomerSchema(exclude=["password"])
customers_schema = CustomerSchema(many= True, exclude=["password"])
customer_login_schema = CustomerSchema(only=["username", "password"])
