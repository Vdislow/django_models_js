# Generated by Django 3.2 on 2022-08-06 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Фамилия Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Электоронная почта')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('company', models.CharField(max_length=50, verbose_name='Место работы')),
                ('postalZip', models.IntegerField(verbose_name='Почтовый индекс')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Данные о месте работы',
                'db_table': 'work',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField(verbose_name='ПИН-код')),
                ('acc_num', models.CharField(max_length=100, verbose_name='Счет')),
                ('pan', models.CharField(max_length=30, verbose_name='Номер карты')),
                ('cvv', models.IntegerField(verbose_name='CVV')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
                'db_table': 'account',
            },
        ),
    ]
