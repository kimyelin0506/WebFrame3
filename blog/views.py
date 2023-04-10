from django.shortcuts import render
from .models import Post #modek에서 Post 참조
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')
    #.all() > 다 가져오기,.objects > 실제 레코드들, other_by() :순서 바꾸기, -pk : 역순

    return render(
        request,'blog/index.html',
        {
            'posts': posts, #posts 라는 변수를 사용가능
        }
    )
def single_post_page(request, pk): #pk : single_post_page라는 함수에서 pk를 변수로 받아들임
    post = Post.objects.get(pk=pk) #get() : 하나만 가져옴 ex)1,2,...
    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )