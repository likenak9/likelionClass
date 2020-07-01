from django.shortcuts import render
import random
from .models import Blog

# Create your views here.

def index(request):
    context={}    # context = dict()
    if request.GET.get('lottery'):
        print("done") # 코드 확인을 하기 위해서 구문 사이에 프린트를 넣어둬라
        lotto_list = list(range(1,46))
        print(lotto_list)
        result_lotto = random.sample(lotto_list,6)
        print(result_lotto)
        context['result_lotto'] = result_lotto
        print(context)
        
    all_blog = Blog.objects.all()
    context['all_blog'] = all_blog
    one_blog = Blog.objects.get(id-1)
    context['one_blog'] = one_blog

    return render(request,'index.html',context)
    