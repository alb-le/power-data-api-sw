import unittest
from unittest.mock import patch, MagicMock

from app.services.exceptions import SwApiNotFoundError, SwApiError
from app.services.swapi import SwApiService


class SwApiServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.swapi_service = SwApiService()
        self.domain_mock = "https://swapi.dev/api"

    @staticmethod
    def generate_mock_response(json_dto, mock_requests, status_code: int = 200):
        mock_res = MagicMock()
        mock_res.status_code = status_code
        mock_res.json.return_value = json_dto
        mock_requests.get = MagicMock(return_value=mock_res)
        return mock_res

    def test_generate_url(self):
        path = "/test"
        generated_url = self.swapi_service._SwApiService__generate_url(path)
        self.assertEqual("https://swapi.dev/api/test", generated_url)

    @patch("app.services.swapi.requests")
    def test_get(self, mock_requests):
        mock_res = MagicMock()
        mock_res.status_code = 200
        json_dto = {'test_key': 'test_value'}
        mock_res.json.return_value = json_dto
        mock_requests.get.return_value = mock_res

        mock_path = "/test"
        res = self.swapi_service.get(mock_path)

        self.assertEqual(json_dto, res)
        mock_requests.get.assert_called_once_with(url='https://swapi.dev/api/test', timeout=self.swapi_service.timeout)

    @patch("app.services.swapi.requests")
    def test_get_not_found(self, mock_requests):
        self.generate_mock_response(json_dto={}, mock_requests=mock_requests, status_code=404)

        with self.assertRaises(SwApiNotFoundError) as context:
            self.swapi_service.get('test')

    @patch("app.services.swapi.requests")
    def test_get_retry(self, mock_requests):
        self.generate_mock_response(json_dto={}, mock_requests=mock_requests, status_code=500)

        with self.assertRaises(SwApiError) as context:
            self.swapi_service.get('test')
        self.assertEqual(self.swapi_service.retry, mock_requests.get.call_count)

    @patch("app.services.swapi.requests")
    def test_get_batch(self, mock_requests):
        def mock_response(url, *arg, **args):
            mock_res_1 = MagicMock()
            mock_res_1.url = self.domain_mock + url
            mock_res_1.status_code = 200
            mock_res_1.json.return_value = {"next": "https://swapi.dev/api/test/?page=2",
                                            "results": [{"test_key1": "test_value1"}]
                                            }
            if url == "https://swapi.dev/api/test":
                return mock_res_1

            mock_res_2 = MagicMock()
            mock_res_2.url = "https://swapi.dev/api/test/?page=2"
            mock_res_2.status_code = 200
            mock_res_2.json.return_value = {"next": None,
                                            "results": [{"test_key2": "test_value2"}]
                                            }
            if url == "https://swapi.dev/api/test/?page=2":
                return mock_res_2

        mock_requests.get = MagicMock(side_effect=mock_response)
        response = self.swapi_service.get('/test')
        self.assertEqual([{"test_key1": "test_value1"}, {"test_key2": "test_value2"}], response)

    @patch("app.services.swapi.requests")
    def test_get_batch_empty_result(self, mock_requests):
        def mock_response(url, *arg, **args):
            mock_res_1 = MagicMock()
            mock_res_1.url = self.domain_mock + url
            mock_res_1.status_code = 200
            mock_res_1.json.return_value = {"next": "https://swapi.dev/api/test/?page=2",
                                            "results": None
                                            }

            mock_res_2 = MagicMock()
            mock_res_2.url = "https://swapi.dev/api/test/?page=2"
            mock_res_2.status_code = 200
            mock_res_2.json.return_value = {"next": "https://swapi.dev/api/test/?page=3",
                                            "results": []
                                            }


            mock_res_3 = MagicMock()
            mock_res_3.url = "https://swapi.dev/api/test/?page=3"
            mock_res_3.status_code = 200
            mock_res_3.json.return_value = {"next": None,
                                            "results": [{"test_key3": "test_value3"}]
                                            }
            match url:
                case "https://swapi.dev/api/test":
                    return mock_res_1
                case "https://swapi.dev/api/test/?page=2":
                    return mock_res_2
                case "https://swapi.dev/api/test/?page=3":
                    return mock_res_3

        mock_requests.get = MagicMock(side_effect=mock_response)
        response = self.swapi_service.get('/test')
        self.assertEqual([{"test_key3": "test_value3"}], response)


if __name__ == '__main__':
    unittest.main()
