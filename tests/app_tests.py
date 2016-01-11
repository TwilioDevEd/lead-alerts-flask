import unittest

from base import BaseTestCase

class AppTests(BaseTestCase):
    def test_get_to_root_should_render_default_view(self):
        self.client.get('/')

        self.assert_template_used('index.html')

if __name__ == '__main__':
    unittest.main()
