# Generated by Django 2.1.2 on 2018-11-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20181108_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('formal-wear', 'formal-wear'), ('boxers', 'boxers'), ('loafers', 'loafers'), ('bombers', 'bombers'), ('dress-pants', 'dress-pants'), ('backpacks', 'backpacks'), ('gloves', 'gloves'), ('polo', 'polo'), ('Hoodies-and-Zipups', 'Hoodies-and-Zipups'), ('other', 'other'), ('bras', 'bras'), ('vests', 'vests'), ('joggers', 'joggers'), ('jewelry', 'jewelry'), ('suits', 'suits'), ('wallets', 'wallets'), ('corsets-and-bodysuits', 'corsets-and-bodysuits'), ('sweatshirts', 'sweatshirts'), ('sweatpants', 'sweatpants'), ('belts', 'belts'), ('hats', 'hats'), ('trousers', 'trousers'), ('crewnecks', 'crewnecks'), ('briefs', 'briefs'), ('scarves', 'scarves'), ('shorts', 'shorts'), ('pants', 'pants'), ('cardigans', 'cardigans'), ('sneakers', 'sneakers'), ('long-sleeves', 'long-sleeves'), ('eyewear', 'eyewear'), ('jackets', 'jackets'), ('coats', 'coats'), ('t-shirt', 't-shirt'), ('jeans', 'jeans'), ('socks', 'socks'), ('tank-tops', 'tank-tops'), ('turtlenecks', 'turtlenecks'), ('thongs', 'thongs'), ('dress-shirt', 'dress-shirt'), ('blazers', 'blazers')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='url_img',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='url_original',
            field=models.URLField(max_length=1000),
        ),
    ]
