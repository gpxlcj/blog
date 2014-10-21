from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

#标签
class Lable(models.Model):
   
    content = models.CharField(verbose_name=u'内容', max_length = 200)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签类'

#文章类
class Article(models.Model):
    
    title = models.CharField(verbose_name=u'标题', max_length=200)
    content = models.CharField(verbose_name=u'内容', max_length=2000)
    top  = models.BooleanField(verbose_name=u'是否置顶', default=False)
    time = models.DateTimeField(verbose_name=u'时间', auto_now=True)
    author = models.CharField(verbose_name=u'作者', auto_now=True)

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章类'

    def __unicode__(self):
        return '%s', %self.title

#评论类
class Comment(MPTTModel):

    name = models.CharField(verbose_name=u'昵称', max_length =100)
    email = models.EmailField(verbose_name=u'邮箱')
    blog = models.UrlField(verbose_name='个人网址', blank = True)
    content = models.CharField(verbose_name=u'内容'， max_length=1000)
    title = models.CharField(verbose_name=u'标题', max_length=200)
    article = models.ForeignKey(Article,verbose_name=u'所属文章')

    parent_comment = models.TreeForeignKey('self', verbose_name=u'父评论', blank=True, null=True)
    
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论类'

    class MPTTMeta:
        parent_atr = 'parent_comment'
    
    def __unicode__(self):
        return '%s', %self.content


