from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from cities.models import City
from routes.forms import RouteForm
from trains.models import Train
from routes import views as routes_views
from cities import views as cities_views
from routes.utils import dfs_paths, get_graph


class AllTestsCase(TestCase):

    def setUp(self):
        self.city_a = City.objects.create(name='A')
        self.city_b = City.objects.create(name='C')
        self.city_c = City.objects.create(name='B')
        self.city_d = City.objects.create(name='D')
        self.city_e = City.objects.create(name='E')
        lst = [
            Train(name='t1', from_city=self.city_a, to_city=self.city_b, travel_time=9),
            Train(name='t2', from_city=self.city_b, to_city=self.city_d, travel_time=8),
            Train(name='t3', from_city=self.city_a, to_city=self.city_c, travel_time=7),
            Train(name='t4', from_city=self.city_c, to_city=self.city_b, travel_time=6),
            Train(name='t5', from_city=self.city_b, to_city=self.city_e, travel_time=3),
            Train(name='t6', from_city=self.city_b, to_city=self.city_a, travel_time=11),
            Train(name='t7', from_city=self.city_a, to_city=self.city_c, travel_time=10),
            Train(name='t8', from_city=self.city_e, to_city=self.city_d, travel_time=5),
            Train(name='t9', from_city=self.city_d, to_city=self.city_e, travel_time=4)
        ]
        Train.objects.bulk_create(lst)

    def test_model_city_duplicate(self):
        """
        Ensures that an error will be raised when creating a duplicate city
        """
        city = City(name='A')
        with self.assertRaises(ValidationError):
            city.full_clean()

    def test_model_train_duplicate(self):
        """
        Ensures that an error will be raised when creating a duplicate train (duble name)
        """
        train = Train(name='t1', from_city=self.city_a, to_city=self.city_b, travel_time=120)
        with self.assertRaises(ValidationError):
            train.full_clean()

    def test_model_train_time_duplicate(self):
        """
        Ensures that an error will be raised when creating a duplicate train (duble time)
        """
        train = Train(name='t123', from_city=self.city_a, to_city=self.city_b, travel_time=9)
        with self.assertRaises(ValidationError):
            train.full_clean()
        try:
            train.full_clean()
        except ValidationError as e:
            self.assertEqual(
                {'__all__': ['Такой поезд уже существует']},
                e.message_dict
            )
            self.assertIn(
                'Такой поезд уже существует',
                e.messages
            )

    def test_home_routes_views(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name='routes/home.html')  # правильный шаблон template
        self.assertEqual(response.resolver_match.func, routes_views.home)  # правильная функция из views

    def test_cbv_detail_views(self):  # class base view
        response = self.client.get(reverse('cities:detail', kwargs={'pk': self.city_a.id}))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name='cities/detail.html')
        self.assertEqual(
            response.resolver_match.func.__name__,
            cities_views.CityDetailView.as_view().__name__  # правильный класс из views
        )

    def test_find_all_routes(self):
        qs = Train.objects.all()
        graph = get_graph(qs)
        all_routes = list(dfs_paths(graph, self.city_a.id, self.city_e.id))
        self.assertEqual(len(all_routes), 4)

    def test_valid_route_form(self):
        # good case:
        data = {
            'from_city': self.city_a.id,
            'to_city': self.city_b.id,
            'travelling_time': 9,
            'cities': [self.city_e.id, self.city_d.id],
        }
        form = RouteForm(data=data)
        self.assertTrue(form.is_valid())
        # bad case:
        data['travelling_time'] = 9.5
        form = RouteForm(data=data)
        self.assertFalse(form.is_valid())
        data.pop('travelling_time')
        form = RouteForm(data=data)
        self.assertFalse(form.is_valid())

    def test_message_error_incorrect_travel_time(self):
        data = {
            'from_city': self.city_a.id,
            'to_city': self.city_e.id,
            'travelling_time': 9,
            'cities': [self.city_c.id],
        }
        response = self.client.post('/find_routes/', data)
        self.assertContains(response, 'Время в пути больше заданного', 1, 200)

    def test_message_error_impossible_route(self):
        data = {
            'from_city': self.city_b.id,
            'to_city': self.city_e.id,
            'travelling_time': 300,
            'cities': [self.city_c.id],
        }
        response = self.client.post('/find_routes/', data)
        self.assertContains(response, 'Маршрут через эти города невозможен', 1, 200)
