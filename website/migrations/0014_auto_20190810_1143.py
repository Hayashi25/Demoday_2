# Generated by Django 2.2.4 on 2019-08-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20190810_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escola',
            name='telefone_escola',
        ),
        migrations.AddField(
            model_name='escola',
            name='diretor_responsavel',
            field=models.CharField(default=1, max_length=12, verbose_name='Diretor Responsável'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='escola',
            name='codigo_acesso',
            field=models.CharField(blank=True, error_messages={'unique': 'Código de acesso já existente.'}, max_length=12, unique=True, verbose_name='Registre um código de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='confirmar_senha',
            field=models.CharField(blank=True, max_length=12, verbose_name='Confirme a senha de acesso'),
        ),
        migrations.AlterField(
            model_name='escola',
            name='senha_acesso',
            field=models.CharField(blank=True, max_length=12, verbose_name='Senha de acesso'),
        ),
    ]
