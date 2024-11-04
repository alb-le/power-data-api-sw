import requests

from app.services.exceptions import SwApiError, SwApiNotFoundError


class SwApiService:
    def __init__(self):
        self.domain = "https://swapi.dev/api"
        self.retry = 3
        self.timeout = 5

    def __generate_url(self, path: str) -> str:
        if self.domain in path:
            return path
        return self.domain + path

    def __get(self, path):
        retry = self.retry
        url = self.__generate_url(path)

        while retry:
            res = requests.get(url=url, timeout=self.timeout)

            if res.status_code == 200:
                return res

            elif res.status_code == 404:
                raise SwApiNotFoundError(f"404: {path}")

            retry -= 1

        raise SwApiError(f"{res.status_code}: {res.text}")

    def __get_batch(self, fist_response) -> list[dict]:
        items = fist_response.get('results') or []
        next_path = fist_response.get('next')

        while next_path:
            response = self.__get(next_path).json()
            next_path = response.get('next')
            items.extend(response.get('results'))

        return items

    def get(self, path: str) -> dict | list[dict]:
        response = self.__get(path).json()
        if 'next' in response:
            return self.__get_batch(response)
        return response
