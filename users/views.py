from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm #was used before
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from users.models import Profile
from shop.models import Shop
def register_view(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid() :
            username=form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}!\n You can now Login In")
            form.save()
            return redirect('users-login')
    else :
        form=UserRegisterForm()
    context={
        "form":form,
        "title":"Register"
    }
    return render(request,'users/register.html',context)

@login_required
def profile_view(request):
        #Profile Update part
        if request.method == 'POST' :
            u_form = UserUpdateForm(request.POST,
                                    instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                    request.FILES, #Because we will update media files as well
                                    instance=request.user.profile)
            if p_form.is_valid() :
                # u_form.save()
                p_form.save()
                messages.success(request,f"Your profile has been updated.")
                return redirect('/profile/')
        else:
            # u_form=UserUpdateForm(instance=request.user)
            p_form=ProfileUpdateForm(instance=request.user.profile)
        #Shops you own (for sellers) part
        shops=Shop.objects.filter(owner=request.user.id)
        context={
                'title':'Profile',
                # 'u_form':u_form,
                'p_form':p_form,
                'shops':shops,
        }
        return render(request, 'users/profile.html',context)

@login_required
def settings_view(request):
    context={
            'title':'Settings'
    }
    return render(request, 'users/settings.html',context)
