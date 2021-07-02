from django.views.generic import ListView,DetailView,CreateView,FormView,DeleteView,UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse



class HomeView(ListView):
    model = Post
    template_name = 'Article/index.html'
    context_object_name = 'blog_entries'
    ordering = ['-publish', ]
    paginate_by = 10

    # login_url = 'users:login'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'Article/post_detail.html'
    # entry = get_object_or_404(Entry)
    # comments = entry.comments.filter()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        context.update({'next': reverse('comments-xtd-sent')})
        return context

    def detail(self,request, slug):
        q = Post.objects.filter(slug__iexact=slug)

        if q.exists():
            q = q.first()
        else:
            return HttpResponse('<h1>Post Not Found</h1>')
        context = {

            'post': q
        }
        return context

    # def my_view(self,request):
    #     if not request.user.is_authenticated:
    #         return redirect('%s?next=%s'%(settings.LOGIN_URL,request.path))


class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    # form = EntryForm
    # form_class = EntryForm
    template_name = 'Article/create_post.html'
    fields = ['title','image','body']
    # success_url = 'blog-home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title','image','body']
    template_name = 'Article/update_post.html'
    # context_object_name = 'update'


class DeletePostView(LoginRequiredMixin,DeleteView):
    model =  Post
    template_name = 'Article/comfirm_delete_post.html'
    # success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

