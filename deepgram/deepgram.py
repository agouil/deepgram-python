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
        self.group_client = Http('http://groupsearch.api.deepgram.com')

    def _get_headers(self):
        """
        Returns the custom request headers.
        """
        return {
            'Content-Type': 'application/json'
        }

    def _make_request(self, data):
        """
        Helper function to perform requests to the API.

        Params:
            data (dict): Data parameters passed to the API request
        """

        try:
            response = self.client.post(
                headers=self._get_headers(), params=data)
        except Exception as e:
            self.logger.error(e)
            raise
        return response

    def check_balance(self):
        """
        Returns the available balance for the user.
        """

        data = {
            "action": "get_balance",
            "userID": self.api_key
        }
        return self._make_request(data)

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
        return self._make_request(data)

    def upload(self, media_url, tags=None):
        """
        Uploads a remote audio file to the API.

        Params:
            media_url (string):           The URL of the remote audio file
            tags      (list) -- optional: Tags to describe the audio file
        """

        data = {
            "action": "index_content",
            "userID": self.api_key,
            "data_url": media_url
        }
        if tags and len(tags) > 0:
            data['tags'] = tags
        return self._make_request(data)

    def upload_list(self, media_list):
        """
        Uploads a list of remote audio files to the API.

        Params:
            media_list (list): A list of remote audio file URLs
        """

        data = {
            "action": "index_content_list",
            "userID": self.api_key,
            "data_url": media_list
        }
        return self._make_request(data)

    def query(self, obj, query, **kwargs):
        """
        Searches the specified object for the given term and returns the parts
        of it that contain any matches to the search term.

        Params:
            obj    (string): The content ID fo the object
            query  (string): The query term
            kwargs (dict):   Extra arguments to pass to the function. Include:
                - Nmax    (int):    The maximum number of matches to return.
                                    Default: 10
                - Pmin    (float):  The minimum probability that qualifies a
                                    match. Default: 0.55
                - snippet (bool):   Whether to return the transcript of a
                                    match. Default: True
                - sort    (string): The term to sort by. Default: 'time'
        """

        data = {
            "action": "object_search",
            "userID": self.api_key,
            "contentID": obj,
            "query": query,
            "snippet": kwargs.get("snippet", True),
            "filter": {
                "Nmax": kwargs.get("Nmax", 10),
                "Pmin": kwargs.get("Pmin", 0.55)
            },
            "sort": kwargs.get("sort", "time")
        }
        return self._make_request(data)

    def group_search(self, query, tag):
        """
        Searches in all the uploaded audio objects with a given 'tag' and
        'term' and returns the contentIDs of any matches.

        Params:
            query (string): The query term
            tag   (string): The tag to use for the search. Narrows down the
                            objects to be searched.
        """

        data = {
            "action": "group_search",
            "userID": self.api_key,
            "tag": tag,
            "query": query
        }
        try:
            response = self.group_client.post(
                headers=self._get_headers(), params=data)
        except Exception as e:
            self.logger.error(e)
            raise
        return response

    def parallel_search(self, query, **kwargs):
        """
        Searched in all the uploaded audio objects with the given 'tag' and
        'term' and returns the parts of it that contain any matches to the
        search term.

        Params:
            query  (string): The query term
            kwargs (dict):   Extra arguments to pass to the function. Include:
                - tag         (string): The tag to use for the search. Narrows
                                        down the objects to be searched.
                - snippet     (bool):   Whether to return the transcript of a
                                        match. Default: True
                - group_Nmax  (int):    The maximum number of objects to return
                                        Default: 10
                - object_Nmax (int):    The maximum number of matches to return
                                        within the same object. Default: 10
                - object_Pmin (float):  The minimum probability that qualifies
                                        a match. Default: 0.55
                - sort        (string): The term to sort by. Default: 'time'
        """

        data = {
            "action": "parallel_search",
            "userID": self.api_key,
            "query": query,
            "tag": kwargs.get("tag", ""),
            "group_filter": {
                "Nmax": kwargs.get("group_Nmax", 10)
            },
            "object_filter": {
                "Nmax": kwargs.get("object_Nmax", 10),
                "Pmin": kwargs.get("object_Pmin", 0.55)
            },
            "snippet": kwargs.get("snippet", True),
            "sort": kwargs.get("sort", "time")
        }
        try:
            response = self.group_client.post(
                headers=self._get_headers(), params=data)
        except Exception as e:
            self.logger.error(e)
            raise
        return response

    def tag(self, obj, tag):
        """
        Tags an audio object in the server with the specified tag.

        Params:
            obj (string): The content ID of the object
            tag (string): The tag of the object
        """

        data = {
            "action": "tag_object",
            "userID": self.api_key,
            "contentID": obj,
            "tag": tag
        }
        return self._make_request(data)

    def get_tags(self, obj):
        """
        Returns the tags that are associated with a specific audio object
        on the server.

        Params:
            obj (string): The content ID of the object
        """

        data = {
            "action": "get_object_tags",
            "userID": self.api_key,
            "contentID": obj
        }
        return self._make_request(data)

    def transcript(self, obj):
        """
        Returns the transcript of a specific audio object.

        Params:
            obj (string): The content ID of the object
        """

        data = {
            "action": "get_object_transcript",
            "userID": self.api_key,
            "contentID": obj
        }
        return self._make_request(data)
