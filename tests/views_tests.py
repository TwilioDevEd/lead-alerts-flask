import unittest
from mock import patch

from base import BaseTestCase

class ViewsTests(BaseTestCase):
    def test_get_to_root_should_render_default_view(self):
        self.client.get('/')
        self.assert_template_used('index.html')

    @patch('lead_alerts.services.twilio_service.TwilioService.send_message')
    def test_post_to_notifications_should_send_a_message(self, mock_service):
        response = self.client.post('/notifications',
                data = dict(
                    house_title = 'house title',
                    name = 'name',
                    phone = 'phone',
                    message = 'message'
                ),
                follow_redirects=True)

        mock_service.assert_called_with(
            'New lead received for house title. Call name at phone. Message message')

if __name__ == '__main__':
    unittest.main()
