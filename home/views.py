from django.shortcuts import render, HttpResponse
from django.templatetags.static import static

# Create your views here.
def index(request):
    my_context = {
        "name": "Taimoor Aftab",
        "designation": "Software Engineer",
        "mailing_address": "taimoor.aftab@arbisoft.com",
        "facebook": "https://www.facebook.com/taimoor.aftab.758/",
        "twitter": "https://twitter.com/taimoor_aftab",
        "linkedin": "https://www.linkedin.com/in/taimoor-aftab-130960185/",
    }
    return render(request, "index.html", context = my_context)