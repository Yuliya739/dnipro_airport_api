from flask.json import jsonify
from sqlalchemy_serializer import SerializerMixin
import uuid

class CustomSerializerMixin(SerializerMixin):
    serialize_types = (
        (uuid.UUID, lambda x: str(x)),
    )