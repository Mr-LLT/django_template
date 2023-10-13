from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    from django.conf import settings
    
    name = getattr(settings, 'SITE_NAME', 'django')
    
    return HttpResponse(f'<h1>Welcome to {name}</h1>')

    