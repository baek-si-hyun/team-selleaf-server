from django.db import models

class User(Period):
    user_email = models.CharField(max_length=255, null=False, blank=False)
    user_password = models.CharField(max_length=255, null=False, blank=False)
    user_name = models.CharField(max_length=255, null=False, blank=False)
    # True: 휴면, False: 비휴면
    user_status = models.BooleanField(default=False)
    # True: 수신 동의, False: 수진 비동의
    marketing_agree = models.BooleanField(default=False)
    # True: 강사, False: 일반 회원
    teacher_status = models.BooleanField(default=False)
    # True: 문자 수신 동의, False: 문자 수신 비동의
    sms_agree = models.BooleanField(default=False)
    user_profile = models.ImageField(null=False, blank=False, upload_to='profile/%Y/%m/%d')

    class Meta:
        db_table = 'tbl_user'

class UserAddress(Address):
    address_name = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'tbl_user_address'
