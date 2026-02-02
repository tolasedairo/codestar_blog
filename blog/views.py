from django.shortcuts import render
#from django.http import HttpResponse
#from .models import Post

#def blog_home(request):
#    posts = Post.objects.filter(status=1).order_by('-created_on')
#    output = '<h1>CodeStar Blog</h1>'
#    for post in posts:
#        output += f'<h2>{post.title}</h2>'
#       output += f'<p>By {post.author} on {post.created_on}</p>'
#        output += f'<p>{post.excerpt}</p>'
#       output += '<hr>'
#    return HttpResponse(output)

from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    #template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6