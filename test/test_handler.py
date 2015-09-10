from base import BaseThemovaTest


class TestRootResourse(BaseThemovaTest):

    def test_root(self):
        expected = {'message': 'TheMova API'}
        response = self.client.get('/')
        self.assertEquals(expected, response.json)
