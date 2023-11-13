from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField("Имя", max_length=50)
    slug = models.SlugField("url", max_length=50, unique=True)
    image = models.ImageField("Фото", upload_to="Gallery/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

class Gallery (models.Model):
    name = models.CharField("Имя", max_length=50)
    slug = models.SlugField("url", max_length=50, unique=True)
    photos = models.ManyToManyField(Photo, verbose_name="Фотографий")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
