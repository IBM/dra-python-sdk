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
Integration Tests for PowerhaAutomationServiceV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_dra_python_sdk.powerha_automation_service_v1 import *

# Config file name
config_file = 'powerha_automation_service_v1.env'


class TestPowerhaAutomationServiceV1:
    """
    Integration Test Class for PowerhaAutomationServiceV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.powerha_automation_service_service = PowerhaAutomationServiceV1.new_instance()
            assert cls.powerha_automation_service_service is not None

            cls.config = read_external_sources(PowerhaAutomationServiceV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.powerha_automation_service_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_api_key(self):
        response = self.powerha_automation_service_service.create_api_key(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            api_key='adfadfdsafsdfdsf',
            accept_language='en-US',
        )

        assert response.get_status_code() == 201
        api_key_response = response.get_result()
        assert api_key_response is not None

    @needscredentials
    def test_get_cluster_node(self):
        response = self.powerha_automation_service_service.get_cluster_node(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        cluster_node_response = response.get_result()
        assert cluster_node_response is not None

    @needscredentials
    def test_create_cluster_node(self):
        response = self.powerha_automation_service_service.create_cluster_node(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            primary_cluster_nodes=['ede4c36e-002c-48da-992e-6039d230c478'],
            secondary_cluster_nodes=['ede4c36e-1234-48da-992e-6039d230c478'],
            accept_language='en-US',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 201
        cluster_node_response = response.get_result()
        assert cluster_node_response is not None

    @needscredentials
    def test_get_powervs_workspace(self):
        response = self.powerha_automation_service_service.get_powervs_workspace(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            location_id='us-south',
            accept_language='en-US',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        pha_workspaces_region_response = response.get_result()
        assert pha_workspaces_region_response is not None

    @needscredentials
    def test_get_pha_last_operation(self):
        response = self.powerha_automation_service_service.get_pha_last_operation(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            accept_language='en-US',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        service_instance_pha_status = response.get_result()
        assert service_instance_pha_status is not None

    @needscredentials
    def test_get_pha_deployment(self):
        response = self.powerha_automation_service_service.get_pha_deployment(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        pha_deployment_response = response.get_result()
        assert pha_deployment_response is not None

    @needscredentials
    def test_create_pha_deployment(self):
        response = self.powerha_automation_service_service.create_pha_deployment(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            location_id='loc-us-south-01',
            primary_workspace='workspace-primary',
            api_key='123635364646fghrtfhbfdhb',
            cluster_type='standard',
            configure_type='automatic',
            primary_cluster_nodes=['ede4c36e-002c-48da-992e-6039d230c478'],
            standby_cluster_nodes=['843a8e1f-05bb-4164-8c73-de39e016c2b4'],
            primary_location='us-south',
            secondary_location='us-east',
            secondary_workspace='workspace-secondary',
            accept_language='en-US',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 201
        pha_deployment_response = response.get_result()
        assert pha_deployment_response is not None

    @needscredentials
    def test_get_supported_location(self):
        response = self.powerha_automation_service_service.get_supported_location(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        pha_supported_locations_response = response.get_result()
        assert pha_supported_locations_response is not None

    @needscredentials
    def test_get_pha_agent_file_download_job_status(self):
        response = self.powerha_automation_service_service.get_pha_agent_file_download_job_status(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            pha_job_id='4235r23r5vdfdf-2323',
            accept_language='en-US',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        pha_agent_job_status_response = response.get_result()
        assert pha_agent_job_status_response is not None

    @needscredentials
    def test_download_pha_agent_file(self):
        response = self.powerha_automation_service_service.download_pha_agent_file(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            accept_language='en-US',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_delete_cluster_node(self):
        response = self.powerha_automation_service_service.delete_cluster_node(
            pha_instance_id='8eefautr-4c02-0009-0086-8bd4d8cf61b6',
            vm_id='r006-2f3b3ab9-2149-49cc-83a1-30a5d93d59b2',
            if_none_match='abcdef',
        )

        assert response.get_status_code() == 200
        cluster_node_response = response.get_result()
        assert cluster_node_response is not None
