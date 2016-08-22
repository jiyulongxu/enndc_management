# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_networkdevice_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostsparepart',
            name='model',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', blank=True),
        ),
        migrations.AddField(
            model_name='networksparepart',
            name='pro_model',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7', blank=True),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='branch',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='tools',
            name='part_No',
            field=models.CharField(max_length=50, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9e\x8b\xe5\x8f\xb7', choices=[('\u5341\u5b57\u87ba\u4e1d\u5200', '\u5341\u5b57\u87ba\u4e1d\u5200'), ('\u4e00\u5b57\u87ba\u4e1d\u5200', '\u4e00\u5b57\u87ba\u4e1d\u5200'), ('\u5e73\u53e3\u94b3', '\u5e73\u53e3\u94b3'), ('\u5c16\u5634\u94b3', '\u5c16\u5634\u94b3'), ('\u659c\u53e3\u94b3', '\u659c\u53e3\u94b3'), ('\u5957\u7b52\u6273\u624b', '\u5957\u7b52\u6273\u624b'), ('\u5f00\u53e3\u6273\u624b', '\u5f00\u53e3\u6273\u624b'), ('\u529b\u77e9\u52a0\u529b\u6746', '\u529b\u77e9\u52a0\u529b\u6746'), ('\u6885\u82b1\u6273\u624b', '\u6885\u82b1\u6273\u624b'), ('\u4e07\u7528\u8868', '\u4e07\u7528\u8868'), ('\u7535\u6d41\u8868', '\u7535\u6d41\u8868'), ('\u5438\u5c18\u5668', '\u5438\u5c18\u5668'), ('\u4fbf\u643a\u5f0f\u8d77\u91cd\u673a', '\u4fbf\u643a\u5f0f\u8d77\u91cd\u673a'), ('PDU16A', 'PDU16A'), ('PDU10A', 'PDU10A'), ('\u4e09\u63d2\u5934', '\u4e09\u63d2\u5934'), ('\u7535\u8111\u684c', '\u7535\u8111\u684c'), ('\u4eba\u5b57\u68af', '\u4eba\u5b57\u68af'), ('\u5730\u725b', '\u5730\u725b'), ('\u63d2\u7ebf\u677f', '\u63d2\u7ebf\u677f'), ('\u6807\u7b7e\u673a', '\u6807\u7b7e\u673a'), ('\u6807\u7b7e\u7eb8', '\u6807\u7b7e\u7eb8'), ('\u5bf9\u8bb2\u673a', '\u5bf9\u8bb2\u673a'), ('\u7a7a\u8c03\u52a0\u6e7f\u7f50', '\u7a7a\u8c03\u52a0\u6e7f\u7f50'), ('\u5de5\u4f5c\u706f', '\u5de5\u4f5c\u706f'), ('\u79fb\u52a8\u786c\u76d8', '\u79fb\u52a8\u786c\u76d8'), ('\u7535\u8bdd\u673a', '\u7535\u8bdd\u673a'), ('\u53cc\u9762\u9ed1\u677f', '\u53cc\u9762\u9ed1\u677f'), ('CD\u76d2', 'CD\u76d2'), ('\u7535\u52a8\u624b\u94bb', '\u7535\u52a8\u624b\u94bb'), ('\u5c16\u5634\u94b3', '\u5c16\u5634\u94b3'), ('\u6587\u4ef6\u67b6', '\u6587\u4ef6\u67b6'), ('\u7535\u70d9\u94c1', '\u7535\u70d9\u94c1'), ('\u7535\u5de5\u5200', '\u7535\u5de5\u5200'), ('\u8001\u864e\u94b3', '\u8001\u864e\u94b3'), ('\u5c16\u5634\u94b3', '\u5c16\u5634\u94b3'), ('\u7ba1\u94b3', '\u7ba1\u94b3'), ('\u9524\u5b50', '\u9524\u5b50'), ('\u62c9\u94c6\u67aa', '\u62c9\u94c6\u67aa'), ('\u58c1\u7eb8\u5200', '\u58c1\u7eb8\u5200'), ('\u6fc0\u5149\u7b14', '\u6fc0\u5149\u7b14'), ('\u8ba2\u4e66\u5668', '\u8ba2\u4e66\u5668'), ('\u8ba1\u7b97\u5668', '\u8ba1\u7b97\u5668'), ('\u626b\u7801\u5668', '\u626b\u7801\u5668'), ('\u5730\u677f\u5438', '\u5730\u677f\u5438'), ('KVM\u8fde\u63a5\u7ebf', 'KVM\u8fde\u63a5\u7ebf'), ('CONSOL\u8fde\u63a5\u7ebf', 'CONSOL\u8fde\u63a5\u7ebf'), ('USB\u8f6cCOM\u8fde\u63a5\u7ebf', 'USB\u8f6cCOM\u8fde\u63a5\u7ebf'), ('\u5343\u5146\u7f51\u7ebf', '\u5343\u5146\u7f51\u7ebf'), ('\u4e07\u5146\u7f51\u7ebf', '\u4e07\u5146\u7f51\u7ebf'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4FC-FC', '\u5355\u6a21\u5343\u5146\u5149\u7ea4FC-FC'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4LC-FC', '\u5355\u6a21\u5343\u5146\u5149\u7ea4LC-FC'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4LC-LC', '\u5355\u6a21\u5343\u5146\u5149\u7ea4LC-LC'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4LC-ST', '\u5355\u6a21\u5343\u5146\u5149\u7ea4LC-ST'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4SC-LC', '\u5355\u6a21\u5343\u5146\u5149\u7ea4SC-LC'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4SC-SC\u65b9\u5934', '\u5355\u6a21\u5343\u5146\u5149\u7ea4SC-SC\u65b9\u5934'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4SC-SL', '\u5355\u6a21\u5343\u5146\u5149\u7ea4SC-SL'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4ST-SC', '\u5355\u6a21\u5343\u5146\u5149\u7ea4ST-SC'), ('\u5355\u6a21\u5343\u5146\u5149\u7ea4ST-ST', '\u5355\u6a21\u5343\u5146\u5149\u7ea4ST-ST'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4FC-FC', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4FC-FC'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4LC-FC', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4LC-FC'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4LC-LC', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4LC-LC'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4LC-ST', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4LC-ST'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4SC-LC', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4SC-LC'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4SC-SC\u65b9\u5934', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4SC-SC\u65b9\u5934'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4SC-SL', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4SC-SL'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4ST-SC', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4ST-SC'), ('\u591a\u6a21\u4e07\u5146\u5149\u7ea4ST-ST', '\u591a\u6a21\u4e07\u5146\u5149\u7ea4ST-ST'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4FC-FC', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4FC-FC'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4LC-FC', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4LC-FC'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4LC-LC', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4LC-LC'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4LC-ST', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4LC-ST'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4SC-LC', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4SC-LC'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4SC-SC\u65b9\u5934', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4SC-SC\u65b9\u5934'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4SC-SL', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4SC-SL'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4ST-SC', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4ST-SC'), ('\u5355\u6a21\u4e07\u5146\u5149\u7ea4ST-ST', '\u5355\u6a21\u4e07\u5146\u5149\u7ea4ST-ST'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4FC-FC', '\u591a\u6a21\u5343\u5146\u5149\u7ea4FC-FC'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4LC-FC', '\u591a\u6a21\u5343\u5146\u5149\u7ea4LC-FC'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4LC-LC', '\u591a\u6a21\u5343\u5146\u5149\u7ea4LC-LC'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4LC-ST', '\u591a\u6a21\u5343\u5146\u5149\u7ea4LC-ST'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4SC-LC', '\u591a\u6a21\u5343\u5146\u5149\u7ea4SC-LC'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4SC-SC\u65b9\u5934', '\u591a\u6a21\u5343\u5146\u5149\u7ea4SC-SC\u65b9\u5934'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4SC-SL', '\u591a\u6a21\u5343\u5146\u5149\u7ea4SC-SL'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4ST-SC', '\u591a\u6a21\u5343\u5146\u5149\u7ea4ST-SC'), ('\u591a\u6a21\u5343\u5146\u5149\u7ea4ST-ST', '\u591a\u6a21\u5343\u5146\u5149\u7ea4ST-ST'), ('FSP', 'FSP'), ('\u5343\u5146\u6a21\u5757', '\u5343\u5146\u6a21\u5757'), ('\u4e07\u5146\u6a21\u5757', '\u4e07\u5146\u6a21\u5757')]),
        ),
    ]