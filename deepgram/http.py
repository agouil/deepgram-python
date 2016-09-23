import requests

from log import logger


class Http(object):

    def __init__(self, endpoint):
        """
        Class constructor.

        Params:
            endpoint (string): The endpoint to make requests to
        """

        self.endpoint = endpoint
        self.logger = logger()

    def parse_response(self, response, format='json'):
        """
        Parses the response from the remote server. Formats the response
        based on the 'format' parameter - default format is JSON.

        Params:
            response (Response): The request response object
            format (string): The format of the response. Defaults to JSON
        """

        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        try:
            # if format is json, then parse the json
            # else return the raw text
            if format == 'json':
                content = response.json()
            else:
                content = response.text
        except ValueError as e:
            self.logger.error(e)
            raise
        return content

    def get(self, params=None, format='json'):
        """
        Executes a GET request to the remote server.

        Params:
            params (dict): A dictionary of any URL parameters to pass
                           to the GET request
            format (string): The response format
        """

        self.logger.debug({
            'endpoint': self.endpoint, 'method': 'GET', 'params': params})
        response = requests.get(self.endpoint, params=params)
        return self.parse_response(response, format)

    def post(self, params=None, format='json'):
        """
        Executes a POST request to the remote server.

        Params:
            params (dict): A dictionary of parameters to pass
                           to the POST request
            format (string): The response format
        """

        self.logger.debug({
            'endpoint': self.endpoint, 'method': 'POST', 'params': params})
        response = requests.post(self.endpoint, data=params)
        return self.parse_response(response, format)
