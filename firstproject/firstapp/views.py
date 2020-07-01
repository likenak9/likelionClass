from django.shortcuts import render
import random
# Create your views here.

def index(request):
    context = {}
    if request.GET.get('lotto'):
        print('clear')
        lotto_list = list(range(1,46))
        print(lotto_list)
        result_lotto = random.sample(lotto_list,6)
        print(result_lotto)
        context['result_lotto'] = result_lotto
        print(context)
    return render(request,'index.html',context)