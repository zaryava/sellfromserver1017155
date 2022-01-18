from django.db import models

class UbntModelTest(models.Model):
    objects = None
    ipubntone = models.CharField(max_length=50, verbose_name='IP адрес РРС')
    nameubnt = models.CharField(max_length=50, verbose_name='Имя РРС')
    nameubntline = models.CharField(max_length=100, verbose_name='Название РРЛ')
    statonoff = models.BooleanField(verbose_name='Включение/Выключение мониторинга РРЛ')
    ipubntremote = models.CharField(max_length=50, verbose_name='IP адрес РРС (remote)')
    nameubntremote = models.CharField(max_length=50, verbose_name='Имя РРС (remote)')
    prm_level = models.IntegerField(default=-90, verbose_name='Минимальный уровень приёма РРС')
    prm_level_for_stat = models.IntegerField(default=-90, verbose_name='Минимальный уровень приёма РРС (Статистика)')
    numberubntline = models.CharField(max_length=50, verbose_name='Номер РРЛ')
    ubntlogin = models.CharField(max_length=50, default='ubnt', verbose_name='Логин для входа в РРС (Для локалной и удалённой РРС)')
    ubntpassword = models.CharField(max_length=50, default='ubnt', verbose_name='Пароль для входа в РРС (Для локальной и удалённой РРС')
    rrsflag = models.IntegerField(default=0, verbose_name='Если "0" - это РРС AirFiber 11, Если "1" - это РРС Alcoma')

    class Meta:
        verbose_name_plural = 'IP адреса РРС'
        verbose_name = 'IP адрес РРС'

    def __str__(self):
        return self.ipubntone

class DataUbntall(models.Model):
    objects = None
    udprml0 = models.IntegerField(verbose_name='Уровень приёма(0) локального РРС')
    udprml1 = models.IntegerField(verbose_name='Уровень приёма(1) локального РРС')
    udprmr0 = models.IntegerField(verbose_name='Уровень приёма(0) удалённого РРС')
    udprmr1 = models.IntegerField(verbose_name='Уровень приёма(1) удалённого РРС')
    udspeedl = models.FloatField(verbose_name='Емкость приёма локального РРС')
    udspeedr = models.FloatField(verbose_name='Емкость приёма удалённого РРС')
    ipubnttwo = models.CharField(max_length=50)
    ipubnttworem = models.CharField(max_length=50)
    mistake_ip = models.CharField(max_length=1000)
    detail_txt = models.CharField(max_length=5000)
    timewrite = models.DateTimeField(auto_now_add=True, verbose_name='Записано')
    
    def __str__(self):
        return self.ipubnttwo

    class Meta:
        verbose_name_plural = 'Уровень приёма локального РРС'
        verbose_name = 'Уровень приёма локального РРС'
        ordering = ['-timewrite']

class DataUbntalways(models.Model):
    objects = None
    ipubnttwo = models.CharField(max_length=50, verbose_name='IP-адрес локальной РРС')
    ipubnttworem = models.CharField(max_length=50, verbose_name='IP-адрес удалённой РРС полученный из JSON')
    udprml0 = models.IntegerField(verbose_name='Уровень приёма(0) локальной РРС полученный из JSON')
    udprml1 = models.IntegerField(verbose_name='Уровень приёма(1) локальной РРС полученный из JSON')
    udprmr0 = models.IntegerField(verbose_name='Уровень приёма(0) удалённой РРС полученный из JSON')
    udprmr1 = models.IntegerField(verbose_name='Уровень приёма(1) удалённой РРС полученный из JSON')
    udspeedl = models.FloatField(verbose_name='Ёмкость приёма локальной РРС полученный из JSON')
    udspeedr = models.FloatField(verbose_name='Ёмкость приёма удалённой РРС полученный из JSON')
    timewrite = models.DateTimeField(auto_now_add=True, verbose_name='Записано')

    def __str__(self):
        return self.ipubnttwo

    class Meta:
        verbose_name_plural = 'Уровень приёма локальной РРС'
        verbose_name = 'Уровень приёма локальной РРС'
        ordering = ['-timewrite']

class DataUbntonce(models.Model):
    objects = None
    ipubnttwo = models.CharField(max_length=50, verbose_name='IP-адрес локальной РРС')
    detail_txt = models.CharField(max_length=5000)
    timewrite = models.DateTimeField(auto_now_add=True, verbose_name='Записано')

    def __str__(self):
        return self.ipubnttwo

    class Meta:
        verbose_name_plural = 'Детальная информация по настройкам РРС'
        verbose_name = 'Детальная информация по настройкам РРС'
        ordering = ['-timewrite']
        
class Ubsuccess(models.Model):
    '''Запись об успешном действии при доступе к РРС'''
    url = models.CharField(max_length=50) # IP-адрес РРС.
    successwrite = models.CharField(max_length=200) # Описание успешного действия.
    timewrite = models.DateTimeField(auto_now_add=True, verbose_name='Записано') 

class Ubfail(models.Model):
    '''Запись об провальном действии при доступе к РРС'''
    url = models.CharField(max_length=50) # IP-адрес РРС.
    failwrite = models.CharField(max_length=200) # Описание провального действия.
    timewrite = models.DateTimeField(auto_now_add=True, verbose_name='Записано')

class Startprocess(models.Model):
    startproc = models.BooleanField(default=False, verbose_name='Старт/Стоп Selenium')

    class Meta:
        verbose_name_plural = 'Старт/Стоп Selenium'
        verbose_name = 'Старт/Стоп Selenium'

class Listipubnt(models.Model):
    objects = None
    current_list_ip = models.CharField(max_length=1000)


class AutoRestart(models.Model):
    objects = None
    schetchik = models.IntegerField()
    firstid = models.IntegerField()	

