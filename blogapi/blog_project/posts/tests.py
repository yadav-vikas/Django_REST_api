from django.test import TestCase

from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):

    @classmethod
    def setUp(cls):
        #user testuser1
        testuser1 = User.objects.create_user('username', 'abc123')
        testuser1.save()

        # blog post
        test_post = Post.objects.create(author=testuser1,title='Blog title',body='Body of testuser1')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'Blog title')
        self.assertEqual(body,'Blog of testuser1')
        

