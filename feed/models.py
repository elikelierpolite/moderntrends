from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Article(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True, blank=True)
  img = models.CharField(max_length=200, null=True, blank=True)
  hook = models.CharField(max_length=200, null=True, blank=True)
  body =  RichTextField(blank=True, null=True)
  body2 = RichTextField(blank=True, null=True)
  slug = models.SlugField(unique=True)
  pub_date = models.DateTimeField('date published', auto_now_add=True, null=True, blank=True)
  BREAKINGNEWS = 'BreakingNews'
  SPORTS = 'Sports'
  HEALTH = 'Health'
  POLITICS = 'Politics'
  BUSINESS = 'Business'
  ADVERT = 'ADVERT'
  category = [
        (BREAKINGNEWS, 'BreakingNews'),
        (SPORTS, 'Sports'),
        (HEALTH, 'Health'),
        (POLITICS, 'Politics'),
        (BUSINESS, 'Business'),
        (ADVERT, 'Advert'),
    ]
  category = models.CharField(
        max_length=200,
        choices=category,
        default=BREAKINGNEWS,
    )
  is_ad = models.BooleanField()
  cta = models.CharField(max_length=500, null=True, blank=True)
  theme = models.CharField(max_length=500, null=True, blank=True)
  ad_url = models.CharField(max_length=500, null=True, blank=True)
  
  def get_absolute_url(self):
    return reverse('articles', args=[str(self.slug)])
  
  def __str__(self):
    return self.headline
    
def create_slug(instance, new_slug=None):
  slug = slugify(instance.title)
  if new_slug is not None:
    slug = new_slug
  qs = Article.objects.filter(slug=slug).order_by("-id")
  exists = qs.exists()
  if exists:
    new_slug = "%s-%s" %(slug, qs.first().id)
    return create_slug(instance, new_slug=new_slug)
  return slug
  
def pre_save_post_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = create_slug(instance)
    
    
pre_save.connect(pre_save_post_receiver, sender=Article)
    
class Discover(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    discover_text = models.CharField(null=True,max_length=200)
    discover_hook = models.CharField(null=True,max_length=200)
    discover_img = models.TextField()
    slug = models.SlugField(unique=True)
    hook = models.CharField(max_length=200, null=True, blank=True)
    is_ad = models.BooleanField(default=False)
    cta = models.CharField(null=True,max_length=200, blank=True)
    url = models.CharField(null=True,max_length=200, blank=True)

    def __str__(self):
        return self.discover_text
        
def create_slug_d(instance, new_slug=None):
  slug = slugify(instance.discover_text)
  if new_slug is not None:
    slug = new_slug
  qs = Article.objects.filter(slug=slug).order_by("-id")
  exists = qs.exists()
  if exists:
    new_slug = "%s-%s" %(slug, qs.first().id)
    return create_slug(instance, new_slug=new_slug)
  return slug
  
def pre_save_post_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = create_slug_d(instance)
    
pre_save.connect(pre_save_post_receiver, sender=Discover)


class DiscoverPage(models.Model):
    discover = models.ForeignKey(Discover, on_delete=models.CASCADE)
    discover_title = models.CharField(max_length=200)
    discover_img = models.TextField()
    up_next_title = models.CharField(max_length=200, null=True)
    up_next_img = models.TextField(null=True)
    up_next_url = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.discover_title
    
class Topten(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    list_headline = models.CharField(null=True,max_length=200)
    list_img = models.TextField(null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.list_headline
        
def create_slug_t(instance, new_slug=None):
  slug = slugify(instance.list_headline)
  if new_slug is not None:
    slug = new_slug
  qs = Article.objects.filter(slug=slug).order_by("-id")
  exists = qs.exists()
  if exists:
    new_slug = "%s-%s" %(slug, qs.first().id)
    return create_slug(instance, new_slug=new_slug)
  return slug
  
def pre_save_post_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = create_slug_t(instance)
    
pre_save.connect(pre_save_post_receiver, sender=Topten)


class ListItem(models.Model):
    topten   = models.ForeignKey(Topten, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=200, null=True)
    item_content = RichTextField(blank=True, null=True)
    

    def __str__(self):
        return self.item_title
        
class Celebrity(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True)
  img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  body = RichTextField(blank=True, null=True)
  def __str__(self):
    return self.headline

def create_slug_d(instance, new_slug=None):
  slug = slugify(instance.headline)
  if new_slug is not None:
    slug = new_slug
  qs = Celebrity.objects.filter(slug=slug).order_by("-id")
  exists = qs.exists()
  if exists:
    new_slug = "%s-%s" %(slug, qs.first().id)
    return create_slug(instance, new_slug=new_slug)
  return slug
  
def pre_save_post_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = create_slug_c(instance)
    
pre_save.connect(pre_save_post_receiver, sender=Celebrity)
  
class Weview(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True)
  img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  body = RichTextField(blank=True, null=True)
  
  def __str__(self):
    return self.headline
  
class Video(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    headline = models.CharField(max_length=200, null=True)
    thumbnail = models.TextField(null=True)
    slug = models.SlugField(unique=True)
    video = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True, null=True)
    
    def __str__(self):
      return self.headline
    
class Finance(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True)
  img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  body = RichTextField(blank=True, null=True)
  
  def __str__(self):
      return self.headline
  
class Future(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True)
  img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  body = RichTextField(blank=True, null=True)
  
  def __str__(self):
      return self.headline
  
  
class Product(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  headline = models.CharField(max_length=200, null=True)
  img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  body = RichTextField(blank=True, null=True)
  name = models.CharField(max_length=200, null=True)
  ELECTRONICS = 'Electronics'
  CLOTHING = 'Clothing'
  HOME = 'Home'
  ACCESSORIES = 'Accessories'
  BEAUTY = 'Beauty'
  BOOKS = 'Books'
  TOYS = 'Toys'
  APPLIANCES = 'Appliances'
  OFFICE = 'Office'
  PERSONAL = 'Personal'
  GAMES = 'Games'
  SPORTS = 'Sports'
  PETS = 'Pets'
  PC = 'Pc'
  VIDEO = 'Video'
  category = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (HOME, 'Home'),
        (ACCESSORIES, 'Accessories'),
        (BEAUTY, 'Beauty'),
        (BOOKS, 'Books'),
        (TOYS, 'Toys'),
        (APPLIANCES, 'Appliances'),
        (OFFICE, 'Office'),
        (PERSONAL, 'Personal'),
        (GAMES, 'Games'),
        (SPORTS, 'Sports'),
        (PETS, 'Pets'),
        (PC, 'Pc'),
        (VIDEO, 'Video'),
    ]
  category = models.CharField(
        max_length=200,
        choices=category,
        default=ELECTRONICS,
    )
  price = models.CharField(max_length=200, null=True)
  description = RichTextField(blank=True, null=True)
  
  def __str__(self):
    return self.headline
  
class Productotd(models.Model):
  name = models.CharField(max_length=200, null=True)
  img = models.TextField(null=True)
  slug = models.SlugField(unique=True)
  price = models.CharField(max_length=200, null=True)
  description = RichTextField(blank=True, null=True)
  cta = models.CharField(max_length=200, null=True)
  url = models.TextField(null=True)
  
  def __str__(self):
    return self.name