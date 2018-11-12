from nose.tools import assert_equal, assert_raises
from coolpay_api_client.api import CPApi
from coolpay_api_client import CPClient
from mock import MagicMock

class TestCPClient(object):
    def setup(self):
        self.client = CPClient('foobar')
        self.api = self.client.api
        self.api.perform = MagicMock()

    def test_api_instance(self):
        assert isinstance(self.client.api, CPApi)

    def test_get_delegation(self):
        self.client.get("/dummy")
        self.api.perform.assert_called_once_with("get", "/dummy")

    def test_post_delegation(self):
        self.client.post("/dummy")
        self.api.perform.assert_called_once_with("post", "/dummy")

    def test_delete_delegation(self):
        self.client.delete("/dummy")
        self.api.perform.assert_called_once_with("delete", "/dummy")

    def test_put_delegation(self):
        self.client.put("/dummy")
        self.api.perform.assert_called_once_with("put", "/dummy")

    def test_patch_delegation(self):
        self.client.patch("/dummy")
        self.api.perform.assert_called_once_with("patch", "/dummy")

    def test_non_http_method(self):
        def request_foobar(client, path):
            return self.client.foobar(path)

        assert_raises(AttributeError, request_foobar, self.client, "/dummy")
