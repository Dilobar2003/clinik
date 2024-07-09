from django.db import models





class DoctorsModel(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/')
    face = models.URLField(max_length=200)
    tel = models.URLField(max_length=200)
    insta = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'


class ServiseModel(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'servise'
        verbose_name_plural = 'servises'



