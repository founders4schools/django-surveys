from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.core.urlresolvers import reverse

from surveys.constants import STAR_RATING_TYPE
from surveys.models import RatingType, Rating, Review
from .models import Post


class SurveyAdminTests(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='tintin', first_name='Tintin', password='test')
        post_1 = Post.objects.create(author=user, title="Welcome", text="Hello World")
        post_2 = Post.objects.create(author=user, title="Another post", text="Bye World")
        rating_type = RatingType.objects.create(name=STAR_RATING_TYPE, min_value=0, max_value=5)
        ratings = [Rating.objects.create(type=rating_type, value=val) for val in range(6)]
        content_type = ContentType.objects.get_for_model(Post)
        Review.objects.create(rating=ratings[1], user=user, content_type=content_type, object_id=post_1.id)
        Review.objects.create(rating=ratings[5], user=user, content_type=content_type, object_id=post_2.id)
        User.objects.create_superuser(username='admin', email='admin@test.com', first_name='Admin', password='admin')

    def test_list_view(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('admin:surveys_review_changelist'))
        self.assertContains(response, 'fa-star', count=6)

    def test_list_view_filter(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('admin:surveys_review_changelist') + '?bad_reviews=y')
        self.assertContains(response, 'fa-star', count=1)
