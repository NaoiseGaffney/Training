from .forms import LoginForm, UserRegistrationForm, \
    UserEditForm, ProfileEditForm, OrderCommentForm
from .models import Profile, Order
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages


"""
Django Account methods for:
- Registration
- Login (Django Authentication using @login_required)
- Edit Character Profile
- Character Dashboard upon successful login
"""


@login_required
def dashboard(request):
    """
    Character Dashboard after successful login.
    """
    order = Order.objects.all()
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard', 'order': order})


def comment_edit(request, comment_id):
    print("comment_id:", comment_id)
    order = get_object_or_404(Order, id=comment_id)
    if request.method == 'POST':
        form = OrderCommentForm(request.POST, instance=order)
        print(request.POST, comment_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success: rating and comment updated.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error: rating and comment NOT updated.')
            
    form = OrderCommentForm(instance=order)
    context = {
        'form': form
    }
    return render(request, 'account/comment_edit.html', context)


@login_required
def comment_delete(request, comment_id):
    """
    Delete comment and rating of order (course or coaching session related).
    """
    comment = get_object_or_404(Order, id=comment_id)
    comment.comment = ''
    comment.rating = 0
    comment.save()
    return redirect('dashboard')


def register(request):
    """
    Register user using UserRegistrationForm.
    If request is GET, render 'account/register.html' to register a new user.
    If request is POST, render 'account/register_done.html' after a successful registration.
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)

            return render(request, 'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    """
    Edit/Update Character Profile after registration and login.
    If request is GET provide current Character Profile.
    If request is POST update Character Profile in DB.
    """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f'{request.user} profile updated successfully.')
        else:
            messages.error(request, f'Error updating {request.user} profile.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})
