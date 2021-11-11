
from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, CreateView  
from .forms import CommentForm
from Sportapp.models import Category, Comment, Post
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Q ApI for advanced search
from django.db.models import Q

# Create your views here.

# SEARCH BAR
def search_bar(request):
    if request.method == 'POST':
        search= request.POST['search']
        posts = Post.objects.filter(title__contains=search)
        return render(request, 'search_results.html', {'search':search, 
                                                        'posts': posts })
    else:
        return render(request, 'search_results.html', {})




def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # we need to add users who clicked on the button when we will include user login
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name = self.kwargs['category']).filter(status=1)
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        'category_list': category_list,
    }
    return context


class PostDetailView(DetailView):
    model= Post
    template_name = 'detail.html'
    queryset = Post.objects.filter(status=1)

    def get_context_data(self,  *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(**kwargs)       
        
        post_like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_like.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        
        return context

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form) 


    success_url = reverse_lazy('home')

   
    