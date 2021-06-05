from sqlalchemy_serializer import SerializerMixin
import uuid

class CustomSerializerMixin(SerializerMixin):
    datetime_format = "%Y-%m-%dT%H:%M:%S%Z"
    serialize_types = (
        (uuid.UUID, lambda x: str(x)),
    )