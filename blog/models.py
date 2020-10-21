from django.db import models
from django.core.exceptions import ValidationError
import django.utils as utils
import datetime as dt
import markdown2


def validate_id(value):
    """ проверяет, что строка value включает только _, a-z, A-Z, 0-9 """
    for c in value:
        if c != '_' and (c < 'a' or c > 'z') and (c < 'A' or c > 'Z') and \
                (c < '0' or c > '9'):
            raise ValidationError("может содержать только _, 0-9, a-z, A-Z")


class Tag(models.Model):
    """ Модель для тегов """

    tag_name = models.CharField(max_length = 200, verbose_name='тег')
    tag_id = models.CharField(max_length = 200, 
                              unique = True, 
                              validators=[validate_id],
                              verbose_name='ID тега для посетителей сайта')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class ArticleManager(models.Manager):
    """ Менеджер, возвращающий только опубликованные статьи  """

    def get_queryset(self):
        """ возвращает опубликованные статьи, в порядке от новых к старым """
        now = utils.timezone.now()
        return super().get_queryset().filter(publication_date__lt = now).\
                order_by('-publication_date')


class Article(models.Model):
    """ Модель для статей """

    markdown_text = models.TextField(verbose_name='текст в формате markdown')
    article_id = models.CharField(max_length = 200, 
        unique=True, 
        validators=[validate_id],
        verbose_name='ID статьи для посетителями сайта')
    preview = models.TextField(max_length = 1024,
        verbose_name=('выдержка из статьи в формате markdown для'
                      ' предварительного просмотра'))
    tags = models.ManyToManyField(Tag, verbose_name='теги')
    publication_date = models.DateTimeField(
        verbose_name='дата и время публикации статьи')

    objects = models.Manager()
    published_articles = ArticleManager()

    def is_published(self):
        """ возвращает True, если статья опубликована """
        now = utils.timezone.now()
        return (self.publication_date - now).days < 0

    def article_header(self):
        """ извлекает первый встретившийся заголовок из текста статьи """
        i = 0
        header = ''

        while i < len(self.markdown_text) and self.markdown_text[i] != '#':
            i += 1

        while i < len(self.markdown_text) and self.markdown_text[i] == '#':
            i += 1

        while i < len(self.markdown_text) and self.markdown_text[i] not in \
                ['#', '\n', '\r']:
            header += self.markdown_text[i]
            i += 1

        if len(header) == 0:
            header += 'No header'

        return header

    def get_tags(self):
        """ возвращает теги, под которыми опубликована статья """
        tag_names = []

        for tag in self.tags.all():
            tag_names.append(tag.tag_name)

        return tag_names

    def html(self):
        """ возвращает текст статьи в формате HTML """
        return markdown2.markdown(self.markdown_text)

    def preview_html(self):
        """ возвращает фрагмент для предварительного просмотра в HTML """
        return markdown2.markdown(self.preview)

    def __str__(self):
        return self.article_header()

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'







