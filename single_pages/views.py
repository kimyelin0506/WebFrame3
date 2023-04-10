from django.shortcuts import render

# Create your views here.
def landing(request): #request : 유저의 요청
    return render(
        request,
        'single_pages/landing.html'
    )
def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

"""
site url ->- request -> (Django)prj -> urls.py 
                            (/admin  -> admin.site.urls
                            (''      -> single_pages/urls.py
                            (/blog   -> blog/urls.py 
                                       (views.landing 
                                       (views.about_me
"""
