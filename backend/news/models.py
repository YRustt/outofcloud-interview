from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=256,
    )
    link = models.URLField(
        max_length=256
    )
    image = models.ImageField(
        blank=True,
        null=True
    )
    description = models.TextField()
    content = models.TextField()
    published = models.DateTimeField()
    categories = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE
    )
    site = models.OneToOneField(
        to='NewsSite',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return f"{str(self.site)}: \"{self.title}\""


class Category(models.Model):
    name = models.CharField(
        max_length=256
    )
    site = models.OneToOneField(
        to="NewsSite",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("name", "site"),)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{str(self.site)}: \"{self.name}\""


class NewsSite(models.Model):
    name = models.CharField(
        max_length=256,
        primary_key=True
    )
    rss_url = models.URLField(
        max_length=256,
        unique=True
    )

    class Meta:
        verbose_name = "News site"
        verbose_name_plural = "News sites"

    def __str__(self):
        return self.name

