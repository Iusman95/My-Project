from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from user_profile.models import Profile
from django.views.generic import DetailView, CreateView
from user_profile.models import UserFollowing

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'

    def get_context_data(self,*args ,**kwargs):
        users = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class CreateProfileView(CreateView):
    model = ProfileView
    success_url = reverse_lazy('my_profile')
    template_name = 'profile/create.html'
    fields = ['avatar', 'bio']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




def post(self, requset):
    user = UserFollowing.objects.get(user_id=self.requset.get('user_id'))
    follow = UserFollowing.objects.get(user_id=self.requset.get('following_user_id'))
    follow.following.add(follow)
    user.save()
    follow.followers.add(user)
    follow.save()
    return render(requset, 'profile/profile.html', {'user':user, 'follow':follow})

