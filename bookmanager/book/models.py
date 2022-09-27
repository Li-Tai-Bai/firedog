from django.db import models

# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        p = []
        p.append(self.name)
        p.append(self.book)
        return p

