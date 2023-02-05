from django.db import models


class Video(models.Model):
    url_video = models.URLField(max_length=1000, verbose_name='Ссылка на видео')
    title = models.CharField(max_length=200, verbose_name='Название видео')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title


class WhatsApp(models.Model):
    url_video = models.URLField(max_length=1000, verbose_name='Ссылка WA')

    class Meta:
        verbose_name = 'Ссылка WA'
        verbose_name_plural = 'Ссылка WA'


class Main(models.Model):
    image_one = models.ImageField(upload_to='images', verbose_name='Фото 1')
    title_one = models.CharField(
        max_length=200,
        verbose_name='Текст внутри фото 1'
    )
    image_two = models.ImageField(upload_to='images', verbose_name='Фото 2')
    title_two = models.CharField(
        max_length=200,
        verbose_name='Текст внутри фото 2'
    )
    image_three = models.ImageField(upload_to='images', verbose_name='Фото 3')
    title_three = models.CharField(
        max_length=200,
        verbose_name='Текст внутри фото 3'
    )
    image_four = models.ImageField(upload_to='images', verbose_name='Фото 4')
    title_four = models.CharField(
        max_length=200,
        verbose_name='Текст внутри фото 4'
    )
    image_five = models.ImageField(upload_to='images', verbose_name='Фото 5')
    title_five = models.CharField(
        max_length=200,
        verbose_name='Текст внутри фото 5'
    )
    image_six = models.ImageField(upload_to='images', verbose_name='Фото 6')
    title_six = models.CharField(
        max_length=200,
        verbose_name='Текст внутри фото 6'
    )
    image_metod = models.ImageField(
        upload_to='images',
        verbose_name='Методичка'
    )
    title_metod = models.TextField()
    image_info = models.ImageField(
        upload_to='images',
        verbose_name='Фото рядом с тестом'
    )
    title_info = models.TextField()

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'
