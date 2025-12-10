# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2025.
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
Unit Tests for DrAutomationServiceV1
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
from ibm_dra_python_sdk.dr_automation_service_v1 import *


_service = DrAutomationServiceV1(authenticator=NoAuthAuthenticator())

_base_url = 'https://power-dra.test.cloud.ibm.com'
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
# Start of Service: DrAutomationConfig
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

        service = DrAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DrAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DrAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestUpdateApikey:
    """
    Test Class for update_apikey
    """

    @responses.activate
    def test_update_apikey_all_params(self):
        """
        update_apikey()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/apikey/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"description": "Key is valid.", "id": "crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::", "status": "Active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        api_key = 'adfadfdsafsdfdsf'
        accept_language = 'testString'

        # Invoke method
        response = _service.update_apikey(
            instance_id,
            api_key,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['api_key'] == 'adfadfdsafsdfdsf'

    def test_update_apikey_all_params_with_retries(self):
        # Enable retries and run test_update_apikey_all_params.
        _service.enable_retries()
        self.test_update_apikey_all_params()

        # Disable retries and run test_update_apikey_all_params.
        _service.disable_retries()
        self.test_update_apikey_all_params()

    @responses.activate
    def test_update_apikey_required_params(self):
        """
        test_update_apikey_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/apikey/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"description": "Key is valid.", "id": "crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::", "status": "Active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        api_key = 'adfadfdsafsdfdsf'

        # Invoke method
        response = _service.update_apikey(
            instance_id,
            api_key,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['api_key'] == 'adfadfdsafsdfdsf'

    def test_update_apikey_required_params_with_retries(self):
        # Enable retries and run test_update_apikey_required_params.
        _service.enable_retries()
        self.test_update_apikey_required_params()

        # Disable retries and run test_update_apikey_required_params.
        _service.disable_retries()
        self.test_update_apikey_required_params()

    @responses.activate
    def test_update_apikey_value_error(self):
        """
        test_update_apikey_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/apikey/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"description": "Key is valid.", "id": "crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::", "status": "Active"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        api_key = 'adfadfdsafsdfdsf'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "api_key": api_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_apikey(**req_copy)

    def test_update_apikey_value_error_with_retries(self):
        # Enable retries and run test_update_apikey_value_error.
        _service.enable_retries()
        self.test_update_apikey_value_error()

        # Disable retries and run test_update_apikey_value_error.
        _service.disable_retries()
        self.test_update_apikey_value_error()


class TestGetDrGrsLocationPair:
    """
    Test Class for get_dr_grs_location_pair
    """

    @responses.activate
    def test_get_dr_grs_location_pair_all_params(self):
        """
        get_dr_grs_location_pair()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_grs_location_pairs/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"location_pairs": {"mapKey": "inner"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        accept_language = 'testString'

        # Invoke method
        response = _service.get_dr_grs_location_pair(
            instance_id,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_grs_location_pair_all_params_with_retries(self):
        # Enable retries and run test_get_dr_grs_location_pair_all_params.
        _service.enable_retries()
        self.test_get_dr_grs_location_pair_all_params()

        # Disable retries and run test_get_dr_grs_location_pair_all_params.
        _service.disable_retries()
        self.test_get_dr_grs_location_pair_all_params()

    @responses.activate
    def test_get_dr_grs_location_pair_required_params(self):
        """
        test_get_dr_grs_location_pair_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_grs_location_pairs/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"location_pairs": {"mapKey": "inner"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Invoke method
        response = _service.get_dr_grs_location_pair(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_grs_location_pair_required_params_with_retries(self):
        # Enable retries and run test_get_dr_grs_location_pair_required_params.
        _service.enable_retries()
        self.test_get_dr_grs_location_pair_required_params()

        # Disable retries and run test_get_dr_grs_location_pair_required_params.
        _service.disable_retries()
        self.test_get_dr_grs_location_pair_required_params()

    @responses.activate
    def test_get_dr_grs_location_pair_value_error(self):
        """
        test_get_dr_grs_location_pair_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_grs_location_pairs/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"location_pairs": {"mapKey": "inner"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dr_grs_location_pair(**req_copy)

    def test_get_dr_grs_location_pair_value_error_with_retries(self):
        # Enable retries and run test_get_dr_grs_location_pair_value_error.
        _service.enable_retries()
        self.test_get_dr_grs_location_pair_value_error()

        # Disable retries and run test_get_dr_grs_location_pair_value_error.
        _service.disable_retries()
        self.test_get_dr_grs_location_pair_value_error()


class TestGetDrLocations:
    """
    Test Class for get_dr_locations
    """

    @responses.activate
    def test_get_dr_locations_all_params(self):
        """
        get_dr_locations()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_locations/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dr_locations": [{"id": "loc123", "name": "US-East-1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        accept_language = 'testString'

        # Invoke method
        response = _service.get_dr_locations(
            instance_id,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_locations_all_params_with_retries(self):
        # Enable retries and run test_get_dr_locations_all_params.
        _service.enable_retries()
        self.test_get_dr_locations_all_params()

        # Disable retries and run test_get_dr_locations_all_params.
        _service.disable_retries()
        self.test_get_dr_locations_all_params()

    @responses.activate
    def test_get_dr_locations_required_params(self):
        """
        test_get_dr_locations_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_locations/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dr_locations": [{"id": "loc123", "name": "US-East-1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Invoke method
        response = _service.get_dr_locations(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_locations_required_params_with_retries(self):
        # Enable retries and run test_get_dr_locations_required_params.
        _service.enable_retries()
        self.test_get_dr_locations_required_params()

        # Disable retries and run test_get_dr_locations_required_params.
        _service.disable_retries()
        self.test_get_dr_locations_required_params()

    @responses.activate
    def test_get_dr_locations_value_error(self):
        """
        test_get_dr_locations_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_locations/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dr_locations": [{"id": "loc123", "name": "US-East-1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dr_locations(**req_copy)

    def test_get_dr_locations_value_error_with_retries(self):
        # Enable retries and run test_get_dr_locations_value_error.
        _service.enable_retries()
        self.test_get_dr_locations_value_error()

        # Disable retries and run test_get_dr_locations_value_error.
        _service.disable_retries()
        self.test_get_dr_locations_value_error()


class TestGetDrManagedVm:
    """
    Test Class for get_dr_managed_vm
    """

    @responses.activate
    def test_get_dr_managed_vm_all_params(self):
        """
        get_dr_managed_vm()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_managed_vms/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"managed_vm_list": {"mapKey": {"core": "0.50", "dr_average_time": "10", "dr_region": "nyc02", "memory": "4", "region": "lon04", "vm_name": "example_vm", "workgroup_name": "Workgroup1", "workspace_name": "Workspace_dallas01"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        accept_language = 'testString'

        # Invoke method
        response = _service.get_dr_managed_vm(
            instance_id,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_managed_vm_all_params_with_retries(self):
        # Enable retries and run test_get_dr_managed_vm_all_params.
        _service.enable_retries()
        self.test_get_dr_managed_vm_all_params()

        # Disable retries and run test_get_dr_managed_vm_all_params.
        _service.disable_retries()
        self.test_get_dr_managed_vm_all_params()

    @responses.activate
    def test_get_dr_managed_vm_required_params(self):
        """
        test_get_dr_managed_vm_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_managed_vms/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"managed_vm_list": {"mapKey": {"core": "0.50", "dr_average_time": "10", "dr_region": "nyc02", "memory": "4", "region": "lon04", "vm_name": "example_vm", "workgroup_name": "Workgroup1", "workspace_name": "Workspace_dallas01"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Invoke method
        response = _service.get_dr_managed_vm(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_managed_vm_required_params_with_retries(self):
        # Enable retries and run test_get_dr_managed_vm_required_params.
        _service.enable_retries()
        self.test_get_dr_managed_vm_required_params()

        # Disable retries and run test_get_dr_managed_vm_required_params.
        _service.disable_retries()
        self.test_get_dr_managed_vm_required_params()

    @responses.activate
    def test_get_dr_managed_vm_value_error(self):
        """
        test_get_dr_managed_vm_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_managed_vms/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"managed_vm_list": {"mapKey": {"core": "0.50", "dr_average_time": "10", "dr_region": "nyc02", "memory": "4", "region": "lon04", "vm_name": "example_vm", "workgroup_name": "Workgroup1", "workspace_name": "Workspace_dallas01"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dr_managed_vm(**req_copy)

    def test_get_dr_managed_vm_value_error_with_retries(self):
        # Enable retries and run test_get_dr_managed_vm_value_error.
        _service.enable_retries()
        self.test_get_dr_managed_vm_value_error()

        # Disable retries and run test_get_dr_managed_vm_value_error.
        _service.disable_retries()
        self.test_get_dr_managed_vm_value_error()


class TestGetDrSummary:
    """
    Test Class for get_dr_summary
    """

    @responses.activate
    def test_get_dr_summary_all_params(self):
        """
        get_dr_summary()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_summary/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"managed_vm_list": {"anyKey": "anyValue"}, "orchestrator_details": {"last_updated_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "last_updated_standby_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "latest_orchestrator_time": "2025-10-16T09:28:13.696Z", "location_id": "location_id", "mfa_enabled": "mfa_enabled", "orch_ext_connectivity_status": "orch_ext_connectivity_status", "orch_standby_node_addition_status": "orch_standby_node_addition_status", "orchestrator_cluster_message": "orchestrator_cluster_message", "orchestrator_config_status": "orchestrator_config_status", "orchestrator_group_leader": "orchestrator_group_leader", "orchestrator_location_type": "orchestrator_location_type", "orchestrator_name": "orchestrator_name", "orchestrator_status": "orchestrator_status", "orchestrator_workspace_name": "orchestrator_workspace_name", "proxy_ip": "proxy_ip", "schematic_workspace_name": "schematic_workspace_name", "schematic_workspace_status": "schematic_workspace_status", "ssh_key_name": "ssh_key_name", "standby_orchestrator_name": "standby_orchestrator_name", "standby_orchestrator_status": "standby_orchestrator_status", "standby_orchestrator_workspace_name": "standby_orchestrator_workspace_name", "transit_gateway_name": "transit_gateway_name", "vpc_name": "vpc_name"}, "service_details": {"crn": "crn", "deployment_name": "deployment_name", "description": "description", "orchestrator_ha": false, "plan_name": "plan_name", "primary_ip_address": "primary_ip_address", "primary_orchestrator_dashboard_url": "primary_orchestrator_dashboard_url", "recovery_location": "recovery_location", "resource_group": "resource_group", "standby_description": "standby_description", "standby_ip_address": "standby_ip_address", "standby_orchestrator_dashboard_url": "standby_orchestrator_dashboard_url", "standby_status": "standby_status", "status": "status"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        accept_language = 'testString'

        # Invoke method
        response = _service.get_dr_summary(
            instance_id,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_summary_all_params_with_retries(self):
        # Enable retries and run test_get_dr_summary_all_params.
        _service.enable_retries()
        self.test_get_dr_summary_all_params()

        # Disable retries and run test_get_dr_summary_all_params.
        _service.disable_retries()
        self.test_get_dr_summary_all_params()

    @responses.activate
    def test_get_dr_summary_required_params(self):
        """
        test_get_dr_summary_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_summary/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"managed_vm_list": {"anyKey": "anyValue"}, "orchestrator_details": {"last_updated_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "last_updated_standby_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "latest_orchestrator_time": "2025-10-16T09:28:13.696Z", "location_id": "location_id", "mfa_enabled": "mfa_enabled", "orch_ext_connectivity_status": "orch_ext_connectivity_status", "orch_standby_node_addition_status": "orch_standby_node_addition_status", "orchestrator_cluster_message": "orchestrator_cluster_message", "orchestrator_config_status": "orchestrator_config_status", "orchestrator_group_leader": "orchestrator_group_leader", "orchestrator_location_type": "orchestrator_location_type", "orchestrator_name": "orchestrator_name", "orchestrator_status": "orchestrator_status", "orchestrator_workspace_name": "orchestrator_workspace_name", "proxy_ip": "proxy_ip", "schematic_workspace_name": "schematic_workspace_name", "schematic_workspace_status": "schematic_workspace_status", "ssh_key_name": "ssh_key_name", "standby_orchestrator_name": "standby_orchestrator_name", "standby_orchestrator_status": "standby_orchestrator_status", "standby_orchestrator_workspace_name": "standby_orchestrator_workspace_name", "transit_gateway_name": "transit_gateway_name", "vpc_name": "vpc_name"}, "service_details": {"crn": "crn", "deployment_name": "deployment_name", "description": "description", "orchestrator_ha": false, "plan_name": "plan_name", "primary_ip_address": "primary_ip_address", "primary_orchestrator_dashboard_url": "primary_orchestrator_dashboard_url", "recovery_location": "recovery_location", "resource_group": "resource_group", "standby_description": "standby_description", "standby_ip_address": "standby_ip_address", "standby_orchestrator_dashboard_url": "standby_orchestrator_dashboard_url", "standby_status": "standby_status", "status": "status"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Invoke method
        response = _service.get_dr_summary(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dr_summary_required_params_with_retries(self):
        # Enable retries and run test_get_dr_summary_required_params.
        _service.enable_retries()
        self.test_get_dr_summary_required_params()

        # Disable retries and run test_get_dr_summary_required_params.
        _service.disable_retries()
        self.test_get_dr_summary_required_params()

    @responses.activate
    def test_get_dr_summary_value_error(self):
        """
        test_get_dr_summary_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/dr_summary/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"managed_vm_list": {"anyKey": "anyValue"}, "orchestrator_details": {"last_updated_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "last_updated_standby_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "latest_orchestrator_time": "2025-10-16T09:28:13.696Z", "location_id": "location_id", "mfa_enabled": "mfa_enabled", "orch_ext_connectivity_status": "orch_ext_connectivity_status", "orch_standby_node_addition_status": "orch_standby_node_addition_status", "orchestrator_cluster_message": "orchestrator_cluster_message", "orchestrator_config_status": "orchestrator_config_status", "orchestrator_group_leader": "orchestrator_group_leader", "orchestrator_location_type": "orchestrator_location_type", "orchestrator_name": "orchestrator_name", "orchestrator_status": "orchestrator_status", "orchestrator_workspace_name": "orchestrator_workspace_name", "proxy_ip": "proxy_ip", "schematic_workspace_name": "schematic_workspace_name", "schematic_workspace_status": "schematic_workspace_status", "ssh_key_name": "ssh_key_name", "standby_orchestrator_name": "standby_orchestrator_name", "standby_orchestrator_status": "standby_orchestrator_status", "standby_orchestrator_workspace_name": "standby_orchestrator_workspace_name", "transit_gateway_name": "transit_gateway_name", "vpc_name": "vpc_name"}, "service_details": {"crn": "crn", "deployment_name": "deployment_name", "description": "description", "orchestrator_ha": false, "plan_name": "plan_name", "primary_ip_address": "primary_ip_address", "primary_orchestrator_dashboard_url": "primary_orchestrator_dashboard_url", "recovery_location": "recovery_location", "resource_group": "resource_group", "standby_description": "standby_description", "standby_ip_address": "standby_ip_address", "standby_orchestrator_dashboard_url": "standby_orchestrator_dashboard_url", "standby_status": "standby_status", "status": "status"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dr_summary(**req_copy)

    def test_get_dr_summary_value_error_with_retries(self):
        # Enable retries and run test_get_dr_summary_value_error.
        _service.enable_retries()
        self.test_get_dr_summary_value_error()

        # Disable retries and run test_get_dr_summary_value_error.
        _service.disable_retries()
        self.test_get_dr_summary_value_error()


# endregion
##############################################################################
# End of Service: DrAutomationConfig
##############################################################################

##############################################################################
# Start of Service: DrAutomationIbmCloud
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

        service = DrAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DrAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DrAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetMachineType:
    """
    Test Class for get_machine_type
    """

    @responses.activate
    def test_get_machine_type_all_params(self):
        """
        get_machine_type()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/machinetypes/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"workspaces": {"mapKey": ["inner"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        primary_workspace_name = 'Test-workspace-wdc06'
        accept_language = 'testString'
        standby_workspace_name = 'Test-workspace-wdc07'

        # Invoke method
        response = _service.get_machine_type(
            instance_id,
            primary_workspace_name,
            accept_language=accept_language,
            standby_workspace_name=standby_workspace_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'primary_workspace_name={}'.format(primary_workspace_name) in query_string
        assert 'standby_workspace_name={}'.format(standby_workspace_name) in query_string

    def test_get_machine_type_all_params_with_retries(self):
        # Enable retries and run test_get_machine_type_all_params.
        _service.enable_retries()
        self.test_get_machine_type_all_params()

        # Disable retries and run test_get_machine_type_all_params.
        _service.disable_retries()
        self.test_get_machine_type_all_params()

    @responses.activate
    def test_get_machine_type_required_params(self):
        """
        test_get_machine_type_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/machinetypes/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"workspaces": {"mapKey": ["inner"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        primary_workspace_name = 'Test-workspace-wdc06'

        # Invoke method
        response = _service.get_machine_type(
            instance_id,
            primary_workspace_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'primary_workspace_name={}'.format(primary_workspace_name) in query_string

    def test_get_machine_type_required_params_with_retries(self):
        # Enable retries and run test_get_machine_type_required_params.
        _service.enable_retries()
        self.test_get_machine_type_required_params()

        # Disable retries and run test_get_machine_type_required_params.
        _service.disable_retries()
        self.test_get_machine_type_required_params()

    @responses.activate
    def test_get_machine_type_value_error(self):
        """
        test_get_machine_type_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/machinetypes/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"workspaces": {"mapKey": ["inner"]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        primary_workspace_name = 'Test-workspace-wdc06'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "primary_workspace_name": primary_workspace_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_machine_type(**req_copy)

    def test_get_machine_type_value_error_with_retries(self):
        # Enable retries and run test_get_machine_type_value_error.
        _service.enable_retries()
        self.test_get_machine_type_value_error()

        # Disable retries and run test_get_machine_type_value_error.
        _service.disable_retries()
        self.test_get_machine_type_value_error()


class TestGetPowervsWorkspaces:
    """
    Test Class for get_powervs_workspaces
    """

    @responses.activate
    def test_get_powervs_workspaces_all_params(self):
        """
        get_powervs_workspaces()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/powervs_workspaces/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dr_standby_workspace_description": "anyValue", "dr_standby_workspaces": [{"details": {"crn": "crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::"}, "id": "id", "location": {"region": "lon06", "type": "data-center", "url": "https://lon.power-iaas.cloud.ibm.com"}, "name": "name", "status": "status"}], "dr_workspace_description": "anyValue", "dr_workspaces": [{"default": true, "details": {"crn": "crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::"}, "id": "id", "location": {"region": "lon06", "type": "data-center", "url": "https://lon.power-iaas.cloud.ibm.com"}, "name": "name", "status": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        location_id = 'testString'

        # Invoke method
        response = _service.get_powervs_workspaces(
            instance_id,
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

    def test_get_powervs_workspaces_all_params_with_retries(self):
        # Enable retries and run test_get_powervs_workspaces_all_params.
        _service.enable_retries()
        self.test_get_powervs_workspaces_all_params()

        # Disable retries and run test_get_powervs_workspaces_all_params.
        _service.disable_retries()
        self.test_get_powervs_workspaces_all_params()

    @responses.activate
    def test_get_powervs_workspaces_value_error(self):
        """
        test_get_powervs_workspaces_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/powervs_workspaces/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dr_standby_workspace_description": "anyValue", "dr_standby_workspaces": [{"details": {"crn": "crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::"}, "id": "id", "location": {"region": "lon06", "type": "data-center", "url": "https://lon.power-iaas.cloud.ibm.com"}, "name": "name", "status": "status"}], "dr_workspace_description": "anyValue", "dr_workspaces": [{"default": true, "details": {"crn": "crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::"}, "id": "id", "location": {"region": "lon06", "type": "data-center", "url": "https://lon.power-iaas.cloud.ibm.com"}, "name": "name", "status": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        location_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "location_id": location_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_powervs_workspaces(**req_copy)

    def test_get_powervs_workspaces_value_error_with_retries(self):
        # Enable retries and run test_get_powervs_workspaces_value_error.
        _service.enable_retries()
        self.test_get_powervs_workspaces_value_error()

        # Disable retries and run test_get_powervs_workspaces_value_error.
        _service.disable_retries()
        self.test_get_powervs_workspaces_value_error()


# endregion
##############################################################################
# End of Service: DrAutomationIbmCloud
##############################################################################

##############################################################################
# Start of Service: DrAutomationManageDr
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

        service = DrAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DrAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DrAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateManageDr:
    """
    Test Class for create_manage_dr
    """

    @responses.activate
    def test_create_manage_dr_all_params(self):
        """
        create_manage_dr()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/manage_dr/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dashboard_url": "https://power-dra.test.cloud.ibm.com/power-dra-ui?instance_id=crn:v1:bluemix:public:power-dr-automation:us-south:a/fe3c2ccd058e407c81e1dba2b5c0e0d6:e3d09875-bbf8-4d8a-b52c-abefb67a53c5::", "id": "crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        location_id = 'dal10'
        machine_type = 'bx2-4x16'
        orchestrator_location_type = 'off-premises'
        orchestrator_name = 'adminUser'
        orchestrator_password = 'testString'
        orchestrator_workspace_id = 'orch-workspace-01'
        api_key = 'testString'
        client_id = 'abcd-97d2-1234-bf62-8eaecc67a1234'
        client_secret = 'abcd1234xM1y123wK6qR9123456789bE2jG0pabcdefgh'
        guid = '123e4567-e89b-12d3-a456-426614174000'
        orchestrator_ha = True
        proxy_ip = '10.40.30.10:8888'
        region_id = 'us-south'
        resource_instance = 'crn:v1:bluemix:public:resource-controller::res123'
        secret = 'testString'
        secret_group = 'default-secret-group'
        ssh_key_name = 'my-ssh-key'
        standby_machine_type = 'bx2-8x32'
        standby_orchestrator_name = 'standbyAdmin'
        standby_orchestrator_workspace_id = 'orch-standby-02'
        standby_tier = 'Premium'
        tenant_name = 'xxx.ibm.com'
        tier = 'Standard'
        stand_by_redeploy = 'testString'
        accept_language = 'testString'
        accepts_incomplete = True

        # Invoke method
        response = _service.create_manage_dr(
            instance_id,
            location_id,
            machine_type,
            orchestrator_location_type,
            orchestrator_name,
            orchestrator_password,
            orchestrator_workspace_id,
            api_key=api_key,
            client_id=client_id,
            client_secret=client_secret,
            guid=guid,
            orchestrator_ha=orchestrator_ha,
            proxy_ip=proxy_ip,
            region_id=region_id,
            resource_instance=resource_instance,
            secret=secret,
            secret_group=secret_group,
            ssh_key_name=ssh_key_name,
            standby_machine_type=standby_machine_type,
            standby_orchestrator_name=standby_orchestrator_name,
            standby_orchestrator_workspace_id=standby_orchestrator_workspace_id,
            standby_tier=standby_tier,
            tenant_name=tenant_name,
            tier=tier,
            stand_by_redeploy=stand_by_redeploy,
            accept_language=accept_language,
            accepts_incomplete=accepts_incomplete,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'stand_by_redeploy={}'.format(stand_by_redeploy) in query_string
        assert 'accepts_incomplete={}'.format('true' if accepts_incomplete else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['location_id'] == 'dal10'
        assert req_body['machine_type'] == 'bx2-4x16'
        assert req_body['orchestrator_location_type'] == 'off-premises'
        assert req_body['orchestrator_name'] == 'adminUser'
        assert req_body['orchestrator_password'] == 'testString'
        assert req_body['orchestrator_workspace_id'] == 'orch-workspace-01'
        assert req_body['api_key'] == 'testString'
        assert req_body['client_id'] == 'abcd-97d2-1234-bf62-8eaecc67a1234'
        assert req_body['client_secret'] == 'abcd1234xM1y123wK6qR9123456789bE2jG0pabcdefgh'
        assert req_body['guid'] == '123e4567-e89b-12d3-a456-426614174000'
        assert req_body['orchestrator_ha'] == True
        assert req_body['proxy_ip'] == '10.40.30.10:8888'
        assert req_body['region_id'] == 'us-south'
        assert req_body['resource_instance'] == 'crn:v1:bluemix:public:resource-controller::res123'
        assert req_body['secret'] == 'testString'
        assert req_body['secret_group'] == 'default-secret-group'
        assert req_body['ssh_key_name'] == 'my-ssh-key'
        assert req_body['standby_machine_type'] == 'bx2-8x32'
        assert req_body['standby_orchestrator_name'] == 'standbyAdmin'
        assert req_body['standby_orchestrator_workspace_id'] == 'orch-standby-02'
        assert req_body['standby_tier'] == 'Premium'
        assert req_body['tenant_name'] == 'xxx.ibm.com'
        assert req_body['tier'] == 'Standard'

    def test_create_manage_dr_all_params_with_retries(self):
        # Enable retries and run test_create_manage_dr_all_params.
        _service.enable_retries()
        self.test_create_manage_dr_all_params()

        # Disable retries and run test_create_manage_dr_all_params.
        _service.disable_retries()
        self.test_create_manage_dr_all_params()

    @responses.activate
    def test_create_manage_dr_required_params(self):
        """
        test_create_manage_dr_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/manage_dr/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dashboard_url": "https://power-dra.test.cloud.ibm.com/power-dra-ui?instance_id=crn:v1:bluemix:public:power-dr-automation:us-south:a/fe3c2ccd058e407c81e1dba2b5c0e0d6:e3d09875-bbf8-4d8a-b52c-abefb67a53c5::", "id": "crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        location_id = 'dal10'
        machine_type = 'bx2-4x16'
        orchestrator_location_type = 'off-premises'
        orchestrator_name = 'adminUser'
        orchestrator_password = 'testString'
        orchestrator_workspace_id = 'orch-workspace-01'
        api_key = 'testString'
        client_id = 'abcd-97d2-1234-bf62-8eaecc67a1234'
        client_secret = 'abcd1234xM1y123wK6qR9123456789bE2jG0pabcdefgh'
        guid = '123e4567-e89b-12d3-a456-426614174000'
        orchestrator_ha = True
        proxy_ip = '10.40.30.10:8888'
        region_id = 'us-south'
        resource_instance = 'crn:v1:bluemix:public:resource-controller::res123'
        secret = 'testString'
        secret_group = 'default-secret-group'
        ssh_key_name = 'my-ssh-key'
        standby_machine_type = 'bx2-8x32'
        standby_orchestrator_name = 'standbyAdmin'
        standby_orchestrator_workspace_id = 'orch-standby-02'
        standby_tier = 'Premium'
        tenant_name = 'xxx.ibm.com'
        tier = 'Standard'

        # Invoke method
        response = _service.create_manage_dr(
            instance_id,
            location_id,
            machine_type,
            orchestrator_location_type,
            orchestrator_name,
            orchestrator_password,
            orchestrator_workspace_id,
            api_key=api_key,
            client_id=client_id,
            client_secret=client_secret,
            guid=guid,
            orchestrator_ha=orchestrator_ha,
            proxy_ip=proxy_ip,
            region_id=region_id,
            resource_instance=resource_instance,
            secret=secret,
            secret_group=secret_group,
            ssh_key_name=ssh_key_name,
            standby_machine_type=standby_machine_type,
            standby_orchestrator_name=standby_orchestrator_name,
            standby_orchestrator_workspace_id=standby_orchestrator_workspace_id,
            standby_tier=standby_tier,
            tenant_name=tenant_name,
            tier=tier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['location_id'] == 'dal10'
        assert req_body['machine_type'] == 'bx2-4x16'
        assert req_body['orchestrator_location_type'] == 'off-premises'
        assert req_body['orchestrator_name'] == 'adminUser'
        assert req_body['orchestrator_password'] == 'testString'
        assert req_body['orchestrator_workspace_id'] == 'orch-workspace-01'
        assert req_body['api_key'] == 'testString'
        assert req_body['client_id'] == 'abcd-97d2-1234-bf62-8eaecc67a1234'
        assert req_body['client_secret'] == 'abcd1234xM1y123wK6qR9123456789bE2jG0pabcdefgh'
        assert req_body['guid'] == '123e4567-e89b-12d3-a456-426614174000'
        assert req_body['orchestrator_ha'] == True
        assert req_body['proxy_ip'] == '10.40.30.10:8888'
        assert req_body['region_id'] == 'us-south'
        assert req_body['resource_instance'] == 'crn:v1:bluemix:public:resource-controller::res123'
        assert req_body['secret'] == 'testString'
        assert req_body['secret_group'] == 'default-secret-group'
        assert req_body['ssh_key_name'] == 'my-ssh-key'
        assert req_body['standby_machine_type'] == 'bx2-8x32'
        assert req_body['standby_orchestrator_name'] == 'standbyAdmin'
        assert req_body['standby_orchestrator_workspace_id'] == 'orch-standby-02'
        assert req_body['standby_tier'] == 'Premium'
        assert req_body['tenant_name'] == 'xxx.ibm.com'
        assert req_body['tier'] == 'Standard'

    def test_create_manage_dr_required_params_with_retries(self):
        # Enable retries and run test_create_manage_dr_required_params.
        _service.enable_retries()
        self.test_create_manage_dr_required_params()

        # Disable retries and run test_create_manage_dr_required_params.
        _service.disable_retries()
        self.test_create_manage_dr_required_params()

    @responses.activate
    def test_create_manage_dr_value_error(self):
        """
        test_create_manage_dr_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/manage_dr/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"dashboard_url": "https://power-dra.test.cloud.ibm.com/power-dra-ui?instance_id=crn:v1:bluemix:public:power-dr-automation:us-south:a/fe3c2ccd058e407c81e1dba2b5c0e0d6:e3d09875-bbf8-4d8a-b52c-abefb67a53c5::", "id": "crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        location_id = 'dal10'
        machine_type = 'bx2-4x16'
        orchestrator_location_type = 'off-premises'
        orchestrator_name = 'adminUser'
        orchestrator_password = 'testString'
        orchestrator_workspace_id = 'orch-workspace-01'
        api_key = 'testString'
        client_id = 'abcd-97d2-1234-bf62-8eaecc67a1234'
        client_secret = 'abcd1234xM1y123wK6qR9123456789bE2jG0pabcdefgh'
        guid = '123e4567-e89b-12d3-a456-426614174000'
        orchestrator_ha = True
        proxy_ip = '10.40.30.10:8888'
        region_id = 'us-south'
        resource_instance = 'crn:v1:bluemix:public:resource-controller::res123'
        secret = 'testString'
        secret_group = 'default-secret-group'
        ssh_key_name = 'my-ssh-key'
        standby_machine_type = 'bx2-8x32'
        standby_orchestrator_name = 'standbyAdmin'
        standby_orchestrator_workspace_id = 'orch-standby-02'
        standby_tier = 'Premium'
        tenant_name = 'xxx.ibm.com'
        tier = 'Standard'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "location_id": location_id,
            "machine_type": machine_type,
            "orchestrator_location_type": orchestrator_location_type,
            "orchestrator_name": orchestrator_name,
            "orchestrator_password": orchestrator_password,
            "orchestrator_workspace_id": orchestrator_workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_manage_dr(**req_copy)

    def test_create_manage_dr_value_error_with_retries(self):
        # Enable retries and run test_create_manage_dr_value_error.
        _service.enable_retries()
        self.test_create_manage_dr_value_error()

        # Disable retries and run test_create_manage_dr_value_error.
        _service.disable_retries()
        self.test_create_manage_dr_value_error()


# endregion
##############################################################################
# End of Service: DrAutomationManageDr
##############################################################################

##############################################################################
# Start of Service: DrAutomationServiceInstance
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

        service = DrAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DrAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DrAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetLastOperation:
    """
    Test Class for get_last_operation
    """

    @responses.activate
    def test_get_last_operation_all_params(self):
        """
        get_last_operation()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/last_operation/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"crn": "crn:v1:staging:public:power-dr-automation:global:a/2c5d7270091f495795350e9adfa8399c:86e0c9a9-80f4-4fcf-88a0-07643de01bb8::", "deployment_name": "dr-deployment-instance-1", "last_updated_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "last_updated_standby_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "mfa_enabled": "true", "orch_ext_connectivity_status": "Connected", "orch_standby_node_addtion_status": "Completed", "orchestrator_cluster_message": "Cluster healthy", "orchestrator_config_status": "Configured", "orchestrator_ha": true, "plan_name": "DR Automation Private Plan", "primary_description": "2/5: Creating primary orchestrator VM.", "primary_ip_address": "192.168.1.10", "primary_orchestrator_status": "orchestrator-VM-creation-in-progress", "recovery_location": "us-east", "resource_group": "Default", "standby_description": "1/4: Service instance is downloading orchestrator image for standby VM creation.", "standby_ip_address": "192.168.1.11", "standby_status": "downloading-orchestrator-image", "status": "Running"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        accept_language = 'testString'

        # Invoke method
        response = _service.get_last_operation(
            instance_id,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_last_operation_all_params_with_retries(self):
        # Enable retries and run test_get_last_operation_all_params.
        _service.enable_retries()
        self.test_get_last_operation_all_params()

        # Disable retries and run test_get_last_operation_all_params.
        _service.disable_retries()
        self.test_get_last_operation_all_params()

    @responses.activate
    def test_get_last_operation_required_params(self):
        """
        test_get_last_operation_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/last_operation/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"crn": "crn:v1:staging:public:power-dr-automation:global:a/2c5d7270091f495795350e9adfa8399c:86e0c9a9-80f4-4fcf-88a0-07643de01bb8::", "deployment_name": "dr-deployment-instance-1", "last_updated_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "last_updated_standby_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "mfa_enabled": "true", "orch_ext_connectivity_status": "Connected", "orch_standby_node_addtion_status": "Completed", "orchestrator_cluster_message": "Cluster healthy", "orchestrator_config_status": "Configured", "orchestrator_ha": true, "plan_name": "DR Automation Private Plan", "primary_description": "2/5: Creating primary orchestrator VM.", "primary_ip_address": "192.168.1.10", "primary_orchestrator_status": "orchestrator-VM-creation-in-progress", "recovery_location": "us-east", "resource_group": "Default", "standby_description": "1/4: Service instance is downloading orchestrator image for standby VM creation.", "standby_ip_address": "192.168.1.11", "standby_status": "downloading-orchestrator-image", "status": "Running"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Invoke method
        response = _service.get_last_operation(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_last_operation_required_params_with_retries(self):
        # Enable retries and run test_get_last_operation_required_params.
        _service.enable_retries()
        self.test_get_last_operation_required_params()

        # Disable retries and run test_get_last_operation_required_params.
        _service.disable_retries()
        self.test_get_last_operation_required_params()

    @responses.activate
    def test_get_last_operation_value_error(self):
        """
        test_get_last_operation_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/last_operation/123456d3-1122-3344-b67d-4389b44b7bf9')
        mock_response = '{"crn": "crn:v1:staging:public:power-dr-automation:global:a/2c5d7270091f495795350e9adfa8399c:86e0c9a9-80f4-4fcf-88a0-07643de01bb8::", "deployment_name": "dr-deployment-instance-1", "last_updated_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "last_updated_standby_orchestrator_deployment_time": "2025-10-16T09:28:13.696Z", "mfa_enabled": "true", "orch_ext_connectivity_status": "Connected", "orch_standby_node_addtion_status": "Completed", "orchestrator_cluster_message": "Cluster healthy", "orchestrator_config_status": "Configured", "orchestrator_ha": true, "plan_name": "DR Automation Private Plan", "primary_description": "2/5: Creating primary orchestrator VM.", "primary_ip_address": "192.168.1.10", "primary_orchestrator_status": "orchestrator-VM-creation-in-progress", "recovery_location": "us-east", "resource_group": "Default", "standby_description": "1/4: Service instance is downloading orchestrator image for standby VM creation.", "standby_ip_address": "192.168.1.11", "standby_status": "downloading-orchestrator-image", "status": "Running"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_last_operation(**req_copy)

    def test_get_last_operation_value_error_with_retries(self):
        # Enable retries and run test_get_last_operation_value_error.
        _service.enable_retries()
        self.test_get_last_operation_value_error()

        # Disable retries and run test_get_last_operation_value_error.
        _service.disable_retries()
        self.test_get_last_operation_value_error()


# endregion
##############################################################################
# End of Service: DrAutomationServiceInstance
##############################################################################

##############################################################################
# Start of Service: DrEvents
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

        service = DrAutomationServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DrAutomationServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DrAutomationServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListEvents:
    """
    Test Class for list_events
    """

    @responses.activate
    def test_list_events_all_params(self):
        """
        list_events()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/service_instances/123456d3-1122-3344-b67d-4389b44b7bf9/events')
        mock_response = '{"events": [{"action": "create", "api_source": "dr-automation-api", "event_id": "1cecfe43-43cd-4b1b-86be-30c2d3d2a25f", "level": "info", "message": "Service Instance created successfully", "message_data": {"anyKey": "anyValue"}, "metadata": {"anyKey": "anyValue"}, "resource": "ProvisionID", "time": "2025-06-23T07:12:49.840Z", "timestamp": "1750662769", "user": {"email": "abcuser@ibm.com", "name": "abcuser", "user_id": "IBMid-695000abc7E"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        time = '2025-06-19T23:59:59Z'
        from_time = '2025-06-19T00:00:00Z'
        to_time = '2025-06-19T23:59:59Z'
        accept_language = 'testString'

        # Invoke method
        response = _service.list_events(
            instance_id,
            time=time,
            from_time=from_time,
            to_time=to_time,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'time={}'.format(time) in query_string
        assert 'from_time={}'.format(from_time) in query_string
        assert 'to_time={}'.format(to_time) in query_string

    def test_list_events_all_params_with_retries(self):
        # Enable retries and run test_list_events_all_params.
        _service.enable_retries()
        self.test_list_events_all_params()

        # Disable retries and run test_list_events_all_params.
        _service.disable_retries()
        self.test_list_events_all_params()

    @responses.activate
    def test_list_events_required_params(self):
        """
        test_list_events_required_params()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/service_instances/123456d3-1122-3344-b67d-4389b44b7bf9/events')
        mock_response = '{"events": [{"action": "create", "api_source": "dr-automation-api", "event_id": "1cecfe43-43cd-4b1b-86be-30c2d3d2a25f", "level": "info", "message": "Service Instance created successfully", "message_data": {"anyKey": "anyValue"}, "metadata": {"anyKey": "anyValue"}, "resource": "ProvisionID", "time": "2025-06-23T07:12:49.840Z", "timestamp": "1750662769", "user": {"email": "abcuser@ibm.com", "name": "abcuser", "user_id": "IBMid-695000abc7E"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Invoke method
        response = _service.list_events(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_events_required_params_with_retries(self):
        # Enable retries and run test_list_events_required_params.
        _service.enable_retries()
        self.test_list_events_required_params()

        # Disable retries and run test_list_events_required_params.
        _service.disable_retries()
        self.test_list_events_required_params()

    @responses.activate
    def test_list_events_value_error(self):
        """
        test_list_events_value_error()
        """
        # Set up mock
        url = preprocess_url('/drautomation/v1/service_instances/123456d3-1122-3344-b67d-4389b44b7bf9/events')
        mock_response = '{"events": [{"action": "create", "api_source": "dr-automation-api", "event_id": "1cecfe43-43cd-4b1b-86be-30c2d3d2a25f", "level": "info", "message": "Service Instance created successfully", "message_data": {"anyKey": "anyValue"}, "metadata": {"anyKey": "anyValue"}, "resource": "ProvisionID", "time": "2025-06-23T07:12:49.840Z", "timestamp": "1750662769", "user": {"email": "abcuser@ibm.com", "name": "abcuser", "user_id": "IBMid-695000abc7E"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_events(**req_copy)

    def test_list_events_value_error_with_retries(self):
        # Enable retries and run test_list_events_value_error.
        _service.enable_retries()
        self.test_list_events_value_error()

        # Disable retries and run test_list_events_value_error.
        _service.disable_retries()
        self.test_list_events_value_error()


class TestGetEvent:
    """
    Test Class for get_event
    """

    @responses.activate
    def test_get_event_all_params(self):
        """
        get_event()
        """
        # Set up mock
        url = preprocess_url(
            '/drautomation/v1/service_instances/123456d3-1122-3344-b67d-4389b44b7bf9/events/00116b2a-9326-4024-839e-fb5364b76898'
        )
        mock_response = '{"action": "create", "api_source": "dr-automation-api", "event_id": "1cecfe43-43cd-4b1b-86be-30c2d3d2a25f", "level": "info", "message": "Service Instance created successfully", "message_data": {"anyKey": "anyValue"}, "metadata": {"anyKey": "anyValue"}, "resource": "ProvisionID", "time": "2025-06-23T07:12:49.840Z", "timestamp": "1750662769", "user": {"email": "abcuser@ibm.com", "name": "abcuser", "user_id": "IBMid-695000abc7E"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        event_id = '00116b2a-9326-4024-839e-fb5364b76898'
        accept_language = 'testString'

        # Invoke method
        response = _service.get_event(
            instance_id,
            event_id,
            accept_language=accept_language,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_event_all_params_with_retries(self):
        # Enable retries and run test_get_event_all_params.
        _service.enable_retries()
        self.test_get_event_all_params()

        # Disable retries and run test_get_event_all_params.
        _service.disable_retries()
        self.test_get_event_all_params()

    @responses.activate
    def test_get_event_required_params(self):
        """
        test_get_event_required_params()
        """
        # Set up mock
        url = preprocess_url(
            '/drautomation/v1/service_instances/123456d3-1122-3344-b67d-4389b44b7bf9/events/00116b2a-9326-4024-839e-fb5364b76898'
        )
        mock_response = '{"action": "create", "api_source": "dr-automation-api", "event_id": "1cecfe43-43cd-4b1b-86be-30c2d3d2a25f", "level": "info", "message": "Service Instance created successfully", "message_data": {"anyKey": "anyValue"}, "metadata": {"anyKey": "anyValue"}, "resource": "ProvisionID", "time": "2025-06-23T07:12:49.840Z", "timestamp": "1750662769", "user": {"email": "abcuser@ibm.com", "name": "abcuser", "user_id": "IBMid-695000abc7E"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        event_id = '00116b2a-9326-4024-839e-fb5364b76898'

        # Invoke method
        response = _service.get_event(
            instance_id,
            event_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_event_required_params_with_retries(self):
        # Enable retries and run test_get_event_required_params.
        _service.enable_retries()
        self.test_get_event_required_params()

        # Disable retries and run test_get_event_required_params.
        _service.disable_retries()
        self.test_get_event_required_params()

    @responses.activate
    def test_get_event_value_error(self):
        """
        test_get_event_value_error()
        """
        # Set up mock
        url = preprocess_url(
            '/drautomation/v1/service_instances/123456d3-1122-3344-b67d-4389b44b7bf9/events/00116b2a-9326-4024-839e-fb5364b76898'
        )
        mock_response = '{"action": "create", "api_source": "dr-automation-api", "event_id": "1cecfe43-43cd-4b1b-86be-30c2d3d2a25f", "level": "info", "message": "Service Instance created successfully", "message_data": {"anyKey": "anyValue"}, "metadata": {"anyKey": "anyValue"}, "resource": "ProvisionID", "time": "2025-06-23T07:12:49.840Z", "timestamp": "1750662769", "user": {"email": "abcuser@ibm.com", "name": "abcuser", "user_id": "IBMid-695000abc7E"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = '123456d3-1122-3344-b67d-4389b44b7bf9'
        event_id = '00116b2a-9326-4024-839e-fb5364b76898'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "event_id": event_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_event(**req_copy)

    def test_get_event_value_error_with_retries(self):
        # Enable retries and run test_get_event_value_error.
        _service.enable_retries()
        self.test_get_event_value_error()

        # Disable retries and run test_get_event_value_error.
        _service.disable_retries()
        self.test_get_event_value_error()


# endregion
##############################################################################
# End of Service: DrEvents
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_DRStandbyWorkspace:
    """
    Test Class for DRStandbyWorkspace
    """

    def test_dr_standby_workspace_serialization(self):
        """
        Test serialization/deserialization for DRStandbyWorkspace
        """

        # Construct dict forms of any model objects needed in order to build this model.

        details_dr_model = {}  # DetailsDr
        details_dr_model['crn'] = (
            'crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::'
        )

        location_dr_model = {}  # LocationDr
        location_dr_model['region'] = 'lon06'
        location_dr_model['type'] = 'data-center'
        location_dr_model['url'] = 'https://lon.power-iaas.cloud.ibm.com'

        # Construct a json representation of a DRStandbyWorkspace model
        dr_standby_workspace_model_json = {}
        dr_standby_workspace_model_json['details'] = details_dr_model
        dr_standby_workspace_model_json['id'] = 'testString'
        dr_standby_workspace_model_json['location'] = location_dr_model
        dr_standby_workspace_model_json['name'] = 'testString'
        dr_standby_workspace_model_json['status'] = 'testString'

        # Construct a model instance of DRStandbyWorkspace by calling from_dict on the json representation
        dr_standby_workspace_model = DRStandbyWorkspace.from_dict(dr_standby_workspace_model_json)
        assert dr_standby_workspace_model != False

        # Construct a model instance of DRStandbyWorkspace by calling from_dict on the json representation
        dr_standby_workspace_model_dict = DRStandbyWorkspace.from_dict(dr_standby_workspace_model_json).__dict__
        dr_standby_workspace_model2 = DRStandbyWorkspace(**dr_standby_workspace_model_dict)

        # Verify the model instances are equivalent
        assert dr_standby_workspace_model == dr_standby_workspace_model2

        # Convert model instance back to dict and verify no loss of data
        dr_standby_workspace_model_json2 = dr_standby_workspace_model.to_dict()
        assert dr_standby_workspace_model_json2 == dr_standby_workspace_model_json


class TestModel_DRWorkspace:
    """
    Test Class for DRWorkspace
    """

    def test_dr_workspace_serialization(self):
        """
        Test serialization/deserialization for DRWorkspace
        """

        # Construct dict forms of any model objects needed in order to build this model.

        details_dr_model = {}  # DetailsDr
        details_dr_model['crn'] = (
            'crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::'
        )

        location_dr_model = {}  # LocationDr
        location_dr_model['region'] = 'lon06'
        location_dr_model['type'] = 'data-center'
        location_dr_model['url'] = 'https://lon.power-iaas.cloud.ibm.com'

        # Construct a json representation of a DRWorkspace model
        dr_workspace_model_json = {}
        dr_workspace_model_json['default'] = True
        dr_workspace_model_json['details'] = details_dr_model
        dr_workspace_model_json['id'] = 'testString'
        dr_workspace_model_json['location'] = location_dr_model
        dr_workspace_model_json['name'] = 'testString'
        dr_workspace_model_json['status'] = 'active'

        # Construct a model instance of DRWorkspace by calling from_dict on the json representation
        dr_workspace_model = DRWorkspace.from_dict(dr_workspace_model_json)
        assert dr_workspace_model != False

        # Construct a model instance of DRWorkspace by calling from_dict on the json representation
        dr_workspace_model_dict = DRWorkspace.from_dict(dr_workspace_model_json).__dict__
        dr_workspace_model2 = DRWorkspace(**dr_workspace_model_dict)

        # Verify the model instances are equivalent
        assert dr_workspace_model == dr_workspace_model2

        # Convert model instance back to dict and verify no loss of data
        dr_workspace_model_json2 = dr_workspace_model.to_dict()
        assert dr_workspace_model_json2 == dr_workspace_model_json


class TestModel_DetailsDr:
    """
    Test Class for DetailsDr
    """

    def test_details_dr_serialization(self):
        """
        Test serialization/deserialization for DetailsDr
        """

        # Construct a json representation of a DetailsDr model
        details_dr_model_json = {}
        details_dr_model_json['crn'] = (
            'crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::'
        )

        # Construct a model instance of DetailsDr by calling from_dict on the json representation
        details_dr_model = DetailsDr.from_dict(details_dr_model_json)
        assert details_dr_model != False

        # Construct a model instance of DetailsDr by calling from_dict on the json representation
        details_dr_model_dict = DetailsDr.from_dict(details_dr_model_json).__dict__
        details_dr_model2 = DetailsDr(**details_dr_model_dict)

        # Verify the model instances are equivalent
        assert details_dr_model == details_dr_model2

        # Convert model instance back to dict and verify no loss of data
        details_dr_model_json2 = details_dr_model.to_dict()
        assert details_dr_model_json2 == details_dr_model_json


class TestModel_DrAutomationGetSummaryResponse:
    """
    Test Class for DrAutomationGetSummaryResponse
    """

    def test_dr_automation_get_summary_response_serialization(self):
        """
        Test serialization/deserialization for DrAutomationGetSummaryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        orchestrator_details_model = {}  # OrchestratorDetails
        orchestrator_details_model['last_updated_orchestrator_deployment_time'] = '2025-10-16T09:28:13.696000Z'
        orchestrator_details_model['last_updated_standby_orchestrator_deployment_time'] = '2025-10-16T09:28:13.696000Z'
        orchestrator_details_model['latest_orchestrator_time'] = '2025-10-16T09:28:13.696000Z'
        orchestrator_details_model['location_id'] = 'testString'
        orchestrator_details_model['mfa_enabled'] = 'testString'
        orchestrator_details_model['orch_ext_connectivity_status'] = 'testString'
        orchestrator_details_model['orch_standby_node_addition_status'] = 'testString'
        orchestrator_details_model['orchestrator_cluster_message'] = 'testString'
        orchestrator_details_model['orchestrator_config_status'] = 'testString'
        orchestrator_details_model['orchestrator_group_leader'] = 'testString'
        orchestrator_details_model['orchestrator_location_type'] = 'testString'
        orchestrator_details_model['orchestrator_name'] = 'testString'
        orchestrator_details_model['orchestrator_status'] = 'testString'
        orchestrator_details_model['orchestrator_workspace_name'] = 'testString'
        orchestrator_details_model['proxy_ip'] = 'testString'
        orchestrator_details_model['schematic_workspace_name'] = 'testString'
        orchestrator_details_model['schematic_workspace_status'] = 'testString'
        orchestrator_details_model['ssh_key_name'] = 'testString'
        orchestrator_details_model['standby_orchestrator_name'] = 'testString'
        orchestrator_details_model['standby_orchestrator_status'] = 'testString'
        orchestrator_details_model['standby_orchestrator_workspace_name'] = 'testString'
        orchestrator_details_model['transit_gateway_name'] = 'testString'
        orchestrator_details_model['vpc_name'] = 'testString'

        service_details_model = {}  # ServiceDetails
        service_details_model['crn'] = 'testString'
        service_details_model['deployment_name'] = 'testString'
        service_details_model['description'] = 'testString'
        service_details_model['orchestrator_ha'] = True
        service_details_model['plan_name'] = 'testString'
        service_details_model['primary_ip_address'] = 'testString'
        service_details_model['primary_orchestrator_dashboard_url'] = 'testString'
        service_details_model['recovery_location'] = 'testString'
        service_details_model['resource_group'] = 'testString'
        service_details_model['standby_description'] = 'testString'
        service_details_model['standby_ip_address'] = 'testString'
        service_details_model['standby_orchestrator_dashboard_url'] = 'testString'
        service_details_model['standby_status'] = 'testString'
        service_details_model['status'] = 'testString'

        # Construct a json representation of a DrAutomationGetSummaryResponse model
        dr_automation_get_summary_response_model_json = {}
        dr_automation_get_summary_response_model_json['managed_vm_list'] = {'anyKey': 'anyValue'}
        dr_automation_get_summary_response_model_json['orchestrator_details'] = orchestrator_details_model
        dr_automation_get_summary_response_model_json['service_details'] = service_details_model

        # Construct a model instance of DrAutomationGetSummaryResponse by calling from_dict on the json representation
        dr_automation_get_summary_response_model = DrAutomationGetSummaryResponse.from_dict(
            dr_automation_get_summary_response_model_json
        )
        assert dr_automation_get_summary_response_model != False

        # Construct a model instance of DrAutomationGetSummaryResponse by calling from_dict on the json representation
        dr_automation_get_summary_response_model_dict = DrAutomationGetSummaryResponse.from_dict(
            dr_automation_get_summary_response_model_json
        ).__dict__
        dr_automation_get_summary_response_model2 = DrAutomationGetSummaryResponse(
            **dr_automation_get_summary_response_model_dict
        )

        # Verify the model instances are equivalent
        assert dr_automation_get_summary_response_model == dr_automation_get_summary_response_model2

        # Convert model instance back to dict and verify no loss of data
        dr_automation_get_summary_response_model_json2 = dr_automation_get_summary_response_model.to_dict()
        assert dr_automation_get_summary_response_model_json2 == dr_automation_get_summary_response_model_json


class TestModel_DrData:
    """
    Test Class for DrData
    """

    def test_dr_data_serialization(self):
        """
        Test serialization/deserialization for DrData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        details_dr_model = {}  # DetailsDr
        details_dr_model['crn'] = (
            'crn:v1:bluemix:public:power-iaas:lon06:a/094f4214c75941f991da601b001df1fe:b6297e60-d0fe-4e24-8b15-276cf0645737::'
        )

        location_dr_model = {}  # LocationDr
        location_dr_model['region'] = 'lon06'
        location_dr_model['type'] = 'data-center'
        location_dr_model['url'] = 'https://lon.power-iaas.cloud.ibm.com'

        dr_standby_workspace_model = {}  # DRStandbyWorkspace
        dr_standby_workspace_model['details'] = details_dr_model
        dr_standby_workspace_model['id'] = 'testString'
        dr_standby_workspace_model['location'] = location_dr_model
        dr_standby_workspace_model['name'] = 'testString'
        dr_standby_workspace_model['status'] = 'testString'

        dr_workspace_model = {}  # DRWorkspace
        dr_workspace_model['default'] = True
        dr_workspace_model['details'] = details_dr_model
        dr_workspace_model['id'] = 'testString'
        dr_workspace_model['location'] = location_dr_model
        dr_workspace_model['name'] = 'testString'
        dr_workspace_model['status'] = 'active'

        # Construct a json representation of a DrData model
        dr_data_model_json = {}
        dr_data_model_json['dr_standby_workspace_description'] = 'testString'
        dr_data_model_json['dr_standby_workspaces'] = [dr_standby_workspace_model]
        dr_data_model_json['dr_workspace_description'] = 'testString'
        dr_data_model_json['dr_workspaces'] = [dr_workspace_model]

        # Construct a model instance of DrData by calling from_dict on the json representation
        dr_data_model = DrData.from_dict(dr_data_model_json)
        assert dr_data_model != False

        # Construct a model instance of DrData by calling from_dict on the json representation
        dr_data_model_dict = DrData.from_dict(dr_data_model_json).__dict__
        dr_data_model2 = DrData(**dr_data_model_dict)

        # Verify the model instances are equivalent
        assert dr_data_model == dr_data_model2

        # Convert model instance back to dict and verify no loss of data
        dr_data_model_json2 = dr_data_model.to_dict()
        assert dr_data_model_json2 == dr_data_model_json


class TestModel_DrLocation:
    """
    Test Class for DrLocation
    """

    def test_dr_location_serialization(self):
        """
        Test serialization/deserialization for DrLocation
        """

        # Construct a json representation of a DrLocation model
        dr_location_model_json = {}
        dr_location_model_json['id'] = 'loc123'
        dr_location_model_json['name'] = 'US-East-1'

        # Construct a model instance of DrLocation by calling from_dict on the json representation
        dr_location_model = DrLocation.from_dict(dr_location_model_json)
        assert dr_location_model != False

        # Construct a model instance of DrLocation by calling from_dict on the json representation
        dr_location_model_dict = DrLocation.from_dict(dr_location_model_json).__dict__
        dr_location_model2 = DrLocation(**dr_location_model_dict)

        # Verify the model instances are equivalent
        assert dr_location_model == dr_location_model2

        # Convert model instance back to dict and verify no loss of data
        dr_location_model_json2 = dr_location_model.to_dict()
        assert dr_location_model_json2 == dr_location_model_json


class TestModel_Event:
    """
    Test Class for Event
    """

    def test_event_serialization(self):
        """
        Test serialization/deserialization for Event
        """

        # Construct dict forms of any model objects needed in order to build this model.

        event_user_model = {}  # EventUser
        event_user_model['email'] = 'abcuser@ibm.com'
        event_user_model['name'] = 'abcuser'
        event_user_model['user_id'] = 'IBMid-695000abc7E'

        # Construct a json representation of a Event model
        event_model_json = {}
        event_model_json['action'] = 'create'
        event_model_json['api_source'] = 'dr-automation-api'
        event_model_json['event_id'] = '1cecfe43-43cd-4b1b-86be-30c2d3d2a25f'
        event_model_json['level'] = 'info'
        event_model_json['message'] = 'Service Instance created successfully'
        event_model_json['message_data'] = {'anyKey': 'anyValue'}
        event_model_json['metadata'] = {'anyKey': 'anyValue'}
        event_model_json['resource'] = 'ProvisionID'
        event_model_json['time'] = '2025-06-23T07:12:49.840000Z'
        event_model_json['timestamp'] = '1750662769'
        event_model_json['user'] = event_user_model

        # Construct a model instance of Event by calling from_dict on the json representation
        event_model = Event.from_dict(event_model_json)
        assert event_model != False

        # Construct a model instance of Event by calling from_dict on the json representation
        event_model_dict = Event.from_dict(event_model_json).__dict__
        event_model2 = Event(**event_model_dict)

        # Verify the model instances are equivalent
        assert event_model == event_model2

        # Convert model instance back to dict and verify no loss of data
        event_model_json2 = event_model.to_dict()
        assert event_model_json2 == event_model_json


class TestModel_EventCollection:
    """
    Test Class for EventCollection
    """

    def test_event_collection_serialization(self):
        """
        Test serialization/deserialization for EventCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        event_user_model = {}  # EventUser
        event_user_model['email'] = 'abcuser@ibm.com'
        event_user_model['name'] = 'abcuser'
        event_user_model['user_id'] = 'IBMid-695000abc7E'

        event_model = {}  # Event
        event_model['action'] = 'create'
        event_model['api_source'] = 'dr-automation-api'
        event_model['event_id'] = '1cecfe43-43cd-4b1b-86be-30c2d3d2a25f'
        event_model['level'] = 'info'
        event_model['message'] = 'Service Instance created successfully'
        event_model['message_data'] = {'anyKey': 'anyValue'}
        event_model['metadata'] = {'anyKey': 'anyValue'}
        event_model['resource'] = 'ProvisionID'
        event_model['time'] = '2025-06-23T07:12:49.840000Z'
        event_model['timestamp'] = '1750662769'
        event_model['user'] = event_user_model

        # Construct a json representation of a EventCollection model
        event_collection_model_json = {}
        event_collection_model_json['events'] = [event_model]

        # Construct a model instance of EventCollection by calling from_dict on the json representation
        event_collection_model = EventCollection.from_dict(event_collection_model_json)
        assert event_collection_model != False

        # Construct a model instance of EventCollection by calling from_dict on the json representation
        event_collection_model_dict = EventCollection.from_dict(event_collection_model_json).__dict__
        event_collection_model2 = EventCollection(**event_collection_model_dict)

        # Verify the model instances are equivalent
        assert event_collection_model == event_collection_model2

        # Convert model instance back to dict and verify no loss of data
        event_collection_model_json2 = event_collection_model.to_dict()
        assert event_collection_model_json2 == event_collection_model_json


class TestModel_EventUser:
    """
    Test Class for EventUser
    """

    def test_event_user_serialization(self):
        """
        Test serialization/deserialization for EventUser
        """

        # Construct a json representation of a EventUser model
        event_user_model_json = {}
        event_user_model_json['email'] = 'abcuser@ibm.com'
        event_user_model_json['name'] = 'abcuser'
        event_user_model_json['user_id'] = 'IBMid-695000abc7E'

        # Construct a model instance of EventUser by calling from_dict on the json representation
        event_user_model = EventUser.from_dict(event_user_model_json)
        assert event_user_model != False

        # Construct a model instance of EventUser by calling from_dict on the json representation
        event_user_model_dict = EventUser.from_dict(event_user_model_json).__dict__
        event_user_model2 = EventUser(**event_user_model_dict)

        # Verify the model instances are equivalent
        assert event_user_model == event_user_model2

        # Convert model instance back to dict and verify no loss of data
        event_user_model_json2 = event_user_model.to_dict()
        assert event_user_model_json2 == event_user_model_json


class TestModel_GetDrLocationsResponse:
    """
    Test Class for GetDrLocationsResponse
    """

    def test_get_dr_locations_response_serialization(self):
        """
        Test serialization/deserialization for GetDrLocationsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dr_location_model = {}  # DrLocation
        dr_location_model['id'] = 'loc123'
        dr_location_model['name'] = 'US-East-1'

        # Construct a json representation of a GetDrLocationsResponse model
        get_dr_locations_response_model_json = {}
        get_dr_locations_response_model_json['dr_locations'] = [dr_location_model]

        # Construct a model instance of GetDrLocationsResponse by calling from_dict on the json representation
        get_dr_locations_response_model = GetDrLocationsResponse.from_dict(get_dr_locations_response_model_json)
        assert get_dr_locations_response_model != False

        # Construct a model instance of GetDrLocationsResponse by calling from_dict on the json representation
        get_dr_locations_response_model_dict = GetDrLocationsResponse.from_dict(
            get_dr_locations_response_model_json
        ).__dict__
        get_dr_locations_response_model2 = GetDrLocationsResponse(**get_dr_locations_response_model_dict)

        # Verify the model instances are equivalent
        assert get_dr_locations_response_model == get_dr_locations_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_dr_locations_response_model_json2 = get_dr_locations_response_model.to_dict()
        assert get_dr_locations_response_model_json2 == get_dr_locations_response_model_json


class TestModel_GetGRSLocationPairResponse:
    """
    Test Class for GetGRSLocationPairResponse
    """

    def test_get_grs_location_pair_response_serialization(self):
        """
        Test serialization/deserialization for GetGRSLocationPairResponse
        """

        # Construct a json representation of a GetGRSLocationPairResponse model
        get_grs_location_pair_response_model_json = {}
        get_grs_location_pair_response_model_json['location_pairs'] = {'key1': 'testString'}

        # Construct a model instance of GetGRSLocationPairResponse by calling from_dict on the json representation
        get_grs_location_pair_response_model = GetGRSLocationPairResponse.from_dict(
            get_grs_location_pair_response_model_json
        )
        assert get_grs_location_pair_response_model != False

        # Construct a model instance of GetGRSLocationPairResponse by calling from_dict on the json representation
        get_grs_location_pair_response_model_dict = GetGRSLocationPairResponse.from_dict(
            get_grs_location_pair_response_model_json
        ).__dict__
        get_grs_location_pair_response_model2 = GetGRSLocationPairResponse(**get_grs_location_pair_response_model_dict)

        # Verify the model instances are equivalent
        assert get_grs_location_pair_response_model == get_grs_location_pair_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_grs_location_pair_response_model_json2 = get_grs_location_pair_response_model.to_dict()
        assert get_grs_location_pair_response_model_json2 == get_grs_location_pair_response_model_json


class TestModel_LocationDr:
    """
    Test Class for LocationDr
    """

    def test_location_dr_serialization(self):
        """
        Test serialization/deserialization for LocationDr
        """

        # Construct a json representation of a LocationDr model
        location_dr_model_json = {}
        location_dr_model_json['region'] = 'lon06'
        location_dr_model_json['type'] = 'data-center'
        location_dr_model_json['url'] = 'https://lon.power-iaas.cloud.ibm.com'

        # Construct a model instance of LocationDr by calling from_dict on the json representation
        location_dr_model = LocationDr.from_dict(location_dr_model_json)
        assert location_dr_model != False

        # Construct a model instance of LocationDr by calling from_dict on the json representation
        location_dr_model_dict = LocationDr.from_dict(location_dr_model_json).__dict__
        location_dr_model2 = LocationDr(**location_dr_model_dict)

        # Verify the model instances are equivalent
        assert location_dr_model == location_dr_model2

        # Convert model instance back to dict and verify no loss of data
        location_dr_model_json2 = location_dr_model.to_dict()
        assert location_dr_model_json2 == location_dr_model_json


class TestModel_MachineTypesByWorkspace:
    """
    Test Class for MachineTypesByWorkspace
    """

    def test_machine_types_by_workspace_serialization(self):
        """
        Test serialization/deserialization for MachineTypesByWorkspace
        """

        # Construct a json representation of a MachineTypesByWorkspace model
        machine_types_by_workspace_model_json = {}
        machine_types_by_workspace_model_json['workspaces'] = {'key1': ['testString']}

        # Construct a model instance of MachineTypesByWorkspace by calling from_dict on the json representation
        machine_types_by_workspace_model = MachineTypesByWorkspace.from_dict(machine_types_by_workspace_model_json)
        assert machine_types_by_workspace_model != False

        # Construct a model instance of MachineTypesByWorkspace by calling from_dict on the json representation
        machine_types_by_workspace_model_dict = MachineTypesByWorkspace.from_dict(
            machine_types_by_workspace_model_json
        ).__dict__
        machine_types_by_workspace_model2 = MachineTypesByWorkspace(**machine_types_by_workspace_model_dict)

        # Verify the model instances are equivalent
        assert machine_types_by_workspace_model == machine_types_by_workspace_model2

        # Convert model instance back to dict and verify no loss of data
        machine_types_by_workspace_model_json2 = machine_types_by_workspace_model.to_dict()
        assert machine_types_by_workspace_model_json2 == machine_types_by_workspace_model_json


class TestModel_ManagedVmDetails:
    """
    Test Class for ManagedVmDetails
    """

    def test_managed_vm_details_serialization(self):
        """
        Test serialization/deserialization for ManagedVmDetails
        """

        # Construct a json representation of a ManagedVmDetails model
        managed_vm_details_model_json = {}
        managed_vm_details_model_json['core'] = '0.50'
        managed_vm_details_model_json['dr_average_time'] = '10'
        managed_vm_details_model_json['dr_region'] = 'nyc02'
        managed_vm_details_model_json['memory'] = '4'
        managed_vm_details_model_json['region'] = 'lon04'
        managed_vm_details_model_json['vm_name'] = 'example_vm'
        managed_vm_details_model_json['workgroup_name'] = 'Workgroup1'
        managed_vm_details_model_json['workspace_name'] = 'Workspace_dallas01'

        # Construct a model instance of ManagedVmDetails by calling from_dict on the json representation
        managed_vm_details_model = ManagedVmDetails.from_dict(managed_vm_details_model_json)
        assert managed_vm_details_model != False

        # Construct a model instance of ManagedVmDetails by calling from_dict on the json representation
        managed_vm_details_model_dict = ManagedVmDetails.from_dict(managed_vm_details_model_json).__dict__
        managed_vm_details_model2 = ManagedVmDetails(**managed_vm_details_model_dict)

        # Verify the model instances are equivalent
        assert managed_vm_details_model == managed_vm_details_model2

        # Convert model instance back to dict and verify no loss of data
        managed_vm_details_model_json2 = managed_vm_details_model.to_dict()
        assert managed_vm_details_model_json2 == managed_vm_details_model_json


class TestModel_ManagedVmMapResponse:
    """
    Test Class for ManagedVmMapResponse
    """

    def test_managed_vm_map_response_serialization(self):
        """
        Test serialization/deserialization for ManagedVmMapResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        managed_vm_details_model = {}  # ManagedVmDetails
        managed_vm_details_model['core'] = '0.50'
        managed_vm_details_model['dr_average_time'] = '10'
        managed_vm_details_model['dr_region'] = 'nyc02'
        managed_vm_details_model['memory'] = '4'
        managed_vm_details_model['region'] = 'nyc01'
        managed_vm_details_model['vm_name'] = 'example_vm'
        managed_vm_details_model['workgroup_name'] = 'Example_Workgroup'
        managed_vm_details_model['workspace_name'] = 'Example_Workspace'

        # Construct a json representation of a ManagedVmMapResponse model
        managed_vm_map_response_model_json = {}
        managed_vm_map_response_model_json['managed_vm_list'] = {'key1': managed_vm_details_model}

        # Construct a model instance of ManagedVmMapResponse by calling from_dict on the json representation
        managed_vm_map_response_model = ManagedVmMapResponse.from_dict(managed_vm_map_response_model_json)
        assert managed_vm_map_response_model != False

        # Construct a model instance of ManagedVmMapResponse by calling from_dict on the json representation
        managed_vm_map_response_model_dict = ManagedVmMapResponse.from_dict(managed_vm_map_response_model_json).__dict__
        managed_vm_map_response_model2 = ManagedVmMapResponse(**managed_vm_map_response_model_dict)

        # Verify the model instances are equivalent
        assert managed_vm_map_response_model == managed_vm_map_response_model2

        # Convert model instance back to dict and verify no loss of data
        managed_vm_map_response_model_json2 = managed_vm_map_response_model.to_dict()
        assert managed_vm_map_response_model_json2 == managed_vm_map_response_model_json


class TestModel_OrchestratorDetails:
    """
    Test Class for OrchestratorDetails
    """

    def test_orchestrator_details_serialization(self):
        """
        Test serialization/deserialization for OrchestratorDetails
        """

        # Construct a json representation of a OrchestratorDetails model
        orchestrator_details_model_json = {}
        orchestrator_details_model_json['last_updated_orchestrator_deployment_time'] = '2025-10-16T09:28:13.696000Z'
        orchestrator_details_model_json['last_updated_standby_orchestrator_deployment_time'] = (
            '2025-10-16T09:28:13.696000Z'
        )
        orchestrator_details_model_json['latest_orchestrator_time'] = '2025-10-16T09:28:13.696000Z'
        orchestrator_details_model_json['location_id'] = 'testString'
        orchestrator_details_model_json['mfa_enabled'] = 'testString'
        orchestrator_details_model_json['orch_ext_connectivity_status'] = 'testString'
        orchestrator_details_model_json['orch_standby_node_addition_status'] = 'testString'
        orchestrator_details_model_json['orchestrator_cluster_message'] = 'testString'
        orchestrator_details_model_json['orchestrator_config_status'] = 'testString'
        orchestrator_details_model_json['orchestrator_group_leader'] = 'testString'
        orchestrator_details_model_json['orchestrator_location_type'] = 'testString'
        orchestrator_details_model_json['orchestrator_name'] = 'testString'
        orchestrator_details_model_json['orchestrator_status'] = 'testString'
        orchestrator_details_model_json['orchestrator_workspace_name'] = 'testString'
        orchestrator_details_model_json['proxy_ip'] = 'testString'
        orchestrator_details_model_json['schematic_workspace_name'] = 'testString'
        orchestrator_details_model_json['schematic_workspace_status'] = 'testString'
        orchestrator_details_model_json['ssh_key_name'] = 'testString'
        orchestrator_details_model_json['standby_orchestrator_name'] = 'testString'
        orchestrator_details_model_json['standby_orchestrator_status'] = 'testString'
        orchestrator_details_model_json['standby_orchestrator_workspace_name'] = 'testString'
        orchestrator_details_model_json['transit_gateway_name'] = 'testString'
        orchestrator_details_model_json['vpc_name'] = 'testString'

        # Construct a model instance of OrchestratorDetails by calling from_dict on the json representation
        orchestrator_details_model = OrchestratorDetails.from_dict(orchestrator_details_model_json)
        assert orchestrator_details_model != False

        # Construct a model instance of OrchestratorDetails by calling from_dict on the json representation
        orchestrator_details_model_dict = OrchestratorDetails.from_dict(orchestrator_details_model_json).__dict__
        orchestrator_details_model2 = OrchestratorDetails(**orchestrator_details_model_dict)

        # Verify the model instances are equivalent
        assert orchestrator_details_model == orchestrator_details_model2

        # Convert model instance back to dict and verify no loss of data
        orchestrator_details_model_json2 = orchestrator_details_model.to_dict()
        assert orchestrator_details_model_json2 == orchestrator_details_model_json


class TestModel_ServiceDetails:
    """
    Test Class for ServiceDetails
    """

    def test_service_details_serialization(self):
        """
        Test serialization/deserialization for ServiceDetails
        """

        # Construct a json representation of a ServiceDetails model
        service_details_model_json = {}
        service_details_model_json['crn'] = 'testString'
        service_details_model_json['deployment_name'] = 'testString'
        service_details_model_json['description'] = 'testString'
        service_details_model_json['orchestrator_ha'] = True
        service_details_model_json['plan_name'] = 'testString'
        service_details_model_json['primary_ip_address'] = 'testString'
        service_details_model_json['primary_orchestrator_dashboard_url'] = 'testString'
        service_details_model_json['recovery_location'] = 'testString'
        service_details_model_json['resource_group'] = 'testString'
        service_details_model_json['standby_description'] = 'testString'
        service_details_model_json['standby_ip_address'] = 'testString'
        service_details_model_json['standby_orchestrator_dashboard_url'] = 'testString'
        service_details_model_json['standby_status'] = 'testString'
        service_details_model_json['status'] = 'testString'

        # Construct a model instance of ServiceDetails by calling from_dict on the json representation
        service_details_model = ServiceDetails.from_dict(service_details_model_json)
        assert service_details_model != False

        # Construct a model instance of ServiceDetails by calling from_dict on the json representation
        service_details_model_dict = ServiceDetails.from_dict(service_details_model_json).__dict__
        service_details_model2 = ServiceDetails(**service_details_model_dict)

        # Verify the model instances are equivalent
        assert service_details_model == service_details_model2

        # Convert model instance back to dict and verify no loss of data
        service_details_model_json2 = service_details_model.to_dict()
        assert service_details_model_json2 == service_details_model_json


class TestModel_ServiceInstanceManageDR:
    """
    Test Class for ServiceInstanceManageDR
    """

    def test_service_instance_manage_dr_serialization(self):
        """
        Test serialization/deserialization for ServiceInstanceManageDR
        """

        # Construct a json representation of a ServiceInstanceManageDR model
        service_instance_manage_dr_model_json = {}
        service_instance_manage_dr_model_json['dashboard_url'] = (
            'https://power-dra.test.cloud.ibm.com/power-dra-ui?instance_id=crn:v1:bluemix:public:power-dr-automation:us-south:a/fe3c2ccd058e407c81e1dba2b5c0e0d6:e3d09875-bbf8-4d8a-b52c-abefb67a53c5::'
        )
        service_instance_manage_dr_model_json['id'] = (
            'crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::'
        )

        # Construct a model instance of ServiceInstanceManageDR by calling from_dict on the json representation
        service_instance_manage_dr_model = ServiceInstanceManageDR.from_dict(service_instance_manage_dr_model_json)
        assert service_instance_manage_dr_model != False

        # Construct a model instance of ServiceInstanceManageDR by calling from_dict on the json representation
        service_instance_manage_dr_model_dict = ServiceInstanceManageDR.from_dict(
            service_instance_manage_dr_model_json
        ).__dict__
        service_instance_manage_dr_model2 = ServiceInstanceManageDR(**service_instance_manage_dr_model_dict)

        # Verify the model instances are equivalent
        assert service_instance_manage_dr_model == service_instance_manage_dr_model2

        # Convert model instance back to dict and verify no loss of data
        service_instance_manage_dr_model_json2 = service_instance_manage_dr_model.to_dict()
        assert service_instance_manage_dr_model_json2 == service_instance_manage_dr_model_json


class TestModel_ServiceInstanceStatus:
    """
    Test Class for ServiceInstanceStatus
    """

    def test_service_instance_status_serialization(self):
        """
        Test serialization/deserialization for ServiceInstanceStatus
        """

        # Construct a json representation of a ServiceInstanceStatus model
        service_instance_status_model_json = {}
        service_instance_status_model_json['crn'] = (
            'crn:v1:staging:public:power-dr-automation:global:a/2c5d7270091f495795350e9adfa8399c:86e0c9a9-80f4-4fcf-88a0-07643de01bb8::'
        )
        service_instance_status_model_json['deployment_name'] = 'dr-deployment-instance-1'
        service_instance_status_model_json['last_updated_orchestrator_deployment_time'] = '2025-10-16T09:28:13.696000Z'
        service_instance_status_model_json['last_updated_standby_orchestrator_deployment_time'] = (
            '2025-10-16T09:28:13.696000Z'
        )
        service_instance_status_model_json['mfa_enabled'] = 'true'
        service_instance_status_model_json['orch_ext_connectivity_status'] = 'Connected'
        service_instance_status_model_json['orch_standby_node_addtion_status'] = 'Completed'
        service_instance_status_model_json['orchestrator_cluster_message'] = 'Cluster healthy'
        service_instance_status_model_json['orchestrator_config_status'] = 'Configured'
        service_instance_status_model_json['orchestrator_ha'] = True
        service_instance_status_model_json['plan_name'] = 'DR Automation Private Plan'
        service_instance_status_model_json['primary_description'] = '2/5: Creating primary orchestrator VM.'
        service_instance_status_model_json['primary_ip_address'] = '192.168.1.10'
        service_instance_status_model_json['primary_orchestrator_status'] = 'orchestrator-VM-creation-in-progress'
        service_instance_status_model_json['recovery_location'] = 'us-east'
        service_instance_status_model_json['resource_group'] = 'Default'
        service_instance_status_model_json['standby_description'] = (
            '1/4: Service instance is downloading orchestrator image for standby VM creation.'
        )
        service_instance_status_model_json['standby_ip_address'] = '192.168.1.11'
        service_instance_status_model_json['standby_status'] = 'downloading-orchestrator-image'
        service_instance_status_model_json['status'] = 'Running'

        # Construct a model instance of ServiceInstanceStatus by calling from_dict on the json representation
        service_instance_status_model = ServiceInstanceStatus.from_dict(service_instance_status_model_json)
        assert service_instance_status_model != False

        # Construct a model instance of ServiceInstanceStatus by calling from_dict on the json representation
        service_instance_status_model_dict = ServiceInstanceStatus.from_dict(
            service_instance_status_model_json
        ).__dict__
        service_instance_status_model2 = ServiceInstanceStatus(**service_instance_status_model_dict)

        # Verify the model instances are equivalent
        assert service_instance_status_model == service_instance_status_model2

        # Convert model instance back to dict and verify no loss of data
        service_instance_status_model_json2 = service_instance_status_model.to_dict()
        assert service_instance_status_model_json2 == service_instance_status_model_json


class TestModel_ValidationKeyResponse:
    """
    Test Class for ValidationKeyResponse
    """

    def test_validation_key_response_serialization(self):
        """
        Test serialization/deserialization for ValidationKeyResponse
        """

        # Construct a json representation of a ValidationKeyResponse model
        validation_key_response_model_json = {}
        validation_key_response_model_json['description'] = 'Key is valid.'
        validation_key_response_model_json['id'] = (
            'crn:v1:staging:public:power-dr-automation:global:a/a123456fb04ceebfb4a9fd38c22334455:123456d3-1122-3344-b67d-4389b44b7bf9::'
        )
        validation_key_response_model_json['status'] = 'Active'

        # Construct a model instance of ValidationKeyResponse by calling from_dict on the json representation
        validation_key_response_model = ValidationKeyResponse.from_dict(validation_key_response_model_json)
        assert validation_key_response_model != False

        # Construct a model instance of ValidationKeyResponse by calling from_dict on the json representation
        validation_key_response_model_dict = ValidationKeyResponse.from_dict(
            validation_key_response_model_json
        ).__dict__
        validation_key_response_model2 = ValidationKeyResponse(**validation_key_response_model_dict)

        # Verify the model instances are equivalent
        assert validation_key_response_model == validation_key_response_model2

        # Convert model instance back to dict and verify no loss of data
        validation_key_response_model_json2 = validation_key_response_model.to_dict()
        assert validation_key_response_model_json2 == validation_key_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
