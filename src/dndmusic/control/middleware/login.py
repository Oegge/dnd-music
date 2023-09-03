from django.shortcuts import redirect
from django.conf import settings
from urllib.parse import urlparse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL

    def __call__(self, request):
        # Check if the user is authenticated and the request is not to the login URL.
        if not request.user.is_authenticated and not self.is_exempted(request.path):
            return redirect(f"{self.login_url}?next={request.path}")
        response = self.get_response(request)
        return response

    def is_exempted(self, path):
        """
        Check if the path is exempted from being behind the login.
        For example: login, logout, static or media urls etc.
        """
        exempted_paths = [
            self.login_url,
            # add other paths if needed like /logout/, /signup/ etc.
        ]
        # Add static and media URLs if they are not served in a different way (like by a web server).
        # Make sure 'django.contrib.staticfiles' is in your INSTALLED_APPS.
        if settings.DEBUG:
            exempted_paths.append(settings.STATIC_URL)
            exempted_paths.append(settings.MEDIA_URL)

        return any(path.startswith(exempted) for exempted in exempted_paths)
