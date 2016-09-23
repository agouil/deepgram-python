import requests

from log import logger
from urlparse import urljoin


class Http(object):

    def __init__(self, root_domain):
        """
        Class constructor.

        Params:
            endpoint (string): The endpoint to make requests to
        """

        self.root_domain = root_domain
        self.logger = logger()

    def get_request_url(self, endpoint):
        return urljoin(self.root_domain, endpoint)

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

    def get(self, endpoint='', params=None, format='json'):
        """
        Executes a GET request to the remote server.

        Params:
            endpoint (string): The remote endpoint
            params (dict): A dictionary of any URL parameters to pass
                           to the GET request
            format (string): The response format
        """
        request_endpoint = self.get_request_url(endpoint)
        self.logger.debug({
            'endpoint': request_endpoint, 'method': 'GET', 'params': params})
        response = requests.get(request_endpoint, params=params)
        return self.parse_response(response, format)

    def post(self, endpoint='', params=None, format='json'):
        """
        Executes a POST request to the remote server.

        Params:
            endpoint (string): The remote endpoint
            params (dict): A dictionary of parameters to pass
                           to the POST request
            format (string): The response format
        """

        request_endpoint = self.get_request_url(endpoint)
        self.logger.debug({
            'endpoint': request_endpoint, 'method': 'POST', 'params': params})
        response = requests.post(request_endpoint, data=params)
        return self.parse_response(response, format)
