import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import User

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        fields = [
            'name', 'email', 'location',
        ]
        interfaces = (graphene.relay.Node,)