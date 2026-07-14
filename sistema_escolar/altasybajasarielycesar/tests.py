from django.test import TestCase
from django.urls import reverse
from .models import Nota


class NotaModelTest(TestCase):
    def test_creacion_nota(self):
        nota = Nota.objects.create(texto="Hola mundo")
        self.assertEqual(str(nota), "Hola mundo")


class IndexViewTest(TestCase):
    def test_get_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_post_guarda_nota(self):
        response = self.client.post(reverse('index'), {'texto': 'Prueba'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Nota.objects.filter(texto='Prueba').exists())
