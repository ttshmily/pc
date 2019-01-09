from account.models import Users, Tokens
from rest_framework.authentication import TokenAuthentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.six import text_type


def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, text_type):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


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

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            msg = 'Authentication needed.'
            raise exceptions.AuthenticationFailed(msg)
            # return None
        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)
        if auth[0].lower() != self.keyword.lower().encode():
            msg = 'Invalid token keyword.'
            raise exceptions.AuthenticationFailed(msg)
        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(token=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')
        # if not token.user.is_active:
        #     raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (token.user, token)


class FirstAuthentication(TokenAuthentication):

    pass
