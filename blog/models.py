from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """
    Django要求模型必须继承models.Model类.
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型,CharField 是字符型。
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然Django 还为我们提供了多种其它的数据类型，如日期类型DataTimeField,整型类型IntegerField等等。
    Django 内置的全部类型可看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

class Tag(models.Model):
    """
    标签Tag也比较简单，和Category一样，
    只有一个 name 实例。
    """
    name = models.CharField(max_length=100)

class Post(models.Model):
    """
    文章的数据表稍微复杂一点，主要涉及的字段更多。
    """
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文，我们使用了 TextField.
    # 存储比较短的字符可以使用CharField，但对于文章的正文来说可能会是一大段文本，因此使用TextField来存储大段文本。
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间， 存储时间的字段用DateTimeField类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下CharField 要求我们必须存入数据，否则会报错。
    # 指定 CharField 的 blank = Ture 值后，就允许为空了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类， 标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章智能对应一个分类， 但是一个分类下可以有多个文章，所以我们使用的是ForeignKey, 即一对多的关联关系。
    # 而对于标签来说， 一篇文章可以有多个标签，同一个标签下也可能有多篇文章， 所以我们使用MonyToManyField，表明这是多对多的关系。
    # 同时我们规定文章可以没有标签，因此为标签tags 制定了 blank=True
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者， 这里User是从django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django内置的应用，专门用于处置网站用户的注册，登录流程，User是Django为我们已经写好的用户模型
    # 这里我们通过ForeignKey 把文章和User关联起来
    # 因为我们规定一篇文章只有一个作者，而一个作者可以写多篇文章，所以这里也是一对多的关系。
    author = models.ForeignKey(User)
