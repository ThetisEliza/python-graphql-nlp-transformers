import graphene
import os
from server.schema.levenshtein_calc import LevenshteinDistanceMutation

class Query(graphene.ObjectType):
    monitoring = graphene.Boolean(required=True)

    def resolve_monitoring(self, info):
        return True


class Mutation(graphene.ObjectType):
    levenshtein_distance = LevenshteinDistanceMutation.Field()

Schema = graphene.Schema(query=Query, mutation=Mutation)