from django.db import models





class BannerModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')
   


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

        




