from django.shortcuts import render, get_object_or_404


from .models import BlogPost
# Create your views here.

def all_blogs( request):
    blogs = BlogPost.objects.order_by('-publication_date')
    return render( request, 'blog/home.html', { 'blogs': blogs})

def detail( request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
