from http import Http
from log import logger


class Deepgram(object):

    def __init__(self, api_key):
        """
        Class constructor.

        Params:
            api_key (string): The API Key
        """

        self.api_key = api_key
        self.logger = logger()
        self.client = Http('http://api.deepgram.com')

    def _get_headers(self):
        """
        Returns the custom request headers.
        """
        return {
            'Content-Type': 'application/json'
        }

    def check_balance(self):
        """
        Returns the available balance for the user.
        """

        data = {
            "action": "get_balance",
            "userID": self.api_key
        }
        try:
            response = self.client.post(
                headers=self._get_headers(), params=data)
        except Exception as e:
            self.logger.error(e)
            raise
        return response

    def check_status(self, obj):
        """
        Returns the status of an audio object on the server.

        Params:
            obj (string): The content ID of the object
        """

        data = {
            "action": "get_object_status",
            "userID": self.api_key,
            "contentID": obj
        }
        try:
            response = self.client.post(
                headers=self._get_headers(), params=data)
        except Exception as e:
            self.logger.error(e)
            raise
        return response

    def media_upload(self, media, tags=None):
        pass

    def media_upload_list(self, media_list):
        pass

    def query(self, query):
        pass

    def group_search(self, query):
        pass

    def parallel_search(self, query):
        pass

    def tag(self, obj):
        pass

    def get_tags(self, obj):
        pass

    def transcript(self, obj):
        pass
