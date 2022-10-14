from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from user.models import User

class CartProduct(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        unique_together = ('cart', 'product')
        

class Cart(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('product.Product', through='CartProduct')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Carts'
    

@receiver(post_save, sender=User)
def _post_save_receiver(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        cart = Cart.objects.create(user=user)
        cart.save()
