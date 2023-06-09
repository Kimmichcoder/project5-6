# Generated by Django 3.2.4 on 2023-04-13 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(db_index=True, max_length=100, verbose_name='所属组织')),
                ('operator', models.CharField(max_length=20, verbose_name='更新人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('apply_person', models.ManyToManyField(related_name='apply_person', to=settings.AUTH_USER_MODEL, verbose_name='可申报人员')),
                ('principal', models.ManyToManyField(related_name='principal', to=settings.AUTH_USER_MODEL, verbose_name='负责人')),
            ],
            options={
                'verbose_name': '组织信息表',
                'verbose_name_plural': '组织信息表',
                'db_table': 'award_declaration_organization',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_level', models.IntegerField(choices=[(1, '中心级'), (2, '部门级'), (3, '普照奖')], verbose_name='奖项级别')),
                ('award_name', models.CharField(max_length=50, verbose_name='奖项名称')),
                ('requirement', models.TextField(verbose_name='参评要求')),
                ('status', models.IntegerField(choices=[(0, '已过期'), (1, '生效中')], default=1, verbose_name='申请状态')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('apply_person_num', models.IntegerField(default=0, verbose_name='申报人数')),
                ('award_person_num', models.IntegerField(default=0, verbose_name='获奖人数')),
                ('need_attachment', models.SmallIntegerField(choices=[(1, '打开'), (0, '关闭')], default=1, verbose_name='上传附件')),
                ('operator', models.CharField(max_length=20, verbose_name='更新人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('belonging_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award_declaration.organization')),
            ],
            options={
                'verbose_name': '奖项信息表',
                'verbose_name_plural': '奖项信息表',
                'db_table': 'award_declaration_award',
                'ordering': ['-create_time'],
            },
        ),
    ]
