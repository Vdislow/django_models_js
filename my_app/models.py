from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Фамилия Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Электоронная почта')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'

    def __str__(self):
        return f'{self.name}'


class Work(models.Model):
    address = models.CharField(max_length=100, verbose_name='Адрес')
    city = models.CharField(max_length=30, verbose_name='Город')
    company = models.CharField(max_length=50, verbose_name='Место работы')
    postalZip = models.CharField(max_length=30, verbose_name='Почтовый индекс')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Данные о месте работы'
        db_table = 'work'

    def __str__(self):
        return f'{self.company}'


class Account(models.Model):
    pin = models.IntegerField(verbose_name='ПИН-код')
    acc_num = models.CharField(max_length=100, verbose_name='Счет')
    pan = models.CharField(max_length=30, verbose_name='Номер карты')
    cvv = models.IntegerField(verbose_name='CVV')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        db_table = 'account'

    def __str__(self):
        return f'{self.acc_num}'
