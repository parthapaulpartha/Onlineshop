from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
#------ profile image -------
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Profile"

#------ slider image -------
class slider_images(models.Model):
    image = models.ImageField(upload_to='slider_images', default='')
    title = models.CharField(max_length=30,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Slider Image"

#----- man ------------
class man_images(models.Model):
    image = models.ImageField(upload_to='man_images', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Man Images"

#----- woman ------------
class woman_images(models.Model):
    image = models.ImageField(upload_to='woman_images', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Woman Images"

#----- kids boy ------------
class kids_boy_image(models.Model):
    image = models.ImageField(upload_to='kids_boy_image', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kids Boy Image"

#----- kids girl ------------
class kids_girl_image(models.Model):
    image = models.ImageField(upload_to='kids_girl_image', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kids Girl Image"

#------- Electronics Phone --------
class electronics_phone(models.Model):
    image = models.ImageField(upload_to='e_phone', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Electronics Phone"

# ------- Electronics Desktop --------
class electronics_desktop(models.Model):
    image = models.ImageField(upload_to='e_desktop', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Electronics Desktop"

# ------- Electronics Laptop --------
class electronics_laptop(models.Model):
    image = models.ImageField(upload_to='e_laptop', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Electronics Laptop"


# ------- Electronics Head Phone --------
class electronics_head_phone(models.Model):
    image = models.ImageField(upload_to='e_h_phone', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Electronics Head Phone"

#----- Watch man ------------
class watch_man(models.Model):
    image = models.ImageField(upload_to='w_man', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Watch Man"

#----- Watch woman ------------
class watch_woman(models.Model):
    image = models.ImageField(upload_to='w_woman', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Watch Woman"

#----- Watch kids ------------
class watch_kids(models.Model):
    image = models.ImageField(upload_to='w_kids', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Watch Kids"

#----- Gift ------------
class gift(models.Model):
    image = models.ImageField(upload_to='gift', default='')
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Gift"

#----- Order product --------
class order(models.Model):
    name = models.ForeignKey(User, default=None, null=True, on_delete='')
    phone_number = models.IntegerField(default='')
    product_code = models.CharField(max_length=20, default='')
    quantity = models.PositiveIntegerField(default=1)
    order_place = models.CharField(max_length=30, default='')
    order_date = models.DateTimeField(default=datetime.now(),)
    delivery_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Order"

#------- Contact us -------
class contact(models.Model):
    name = models.ForeignKey(User, default=None, null=False, on_delete='')
    email = models.EmailField(max_length=50, default='')
    message = models.TextField(max_length=200, default='')

    def __str__(self):
        return str(self.name)



