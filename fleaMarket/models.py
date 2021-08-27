from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import os

class FleaMarket(models.Model):
    title = models.CharField('제품명', max_length=200)    # 제품 제목
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #작성자   
    price = models.CharField('가격', max_length=100)    # 가격

    region = models.CharField('지역', max_length=30)    # 지역
    lat = models.FloatField('위도') # 위도
    long = models.FloatField('경도') # 경도

    category_choices = (
        ('디지털기기','디지털기기'),
        ('생활가전','생활가전'),
        ('가구/인테리어','가구/인테리어'),
        ('유아동','유아동'),
        ('생활/가공식품','생활/가공식품'),
        ('스포츠/레저','스포트/레저'),
        ('여성잡회/의류', '여성잡화/의류'),
        ('남성잡화/의류', '남성잡화/의류'),
        ('뷰티/미용', '뷰티/미용'),
        ('도서/티켓/음반', '도서/티켓/음반'),
        ('기타 중고물품', '기타 중고물품'),
    )
    category = models.TextField('카테고리', choices=category_choices) # 제품 카테고리
    pub_date = models.DateTimeField() # 게시 날짜
    content = models.TextField('설명')       # 제품 설명
    image = models.ImageField('제품 사진', upload_to='fleaMarket/', blank = True, null = True)  
    image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(200,200)], options={'quality': 100})  # 썸네일

    file = models.FileField('첨부 파일', upload_to='fleaMarket/',  blank = True, null = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50]

    def get_filename(self):
        return os.path.basename(self.file.name)