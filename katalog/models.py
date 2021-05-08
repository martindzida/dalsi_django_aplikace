from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

# Create your models here.


class Kategorie(models.Model):
    nazev_kategorie = models.CharField(max_length=50, unique=True, verbose_name="Název kategorie",
                                       help_text='Zadejte název kategorie o maximální délce 50 znaků; název musí být jedinečný')

    class Meta:
        ordering = ["nazev_kategorie"]
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return f"{self.nazev_kategorie}"

    def get_absolute_url(self):
        return reverse('kategorie', args=[str(self.id)])


class Kolekce(models.Model):
    nazev_kolekce = models.CharField(max_length=50, unique=True, verbose_name="Název kolekce",
                                     help_text='Zadejte název kolekce o maximální délce 50 znaků; název musí být jedinečný')
    datum_vydani = models.DateField(
        verbose_name="Datum vydání kolekce", help_text='Zadejte datum vydání kolekce')

    class Meta:
        ordering = ["nazev_kolekce"]
        verbose_name = 'Kolekce'
        verbose_name_plural = 'Kolekce'

    def __str__(self):
        return f"{self.nazev_kolekce}"

    def get_absolute_url(self):
        return reverse('kolekce', args=[str(self.id)])


class Produkt(models.Model):
    nazev = models.CharField(max_length=50, unique=True, verbose_name="Název prodkutu",
                             help_text='Zadejte název produktu o maximální délce 50 znaků; název musí být jedinečný')
    popis = models.TextField(blank=True, null=True,
                             verbose_name="Popis produktu")
    cena = models.IntegerField(validators=[MinValueValidator(
        1)], verbose_name="Cena produktu", help_text='Zadejte cenu produktu vyšší než 1')
    pocet_ks = models.IntegerField(validators=[MinValueValidator(
        0)], verbose_name="Počet kusů na skladě", help_text='Zadejte počet kusů na skladě')
    foto = models.ImageField(upload_to='produkty',
                             blank=True, verbose_name="Fotka produktu")
    kategorie = models.ForeignKey(Kategorie, on_delete=models.RESTRICT)
    kolekce = models.ForeignKey(Kolekce, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["-cena", "nazev"]
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return f"{self.nazev}, {self.kategorie}"

    def get_absolute_url(self):
        return reverse('produkt', args=[str(self.id)])
