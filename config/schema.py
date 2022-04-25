import graphene

import auth.schema

schema = graphene.Schema(mutation=auth.schema.Mutation)