import graphene

import auth.schema

schema = graphene.Schema(query=auth.schema.Query, mutation=auth.schema.Mutation)