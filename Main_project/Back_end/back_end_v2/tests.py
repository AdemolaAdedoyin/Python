import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import Back_end_views
        request = testing.DummyRequest()
        info = Back_end_views(request)
        self.assertEqual(info['project'], 'Back_end')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from Back_end.back_end_v2 import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
