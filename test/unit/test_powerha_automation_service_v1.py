# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for PowerhaAutomationServiceV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_dra_python_sdk.powerha_automation_service_v1 import *

_service = PowerhaAutomationServiceV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://power-dra.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: PowerhaAutomationConfig
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PowerhaAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PowerhaAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PowerhaAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateApiKey:
    """
    Test Class for create_api_key
    """

    @responses.activate
    def test_create_api_key_all_params(self):
        """
        create_api_key()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/api_key/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"status": "Success", "id": "9676767890"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        api_key = 'adfadfdsafsdfdsf'
        accept_language = 'en-US'

        # Invoke method
        response = _service.create_api_key(
            pha_instance_id,
            api_key=api_key,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['api_key'] == 'adfadfdsafsdfdsf'

    def test_create_api_key_all_params_with_retries(self):
        # Enable retries and run test_create_api_key_all_params.
        _service.enable_retries()
        self.test_create_api_key_all_params()

        # Disable retries and run test_create_api_key_all_params.
        _service.disable_retries()
        self.test_create_api_key_all_params()

    @responses.activate
    def test_create_api_key_required_params(self):
        """
        test_create_api_key_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/api_key/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"status": "Success", "id": "9676767890"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        api_key = 'adfadfdsafsdfdsf'

        # Invoke method
        response = _service.create_api_key(
            pha_instance_id,
            api_key=api_key,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['api_key'] == 'adfadfdsafsdfdsf'

    def test_create_api_key_required_params_with_retries(self):
        # Enable retries and run test_create_api_key_required_params.
        _service.enable_retries()
        self.test_create_api_key_required_params()

        # Disable retries and run test_create_api_key_required_params.
        _service.disable_retries()
        self.test_create_api_key_required_params()

    @responses.activate
    def test_create_api_key_value_error(self):
        """
        test_create_api_key_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/api_key/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"status": "Success", "id": "9676767890"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        api_key = 'adfadfdsafsdfdsf'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_api_key(**req_copy)

    def test_create_api_key_value_error_with_retries(self):
        # Enable retries and run test_create_api_key_value_error.
        _service.enable_retries()
        self.test_create_api_key_value_error()

        # Disable retries and run test_create_api_key_value_error.
        _service.disable_retries()
        self.test_create_api_key_value_error()


class TestGetClusterNode:
    """
    Test Class for get_cluster_node
    """

    @responses.activate
    def test_get_cluster_node_all_params(self):
        """
        get_cluster_node()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.get_cluster_node(
            pha_instance_id,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_cluster_node_all_params_with_retries(self):
        # Enable retries and run test_get_cluster_node_all_params.
        _service.enable_retries()
        self.test_get_cluster_node_all_params()

        # Disable retries and run test_get_cluster_node_all_params.
        _service.disable_retries()
        self.test_get_cluster_node_all_params()

    @responses.activate
    def test_get_cluster_node_required_params(self):
        """
        test_get_cluster_node_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Invoke method
        response = _service.get_cluster_node(
            pha_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_cluster_node_required_params_with_retries(self):
        # Enable retries and run test_get_cluster_node_required_params.
        _service.enable_retries()
        self.test_get_cluster_node_required_params()

        # Disable retries and run test_get_cluster_node_required_params.
        _service.disable_retries()
        self.test_get_cluster_node_required_params()

    @responses.activate
    def test_get_cluster_node_value_error(self):
        """
        test_get_cluster_node_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_cluster_node(**req_copy)

    def test_get_cluster_node_value_error_with_retries(self):
        # Enable retries and run test_get_cluster_node_value_error.
        _service.enable_retries()
        self.test_get_cluster_node_value_error()

        # Disable retries and run test_get_cluster_node_value_error.
        _service.disable_retries()
        self.test_get_cluster_node_value_error()


class TestCreateClusterNode:
    """
    Test Class for create_cluster_node
    """

    @responses.activate
    def test_create_cluster_node_all_params(self):
        """
        create_cluster_node()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        primary_cluster_nodes = ['ede4c36e-002c-48da-992e-6039d230c478']
        secondary_cluster_nodes = ['ede4c36e-1234-48da-992e-6039d230c478']
        accept_language = 'en-US'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.create_cluster_node(
            pha_instance_id,
            primary_cluster_nodes,
            secondary_cluster_nodes=secondary_cluster_nodes,
            accept_language=accept_language,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['primary_cluster_nodes'] == ['ede4c36e-002c-48da-992e-6039d230c478']
        assert req_body['secondary_cluster_nodes'] == ['ede4c36e-1234-48da-992e-6039d230c478']

    def test_create_cluster_node_all_params_with_retries(self):
        # Enable retries and run test_create_cluster_node_all_params.
        _service.enable_retries()
        self.test_create_cluster_node_all_params()

        # Disable retries and run test_create_cluster_node_all_params.
        _service.disable_retries()
        self.test_create_cluster_node_all_params()

    @responses.activate
    def test_create_cluster_node_required_params(self):
        """
        test_create_cluster_node_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        primary_cluster_nodes = ['ede4c36e-002c-48da-992e-6039d230c478']
        secondary_cluster_nodes = ['ede4c36e-1234-48da-992e-6039d230c478']

        # Invoke method
        response = _service.create_cluster_node(
            pha_instance_id,
            primary_cluster_nodes,
            secondary_cluster_nodes=secondary_cluster_nodes,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['primary_cluster_nodes'] == ['ede4c36e-002c-48da-992e-6039d230c478']
        assert req_body['secondary_cluster_nodes'] == ['ede4c36e-1234-48da-992e-6039d230c478']

    def test_create_cluster_node_required_params_with_retries(self):
        # Enable retries and run test_create_cluster_node_required_params.
        _service.enable_retries()
        self.test_create_cluster_node_required_params()

        # Disable retries and run test_create_cluster_node_required_params.
        _service.disable_retries()
        self.test_create_cluster_node_required_params()

    @responses.activate
    def test_create_cluster_node_value_error(self):
        """
        test_create_cluster_node_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        primary_cluster_nodes = ['ede4c36e-002c-48da-992e-6039d230c478']
        secondary_cluster_nodes = ['ede4c36e-1234-48da-992e-6039d230c478']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
            "primary_cluster_nodes": primary_cluster_nodes,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_cluster_node(**req_copy)

    def test_create_cluster_node_value_error_with_retries(self):
        # Enable retries and run test_create_cluster_node_value_error.
        _service.enable_retries()
        self.test_create_cluster_node_value_error()

        # Disable retries and run test_create_cluster_node_value_error.
        _service.disable_retries()
        self.test_create_cluster_node_value_error()


class TestDeleteClusterNode:
    """
    Test Class for delete_cluster_node
    """

    @responses.activate
    def test_delete_cluster_node_all_params(self):
        """
        delete_cluster_node()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        vm_id = 'r006-2f3b3ab9-2149-49cc-83a1-30a5d93d59b2'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.delete_cluster_node(
            pha_instance_id,
            vm_id,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'vm_id={}'.format(vm_id) in query_string

    def test_delete_cluster_node_all_params_with_retries(self):
        # Enable retries and run test_delete_cluster_node_all_params.
        _service.enable_retries()
        self.test_delete_cluster_node_all_params()

        # Disable retries and run test_delete_cluster_node_all_params.
        _service.disable_retries()
        self.test_delete_cluster_node_all_params()

    @responses.activate
    def test_delete_cluster_node_required_params(self):
        """
        test_delete_cluster_node_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        vm_id = 'r006-2f3b3ab9-2149-49cc-83a1-30a5d93d59b2'

        # Invoke method
        response = _service.delete_cluster_node(
            pha_instance_id,
            vm_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'vm_id={}'.format(vm_id) in query_string

    def test_delete_cluster_node_required_params_with_retries(self):
        # Enable retries and run test_delete_cluster_node_required_params.
        _service.enable_retries()
        self.test_delete_cluster_node_required_params()

        # Disable retries and run test_delete_cluster_node_required_params.
        _service.disable_retries()
        self.test_delete_cluster_node_required_params()

    @responses.activate
    def test_delete_cluster_node_value_error(self):
        """
        test_delete_cluster_node_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/cluster_nodes/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"id": "cluster-response-01", "primary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}], "secondary_node_details": [{"agent_status": "running", "cores": 8.0, "ip_addresses": ["ip_addresses"], "memory": 64.0, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-9b7c2d11", "vm_name": "pha-node-primary-1", "vm_status": "ACTIVE", "workspace_id": "workspace-primary-001"}]}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        vm_id = 'r006-2f3b3ab9-2149-49cc-83a1-30a5d93d59b2'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
            "vm_id": vm_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_cluster_node(**req_copy)

    def test_delete_cluster_node_value_error_with_retries(self):
        # Enable retries and run test_delete_cluster_node_value_error.
        _service.enable_retries()
        self.test_delete_cluster_node_value_error()

        # Disable retries and run test_delete_cluster_node_value_error.
        _service.disable_retries()
        self.test_delete_cluster_node_value_error()


class TestGetPowervsWorkspace:
    """
    Test Class for get_powervs_workspace
    """

    @responses.activate
    def test_get_powervs_workspace_all_params(self):
        """
        get_powervs_workspace()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/powervs_workspaces/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"workspaces": [{"id": "ws-001", "name": "primary-workspace"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        location_id = 'us-south'
        accept_language = 'en-US'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.get_powervs_workspace(
            pha_instance_id,
            location_id,
            accept_language=accept_language,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'location_id={}'.format(location_id) in query_string

    def test_get_powervs_workspace_all_params_with_retries(self):
        # Enable retries and run test_get_powervs_workspace_all_params.
        _service.enable_retries()
        self.test_get_powervs_workspace_all_params()

        # Disable retries and run test_get_powervs_workspace_all_params.
        _service.disable_retries()
        self.test_get_powervs_workspace_all_params()

    @responses.activate
    def test_get_powervs_workspace_required_params(self):
        """
        test_get_powervs_workspace_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/powervs_workspaces/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"workspaces": [{"id": "ws-001", "name": "primary-workspace"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        location_id = 'us-south'

        # Invoke method
        response = _service.get_powervs_workspace(
            pha_instance_id,
            location_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'location_id={}'.format(location_id) in query_string

    def test_get_powervs_workspace_required_params_with_retries(self):
        # Enable retries and run test_get_powervs_workspace_required_params.
        _service.enable_retries()
        self.test_get_powervs_workspace_required_params()

        # Disable retries and run test_get_powervs_workspace_required_params.
        _service.disable_retries()
        self.test_get_powervs_workspace_required_params()

    @responses.activate
    def test_get_powervs_workspace_value_error(self):
        """
        test_get_powervs_workspace_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/powervs_workspaces/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"workspaces": [{"id": "ws-001", "name": "primary-workspace"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        location_id = 'us-south'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
            "location_id": location_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_powervs_workspace(**req_copy)

    def test_get_powervs_workspace_value_error_with_retries(self):
        # Enable retries and run test_get_powervs_workspace_value_error.
        _service.enable_retries()
        self.test_get_powervs_workspace_value_error()

        # Disable retries and run test_get_powervs_workspace_value_error.
        _service.disable_retries()
        self.test_get_powervs_workspace_value_error()


# endregion
##############################################################################
# End of Service: PowerhaAutomationConfig
##############################################################################

##############################################################################
# Start of Service: PowerhaAutomationServiceInstance
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PowerhaAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PowerhaAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PowerhaAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetPhaLastOperation:
    """
    Test Class for get_pha_last_operation
    """

    @responses.activate
    def test_get_pha_last_operation_all_params(self):
        """
        get_pha_last_operation()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/last_operation/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"deployment_name": "pha-deployment-prod-01", "provision_id": "8eefautr-4c02-0009-0086-8bd4d8cf61b6", "resource_group": "resource_group", "status": "ACTIVE"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        accept_language = 'en-US'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.get_pha_last_operation(
            pha_instance_id,
            accept_language=accept_language,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pha_last_operation_all_params_with_retries(self):
        # Enable retries and run test_get_pha_last_operation_all_params.
        _service.enable_retries()
        self.test_get_pha_last_operation_all_params()

        # Disable retries and run test_get_pha_last_operation_all_params.
        _service.disable_retries()
        self.test_get_pha_last_operation_all_params()

    @responses.activate
    def test_get_pha_last_operation_required_params(self):
        """
        test_get_pha_last_operation_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/last_operation/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"deployment_name": "pha-deployment-prod-01", "provision_id": "8eefautr-4c02-0009-0086-8bd4d8cf61b6", "resource_group": "resource_group", "status": "ACTIVE"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Invoke method
        response = _service.get_pha_last_operation(
            pha_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pha_last_operation_required_params_with_retries(self):
        # Enable retries and run test_get_pha_last_operation_required_params.
        _service.enable_retries()
        self.test_get_pha_last_operation_required_params()

        # Disable retries and run test_get_pha_last_operation_required_params.
        _service.disable_retries()
        self.test_get_pha_last_operation_required_params()

    @responses.activate
    def test_get_pha_last_operation_value_error(self):
        """
        test_get_pha_last_operation_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/last_operation/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"deployment_name": "pha-deployment-prod-01", "provision_id": "8eefautr-4c02-0009-0086-8bd4d8cf61b6", "resource_group": "resource_group", "status": "ACTIVE"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_pha_last_operation(**req_copy)

    def test_get_pha_last_operation_value_error_with_retries(self):
        # Enable retries and run test_get_pha_last_operation_value_error.
        _service.enable_retries()
        self.test_get_pha_last_operation_value_error()

        # Disable retries and run test_get_pha_last_operation_value_error.
        _service.disable_retries()
        self.test_get_pha_last_operation_value_error()


class TestGetPhaDeployment:
    """
    Test Class for get_pha_deployment
    """

    @responses.activate
    def test_get_pha_deployment_all_params(self):
        """
        get_pha_deployment()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_deployment/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"cloud_account_id": "adfadfdsafsdfdsf", "connectivity_type": "private", "creation_time": "2026-01-10T08:15:30Z", "custom_network": ["custom_network"], "deprovision_time": "2026-01-20T12:45:00Z", "guid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "is_duplicate": false, "plan_id": "powerha-standard", "plan_name": "PowerHA Standard", "powerha_cluster_name": "pha-cluster-prod", "powerha_cluster_type": "standard", "powerha_level": "7.2.1", "primary_cluster_nodes_details": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "primary_location": "us-south", "primary_region_name": "Dallas", "primary_workspace": "ws-primary-001", "primary_workspace_name": "primary-ws-01", "provision_end_time": "2026-01-10T08:30:00Z", "id": "prov-9f8a7b6c", "provision_start_time": "2026-01-10T08:16:00Z", "provision_status": "SUCCEEDED", "region_id": "us-south", "resource_group": "rg-pha-prod", "resource_group_crn": "crn:v1:bluemix:public:resource-group:us-south:a/123456::rg:abcd1234", "resource_instance": "resource-instance-01", "secondary_cluster_nodes": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "secondary_location": "us-east", "secondary_workspace": "ws-secondary-001", "service_description": "PowerHA disaster recovery deployment", "service_id": "powerha", "service_name": "IBM PowerHA", "standby_region_name": "Washington", "standby_workspace_name": "standby-ws-01", "user_tags": "env:prod,team:dr"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.get_pha_deployment(
            pha_instance_id,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pha_deployment_all_params_with_retries(self):
        # Enable retries and run test_get_pha_deployment_all_params.
        _service.enable_retries()
        self.test_get_pha_deployment_all_params()

        # Disable retries and run test_get_pha_deployment_all_params.
        _service.disable_retries()
        self.test_get_pha_deployment_all_params()

    @responses.activate
    def test_get_pha_deployment_required_params(self):
        """
        test_get_pha_deployment_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_deployment/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"cloud_account_id": "adfadfdsafsdfdsf", "connectivity_type": "private", "creation_time": "2026-01-10T08:15:30Z", "custom_network": ["custom_network"], "deprovision_time": "2026-01-20T12:45:00Z", "guid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "is_duplicate": false, "plan_id": "powerha-standard", "plan_name": "PowerHA Standard", "powerha_cluster_name": "pha-cluster-prod", "powerha_cluster_type": "standard", "powerha_level": "7.2.1", "primary_cluster_nodes_details": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "primary_location": "us-south", "primary_region_name": "Dallas", "primary_workspace": "ws-primary-001", "primary_workspace_name": "primary-ws-01", "provision_end_time": "2026-01-10T08:30:00Z", "id": "prov-9f8a7b6c", "provision_start_time": "2026-01-10T08:16:00Z", "provision_status": "SUCCEEDED", "region_id": "us-south", "resource_group": "rg-pha-prod", "resource_group_crn": "crn:v1:bluemix:public:resource-group:us-south:a/123456::rg:abcd1234", "resource_instance": "resource-instance-01", "secondary_cluster_nodes": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "secondary_location": "us-east", "secondary_workspace": "ws-secondary-001", "service_description": "PowerHA disaster recovery deployment", "service_id": "powerha", "service_name": "IBM PowerHA", "standby_region_name": "Washington", "standby_workspace_name": "standby-ws-01", "user_tags": "env:prod,team:dr"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Invoke method
        response = _service.get_pha_deployment(
            pha_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pha_deployment_required_params_with_retries(self):
        # Enable retries and run test_get_pha_deployment_required_params.
        _service.enable_retries()
        self.test_get_pha_deployment_required_params()

        # Disable retries and run test_get_pha_deployment_required_params.
        _service.disable_retries()
        self.test_get_pha_deployment_required_params()

    @responses.activate
    def test_get_pha_deployment_value_error(self):
        """
        test_get_pha_deployment_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_deployment/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"cloud_account_id": "adfadfdsafsdfdsf", "connectivity_type": "private", "creation_time": "2026-01-10T08:15:30Z", "custom_network": ["custom_network"], "deprovision_time": "2026-01-20T12:45:00Z", "guid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "is_duplicate": false, "plan_id": "powerha-standard", "plan_name": "PowerHA Standard", "powerha_cluster_name": "pha-cluster-prod", "powerha_cluster_type": "standard", "powerha_level": "7.2.1", "primary_cluster_nodes_details": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "primary_location": "us-south", "primary_region_name": "Dallas", "primary_workspace": "ws-primary-001", "primary_workspace_name": "primary-ws-01", "provision_end_time": "2026-01-10T08:30:00Z", "id": "prov-9f8a7b6c", "provision_start_time": "2026-01-10T08:16:00Z", "provision_status": "SUCCEEDED", "region_id": "us-south", "resource_group": "rg-pha-prod", "resource_group_crn": "crn:v1:bluemix:public:resource-group:us-south:a/123456::rg:abcd1234", "resource_instance": "resource-instance-01", "secondary_cluster_nodes": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "secondary_location": "us-east", "secondary_workspace": "ws-secondary-001", "service_description": "PowerHA disaster recovery deployment", "service_id": "powerha", "service_name": "IBM PowerHA", "standby_region_name": "Washington", "standby_workspace_name": "standby-ws-01", "user_tags": "env:prod,team:dr"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_pha_deployment(**req_copy)

    def test_get_pha_deployment_value_error_with_retries(self):
        # Enable retries and run test_get_pha_deployment_value_error.
        _service.enable_retries()
        self.test_get_pha_deployment_value_error()

        # Disable retries and run test_get_pha_deployment_value_error.
        _service.disable_retries()
        self.test_get_pha_deployment_value_error()


class TestCreatePhaDeployment:
    """
    Test Class for create_pha_deployment
    """

    @responses.activate
    def test_create_pha_deployment_all_params(self):
        """
        create_pha_deployment()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_deployment/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"cloud_account_id": "adfadfdsafsdfdsf", "connectivity_type": "private", "creation_time": "2026-01-10T08:15:30Z", "custom_network": ["custom_network"], "deprovision_time": "2026-01-20T12:45:00Z", "guid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "is_duplicate": false, "plan_id": "powerha-standard", "plan_name": "PowerHA Standard", "powerha_cluster_name": "pha-cluster-prod", "powerha_cluster_type": "standard", "powerha_level": "7.2.1", "primary_cluster_nodes_details": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "primary_location": "us-south", "primary_region_name": "Dallas", "primary_workspace": "ws-primary-001", "primary_workspace_name": "primary-ws-01", "provision_end_time": "2026-01-10T08:30:00Z", "id": "prov-9f8a7b6c", "provision_start_time": "2026-01-10T08:16:00Z", "provision_status": "SUCCEEDED", "region_id": "us-south", "resource_group": "rg-pha-prod", "resource_group_crn": "crn:v1:bluemix:public:resource-group:us-south:a/123456::rg:abcd1234", "resource_instance": "resource-instance-01", "secondary_cluster_nodes": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "secondary_location": "us-east", "secondary_workspace": "ws-secondary-001", "service_description": "PowerHA disaster recovery deployment", "service_id": "powerha", "service_name": "IBM PowerHA", "standby_region_name": "Washington", "standby_workspace_name": "standby-ws-01", "user_tags": "env:prod,team:dr"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        location_id = 'loc-us-south-01'
        primary_workspace = 'workspace-primary'
        api_key = '123635364646fghrtfhbfdhb'
        cluster_type = 'standard'
        configure_type = 'automatic'
        primary_cluster_nodes = ['ede4c36e-002c-48da-992e-6039d230c478']
        standby_cluster_nodes = ['843a8e1f-05bb-4164-8c73-de39e016c2b4']
        primary_location = 'us-south'
        secondary_location = 'us-east'
        secondary_workspace = 'workspace-secondary'
        accept_language = 'en-US'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.create_pha_deployment(
            pha_instance_id,
            location_id,
            primary_workspace,
            api_key=api_key,
            cluster_type=cluster_type,
            configure_type=configure_type,
            primary_cluster_nodes=primary_cluster_nodes,
            standby_cluster_nodes=standby_cluster_nodes,
            primary_location=primary_location,
            secondary_location=secondary_location,
            secondary_workspace=secondary_workspace,
            accept_language=accept_language,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['location_id'] == 'loc-us-south-01'
        assert req_body['primary_workspace'] == 'workspace-primary'
        assert req_body['api_key'] == '123635364646fghrtfhbfdhb'
        assert req_body['cluster_type'] == 'standard'
        assert req_body['configure_type'] == 'automatic'
        assert req_body['primary_cluster_nodes'] == ['ede4c36e-002c-48da-992e-6039d230c478']
        assert req_body['standby_cluster_nodes'] == ['843a8e1f-05bb-4164-8c73-de39e016c2b4']
        assert req_body['primary_location'] == 'us-south'
        assert req_body['secondary_location'] == 'us-east'
        assert req_body['secondary_workspace'] == 'workspace-secondary'

    def test_create_pha_deployment_all_params_with_retries(self):
        # Enable retries and run test_create_pha_deployment_all_params.
        _service.enable_retries()
        self.test_create_pha_deployment_all_params()

        # Disable retries and run test_create_pha_deployment_all_params.
        _service.disable_retries()
        self.test_create_pha_deployment_all_params()

    @responses.activate
    def test_create_pha_deployment_required_params(self):
        """
        test_create_pha_deployment_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_deployment/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"cloud_account_id": "adfadfdsafsdfdsf", "connectivity_type": "private", "creation_time": "2026-01-10T08:15:30Z", "custom_network": ["custom_network"], "deprovision_time": "2026-01-20T12:45:00Z", "guid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "is_duplicate": false, "plan_id": "powerha-standard", "plan_name": "PowerHA Standard", "powerha_cluster_name": "pha-cluster-prod", "powerha_cluster_type": "standard", "powerha_level": "7.2.1", "primary_cluster_nodes_details": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "primary_location": "us-south", "primary_region_name": "Dallas", "primary_workspace": "ws-primary-001", "primary_workspace_name": "primary-ws-01", "provision_end_time": "2026-01-10T08:30:00Z", "id": "prov-9f8a7b6c", "provision_start_time": "2026-01-10T08:16:00Z", "provision_status": "SUCCEEDED", "region_id": "us-south", "resource_group": "rg-pha-prod", "resource_group_crn": "crn:v1:bluemix:public:resource-group:us-south:a/123456::rg:abcd1234", "resource_instance": "resource-instance-01", "secondary_cluster_nodes": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "secondary_location": "us-east", "secondary_workspace": "ws-secondary-001", "service_description": "PowerHA disaster recovery deployment", "service_id": "powerha", "service_name": "IBM PowerHA", "standby_region_name": "Washington", "standby_workspace_name": "standby-ws-01", "user_tags": "env:prod,team:dr"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        location_id = 'loc-us-south-01'
        primary_workspace = 'workspace-primary'
        api_key = '123635364646fghrtfhbfdhb'
        cluster_type = 'standard'
        configure_type = 'automatic'
        primary_cluster_nodes = ['ede4c36e-002c-48da-992e-6039d230c478']
        standby_cluster_nodes = ['843a8e1f-05bb-4164-8c73-de39e016c2b4']
        primary_location = 'us-south'
        secondary_location = 'us-east'
        secondary_workspace = 'workspace-secondary'

        # Invoke method
        response = _service.create_pha_deployment(
            pha_instance_id,
            location_id,
            primary_workspace,
            api_key=api_key,
            cluster_type=cluster_type,
            configure_type=configure_type,
            primary_cluster_nodes=primary_cluster_nodes,
            standby_cluster_nodes=standby_cluster_nodes,
            primary_location=primary_location,
            secondary_location=secondary_location,
            secondary_workspace=secondary_workspace,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['location_id'] == 'loc-us-south-01'
        assert req_body['primary_workspace'] == 'workspace-primary'
        assert req_body['api_key'] == '123635364646fghrtfhbfdhb'
        assert req_body['cluster_type'] == 'standard'
        assert req_body['configure_type'] == 'automatic'
        assert req_body['primary_cluster_nodes'] == ['ede4c36e-002c-48da-992e-6039d230c478']
        assert req_body['standby_cluster_nodes'] == ['843a8e1f-05bb-4164-8c73-de39e016c2b4']
        assert req_body['primary_location'] == 'us-south'
        assert req_body['secondary_location'] == 'us-east'
        assert req_body['secondary_workspace'] == 'workspace-secondary'

    def test_create_pha_deployment_required_params_with_retries(self):
        # Enable retries and run test_create_pha_deployment_required_params.
        _service.enable_retries()
        self.test_create_pha_deployment_required_params()

        # Disable retries and run test_create_pha_deployment_required_params.
        _service.disable_retries()
        self.test_create_pha_deployment_required_params()

    @responses.activate
    def test_create_pha_deployment_value_error(self):
        """
        test_create_pha_deployment_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_deployment/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"cloud_account_id": "adfadfdsafsdfdsf", "connectivity_type": "private", "creation_time": "2026-01-10T08:15:30Z", "custom_network": ["custom_network"], "deprovision_time": "2026-01-20T12:45:00Z", "guid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "is_duplicate": false, "plan_id": "powerha-standard", "plan_name": "PowerHA Standard", "powerha_cluster_name": "pha-cluster-prod", "powerha_cluster_type": "standard", "powerha_level": "7.2.1", "primary_cluster_nodes_details": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "primary_location": "us-south", "primary_region_name": "Dallas", "primary_workspace": "ws-primary-001", "primary_workspace_name": "primary-ws-01", "provision_end_time": "2026-01-10T08:30:00Z", "id": "prov-9f8a7b6c", "provision_start_time": "2026-01-10T08:16:00Z", "provision_status": "SUCCEEDED", "region_id": "us-south", "resource_group": "rg-pha-prod", "resource_group_crn": "crn:v1:bluemix:public:resource-group:us-south:a/123456::rg:abcd1234", "resource_instance": "resource-instance-01", "secondary_cluster_nodes": [{"agent_status": "RUNNING", "cores": 8.0, "ip_address": "10.0.2.45", "memory": 32, "pha_level": "7.2.1", "region": "us-south", "vm_id": "vm-3c91af27", "vm_name": "pha-node-01", "vm_status": "ACTIVE", "workspace_id": "workspace-pha-prod"}], "secondary_location": "us-east", "secondary_workspace": "ws-secondary-001", "service_description": "PowerHA disaster recovery deployment", "service_id": "powerha", "service_name": "IBM PowerHA", "standby_region_name": "Washington", "standby_workspace_name": "standby-ws-01", "user_tags": "env:prod,team:dr"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        location_id = 'loc-us-south-01'
        primary_workspace = 'workspace-primary'
        api_key = '123635364646fghrtfhbfdhb'
        cluster_type = 'standard'
        configure_type = 'automatic'
        primary_cluster_nodes = ['ede4c36e-002c-48da-992e-6039d230c478']
        standby_cluster_nodes = ['843a8e1f-05bb-4164-8c73-de39e016c2b4']
        primary_location = 'us-south'
        secondary_location = 'us-east'
        secondary_workspace = 'workspace-secondary'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
            "location_id": location_id,
            "primary_workspace": primary_workspace,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_pha_deployment(**req_copy)

    def test_create_pha_deployment_value_error_with_retries(self):
        # Enable retries and run test_create_pha_deployment_value_error.
        _service.enable_retries()
        self.test_create_pha_deployment_value_error()

        # Disable retries and run test_create_pha_deployment_value_error.
        _service.disable_retries()
        self.test_create_pha_deployment_value_error()


# endregion
##############################################################################
# End of Service: PowerhaAutomationServiceInstance
##############################################################################

##############################################################################
# Start of Service: PowerhaAutomationIbmCloud
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PowerhaAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PowerhaAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PowerhaAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetSupportedLocation:
    """
    Test Class for get_supported_location
    """

    @responses.activate
    def test_get_supported_location_all_params(self):
        """
        get_supported_location()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/supported_locations/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"locations": [{"id": "loc-us-south-01", "name": "Dallas (us-south)"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.get_supported_location(
            pha_instance_id,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_supported_location_all_params_with_retries(self):
        # Enable retries and run test_get_supported_location_all_params.
        _service.enable_retries()
        self.test_get_supported_location_all_params()

        # Disable retries and run test_get_supported_location_all_params.
        _service.disable_retries()
        self.test_get_supported_location_all_params()

    @responses.activate
    def test_get_supported_location_required_params(self):
        """
        test_get_supported_location_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/supported_locations/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"locations": [{"id": "loc-us-south-01", "name": "Dallas (us-south)"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Invoke method
        response = _service.get_supported_location(
            pha_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_supported_location_required_params_with_retries(self):
        # Enable retries and run test_get_supported_location_required_params.
        _service.enable_retries()
        self.test_get_supported_location_required_params()

        # Disable retries and run test_get_supported_location_required_params.
        _service.disable_retries()
        self.test_get_supported_location_required_params()

    @responses.activate
    def test_get_supported_location_value_error(self):
        """
        test_get_supported_location_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/supported_locations/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = '{"locations": [{"id": "loc-us-south-01", "name": "Dallas (us-south)"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_supported_location(**req_copy)

    def test_get_supported_location_value_error_with_retries(self):
        # Enable retries and run test_get_supported_location_value_error.
        _service.enable_retries()
        self.test_get_supported_location_value_error()

        # Disable retries and run test_get_supported_location_value_error.
        _service.disable_retries()
        self.test_get_supported_location_value_error()


# endregion
##############################################################################
# End of Service: PowerhaAutomationIbmCloud
##############################################################################

##############################################################################
# Start of Service: PowerhaAutomationAgent
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = PowerhaAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, PowerhaAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = PowerhaAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetPhaAgentFileDownloadJobStatus:
    """
    Test Class for get_pha_agent_file_download_job_status
    """

    @responses.activate
    def test_get_pha_agent_file_download_job_status_all_params(self):
        """
        get_pha_agent_file_download_job_status()
        """
        # Set up mock
        url = preprocess_url(
            '/powerha_automation/v1/pha_agent/download/8eefautr-4c02-0009-0086-8bd4d8cf61b6/jobs/4235r23r5vdfdf-2323'
        )
        mock_response = '{"bytes_downloaded": 52428800, "creation_at": "2026-01-08T11:00:00.000Z", "file_name": "power_agent", "job_id": "job-98765", "last_updated_at": "2026-01-08T12:15:00.000Z", "service_instance_id": "service-12345", "status": "running", "total_bytes": 104857600, "vm_id": "vm-12345"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        pha_job_id = '4235r23r5vdfdf-2323'
        accept_language = 'en-US'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.get_pha_agent_file_download_job_status(
            pha_instance_id,
            pha_job_id,
            accept_language=accept_language,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pha_agent_file_download_job_status_all_params_with_retries(self):
        # Enable retries and run test_get_pha_agent_file_download_job_status_all_params.
        _service.enable_retries()
        self.test_get_pha_agent_file_download_job_status_all_params()

        # Disable retries and run test_get_pha_agent_file_download_job_status_all_params.
        _service.disable_retries()
        self.test_get_pha_agent_file_download_job_status_all_params()

    @responses.activate
    def test_get_pha_agent_file_download_job_status_required_params(self):
        """
        test_get_pha_agent_file_download_job_status_required_params()
        """
        # Set up mock
        url = preprocess_url(
            '/powerha_automation/v1/pha_agent/download/8eefautr-4c02-0009-0086-8bd4d8cf61b6/jobs/4235r23r5vdfdf-2323'
        )
        mock_response = '{"bytes_downloaded": 52428800, "creation_at": "2026-01-08T11:00:00.000Z", "file_name": "power_agent", "job_id": "job-98765", "last_updated_at": "2026-01-08T12:15:00.000Z", "service_instance_id": "service-12345", "status": "running", "total_bytes": 104857600, "vm_id": "vm-12345"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        pha_job_id = '4235r23r5vdfdf-2323'

        # Invoke method
        response = _service.get_pha_agent_file_download_job_status(
            pha_instance_id,
            pha_job_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pha_agent_file_download_job_status_required_params_with_retries(self):
        # Enable retries and run test_get_pha_agent_file_download_job_status_required_params.
        _service.enable_retries()
        self.test_get_pha_agent_file_download_job_status_required_params()

        # Disable retries and run test_get_pha_agent_file_download_job_status_required_params.
        _service.disable_retries()
        self.test_get_pha_agent_file_download_job_status_required_params()

    @responses.activate
    def test_get_pha_agent_file_download_job_status_value_error(self):
        """
        test_get_pha_agent_file_download_job_status_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/powerha_automation/v1/pha_agent/download/8eefautr-4c02-0009-0086-8bd4d8cf61b6/jobs/4235r23r5vdfdf-2323'
        )
        mock_response = '{"bytes_downloaded": 52428800, "creation_at": "2026-01-08T11:00:00.000Z", "file_name": "power_agent", "job_id": "job-98765", "last_updated_at": "2026-01-08T12:15:00.000Z", "service_instance_id": "service-12345", "status": "running", "total_bytes": 104857600, "vm_id": "vm-12345"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        pha_job_id = '4235r23r5vdfdf-2323'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
            "pha_job_id": pha_job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_pha_agent_file_download_job_status(**req_copy)

    def test_get_pha_agent_file_download_job_status_value_error_with_retries(self):
        # Enable retries and run test_get_pha_agent_file_download_job_status_value_error.
        _service.enable_retries()
        self.test_get_pha_agent_file_download_job_status_value_error()

        # Disable retries and run test_get_pha_agent_file_download_job_status_value_error.
        _service.disable_retries()
        self.test_get_pha_agent_file_download_job_status_value_error()


class TestDownloadPhaAgentFile:
    """
    Test Class for download_pha_agent_file
    """

    @responses.activate
    def test_download_pha_agent_file_all_params(self):
        """
        download_pha_agent_file()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_agent/download/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/octet-stream',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        accept_language = 'en-US'
        if_none_match = 'abcdef'

        # Invoke method
        response = _service.download_pha_agent_file(
            pha_instance_id,
            accept_language=accept_language,
            if_none_match=if_none_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_download_pha_agent_file_all_params_with_retries(self):
        # Enable retries and run test_download_pha_agent_file_all_params.
        _service.enable_retries()
        self.test_download_pha_agent_file_all_params()

        # Disable retries and run test_download_pha_agent_file_all_params.
        _service.disable_retries()
        self.test_download_pha_agent_file_all_params()

    @responses.activate
    def test_download_pha_agent_file_required_params(self):
        """
        test_download_pha_agent_file_required_params()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_agent/download/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/octet-stream',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Invoke method
        response = _service.download_pha_agent_file(
            pha_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_download_pha_agent_file_required_params_with_retries(self):
        # Enable retries and run test_download_pha_agent_file_required_params.
        _service.enable_retries()
        self.test_download_pha_agent_file_required_params()

        # Disable retries and run test_download_pha_agent_file_required_params.
        _service.disable_retries()
        self.test_download_pha_agent_file_required_params()

    @responses.activate
    def test_download_pha_agent_file_value_error(self):
        """
        test_download_pha_agent_file_value_error()
        """
        # Set up mock
        url = preprocess_url('/powerha_automation/v1/pha_agent/download/8eefautr-4c02-0009-0086-8bd4d8cf61b6')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/octet-stream',
            status=200,
        )

        # Set up parameter values
        pha_instance_id = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pha_instance_id": pha_instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.download_pha_agent_file(**req_copy)

    def test_download_pha_agent_file_value_error_with_retries(self):
        # Enable retries and run test_download_pha_agent_file_value_error.
        _service.enable_retries()
        self.test_download_pha_agent_file_value_error()

        # Disable retries and run test_download_pha_agent_file_value_error.
        _service.disable_retries()
        self.test_download_pha_agent_file_value_error()


# endregion
##############################################################################
# End of Service: PowerhaAutomationAgent
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_ApiKeyResponse:
    """
    Test Class for ApiKeyResponse
    """

    def test_api_key_response_serialization(self):
        """
        Test serialization/deserialization for ApiKeyResponse
        """

        # Construct a json representation of a ApiKeyResponse model
        api_key_response_model_json = {}
        api_key_response_model_json['status'] = 'Success'
        api_key_response_model_json['id'] = '9676767890'

        # Construct a model instance of ApiKeyResponse by calling from_dict on the json representation
        api_key_response_model = ApiKeyResponse.from_dict(api_key_response_model_json)
        assert api_key_response_model != False

        # Construct a model instance of ApiKeyResponse by calling from_dict on the json representation
        api_key_response_model_dict = ApiKeyResponse.from_dict(api_key_response_model_json).__dict__
        api_key_response_model2 = ApiKeyResponse(**api_key_response_model_dict)

        # Verify the model instances are equivalent
        assert api_key_response_model == api_key_response_model2

        # Convert model instance back to dict and verify no loss of data
        api_key_response_model_json2 = api_key_response_model.to_dict()
        assert api_key_response_model_json2 == api_key_response_model_json


class TestModel_ClusterNodeInfo:
    """
    Test Class for ClusterNodeInfo
    """

    def test_cluster_node_info_serialization(self):
        """
        Test serialization/deserialization for ClusterNodeInfo
        """

        # Construct a json representation of a ClusterNodeInfo model
        cluster_node_info_model_json = {}
        cluster_node_info_model_json['agent_status'] = 'RUNNING'
        cluster_node_info_model_json['cores'] = 8.0
        cluster_node_info_model_json['ip_address'] = '10.0.2.45'
        cluster_node_info_model_json['memory'] = 32
        cluster_node_info_model_json['pha_level'] = '7.2.1'
        cluster_node_info_model_json['region'] = 'us-south'
        cluster_node_info_model_json['vm_id'] = 'vm-3c91af27'
        cluster_node_info_model_json['vm_name'] = 'pha-node-01'
        cluster_node_info_model_json['vm_status'] = 'ACTIVE'
        cluster_node_info_model_json['workspace_id'] = 'workspace-pha-prod'

        # Construct a model instance of ClusterNodeInfo by calling from_dict on the json representation
        cluster_node_info_model = ClusterNodeInfo.from_dict(cluster_node_info_model_json)
        assert cluster_node_info_model != False

        # Construct a model instance of ClusterNodeInfo by calling from_dict on the json representation
        cluster_node_info_model_dict = ClusterNodeInfo.from_dict(cluster_node_info_model_json).__dict__
        cluster_node_info_model2 = ClusterNodeInfo(**cluster_node_info_model_dict)

        # Verify the model instances are equivalent
        assert cluster_node_info_model == cluster_node_info_model2

        # Convert model instance back to dict and verify no loss of data
        cluster_node_info_model_json2 = cluster_node_info_model.to_dict()
        assert cluster_node_info_model_json2 == cluster_node_info_model_json


class TestModel_ClusterNodeResponse:
    """
    Test Class for ClusterNodeResponse
    """

    def test_cluster_node_response_serialization(self):
        """
        Test serialization/deserialization for ClusterNodeResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        node_detail_model = {}  # NodeDetail
        node_detail_model['agent_status'] = 'running'
        node_detail_model['cores'] = 8.0
        node_detail_model['ip_addresses'] = ['192.168.1.10', '10.0.0.10']
        node_detail_model['memory'] = 64.0
        node_detail_model['pha_level'] = '7.2.1'
        node_detail_model['region'] = 'us-south'
        node_detail_model['vm_id'] = 'vm-primary-01'
        node_detail_model['vm_name'] = 'pha-primary-node-1'
        node_detail_model['vm_status'] = 'ACTIVE'
        node_detail_model['workspace_id'] = 'workspace-primary-001'

        # Construct a json representation of a ClusterNodeResponse model
        cluster_node_response_model_json = {}
        cluster_node_response_model_json['id'] = 'cluster-response-01'
        cluster_node_response_model_json['primary_node_details'] = [node_detail_model]
        cluster_node_response_model_json['secondary_node_details'] = [node_detail_model]

        # Construct a model instance of ClusterNodeResponse by calling from_dict on the json representation
        cluster_node_response_model = ClusterNodeResponse.from_dict(cluster_node_response_model_json)
        assert cluster_node_response_model != False

        # Construct a model instance of ClusterNodeResponse by calling from_dict on the json representation
        cluster_node_response_model_dict = ClusterNodeResponse.from_dict(cluster_node_response_model_json).__dict__
        cluster_node_response_model2 = ClusterNodeResponse(**cluster_node_response_model_dict)

        # Verify the model instances are equivalent
        assert cluster_node_response_model == cluster_node_response_model2

        # Convert model instance back to dict and verify no loss of data
        cluster_node_response_model_json2 = cluster_node_response_model.to_dict()
        assert cluster_node_response_model_json2 == cluster_node_response_model_json


class TestModel_NodeDetail:
    """
    Test Class for NodeDetail
    """

    def test_node_detail_serialization(self):
        """
        Test serialization/deserialization for NodeDetail
        """

        # Construct a json representation of a NodeDetail model
        node_detail_model_json = {}
        node_detail_model_json['agent_status'] = 'running'
        node_detail_model_json['cores'] = 8.0
        node_detail_model_json['ip_addresses'] = ['10.0.0.21', '10.0.0.22']
        node_detail_model_json['memory'] = 64.0
        node_detail_model_json['pha_level'] = '7.2.1'
        node_detail_model_json['region'] = 'us-south'
        node_detail_model_json['vm_id'] = 'vm-9b7c2d11'
        node_detail_model_json['vm_name'] = 'pha-node-primary-1'
        node_detail_model_json['vm_status'] = 'ACTIVE'
        node_detail_model_json['workspace_id'] = 'workspace-primary-001'

        # Construct a model instance of NodeDetail by calling from_dict on the json representation
        node_detail_model = NodeDetail.from_dict(node_detail_model_json)
        assert node_detail_model != False

        # Construct a model instance of NodeDetail by calling from_dict on the json representation
        node_detail_model_dict = NodeDetail.from_dict(node_detail_model_json).__dict__
        node_detail_model2 = NodeDetail(**node_detail_model_dict)

        # Verify the model instances are equivalent
        assert node_detail_model == node_detail_model2

        # Convert model instance back to dict and verify no loss of data
        node_detail_model_json2 = node_detail_model.to_dict()
        assert node_detail_model_json2 == node_detail_model_json


class TestModel_PhaAgentJobStatusResponse:
    """
    Test Class for PhaAgentJobStatusResponse
    """

    def test_pha_agent_job_status_response_serialization(self):
        """
        Test serialization/deserialization for PhaAgentJobStatusResponse
        """

        # Construct a json representation of a PhaAgentJobStatusResponse model
        pha_agent_job_status_response_model_json = {}
        pha_agent_job_status_response_model_json['bytes_downloaded'] = 52428800
        pha_agent_job_status_response_model_json['creation_at'] = '2026-01-08T11:00:00Z'
        pha_agent_job_status_response_model_json['file_name'] = 'power_agent'
        pha_agent_job_status_response_model_json['job_id'] = 'job-98765'
        pha_agent_job_status_response_model_json['last_updated_at'] = '2026-01-08T12:15:00Z'
        pha_agent_job_status_response_model_json['service_instance_id'] = 'service-12345'
        pha_agent_job_status_response_model_json['status'] = 'running'
        pha_agent_job_status_response_model_json['total_bytes'] = 104857600
        pha_agent_job_status_response_model_json['vm_id'] = 'vm-12345'

        # Construct a model instance of PhaAgentJobStatusResponse by calling from_dict on the json representation
        pha_agent_job_status_response_model = PhaAgentJobStatusResponse.from_dict(
            pha_agent_job_status_response_model_json
        )
        assert pha_agent_job_status_response_model != False

        # Construct a model instance of PhaAgentJobStatusResponse by calling from_dict on the json representation
        pha_agent_job_status_response_model_dict = PhaAgentJobStatusResponse.from_dict(
            pha_agent_job_status_response_model_json
        ).__dict__
        pha_agent_job_status_response_model2 = PhaAgentJobStatusResponse(**pha_agent_job_status_response_model_dict)

        # Verify the model instances are equivalent
        assert pha_agent_job_status_response_model == pha_agent_job_status_response_model2

        # Convert model instance back to dict and verify no loss of data
        pha_agent_job_status_response_model_json2 = pha_agent_job_status_response_model.to_dict()
        assert pha_agent_job_status_response_model_json2 == pha_agent_job_status_response_model_json


class TestModel_PhaDeploymentResponse:
    """
    Test Class for PhaDeploymentResponse
    """

    def test_pha_deployment_response_serialization(self):
        """
        Test serialization/deserialization for PhaDeploymentResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cluster_node_info_model = {}  # ClusterNodeInfo
        cluster_node_info_model['agent_status'] = 'RUNNING'
        cluster_node_info_model['cores'] = 8.0
        cluster_node_info_model['ip_address'] = '10.0.2.45'
        cluster_node_info_model['memory'] = 16
        cluster_node_info_model['pha_level'] = '7.2.1'
        cluster_node_info_model['region'] = 'us-south'
        cluster_node_info_model['vm_id'] = 'vm-primary-01'
        cluster_node_info_model['vm_name'] = 'pha-primary-01'
        cluster_node_info_model['vm_status'] = 'ACTIVE'
        cluster_node_info_model['workspace_id'] = 'workspace-primary'

        # Construct a json representation of a PhaDeploymentResponse model
        pha_deployment_response_model_json = {}
        pha_deployment_response_model_json['cloud_account_id'] = 'adfadfdsafsdfdsf'
        pha_deployment_response_model_json['connectivity_type'] = 'private'
        pha_deployment_response_model_json['creation_time'] = '2026-01-10T08:15:30Z'
        pha_deployment_response_model_json['custom_network'] = ['10.0.0.0/24', '10.0.1.0/24']
        pha_deployment_response_model_json['deprovision_time'] = '2026-01-20T12:45:00Z'
        pha_deployment_response_model_json['guid'] = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
        pha_deployment_response_model_json['is_duplicate'] = False
        pha_deployment_response_model_json['plan_id'] = 'powerha-standard'
        pha_deployment_response_model_json['plan_name'] = 'PowerHA Standard'
        pha_deployment_response_model_json['powerha_cluster_name'] = 'pha-cluster-prod'
        pha_deployment_response_model_json['powerha_cluster_type'] = 'standard'
        pha_deployment_response_model_json['powerha_level'] = '7.2.1'
        pha_deployment_response_model_json['primary_cluster_nodes_details'] = [cluster_node_info_model]
        pha_deployment_response_model_json['primary_location'] = 'us-south'
        pha_deployment_response_model_json['primary_region_name'] = 'Dallas'
        pha_deployment_response_model_json['primary_workspace'] = 'ws-primary-001'
        pha_deployment_response_model_json['primary_workspace_name'] = 'primary-ws-01'
        pha_deployment_response_model_json['provision_end_time'] = '2026-01-10T08:30:00Z'
        pha_deployment_response_model_json['id'] = 'prov-9f8a7b6c'
        pha_deployment_response_model_json['provision_start_time'] = '2026-01-10T08:16:00Z'
        pha_deployment_response_model_json['provision_status'] = 'SUCCEEDED'
        pha_deployment_response_model_json['region_id'] = 'us-south'
        pha_deployment_response_model_json['resource_group'] = 'rg-pha-prod'
        pha_deployment_response_model_json['resource_group_crn'] = (
            'crn:v1:bluemix:public:resource-group:us-south:a/123456::rg:abcd1234'
        )
        pha_deployment_response_model_json['resource_instance'] = 'resource-instance-01'
        pha_deployment_response_model_json['secondary_cluster_nodes'] = [cluster_node_info_model]
        pha_deployment_response_model_json['secondary_location'] = 'us-east'
        pha_deployment_response_model_json['secondary_workspace'] = 'ws-secondary-001'
        pha_deployment_response_model_json['service_description'] = 'PowerHA disaster recovery deployment'
        pha_deployment_response_model_json['service_id'] = 'powerha'
        pha_deployment_response_model_json['service_name'] = 'IBM PowerHA'
        pha_deployment_response_model_json['standby_region_name'] = 'Washington'
        pha_deployment_response_model_json['standby_workspace_name'] = 'standby-ws-01'
        pha_deployment_response_model_json['user_tags'] = 'env:prod,team:dr'

        # Construct a model instance of PhaDeploymentResponse by calling from_dict on the json representation
        pha_deployment_response_model = PhaDeploymentResponse.from_dict(pha_deployment_response_model_json)
        assert pha_deployment_response_model != False

        # Construct a model instance of PhaDeploymentResponse by calling from_dict on the json representation
        pha_deployment_response_model_dict = PhaDeploymentResponse.from_dict(
            pha_deployment_response_model_json
        ).__dict__
        pha_deployment_response_model2 = PhaDeploymentResponse(**pha_deployment_response_model_dict)

        # Verify the model instances are equivalent
        assert pha_deployment_response_model == pha_deployment_response_model2

        # Convert model instance back to dict and verify no loss of data
        pha_deployment_response_model_json2 = pha_deployment_response_model.to_dict()
        assert pha_deployment_response_model_json2 == pha_deployment_response_model_json


class TestModel_PhaLocation:
    """
    Test Class for PhaLocation
    """

    def test_pha_location_serialization(self):
        """
        Test serialization/deserialization for PhaLocation
        """

        # Construct a json representation of a PhaLocation model
        pha_location_model_json = {}
        pha_location_model_json['id'] = 'loc-us-south-01'
        pha_location_model_json['name'] = 'Dallas (us-south)'

        # Construct a model instance of PhaLocation by calling from_dict on the json representation
        pha_location_model = PhaLocation.from_dict(pha_location_model_json)
        assert pha_location_model != False

        # Construct a model instance of PhaLocation by calling from_dict on the json representation
        pha_location_model_dict = PhaLocation.from_dict(pha_location_model_json).__dict__
        pha_location_model2 = PhaLocation(**pha_location_model_dict)

        # Verify the model instances are equivalent
        assert pha_location_model == pha_location_model2

        # Convert model instance back to dict and verify no loss of data
        pha_location_model_json2 = pha_location_model.to_dict()
        assert pha_location_model_json2 == pha_location_model_json


class TestModel_PhaSupportedLocationsResponse:
    """
    Test Class for PhaSupportedLocationsResponse
    """

    def test_pha_supported_locations_response_serialization(self):
        """
        Test serialization/deserialization for PhaSupportedLocationsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pha_location_model = {}  # PhaLocation
        pha_location_model['id'] = 'loc-us-south-01'
        pha_location_model['name'] = 'Dallas (us-south)'

        # Construct a json representation of a PhaSupportedLocationsResponse model
        pha_supported_locations_response_model_json = {}
        pha_supported_locations_response_model_json['locations'] = [pha_location_model]

        # Construct a model instance of PhaSupportedLocationsResponse by calling from_dict on the json representation
        pha_supported_locations_response_model = PhaSupportedLocationsResponse.from_dict(
            pha_supported_locations_response_model_json
        )
        assert pha_supported_locations_response_model != False

        # Construct a model instance of PhaSupportedLocationsResponse by calling from_dict on the json representation
        pha_supported_locations_response_model_dict = PhaSupportedLocationsResponse.from_dict(
            pha_supported_locations_response_model_json
        ).__dict__
        pha_supported_locations_response_model2 = PhaSupportedLocationsResponse(
            **pha_supported_locations_response_model_dict
        )

        # Verify the model instances are equivalent
        assert pha_supported_locations_response_model == pha_supported_locations_response_model2

        # Convert model instance back to dict and verify no loss of data
        pha_supported_locations_response_model_json2 = pha_supported_locations_response_model.to_dict()
        assert pha_supported_locations_response_model_json2 == pha_supported_locations_response_model_json


class TestModel_PhaWorkspaceSummary:
    """
    Test Class for PhaWorkspaceSummary
    """

    def test_pha_workspace_summary_serialization(self):
        """
        Test serialization/deserialization for PhaWorkspaceSummary
        """

        # Construct a json representation of a PhaWorkspaceSummary model
        pha_workspace_summary_model_json = {}
        pha_workspace_summary_model_json['id'] = 'ws-001'
        pha_workspace_summary_model_json['name'] = 'primary-workspace'

        # Construct a model instance of PhaWorkspaceSummary by calling from_dict on the json representation
        pha_workspace_summary_model = PhaWorkspaceSummary.from_dict(pha_workspace_summary_model_json)
        assert pha_workspace_summary_model != False

        # Construct a model instance of PhaWorkspaceSummary by calling from_dict on the json representation
        pha_workspace_summary_model_dict = PhaWorkspaceSummary.from_dict(pha_workspace_summary_model_json).__dict__
        pha_workspace_summary_model2 = PhaWorkspaceSummary(**pha_workspace_summary_model_dict)

        # Verify the model instances are equivalent
        assert pha_workspace_summary_model == pha_workspace_summary_model2

        # Convert model instance back to dict and verify no loss of data
        pha_workspace_summary_model_json2 = pha_workspace_summary_model.to_dict()
        assert pha_workspace_summary_model_json2 == pha_workspace_summary_model_json


class TestModel_PhaWorkspacesRegionResponse:
    """
    Test Class for PhaWorkspacesRegionResponse
    """

    def test_pha_workspaces_region_response_serialization(self):
        """
        Test serialization/deserialization for PhaWorkspacesRegionResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pha_workspace_summary_model = {}  # PhaWorkspaceSummary
        pha_workspace_summary_model['id'] = 'ws-001'
        pha_workspace_summary_model['name'] = 'primary-workspace'

        # Construct a json representation of a PhaWorkspacesRegionResponse model
        pha_workspaces_region_response_model_json = {}
        pha_workspaces_region_response_model_json['workspaces'] = [pha_workspace_summary_model]

        # Construct a model instance of PhaWorkspacesRegionResponse by calling from_dict on the json representation
        pha_workspaces_region_response_model = PhaWorkspacesRegionResponse.from_dict(
            pha_workspaces_region_response_model_json
        )
        assert pha_workspaces_region_response_model != False

        # Construct a model instance of PhaWorkspacesRegionResponse by calling from_dict on the json representation
        pha_workspaces_region_response_model_dict = PhaWorkspacesRegionResponse.from_dict(
            pha_workspaces_region_response_model_json
        ).__dict__
        pha_workspaces_region_response_model2 = PhaWorkspacesRegionResponse(**pha_workspaces_region_response_model_dict)

        # Verify the model instances are equivalent
        assert pha_workspaces_region_response_model == pha_workspaces_region_response_model2

        # Convert model instance back to dict and verify no loss of data
        pha_workspaces_region_response_model_json2 = pha_workspaces_region_response_model.to_dict()
        assert pha_workspaces_region_response_model_json2 == pha_workspaces_region_response_model_json


class TestModel_ServiceInstancePhaStatus:
    """
    Test Class for ServiceInstancePhaStatus
    """

    def test_service_instance_pha_status_serialization(self):
        """
        Test serialization/deserialization for ServiceInstancePhaStatus
        """

        # Construct a json representation of a ServiceInstancePhaStatus model
        service_instance_pha_status_model_json = {}
        service_instance_pha_status_model_json['deployment_name'] = 'pha-deployment-prod-01'
        service_instance_pha_status_model_json['provision_id'] = '8eefautr-4c02-0009-0086-8bd4d8cf61b6'
        service_instance_pha_status_model_json['resource_group'] = 'testString'
        service_instance_pha_status_model_json['status'] = 'ACTIVE'

        # Construct a model instance of ServiceInstancePhaStatus by calling from_dict on the json representation
        service_instance_pha_status_model = ServiceInstancePhaStatus.from_dict(service_instance_pha_status_model_json)
        assert service_instance_pha_status_model != False

        # Construct a model instance of ServiceInstancePhaStatus by calling from_dict on the json representation
        service_instance_pha_status_model_dict = ServiceInstancePhaStatus.from_dict(
            service_instance_pha_status_model_json
        ).__dict__
        service_instance_pha_status_model2 = ServiceInstancePhaStatus(**service_instance_pha_status_model_dict)

        # Verify the model instances are equivalent
        assert service_instance_pha_status_model == service_instance_pha_status_model2

        # Convert model instance back to dict and verify no loss of data
        service_instance_pha_status_model_json2 = service_instance_pha_status_model.to_dict()
        assert service_instance_pha_status_model_json2 == service_instance_pha_status_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
