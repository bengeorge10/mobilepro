from django.shortcuts import redirect


def login_required(func):  # decorator function
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("userlogin")
        return func(request, *args, **kwargs)

    return wrapper


# giving requirements to admin
def admin_only(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:  # checking user is superuser means admin
            return redirect("userlogin")
        return func(request, *args, **kwargs)

    return wrapper
