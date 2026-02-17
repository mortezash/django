# blog/middleware.py

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("Middleware initialized")  # فقط برای تست

    def __call__(self, request):

        blocked_ip = "127.0.0.111"
        print(request.META.get("REMOTE_ADDR"))
        if request.META.get("REMOTE_ADDR") == blocked_ip:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("دسترسی ممنوع!")

        print(f"Incoming request path: {request.path}")  # قبل از View
        response = self.get_response(request)
        print(f"Outgoing response status: {response.status_code}")  # بعد از View
        return response
