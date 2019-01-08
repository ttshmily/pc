from account.models import Users, Tokens
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class Authentication(TokenAuthentication):
    model = Tokens
    keyword = 'Token'

    # def authenticate(self, request):
    #     token = request.META.get("HTTP_X_AUTH_TOKEN")
    #     if not token:
    #         raise exceptions.NotAuthenticated("X-Auth-Token is required")
    #     t1 = Tokens.objects.filter(token=token).first()
    #     if not t1:
    #         raise exceptions.AuthenticationFailed('认证失败')
    #     return (t1.user, t1.token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(token=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')
        # if not token.user.is_active:
        #     raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (token.user, token)

    def authenticate_header(self, request):
        pass


class FirstAuthentication(TokenAuthentication):

    pass
