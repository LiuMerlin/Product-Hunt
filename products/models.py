from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(default='例：百词斩-今天也是背单词的一天呦！', max_length=50)
    intro = models.TextField(default='在这里写APP介绍')
    url = models.CharField(default='http://', max_length=50)
    icon = models.ImageField(default='default_icon.png', upload_to='images/')
    image = models.ImageField(default='default_image.png', upload_to='images/')

    votes = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.title