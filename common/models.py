from django.db import models
# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=32, unique = True, verbose_name = '아이디')
    user_pwd = models.CharField(max_length= 128, verbose_name = '비밀번호')
    user_name = models.CharField(max_length = 16, unique = True , verbose_name = '이릉')
    user_email = models.CharField(max_length=128, unique=True, verbose_name='이메일')
    user_reg_dt = models.DateTimeField(auto_now_add = True, verbose_name='계정 생성 일시')
    #user_house = models.ForeignKey('aptcomplex.Houseinfo',on_delete = models.CASCADE)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table ='user'
        verbose_name ='유저'
        verbose_name_plural = '유저'