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
Examples for DrAutomationServiceV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_dra_python_sdk.dr_automation_service_v1 import *

#
# This file provides an example of how to use the DrAutomation Service service.
#
# The following configuration properties are assumed to be defined:
# DR_AUTOMATION_SERVICE_URL=<service base url>
# DR_AUTOMATION_SERVICE_AUTH_TYPE=iam
# DR_AUTOMATION_SERVICE_APIKEY=<IAM apikey>
# DR_AUTOMATION_SERVICE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'dr_automation_service_v1.env'

dr_automation_service_service = None

config = None


##############################################################################
# Start of Examples for Service: DrAutomationServiceV1
##############################################################################
# region
class TestDrAutomationServiceV1Examples:
    """
    Example Test Class for DrAutomationServiceV1
    """

    @classmethod
    def setup_class(cls):
        global dr_automation_service_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            dr_automation_service_service = DrAutomationServiceV1.new_instance(
            )

            # end-common
            assert dr_automation_service_service is not None

            # Load the configuration
            global config
            config = read_external_sources(DrAutomationServiceV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_update_apikey_example(self):
        """
        update_apikey request example
        """
        try:
            print('\nupdate_apikey() result:')

            # begin-update_apikey

            response = dr_automation_service_service.update_apikey(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
                api_key='adfadfdsafsdfdsf',
            )
            validation_key_response = response.get_result()

            print(json.dumps(validation_key_response, indent=2))

            # end-update_apikey

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_dr_grs_location_pair_example(self):
        """
        get_dr_grs_location_pair request example
        """
        try:
            print('\nget_dr_grs_location_pair() result:')

            # begin-get_dr_grs_location_pair

            response = dr_automation_service_service.get_dr_grs_location_pair(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            )
            get_grs_location_pair_response = response.get_result()

            print(json.dumps(get_grs_location_pair_response, indent=2))

            # end-get_dr_grs_location_pair

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_dr_locations_example(self):
        """
        get_dr_locations request example
        """
        try:
            print('\nget_dr_locations() result:')

            # begin-get_dr_locations

            response = dr_automation_service_service.get_dr_locations(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            )
            get_dr_locations_response = response.get_result()

            print(json.dumps(get_dr_locations_response, indent=2))

            # end-get_dr_locations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_dr_managed_vm_example(self):
        """
        get_dr_managed_vm request example
        """
        try:
            print('\nget_dr_managed_vm() result:')

            # begin-get_dr_managed_vm

            response = dr_automation_service_service.get_dr_managed_vm(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            )
            managed_vm_map_response = response.get_result()

            print(json.dumps(managed_vm_map_response, indent=2))

            # end-get_dr_managed_vm

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_dr_summary_example(self):
        """
        get_dr_summary request example
        """
        try:
            print('\nget_dr_summary() result:')

            # begin-get_dr_summary

            response = dr_automation_service_service.get_dr_summary(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            )
            dr_automation_get_summary_response = response.get_result()

            print(json.dumps(dr_automation_get_summary_response, indent=2))

            # end-get_dr_summary

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_machine_type_example(self):
        """
        get_machine_type request example
        """
        try:
            print('\nget_machine_type() result:')

            # begin-get_machine_type

            response = dr_automation_service_service.get_machine_type(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
                primary_workspace_name='Test-workspace-wdc06',
                standby_workspace_name='Test-workspace-wdc07',
            )
            machine_types_by_workspace = response.get_result()

            print(json.dumps(machine_types_by_workspace, indent=2))

            # end-get_machine_type

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_powervs_workspaces_example(self):
        """
        get_powervs_workspaces request example
        """
        try:
            print('\nget_powervs_workspaces() result:')

            # begin-get_powervs_workspaces

            response = dr_automation_service_service.get_powervs_workspaces(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
                location_id='testString',
            )
            dr_data = response.get_result()

            print(json.dumps(dr_data, indent=2))

            # end-get_powervs_workspaces

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_manage_dr_example(self):
        """
        create_manage_dr request example
        """
        try:
            print('\ncreate_manage_dr() result:')

            # begin-create_manage_dr

            response = dr_automation_service_service.create_manage_dr(
                # Required parameters
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
                location_id='dal10',
                machine_type='s922',
                orchestrator_location_type='off-premises',
                orchestrator_name='drautomationprimarybypyh1105',
                orchestrator_password='EverytimeNewPassword@1',
                orchestrator_workspace_id='75cbf05b-78f6-406e-afe7-a904f646d798',
                
                # Optional parameters (but commonly used)
                api_key='apikey should pass',
                orchestrator_ha=True,
                tier='tier1',
                ssh_key_name='vijaykey',
                
                # Standby fields (only for HA)
                standby_orchestrator_name='drautomationstandbypyh1105',
                standby_orchestrator_workspace_id='71027b79-0e31-44f6-a499-63eca1a66feb',
                standby_machine_type='s922',
                standby_tier='tier1',
                
                # MFA fields (optional)
                client_id='123abcd-97d2-4b14-bf62-8eaecc67a122',
                client_secret='abcdefgT5rS8wK6qR9dD7vF1hU4sA3bE2jG0pL9oX7yC',
                tenant_name='xxx.ibm.com',
            )

            service_instance_manage_dr = response.get_result()

            print(json.dumps(service_instance_manage_dr, indent=2))

            # end-create_manage_dr

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_last_operation_example(self):
        """
        get_last_operation request example
        """
        try:
            print('\nget_last_operation() result:')

            # begin-get_last_operation

            response = dr_automation_service_service.get_last_operation(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9',
            )
            service_instance_status = response.get_result()

            print(json.dumps(service_instance_status, indent=2))

            # end-get_last_operation

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_events_example(self):
        """
        list_events request example
        """
        try:
            print('\nlist_events() result:')

            # begin-list_events

            response = dr_automation_service_service.list_events(
                instance_id='df6b8951-5442-44e9-a2a4-399923e5678j29d',
                from_time='2025-12-02T03:10:00Z',
                to_time='2025-12-09T23:59:59Z',
            )
            event_collection = response.get_result()

            print(json.dumps(event_collection, indent=2))

            # end-list_events

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_event_example(self):
        """
        get_event request example
        """
        try:
            print('\nget_event() result:')

            # begin-get_event

            response = dr_automation_service_service.get_event(
                instance_id='df6b8951-5442-44e9-a2a4-399923e5678j29d',
                event_id='df6b8951-5442-44e9-a2a4-399923e5678j29d-1764680961045247391',
            )
            event = response.get_result()

            print(json.dumps(event, indent=2))

            # end-get_event

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: DrAutomationServiceV1
##############################################################################
