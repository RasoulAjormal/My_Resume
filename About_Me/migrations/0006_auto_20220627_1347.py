# Generated by Django 3.2.13 on 2022-06-27 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('About_Me', '0005_alter_commentsofothersmodel_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TitleWork',
            new_name='CertificateCategory',
        ),
        migrations.RenameModel(
            old_name='TitleCertificate',
            new_name='WorkSampleCategory',
        ),
        migrations.AlterModelOptions(
            name='certificatecategory',
            options={'verbose_name': 'Category Title', 'verbose_name_plural': 'Categories Titles'},
        ),
        migrations.AlterModelOptions(
            name='worksamplecategory',
            options={'verbose_name': 'WorkSampleCategory', 'verbose_name_plural': 'WorkSampleCategories'},
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='worksamples',
            name='Title',
        ),
        migrations.AddField(
            model_name='certificate',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='About_Me.certificatecategory', verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='worksamples',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='About_Me.worksamplecategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='worksamples',
            name='Company',
            field=models.CharField(max_length=100, null=True, verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='worksamples',
            name='Date',
            field=models.CharField(max_length=50, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='worksamples',
            name='Description',
            field=models.TextField(max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Web_Site',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='WebSite'),
        ),
        migrations.CreateModel(
            name='WorkSampleGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(null=True, upload_to='', verbose_name='Image')),
                ('WorkSample', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='About_Me.worksamples', verbose_name='WorkSample')),
            ],
            options={
                'verbose_name': 'WorkSampleGallery',
                'verbose_name_plural': 'WorkSampleGalleries',
            },
        ),
    ]
