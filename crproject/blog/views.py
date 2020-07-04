from django.shortcuts import render,redirect

from .models import Post
# Create your views here.
def index(request):
    context = dict()
    all_post = Post.objects.all()
    
    context['display_post'] = all_post
    return render(request, 'index.html', context)
    
def second(request):
    return render(request, 'second.html')

def create(request):
#    tmp_post = Post()
#    tmp_post.tilte = request.GET.get('title')
#    tmp_post.nickname = request.GET.get('nickname')
#    tmp_post.nickname = request.GET.get('body')
#
#    tmp_post.save()
    Post.objects.create(title = request.POST.get('title'), nickname = request.POST.get('nickname'), body = request.POST.get('body'))
    print(request.POST.get('title'))
    return redirect('index')