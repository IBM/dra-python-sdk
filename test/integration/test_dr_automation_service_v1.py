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
Integration Tests for DrAutomationServiceV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_dra_python_sdk.dr_automation_service_v1 import *

# Config file name
config_file = 'dr_automation_service_v1.env'


class TestDrAutomationServiceV1:
    """
    Integration Test Class for DrAutomationServiceV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.dr_automation_service_service = DrAutomationServiceV1.new_instance(
            )
            assert cls.dr_automation_service_service is not None

            cls.config = read_external_sources(DrAutomationServiceV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.dr_automation_service_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_update_apikey(self):
        response = self.dr_automation_service_service.update_apikey(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            api_key='adfadfdsafsdfdsf',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        validation_key_response = response.get_result()
        assert validation_key_response is not None

    @needscredentials
    def test_get_dr_grs_location_pair(self):
        response = self.dr_automation_service_service.get_dr_grs_location_pair(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        get_grs_location_pair_response = response.get_result()
        assert get_grs_location_pair_response is not None

    @needscredentials
    def test_get_dr_locations(self):
        response = self.dr_automation_service_service.get_dr_locations(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        get_dr_locations_response = response.get_result()
        assert get_dr_locations_response is not None

    @needscredentials
    def test_get_dr_managed_vm(self):
        response = self.dr_automation_service_service.get_dr_managed_vm(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        managed_vm_map_response = response.get_result()
        assert managed_vm_map_response is not None

    @needscredentials
    def test_get_dr_summary(self):
        response = self.dr_automation_service_service.get_dr_summary(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        dr_automation_get_summary_response = response.get_result()
        assert dr_automation_get_summary_response is not None

    @needscredentials
    def test_get_machine_type(self):
        response = self.dr_automation_service_service.get_machine_type(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            primary_workspace_name='Test-workspace-wdc06',
            accept_language='testString',
            standby_workspace_name='Test-workspace-wdc07',
        )

        assert response.get_status_code() == 200
        machine_types_by_workspace = response.get_result()
        assert machine_types_by_workspace is not None

    @needscredentials
    def test_get_powervs_workspaces(self):
        response = self.dr_automation_service_service.get_powervs_workspaces(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            location_id='testString',
        )

        assert response.get_status_code() == 200
        dr_data = response.get_result()
        assert dr_data is not None

    @needscredentials
    def test_create_manage_dr(self):
        response = self.dr_automation_service_service.create_manage_dr(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            location_id='dal10',
            machine_type='bx2-4x16',
            orchestrator_location_type='off-premises',
            orchestrator_name='adminUser',
            orchestrator_password='testString',
            orchestrator_workspace_id='orch-workspace-01',
            api_key='testString',
            client_id='abcd-97d2-1234-bf62-8eaecc67a1234',
            client_secret='abcd1234xM1y123wK6qR9123456789bE2jG0pabcdefgh',
            guid='123e4567-e89b-12d3-a456-426614174000',
            orchestrator_ha=True,
            proxy_ip='10.40.30.10:8888',
            region_id='us-south',
            resource_instance='crn:v1:bluemix:public:resource-controller::res123',
            secret='testString',
            secret_group='default-secret-group',
            ssh_key_name='my-ssh-key',
            standby_machine_type='bx2-8x32',
            standby_orchestrator_name='standbyAdmin',
            standby_orchestrator_workspace_id='orch-standby-02',
            standby_tier='Premium',
            tenant_name='xxx.ibm.com',
            tier='Standard',
            stand_by_redeploy='testString',
            accept_language='testString',
            accepts_incomplete=True,
        )

        assert response.get_status_code() == 200
        service_instance_manage_dr = response.get_result()
        assert service_instance_manage_dr is not None

    @needscredentials
    def test_get_last_operation(self):
        response = self.dr_automation_service_service.get_last_operation(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        service_instance_status = response.get_result()
        assert service_instance_status is not None

    @needscredentials
    def test_list_events(self):
        response = self.dr_automation_service_service.list_events(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            time='2025-06-19T23:59:59Z',
            from_time='2025-06-19T00:00:00Z',
            to_time='2025-06-19T23:59:59Z',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        event_collection = response.get_result()
        assert event_collection is not None

    @needscredentials
    def test_get_event(self):
        response = self.dr_automation_service_service.get_event(
            instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            event_id='00116b2a-9326-4024-839e-fb5364b76898',
            accept_language='testString',
        )

        assert response.get_status_code() == 200
        event = response.get_result()
        assert event is not None
