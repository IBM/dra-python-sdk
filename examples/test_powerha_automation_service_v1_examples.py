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
Examples for PowerhaAutomationServiceV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_dra_python_sdk.powerha_automation_service_v1 import *

#
# This file provides an example of how to use the PowerhaAutomation Service service.
#
# The following configuration properties are assumed to be defined:
# POWERHA_AUTOMATION_SERVICE_URL=<service base url>
# POWERHA_AUTOMATION_SERVICE_AUTH_TYPE=iam
# POWERHA_AUTOMATION_SERVICE_APIKEY=<IAM apikey>
# POWERHA_AUTOMATION_SERVICE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'powerha_automation_service_v1.env'

powerha_automation_service_service = None

config = None


##############################################################################
# Start of Examples for Service: PowerhaAutomationServiceV1
##############################################################################
# region
class TestPowerhaAutomationServiceV1Examples:
    """
    Example Test Class for PowerhaAutomationServiceV1
    """

    @classmethod
    def setup_class(cls):
        global powerha_automation_service_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            powerha_automation_service_service = PowerhaAutomationServiceV1.new_instance()

            # end-common
            assert powerha_automation_service_service is not None

            # Load the configuration
            global config
            config = read_external_sources(PowerhaAutomationServiceV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_api_key_example(self):
        """
        create_api_key request example
        """
        try:
            print('\ncreate_api_key() result:')

            # begin-create_api_key

            response = powerha_automation_service_service.create_api_key(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                accept_language='en-US',
            )
            api_key_response = response.get_result()

            print(json.dumps(api_key_response, indent=2))

            # end-create_api_key

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_cluster_node_example(self):
        """
        get_cluster_node request example
        """
        try:
            print('\nget_cluster_node() result:')

            # begin-get_cluster_node

            response = powerha_automation_service_service.get_cluster_node(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                if_none_match='abcdef',
            )
            cluster_node_response = response.get_result()

            print(json.dumps(cluster_node_response, indent=2))

            # end-get_cluster_node

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_cluster_node_example(self):
        """
        create_cluster_node request example
        """
        try:
            print('\ncreate_cluster_node() result:')

            # begin-create_cluster_node

            response = powerha_automation_service_service.create_cluster_node(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                primary_cluster_nodes=['ede4c36e-002c-48da-992e-6039d230c478'],
                accept_language='en-US',
                if_none_match='abcdef',
            )
            cluster_node_response = response.get_result()

            print(json.dumps(cluster_node_response, indent=2))

            # end-create_cluster_node

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_powervs_workspace_example(self):
        """
        get_powervs_workspace request example
        """
        try:
            print('\nget_powervs_workspace() result:')

            # begin-get_powervs_workspace

            response = powerha_automation_service_service.get_powervs_workspace(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                location_id='us-south',
                accept_language='en-US',
                if_none_match='abcdef',
            )
            pha_workspaces_region_response = response.get_result()

            print(json.dumps(pha_workspaces_region_response, indent=2))

            # end-get_powervs_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_pha_last_operation_example(self):
        """
        get_pha_last_operation request example
        """
        try:
            print('\nget_pha_last_operation() result:')

            # begin-get_pha_last_operation

            response = powerha_automation_service_service.get_pha_last_operation(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                accept_language='en-US',
                if_none_match='abcdef',
            )
            service_instance_pha_status = response.get_result()

            print(json.dumps(service_instance_pha_status, indent=2))

            # end-get_pha_last_operation

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_pha_deployment_example(self):
        """
        get_pha_deployment request example
        """
        try:
            print('\nget_pha_deployment() result:')

            # begin-get_pha_deployment

            response = powerha_automation_service_service.get_pha_deployment(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                if_none_match='abcdef',
            )
            pha_deployment_response = response.get_result()

            print(json.dumps(pha_deployment_response, indent=2))

            # end-get_pha_deployment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_pha_deployment_example(self):
        """
        create_pha_deployment request example
        """
        try:
            print('\ncreate_pha_deployment() result:')

            # begin-create_pha_deployment

            response = powerha_automation_service_service.create_pha_deployment(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                location_id='loc-us-south-01',
                primary_workspace='workspace-primary',
                accept_language='en-US',
                if_none_match='abcdef',
            )
            pha_deployment_response = response.get_result()

            print(json.dumps(pha_deployment_response, indent=2))

            # end-create_pha_deployment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_supported_location_example(self):
        """
        get_supported_location request example
        """
        try:
            print('\nget_supported_location() result:')

            # begin-get_supported_location

            response = powerha_automation_service_service.get_supported_location(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                if_none_match='abcdef',
            )
            pha_supported_locations_response = response.get_result()

            print(json.dumps(pha_supported_locations_response, indent=2))

            # end-get_supported_location

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_pha_agent_file_download_job_status_example(self):
        """
        get_pha_agent_file_download_job_status request example
        """
        try:
            print('\nget_pha_agent_file_download_job_status() result:')

            # begin-get_pha_agent_file_download_job_status

            response = powerha_automation_service_service.get_pha_agent_file_download_job_status(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                pha_job_id='4235r23r5vdfdf-2323',
                accept_language='en-US',
                if_none_match='abcdef',
            )
            pha_agent_job_status_response = response.get_result()

            print(json.dumps(pha_agent_job_status_response, indent=2))

            # end-get_pha_agent_file_download_job_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_download_pha_agent_file_example(self):
        """
        download_pha_agent_file request example
        """
        try:
            print('\ndownload_pha_agent_file() result:')

            # begin-download_pha_agent_file

            response = powerha_automation_service_service.download_pha_agent_file(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                accept_language='en-US',
                if_none_match='abcdef',
            )
            result = response.get_result()

            with open('/tmp/result.out', 'wb') as fp:
                fp.write(result.content)

            # end-download_pha_agent_file

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_cluster_node_example(self):
        """
        delete_cluster_node request example
        """
        try:
            print('\ndelete_cluster_node() result:')

            # begin-delete_cluster_node

            response = powerha_automation_service_service.delete_cluster_node(
                pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
                vm_id='r006-2f3b3ab9-2149-49cc-83a1-30a5d93d59b2',
                if_none_match='abcdef',
            )
            cluster_node_response = response.get_result()

            print(json.dumps(cluster_node_response, indent=2))

            # end-delete_cluster_node

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: PowerhaAutomationServiceV1
##############################################################################
