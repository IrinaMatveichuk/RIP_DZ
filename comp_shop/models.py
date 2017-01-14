from django.db import models
from django.contrib.auth.models import AbstractUser


class Computer(models.Model):
    id = models.AutoField(primary_key=True)
    serial_num = models.CharField(max_length=19, unique=True,
                                  verbose_name='Серийный номер')
    comp_pic = models.ImageField(upload_to='media/', blank=True,
                                 max_length=1000,
                                 verbose_name='Фото компьютера')
    brand = models.CharField(max_length=20, default='',
                             verbose_name='Производитель')
    type = models.CharField(max_length=10, default='',
                            verbose_name='Тип')  # desktops, laptop, tablet
    screen_size = models.FloatField(verbose_name='Размер экрана')
    installed_OS = models.CharField(max_length=20, default='',
                                    verbose_name='ОС')
    processor_type = models.CharField(max_length=20, default='',
                                      verbose_name='Тип процессора')
    RAM = models.FloatField(verbose_name='Оперативная память')
    price = models.CharField(max_length=20, default='', verbose_name='Цена')

    def __str__(self):
        return str(self.serial_num)

    def in_orders(self):
        data = Computer.order_set.all()
        return len(data)

    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьтеры'


class User(AbstractUser):
    phone = models.CharField(max_length=15, default='')
    address = models.TextField(verbose_name='Адрес', default='')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.DateField(verbose_name='Дата заказа')
    user_id = models.ForeignKey(User, verbose_name='Заказчик')
    computers = models.ManyToManyField('Computer', verbose_name='Компьютеры')

    def __str__(self):
        return str(self.id)

    def count_computers(self):
        data = Order.computers.all()
        return len(data)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
