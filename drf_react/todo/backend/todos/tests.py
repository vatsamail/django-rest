from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first-test todo')
        Todo.objects.create(description='some random description given')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first-test todo')

    def test_description_content(self):
        todo = Todo.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'some random description given')
