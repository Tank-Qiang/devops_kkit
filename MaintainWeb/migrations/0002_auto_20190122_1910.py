# Generated by Django 2.1.4 on 2019-01-22 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MaintainWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minionname', models.CharField(max_length=64, null=True, unique=True, verbose_name='minion名')),
                ('biosversion', models.CharField(max_length=32, null=True, verbose_name='bios版本')),
                ('cpu_model', models.CharField(max_length=128, null=True, verbose_name='cpu型号')),
                ('cpuarch', models.CharField(max_length=32, null=True, verbose_name='系统位码')),
                ('hostname', models.CharField(max_length=64, null=True, verbose_name='主机名')),
                ('kernelrelease', models.CharField(max_length=64, null=True, verbose_name='内核版本')),
                ('machine_id', models.CharField(max_length=64, null=True, verbose_name='machine_id')),
                ('master', models.CharField(max_length=64, null=True, verbose_name='master名称')),
                ('num_cpus', models.IntegerField(null=True, verbose_name='cpu数量')),
                ('mem_total', models.IntegerField(null=True, verbose_name='内存')),
                ('osfinger', models.CharField(max_length=64, null=True, verbose_name='系统版本')),
                ('osrelease', models.CharField(max_length=64, null=True, verbose_name='系统发行版本号')),
                ('productname', models.CharField(max_length=64, null=True, verbose_name='产品名称')),
            ],
        ),
        migrations.CreateModel(
            name='Trouble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('detail', models.TextField()),
                ('ctime', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, '未处理'), (2, '处理中'), (3, '已处理')], default=1)),
                ('solution', models.TextField(null=True)),
                ('ptime', models.DateTimeField(null=True)),
                ('pj', models.IntegerField(choices=[(1, '不满意'), (2, '一般'), (3, '活很好')], default=2, null=True)),
                ('processer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='hosts',
            options={},
        ),
        migrations.RemoveField(
            model_name='hosts',
            name='hostname',
        ),
        migrations.AddField(
            model_name='hosts',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hosts',
            name='minionstatus',
            field=models.CharField(choices=[('Unaccepted', 'Unaccepted'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Unaccepted', max_length=32, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='jid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tasklogdetail',
            name='jid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tasklogdetail',
            name='pid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='action_type',
            field=models.IntegerField(choices=[(0, 'CMD'), (1, 'Login'), (2, 'Logout'), (3, 'GetFile'), (4, 'SendFile'), (5, 'exception'), (6, 'Accredit')], default=0),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MaintainWeb.IDC', verbose_name='IDC'),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='ip_addr',
            field=models.GenericIPAddressField(unique=True, verbose_name='主机ip'),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='memo',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='备注信息'),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='port',
            field=models.IntegerField(default=22, verbose_name='端口'),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='system_type',
            field=models.CharField(choices=[('windows', 'Windows'), ('linux', 'Linux/Unix')], default='linux', max_length=32, verbose_name='系统'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='name',
            field=models.CharField(choices=[('1', '北京'), ('2', '天津')], max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='tasklog',
            name='task_type',
            field=models.CharField(choices=[('cmd', 'CMD'), ('file_send', '批量发送文件'), ('file_get', '批量下载文件'), ('Accredit', 'token授予'), ('saltstack', 'saltstack操作')], max_length=50),
        ),
        migrations.AlterField(
            model_name='tasklogdetail',
            name='result',
            field=models.CharField(choices=[('success', 'Success'), ('failed', 'Failed'), ('unknown', 'Unknown'), ('delete', 'Delete')], default='unknown', max_length=30),
        ),
        migrations.AlterField(
            model_name='token',
            name='expire',
            field=models.IntegerField(default=600),
        ),
        migrations.AddField(
            model_name='hosts',
            name='hostinfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MaintainWeb.HostInfo', verbose_name='主机详情'),
        ),
    ]
