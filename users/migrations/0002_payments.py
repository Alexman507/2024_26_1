# Generated by Django 4.2.14 on 2024-07-30 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_course_owner_lesson_owner_subscription'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата оплаты')),
                ('payment_amount', models.PositiveIntegerField(verbose_name='Сумма оплаты')),
                ('payment_type', models.CharField(choices=[('CASH', 'Наличными'), ('ONLINE', 'Перевод')], max_length=20, verbose_name='Тип оплаты')),
                ('session_id', models.CharField(blank=True, max_length=400, null=True, verbose_name='ID сессии')),
                ('link', models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Оплаченный курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='Оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
