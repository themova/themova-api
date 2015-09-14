from base import BaseThemovaTest


class TestRootResourse(BaseThemovaTest):

    def test_root(self):
        expected = {'message': 'TheMova API'}
        response = self.client.get('/')
        self.assertEquals(expected, response.json)


class TestTranslationListResourse(BaseThemovaTest):

    def test_create_translation_empty_data(self):
        expected = {'error': 'No input data provided.'}
        params = {}
        response = self.client.post('/translations/', data=params)
        self.assertEquals(expected, response.json)
        self.assertEquals(400, response.status_code)

    def test_create_translation_empty_title(self):
        expected = {'error': {'title': ['Data not provided.']}}
        params = {'title': '',
                  'text': 'A bunch of text to test.'}
        response = self.client.post('/translations/', data=params)
        self.assertEquals(expected, response.json)
        self.assertEquals(422, response.status_code)

    def test_create_translation_empty_text(self):
        expected = {'error': {'text': ['Data not provided.']}}
        params = {'title': 'title',
                  'text': ''}
        response = self.client.post('/translations/', data=params)
        self.assertEquals(expected, response.json)
        self.assertEquals(422, response.status_code)

    def test_create_translation(self):
        expected = {'title': 'testing title', 'text': ''}
        params = {'title': 'testing title',
                  'text': 'A bunch of text to test.'}
        response = self.client.post('/translations/', data=params)
        self.assertEquals(expected, response.json)
        self.assertEquals(201, response.status_code)
