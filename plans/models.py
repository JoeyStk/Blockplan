# from tabnanny import verbose
# from tkinter import CASCADE
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

class Class(models.Model):
    """
    Das Klassen-Model

    name: CharField, frei wählbar (z.B. 11aFI2)
    profession: CharField, Dropdown-Feld für den Beruf. Optionen: Elektro oder IT (editiere PROFESSION_CHOICES um mehr Optionen hinzuzufügen)
    year: CharField, Dropdown-Feld für die Jahrgangsstufe. Optionen: 10. bis 13. Klasse (editiere YEAR_CHOICES um mehr Optionen hinzuzufügen)
    group: CharField, Dropdown-Feld für den Block. Optionen: a bis c (editiere GROUP_CHOICES um mehr Optionen hinzufügen)

    """
    name = models.CharField(max_length=32)
    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES, default='it')
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, default="10")
    group = models.CharField(max_length=12, choices=GROUP_CHOICES, default="a", null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Klassen"

class Week(models.Model):
    """
    Das Wochen-Model

    name: CharField, frei wählbar (z.B. 22KW37)
    week_id: IntegerField, frei wählbar (z.B. 37 für KW37)
    school: Boolean Field, bei False wird die Woche farblich markiert (für Ferienwochen deaktivieren)
    start_date: DateField, Startdatum für die Woche festlegen
    end_date: DateField, Enddatum für die Woche festlegen
    commentary: CharField, frei wählbar um einen Kommentar zur Woche hinzuzufügen
    amound_of_days: IntegerField, Anzahl der Tage an denen die Berufsschule stattfindet
    reference: ManyToManyField, Feld um die Klassen zuzuweisen
    ordering: Option die Sortierung zu ändern

    """
    name = models.CharField(max_length=255, verbose_name="Name")
    week_id = models.IntegerField(
        null = True,
        default=1,
        verbose_name="Kalendarwoche"
    )
    school = models.BooleanField(verbose_name="Schulwoche", null=False, default=True)
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
    ordering = ('-week_id')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blockwochen"
    
class Plan(models.Model):
    """
    Das Blockplan-Model

    name: CharField, freiwählbar. Name des Blockplans
    status: BooleanField, standardmäßig deaktiviert (um neuen Blockplan anzeigen zu lassen Checkbox aktivieren)
    weeks: ManyToManyField, die Wochen für einen Blockplan wählen

    """
    name = models.CharField(max_length=255)
    status = models.BooleanField(verbose_name="Blockplan online stellen")
    weeks = models.ManyToManyField(Week, default="", verbose_name="Wochen zuordnen")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blockpläne"
