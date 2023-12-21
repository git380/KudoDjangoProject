import os
import django

# Django設定をロード
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KudoDjangoProject.settings')
django.setup()

# DB作成
from MediConnect import models

# Create Employee entries
employee_data = [
    {"empid": "11111111", "empfname": "cd", "emplname": "ab", "emppasswd": "11111111", "emprole": 1},
    {"empid": "201011", "empfname": "kakeru", "emplname": "kudo", "emppasswd": "11111111", "emprole": 2},
    {"empid": "2070077", "empfname": "sho", "emplname": "kudou", "emppasswd": "11111111", "emprole": 1},
    {"empid": "333333", "empfname": "b", "emplname": "v", "emppasswd": "33333333", "emprole": 2},
    {"empid": "aaa", "empfname": "a", "emplname": "a", "emppasswd": "11111111", "emprole": 2},
]

for data in employee_data:
    models.Employee.objects.create(**data)

tabyouin_data = [
    {"tabyouinid": "1", "tabyouinmei": "nyt", "tabyouinaddres": "thrah", "tabyouintel": "090-1234-1234", "tabyouinshihonkin": 11, "kyukyu": 0},
    {"tabyouinid": "0000", "tabyouinmei": "test", "tabyouinaddres": "広島県広島市南区比治山本町１６−３５", "tabyouintel": "111-1111-1111", "tabyouinshihonkin": 100, "kyukyu": 0},
    {"tabyouinid": "0001", "tabyouinmei": "aaaa", "tabyouinaddres": "hiro", "tabyouintel": "111-1111-1111", "tabyouinshihonkin": 9999, "kyukyu": 1},
]
for data in tabyouin_data:
    models.Tabyouin.objects.create(**data)