from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware to restrict access to authenticated users only.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Cek apakah pengguna telah login atau belum
        if not request.user.is_authenticated and not request.path == reverse('login'):
            return HttpResponseRedirect(reverse('login'))
        response = self.get_response(request)
        return response
