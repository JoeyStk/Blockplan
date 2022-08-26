from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

PROFESSION_CHOICES = (
    ('it','It-Berufe'),
    ('elektro', 'Elektro-Berufe'),
)

YEAR_CHOICES = (
    ('10', '10. Klasse'),
    ('11', '11. Klasse'),
    ('12', '12. Klasse'),
    ('13', '13. Klasse'),
)

GROUP_CHOICES = (
    ('a', 'A-Block'),
    ('b', 'B-Block'),
    ('c', 'C-Block'),
)

ELECTRO = (
    ('a', 'A-Block'),
    ('b', 'B-Block'),
    ('c', 'C-Block'),
    ('13', '13. Klasse')
)

class Class(models.Model):
    name = models.CharField(max_length=32)
    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES, default='it')
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, default="10")
    group = models.CharField(max_length=12, choices=GROUP_CHOICES, default="a", null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Klassen"

CLASSES = (
    Class.objects.all()
)

class Week(models.Model):
    week_id = models.IntegerField(
        null = True,
        default=1,
        verbose_name="Kalendarwoche"
    )
    school = models.BooleanField(verbose_name="Schulwoche", null=False, default=True)
    name = models.CharField(max_length=255, verbose_name="Name")
    start_date = models.DateField(verbose_name="Startdatum")
    end_date = models.DateField(verbose_name="Enddatum")
    commentary = models.CharField(max_length=255, default="", verbose_name="Kommentar", blank=True)
    amound_of_days = models.IntegerField(
        null=False, 
        default=5,
        verbose_name="Anzahl an Tagen"
    )
    reference = models.ManyToManyField(
        Class, 
        verbose_name="Klassen zuordnen",
        default=""
    )
    odering = ('-week_id')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blockwochen"
    
class Plan(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(verbose_name="Blockplan online stellen")
    weeks = models.ManyToManyField(Week, default="", verbose_name="Wochen zuordnen")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blockpläne"
