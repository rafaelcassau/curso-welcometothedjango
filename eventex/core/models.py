# coding: utf-8

from django.db import models

# Create your models here.

from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager
from django.db.models.fields.related import ManyToManyField


class Speaker(models.Model):

    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})


class Contact(models.Model):
    
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
    )
    
    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)
    
    objects = models.Manager()
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')
    
    def __unicode__(self):
        return self.value


class Talk(models.Model):
    title = models.CharField(_(u'Título'), max_length=200)
    description = models.TextField(_(u'Descrição'))
    start_time = models.TimeField(_(u'Horário'), blank=True)
    speakers = ManyToManyField('Speaker', verbose_name=_('palestrantes'))
    
    @property
    def slides(self):
        return self.media_set.filter(kind='SL')

    @property
    def videos(self):
        return self.media_set.filter(kind='YT')
    
    objects = PeriodManager()
    
    class Meta:
        verbose_name = _('palestra')
        verbose_name_plural = _('palestras')
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('core:talk_detail', (), {'pk': self.pk})


class Course(Talk):
    slots = models.IntegerField(_('vagas'))
    notes = models.TextField(_(u'observações'))

    objects = PeriodManager()


class Media(models.Model):
    
    MEDIAS = (
        ('YT', _('YouTube')),
        ('SL', _('SlideShare')),
    )
    
    talk = models.ForeignKey('Talk', verbose_name=_('palestra'))
    kind = models.CharField(_('tipo'), max_length=2, choices=MEDIAS)
    title = models.CharField(_(u'título'), max_length=255)
    media_id = models.CharField(_('ref'), max_length=255)
    
    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)

    
