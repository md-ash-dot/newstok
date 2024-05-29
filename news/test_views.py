from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Article

class TestNewsViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.article = Article(title="Article title", author=self.user,
                         slug="article-title", excerpt="Article excerpt",
                         content="Article content", status=1)
        self.article.save()

    def test_render_article_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'article_detail', args=['article-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Article title", response.content)
        self.assertIn(b"Article content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    # def test_successful_comment_submission(self):
    #     """Test for posting a comment on a post"""
    #     self.client.login(
    #         username="myUsername", password="myPassword")
    #     post_data = {
    #         'body': 'This is a test comment.'
    #     }
    #     response = self.client.post(reverse(
    #         'article_detail', args=['article']), post_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(
    #         b'Comment submitted and awaiting approval',
    #         response.content
    #     )