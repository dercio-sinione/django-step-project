import graphql_jwt
from graphene import ObjectType, Schema
from django.dispatch import receiver
from graphql_jwt.refresh_token.signals import refresh_token_rotated
from .utils import ObtainJSONWebToken

# Here is where you will put your schema from app you have created
from users.graphql.schema import Query as usersQuery, Mutation as usersMutation


class Query(usersQuery, ObjectType):
    pass


class Mutation( usersMutation, ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.refresh_token.relay.DeleteRefreshTokenCookie.Field()
        
    #One time only use refresh token
    @receiver(refresh_token_rotated)
    def revoke_refresh_token(sender, request, refresh_token, **kwargs):
        refresh_token.revoke(request)


schema = Schema(query=Query, mutation=Mutation)
