# coding: utf-8

"""
    Esper SDK

    Python client library for Esper Manage APIs. You can find out more about Esper at [https://shoonya.io](https://shoonya.io).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@esper.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import esperclient
from esperclient.models.device_command_request import DeviceCommandRequest
from esperclient.rest import ApiException


class TestDeviceCommandRequest(unittest.TestCase):
    """DeviceCommandRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeviceCommandRequest(self):
        """Test DeviceCommandRequest"""
        model = esperclient.models.device_command_request.DeviceCommandRequest()
        pass


if __name__ == '__main__':
    unittest.main()
