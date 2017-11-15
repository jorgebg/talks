a = Blog(name='Apple Blog', tagline='News about apples')
a.name
a.tagline
a.id
a.save()
a.id


Blog.objects
Blog.objects.get(id=1)
Blog.objects.get(name='Apple Blog')
Blog.objects.get(name='Guacamole')
Blog.DoesNotExist
b = Blog.objects.get(name='Apple Blog')

a == b

b.name = 'Banana Blog'
b.save()

a.name
a.save()

b.tagline = 'I like fruit'
b.save(update_fields=('tagline',))

a.tagline
a.refresh_from_db()
a.tagline

b.id
b.id = None
b.save()
b.id
b.delete()
b.save()

###

Blog.objects
Blog.objects.all()
# django/db/models/query.py:30
list(Blog.objects.all())
Blog.objects.filter(name='Apple Blog')
Blog.objects.filter(id=1, name='Apple Blog')
Blog.objects.filter(name='Apple Blog').get()
Blog.objects.get(name='Apple Blog')
c = Blog.objects.create(name='Cherry Blog', tagline='News about cherries')
c.id


c.tagline
Blog.objects.update(tagline='I like fruit')
c.refresh_from_db()
c.tagline
a.refresh_from_db()
a.tagline

Blog.objects.filter(id=1).update(tagline='I like apples')

Blog.objects.delete
Blog.objects.filter(id=3).delete()
c.delete()


###

for name in ('Bubblegum', 'Finn', 'Jake'):
    author = Author(name=name)
    author.save()

Author.objects.all().delete()

Author.objects.bulk_create(
    Author(name=name) for name in ('Bubblegum', 'Finn', 'Jake')
)

###

Author.objects.all()[:2]
Author.objects.all()[2:]

Author.objects.filter(id__gt=2)
Author.objects.filter(id__gte=2)
Blog.objects.filter(name__contains='Blog')


###

post = Post(title='How to open a banana like a monkey')
post.body
post.save()
post.blog_id = 1
post.save()

b
post.blog = b
post.save()

b.post_set
b.post_set.all()


post.authors
post.authors.all()

post.authors.add(1)
post.authors.remove(1)

Author.objects.all()
post.authors.add(1)
post.authors.all().delete()
Author.objects.all()

finn, jake = Author.objects.all()
post.authors.add(finn, jake)

finn.post_set
finn.post_set.all()

###
b.post_set
Blog.objects.filter(post__id=1)
Blog.objects.filter(post__title__contains='banana')

###

post = Post.objects.last()
post.blog
post.blog

Post.objects.bulk_create(
    Post(title='Post of ' + blog.name, blog=blog) for blog in Blog.objects.all()
)

posts = Post.objects.all()
for post in posts:
    post.blog

Post.objects.select_related('blog')
posts = Post.objects.select_related('blog')
posts[0].blog

from time import time

t = time()
posts = Post.objects.all()
for post in posts:
    post.blog
print(time()-t)

t = time()
posts = Post.objects.select_related('blog')
print(time()-t)

###

blog = Blog.objects.first()
blog.post_set.all()

blog = Blog.objects.prefetch_related('post_set').first()
blog.post_set.all()

author = Author.objects.prefetch_related('post_set').first()
author.post_set.all()

###

Post.objects.filter(n_visits__gt=F('blog__n_visits'))
Blog.objects.filter(id=b.id).update(n_visits=F('n_visits')+1)

###

Q(title__startswith='Post')
Post.objects.filter(Q(title__startswith='Post'))
Post.objects.filter(title__startswith='Post')

Q(title__startswith='Post') & Q(title__startswith='How to')
Q(title__startswith='Post') | Q(title__startswith='How to')
Post.objects.filter(Q(title__startswith='Post') | Q(title__startswith='How to'))


Q(title__startswith='Post') | ~Q(title='Post of Apple Blog')
Post.objects.filter(Q(title__startswith='Post') | ~Q(title='Post of Apple Blog'))

###
