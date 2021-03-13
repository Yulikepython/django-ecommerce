AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS=False
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 認証方法をメールアドレスにする
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # Userモデルにusernameは無い
ACCOUNT_EMAIL_REQUIRED = True # メールアドレスを要求する
ACCOUNT_USERNAME_REQUIRED = False # ユーザー名を要求しない
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_MAX_EMAIL_ADDRESSES = 10

ACCOUNT_FORMS = {
    'login': 'accounts.allauth_forms.LoginAllauthForm',
}