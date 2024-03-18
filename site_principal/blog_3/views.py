from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Biscoito, Post, Projeto, Assuntos
from ..resume.models import Resume

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)

        context['biscoito'] = Biscoito.objects.order_by('?').first()
        context['projetos'] = Projeto.objects.order_by('-created')[:5]
        context['post'] = Post.objects.order_by('-created')[:10]

        return context


class PostView(TemplateView):
    template_name = 'post.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        pk = self.request.GET.get('pk')        
       
        post = get_object_or_404(Post, id=pk)
        context = {
            'post': post,
            'biscoito': Biscoito.objects.order_by('?').first()
                  }
            
        return render(request, self.template_name, context)
    

class ProjetoView(TemplateView):
    template_name = 'projeto.html'

