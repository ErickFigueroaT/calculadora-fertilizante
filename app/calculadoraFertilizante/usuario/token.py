from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class Token(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: AbstractBaseUser, timestamp):

        return (six.text_type(user.pk) + six.text_type(timestamp)) + six.text_type(user.is_active)

token_activacion=Token()