from allauth.account.forms import LoginForm, SignupForm

#reference: https://django-allauth.readthedocs.io/en/latest/forms.html

class LoginAllauthForm(LoginForm):

    def __init__(self, *args, **kwargs):
        print(self.base_fields)
        #ここでフォームのcssをいじる
        super().__init__(*args, **kwargs)

    def login(self, *args, **kwargs):
        print(self)
        print(dir(self))

        # Add your own processing here.

        # You must return the original result.
        return super().login(*args, **kwargs)

class SignupAllauthForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super().save(request)

        # Add your own processing here.

        # You must return the original result.
        return user