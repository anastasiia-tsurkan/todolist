from django.test import TestCase
from django.urls import reverse

from tasklist.models import Task, Tag


class AllTests(TestCase):
    def setUp(self):
        Tag.objects.create(name="test")
        Task.objects.create(
            content="Test content",
            status=True,
        )

    def test_task_str(self):
        test_task = Task.objects.get(id=1)
        self.assertEqual(str(test_task), "Test content")

    def test_correct_task_list_response_with_correct_template(self):
        response = self.client.get(reverse("tasklist:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasklist/index.html")

    def test_tag_str(self):
        test_tag = Tag.objects.get(id=1)
        self.assertEqual(str(test_tag), "test")

    def test_correct_tag_list_response_with_correct_template(self):
        response = self.client.get(reverse("tasklist:tags-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasklist/tags_list.html")
