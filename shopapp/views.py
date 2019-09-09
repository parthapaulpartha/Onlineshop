from django.shortcuts import render, redirect
from shopapp.forms import (
        RegistrationForm,
        LoginForm,
        EditprofileForm,
        EditProfilePicForm,
        OrderProductForm,
        ContactForm,

    )
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import (
        authenticate,
        login,
        logout,
        update_session_auth_hash,
    )
from .models import (
    slider_images, man_images,
    woman_images, kids_boy_image,
    kids_girl_image, electronics_phone,
    electronics_desktop, electronics_laptop,
    electronics_head_phone, watch_man,
    watch_woman, watch_kids, gift, order
)
from django.contrib import messages

# Create your views here.

# -------- Home ------
def home(request):
    slider_image_view = slider_images.objects.all()
    arg = {'slider_image': slider_image_view}
    return render(request, 'shopapp/home.html', arg)

# -------- Registration ------
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! Your account signup successfully')
            return redirect('onlineshop/ragistration')

        else:
            messages.error(request, 'Please enter currenct informations')
            return redirect('onlineshop/registration')

    else:
        form = RegistrationForm()
        arg = {'form': form}
    return render(request, 'shopapp/registration.html', arg)

# -------- Login ------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if not user:
                messages.error(request, 'Username and Password did not matched')
                return redirect('/onlineshop/login')
            login(request, user)
            return redirect('/onlineshop/home/')
    else:
        form = LoginForm()
        arg = {'form': form}
    return render(request, 'shopapp/login.html', arg)

# -------- Logout ------
def logout_view(request):
    logout(request)
    return redirect('/onlineshop/login/')

# ------ Profile ---------
def profile(request):
    return render(request, 'shopapp/profile.html')

# ------- Edit Profile -------
def edit_profile(request):
    if request.method == 'POST':
        form_u = EditprofileForm(request.POST, instance=request.user)
        form_i = EditProfilePicForm(request.POST, request.FILES, instance=request.user.profile)
        if form_u.is_valid() and form_i.is_valid():
            form_u.save()
            form_i.save()
            messages.success(request, 'Profile Update successfully')
            return redirect('/onlineshop/profile/')
    else:
        form_u = EditprofileForm(instance=request.user)
        form_i = EditProfilePicForm(instance=request.user.profile)
        arg = {'form_u': form_u, 'form_i': form_i}
    return render(request, 'shopapp/edit_profile.html', arg)

# -------- Change Password ---------
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Change Successfully')
            return redirect('/onlineshop/profile')
        else:
            messages.error(request, 'Did not match')
            return redirect('/onlineshop/change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'shopapp/change_password.html', args)

# -------- mans product ---------
def man_image(request):
    mans_image = man_images.objects.all()
    args = {'mans': mans_image}
    return render(request, 'shopapp/man.html', args)

# -------- womans product ---------
def woman_image(request):
    womans_image = woman_images.objects.all()
    args = {'womans': womans_image}
    return render(request, 'shopapp/woman.html', args)

# -------- kids boy product ---------
def kidsboy_image(request):
    kids_boy = kids_boy_image.objects.all()
    args = {'kids': kids_boy}
    return render(request, 'shopapp/kids/boy.html', args)

# -------- kids girl product ---------
def kidsgirl_image(request):
    kids_girl = kids_girl_image.objects.all()
    args = {'kids': kids_girl}
    return render(request, 'shopapp/kids/girl.html', args)

# ------- Electronic Phone -------
def electronic_phone(request):
    e_phone = electronics_phone.objects.all()
    args = {'e_phones': e_phone}
    return render(request, 'shopapp/electronic/phone.html', args)

# ------- Electronic Desktop -------
def electronic_desktop(request):
    e_desktop = electronics_desktop.objects.all()
    args = {'e_desktops': e_desktop}
    return render(request, 'shopapp/electronic/desktop.html', args)

# ------- Electronic Laptop -------
def electronic_laptop(request):
    e_laptop = electronics_laptop.objects.all()
    args = {'e_laptops': e_laptop}
    return render(request, 'shopapp/electronic/laptop.html', args)

# ------- Electronic Phone -------
def electronic_head_phone(request):
    e_head_phone = electronics_head_phone.objects.all()
    args = {'e_head_phones': e_head_phone}
    return render(request, 'shopapp/electronic/head_phone.html', args)

# -------- watch man product ---------
def watch_mans(request):
    w_man = watch_man.objects.all()
    args = {'w_mans': w_man}
    return render(request, 'shopapp/watch/w_man.html', args)

# -------- watch woman product ---------
def watch_womans(request):
    w_woman = watch_woman.objects.all()
    args = {'w_womans': w_woman}
    return render(request, 'shopapp/watch/w_woman.html', args)

# -------- watch kids product ---------
def watch_kid(request):
    w_kid = watch_kids.objects.all()
    args = {'w_kids': w_kid}
    return render(request, 'shopapp/watch/w_kids.html', args)

# -------- gift ---------
def gifts(request):
    all_gift = gift.objects.all()
    args = {'all_gifts': all_gift}
    return render(request, 'shopapp/gift.html', args)

#-------- order products --------
def order_products(request):
    if request.method == 'POST':
        form = OrderProductForm(request.POST)
        if form.is_valid():
            form.save()
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
            messages.success(request, 'Order Successful')
            return redirect('/onlineshop/order/')

    form = OrderProductForm()
    args = {'form': form}
    return render(request, 'shopapp/order.html', args)

#-------- my order list --------
def my_order_list(request):
    my_order = order.objects.filter(name=request.user)
    args = {'my_order': my_order}
    return render(request, 'shopapp/my_order.html', args)

# -------- Edit order -------
def order_edit(request, id):
    edit = order.objects.get(id=id)
    form = OrderProductForm(request.POST, instance=edit)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Order Update successfully')
        return redirect('/onlineshop/my_order')

    else:
        form = OrderProductForm(instance=edit)
        args = {'form': form}
        return render(request, 'shopapp/order_edit.html', args)

# -------- Delete order -------
def order_delete(request, id):
    delete_order = order.objects.get(id=id)
    delete_order.delete()
    messages.success(request, 'Order Delete successfully')
    return redirect('/onlineshop/my_order/')

# -------- Contact us -------
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
            return redirect('onlineshop/contact/')
    else:
        form = ContactForm()
        args = {'form': form}
        return render(request, 'shopapp/contact.html', args)

# -------- About us -------
def about_us(request):
    return render(request, 'shopapp/about_us.html')