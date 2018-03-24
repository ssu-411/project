# Generated by Django 2.0.3 on 2018-03-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_middleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bigImage',
            field=models.ImageField(blank=True, default='books/None/no-imgl.jpg', upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='middleImage',
            field=models.ImageField(blank=True, default='books/None/no-imgm.jpg', upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='smallImage',
            field=models.ImageField(blank=True, default='books/None/no-imgs.jpg', upload_to='books'),
        ),
    ]