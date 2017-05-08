# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from braces.views import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import CreateAPIView

from .serializers import StarRatedReviewSerializer
from .settings import surveys_settings


class CreateStarReviewBase(CreateAPIView):
    serializer_class = StarRatedReviewSerializer

    def clean_data(self, **kwargs):
        data = kwargs['data']
        data.update({
            'content_type': self.kwargs["content_type_id"],
            'object_id': self.rated_object_id(),
            'user': self.get_user_id(),
        })
        return data

    def get_user_id(self):
        request_user = self.request.user
        if request_user.is_authenticated():
            return request_user.id

    def rated_object_id(self):
        raise NotImplementedError()

    def get_serializer(self, *args, **kwargs):
        kwargs['data'] = self.clean_data(**kwargs)
        return super(CreateStarReviewBase, self).get_serializer(*args, **kwargs)


class QuickCreateStarReviewView(CreateStarReviewBase):
    """Doesn't require login: should be hidden behind a hashed URL"""

    def rated_object_id(self):
        model_class = ContentType.objects.get_for_id(self.kwargs['content_type_id']).model_class()
        instance = model_class.objects.get(uuid=self.kwargs['uuid'])
        return instance.id

    def get_user_id(self):
        lookup_kwargs = {surveys_settings.USER_HASH_FIELD: self.kwargs['user_uid']}
        return get_user_model().objects.get(**lookup_kwargs).id


class AddStarReviewView(LoginRequiredMixin, CreateStarReviewBase):
    def rated_object_id(self):
        return self.kwargs["content_id"]
