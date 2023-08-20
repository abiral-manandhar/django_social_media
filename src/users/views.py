from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import UserRegisterForm, ProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from posts.models import Post

def HomeView(request):
    if request.user.is_authenticated:
        return redirect('posts:post_list')


    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/login.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'dominantColor': ((request.user.profile.dominant_color[1:len(request.user.profile.dominant_color) - 1])),
        'user_posts': Post.objects.filter(user = request.user),


    }
    print(context['user_posts'])
    return render(request, 'users/profile.html', context)
#





class PostDetail(DetailView):
    model = Post
    context_object_name = 'p'
    template_name = 'users/user-detail.html'




# def login_view(request):
#     if request.method == 'POST':
#         form = CustomAuthForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('list')
#         else:
#             print(form.errors)
#
#     else:
#         form = CustomAuthForm()
#
#     return render(request, 'users/home.html', {'form': form})
#
