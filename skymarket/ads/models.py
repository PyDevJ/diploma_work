from django.utils import timezone
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    """Модель объявление."""
    title = models.CharField(max_length=100, verbose_name='название товара')
    price = models.PositiveIntegerField(verbose_name='цена товара', default=0)
    description = models.TextField(verbose_name='описание товара', **NULLABLE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='автор объявления', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='дата и время создания объявления')
    image = models.ImageField(upload_to='ads/', verbose_name='фото товара', **NULLABLE)

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ('-created_at',)


class Comment(models.Model):
    """Модель отзыв."""
    text = models.TextField(verbose_name='текст отзыва')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='автор отзыва', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление, под которым оставлен отзыв',
                           **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='дата и время создания отзыва')

    def __str__(self):
        return f'{self.text} - {self.author}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ('-created_at',)
