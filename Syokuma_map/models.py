from django.db import models


class Customer(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'


class Shop(models.Model):
    shop_id = models.CharField('店id', max_length=255, primary_key=True)
    shop_name = models.CharField('店舗名', max_length=255)
    shop_ruby = models.CharField('店舗名かな', max_length=255)
    shop_address = models.CharField('店舗住所', max_length=255)
    shop_lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    shop_lng = models.DecimalField('経度', max_digits=9, decimal_places=6)
    shop_url = models.URLField('店舗URL', max_length=1000)
    shop_tel = models.DecimalField('店電話番号', max_length=12)
    shop_imageurl = models.CharField('店舗画像URL', max_length=1000)
    shop_businesshour = models.DateTimeField('店舗営業時間', max_length=30)


class Review(models.Model):
    shop_id = models.ForeignKey('店id', max_length=255)
    F_Judge = models.DecimalField('判断', max_length=20, primary_key=True)
    review_Scorenum = models.FloatField('店舗スコア', max_length=10)
    review_Commentbody = models.CharField('コメント', max_length=255)


class F_judge(models.Model):
    F_judge = models.ForeignKey()
    APPName = models.CharField('',)