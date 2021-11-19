import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    COMPANY = 'COMP'
    PRIVATE_PERSON = 'PRIV'
    COMPANY_PRIVATE = [
        (COMPANY, 'Компания'),
        (PRIVATE_PERSON, 'Частное лицо'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(verbose_name='Организация', max_length=250,
                                 unique=True, null=True, blank=True)
    third_name = models.CharField(verbose_name='Отчество', max_length=250, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=250, null=True, blank=True)
    status = models.CharField(verbose_name='Юр/Физлицо', max_length=50, choices=COMPANY_PRIVATE,
                              default=COMPANY)
    id_num = models.CharField(verbose_name='ИИН', max_length=15, default='000000000000', null=True, blank=True)
    # available_vacations = models.IntegerField(verbose_name='Доступные дни отпуска', default=0, blank=True)
    # deleted because not used


class Vacations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    doc_name = models.CharField(verbose_name='Название документа', max_length=250)

    # doc_id_1c = models.CharField(verbose_name='Идентификатор документа 1С', max_length=250, default='')
    # doc_id_1cDoc = models.CharField(verbose_name='Идентификатор документа 1С.Документооборот', max_length=250,
    #                                 default='')

    # days_used = models.IntegerField(verbose_name='Количество дней отпуска', default=0) deleted because not used

    id_user = models.UUIDField(default=uuid.uuid4, verbose_name='Идентификатор пользователя')
    id_num = models.CharField(verbose_name='ИИН', max_length=15, default='000000000000', null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    full_name = models.CharField(verbose_name='Организация', max_length=250)

    start_vacation = models.DateField(verbose_name='Начало отпуска', null=True)
    end_vacation = models.DateField(verbose_name='Окончание отпуска', null=True)

    doc_date = models.DateTimeField(verbose_name='Дата создания', null=True, auto_now=True, blank=True)

    vacation_status = models.CharField(verbose_name='Статус', max_length=250)
    vacation_type = models.CharField(verbose_name='Тип отпуска', max_length=250)

    class Meta:
        verbose_name = 'Заявки на отпуск'
        verbose_name_plural = 'Заявки на отпуск'


class LogList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)

    # doc_id_1c = models.CharField(verbose_name='Идентификатор документа 1С', max_length=250, default='')
    # doc_id_1cDoc = models.CharField(verbose_name='Идентификатор документа 1С.Документооборот', max_length=250,
    #                                 default='')

    id_user = models.UUIDField(default=uuid.uuid4, verbose_name='Идентификатор пользователя', editable=False)
    id_num = models.CharField(verbose_name='ИИН', max_length=15, default='000000000000', null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    full_name = models.CharField(verbose_name='Организация', max_length=250)

    doc_name = models.CharField(verbose_name='Название документа', max_length=250)
    doc_date = models.DateTimeField(verbose_name='Дата создания', null=True, auto_now=True)
    doc_status = models.CharField(verbose_name='Статус', max_length=250)

    class Meta:
        verbose_name = 'Список логов'
        verbose_name_plural = 'Список логов'


