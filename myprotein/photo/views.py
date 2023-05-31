from django.shortcuts import render
#djang.views.geneticからTemplateViewをインポート
from django.vies.genetic import TemplateView

class IndexView(TemplateView):
    #トップページのビュー
#index.htmlをレンダリングする
template_name = 'index.html'
# Create your views here.