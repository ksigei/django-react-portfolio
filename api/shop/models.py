from django.db import models
from blog.models import Category
import uuid

# product images
def product_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'media/products/%s' % (filename)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-id']

# cart and checkout
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_id = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['-date_added']

class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        ordering = ['-id']

# order
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    token = models.CharField(max_length=200, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Order Total')
    emailAddress = models.EmailField(max_length=200, blank=True, verbose_name='Email Address')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

# order item
class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=1, verbose_name='Quantity')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    def sub_total(self):
        return self.quantity * self.price
    
    def __str__(self):
        return self.product
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        ordering = ['-id']

# search
class Search(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    search = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.search
    
    class Meta:
        verbose_name = 'Search'
        verbose_name_plural = 'Searches'
        ordering = ['-created_at']

# review
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    rating = models.IntegerField(default=1)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']

# wishlist

# order tracker

# payment

# shipping

# refund

# coupon

# discount

# gift card

# faq

# terms and conditions

# privacy policy

# return policy

# shipping policy


