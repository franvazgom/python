from django.test import TestCase
from blog.models import Category, Post
from django.contrib.auth.models import User


class TestCategoryPostModel(TestCase):
    @classmethod
    def setUpTestData(self): 
        category = Category.objects.create(name = 'Categoria 1')
        user = User.objects.create_user(username='usuario1', password='12345')
        post = Post.objects.create(
            title = "Post 1" , 
            content = "Contenido del post 1",   
            author = user
        )
        post.categories.add(category)
        post.save()
    
    def test_save(self):
        posts = Post.objects.all()
        print(posts[0], posts[0].content, posts[0].categories.all()[0])
    
    