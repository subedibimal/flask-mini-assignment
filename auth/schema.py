import graphene

from sqlalchemy.exc import IntegrityError

from werkzeug.security import generate_password_hash

from config.database import db_session
from config.helpers import check

from .models import User

class Register(graphene.Mutation):
    error = graphene.String()
    message  = graphene.String()
    success = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        email = graphene.String(required=True)
        location = graphene.String()
        password = graphene.String(required=True)
        confirm_password = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name, email, location, password, confirm_password):
        if not check(email):
            return Register(error="Please enter correct email address.")
        if password != confirm_password:
            return Register(error="Passwords did not match.")
        try:
            new_user = User(
                name=name,
                email=email,
                location=location,
                password=generate_password_hash(password, method="sha256")
            )
            db_session.add(new_user)
            db_session.commit()
        except IntegrityError as e:
            return Register(error=f'{ e.orig }')
        return Register(success=True, message="User successfully created.")

class Mutation(graphene.ObjectType):
    register = Register.Field()