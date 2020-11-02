from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default=None)
    category_h1 = models.TextField(blank=True, null=True, default=None, verbose_name='Заголовок страницы', help_text='Данный текст будет помещен в заголовок h1 карточки товара. Если значение не указано, то заголовок будет браться из названия товара')
    category_seo_title = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='ТЭГ <title>', help_text='Данный текст будет помещен в значение тега title. Значение этого поля будет отобображено во вкладке браузера. Это поле необходисо для SEO продвижения')
    category_seo_meta_description = models.CharField(max_length=225, blank=True, null=True, default=None, verbose_name='ТЭГ <meta description> (для SEO)', help_text='Данный текст будет отображен в meta теге description, в качестве значения атрибута content. Это поле необходимо для SEO продвижения')
    category_seo_meta_keywords = models.CharField(max_length=225, blank=True, null=True, default=None, verbose_name='ТЭГ <meta keywords>', help_text='Данный текст будет отображен в meta теге keywords, в квчестве значения атрибута content. Это поле необъодимо для SEO продвижения')
    category_seo_hidden_title_h2 = models.CharField(max_length=125, blank=True, null=True, default=None, verbose_name='ТЭГ <h2>. Скрытый заголовок (для SEO)', help_text='Скрытый текст! Данный текст будет помещен в заголовок h2 карточки товара')
    category_seo_hidden_text_after_h2 = models.TextField(blank=True, null=True, default=None, verbose_name='ТЭГ <p>. Скрытый текст, относящийся к <h2> (для SEO)', help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h2')

    is_active = models.BooleanField(default=True)


    def __str__(self):
        return 'Категория %s' % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default=None, verbose_name='Наименование товара')
    price = models.IntegerField(default=0, null=True, verbose_name='Цена товара без скидки')  #max_digits=10, decimal_places=2, default=0
    discount = models.IntegerField(default=0, null=True, verbose_name='Цена товара со скидкой')
    quantity = models.IntegerField(default=0, null=True, verbose_name='Количество')
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, verbose_name='Категория товара')
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание, выводимое на странице категорий')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание, выводимое в карточке товара')
    is_active = models.BooleanField(default=True, verbose_name='Активность')  # отображать товар или нет
    title_h1 = models.TextField(blank=True, null=True, default=None, verbose_name='Заголовок страницы', help_text='Данный текст будет помещен в заголовок h1 карточки товара. Если значение не указано, то заголовок будет браться из названия товара')
    seo_hidden_title_h2 = models.CharField(max_length=125, blank=True, null=True, default=None, verbose_name='ТЭГ <h2>. Скрытый заголовок (для SEO)', help_text='Скрытый текст! Данный текст будет помещен в заголовок h2 карточки товара')
    seo_hidden_text_after_h2 = models.TextField(blank=True, null=True, default=None, verbose_name='ТЭГ <p>. Скрытый текст, относящийся к <h2> (для SEO)', help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h2')
    seo_hidden_title_h3 = models.CharField(max_length=125, blank=True, null=True, default=None, verbose_name='ТЭГ <h3>. Скрытый заголовок (для SEO)', help_text='Скрытый текст! Данный текст будет помещен в заголовок h3 карточки товара')
    seo_hidden_text_after_h3 = models.TextField(blank=True, null=True, default=None, verbose_name='ТЭГ <p>. Скрытый текст, относящийся к <h3> (для SEO)', help_text='Скрытый текст! Данный текст будет помещен в тег p в карточке товара под заголовком h3')
    text_blockquote = models.TextField(blank=True, null=True, default=None, verbose_name='ТЭГ <blockquote>. Скрытая цитата. (для SEO)', help_text='Данный текст будет помещен в тег blockquote карточки товара')
    seo_meta_description = models.CharField(max_length=225, blank=True, null=True, default=None, verbose_name='ТЭГ <meta description> (для SEO)', help_text='Данный текст будет отображен в meta теге description, в качестве значения атрибута content. Это поле необходимо для SEO продвижения')
    seo_meta_keywords = models.CharField(max_length=225, blank=True, null=True, default=None, verbose_name='ТЭГ <meta keywords>', help_text='Данный текст будет отображен в meta теге keywords, в квчестве значения атрибута content. Это поле необъодимо для SEO продвижения')
    seo_title = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name='ТЭГ <title>', help_text='Данный текст будет помещен в значение тега title. Значение этого поля будет отобображено во вкладке браузера. Это поле необходисо для SEO продвижения')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # как будет отображаться каждая заявка (ссылочка)
    # и так он будет выглядеть в выпадашке
    def __str__(self):
        return '%s, %s' % (self.price, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')  # куда загружать картинку относительно папки медиа НЕ СТАВИТЬ ЛИШНИЙ СЛЕШ
    alt_text = models.CharField(max_length=200, blank=True, null=True, default=None, verbose_name='Альтернативный текст для изображения. Он будет отображаться, если картинка не подгрузилась. Необходим для SEO оптимизации')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # как будет отображаться каждая заявка (ссылочка)
    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


# Подписчики
class Subscribers(models.Model):
    class Meta():
        db_table = 'Заявки по e_mail'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Все заявки'

    name = models.CharField(max_length=200, verbose_name="Имя")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    comments = models.TextField(blank=True, null=True, default=None, verbose_name="Комментарий к заказу")

#как будет отображаться каждая заявка ()
    def __str__(self):
        return self.name
