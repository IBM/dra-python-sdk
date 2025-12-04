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
from dra_python_sdk.dr_automation_service_v1 import *

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
    def test_create_manage_dr_ha_with_sshkey_example(self):
        """
        create_manage_dr_ha_with_sshkey request example
        """
        try:
            print('\ncreate_manage_dr_ha_with_sshkey:')

            # begin-create_manage_dr_ha_with_sshkey

            response = dr_automation_service_service.create_manage_dr(
                instance_id='123456d3-1122-3344-b67d-4389b44b7bf9pyha1',
                stand_by_redeploy='true',
                
                orchestrator_ha=True,
                orchestrator_location_type='off-premises',
                location_id='dal10',
                orchestrator_workspace_id='75cbf05b-78f6-406e-afe7-a904f646d798',
                orchestrator_name='drautomationprimarybypyh1105',
                orchestrator_password='abcdefgh@123456',
                machine_type='s922',
                tier='tier1',
                ssh_key_name='vijaykey',
                api_key='apikey should pass',
                # Standby fields (only for HA)
                standby_orchestrator_name='drautomationstandbypyh1105',
                standby_orchestrator_workspace_id='71027b79-0e31-44f6-a499-63eca1a66feb',
                standby_machine_type='s922',
                standby_tier='tier1',

                # MFA fields
                client_id='123abcd-abcd-4b14-bf62-123456abcdef',
                client_secret='abcdefgh123456abcdefg123456',
                tenant_name='xxx.ibm.com'
            )
            service_instance_manage_dr = response.get_result()

            print(json.dumps(service_instance_manage_dr, indent=2))

            # end-create_manage_dr_ha_with_sshkey

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_manage_dr_ha_with_secrets_example(self):
        """
        begin_create_manage_dr_ha_with_secrets request example
        """
        try:
            print('\ncreate_manage_dr_ha_with_secrets')

            # begin-create_manage_dr_ha_with_secrets

            response = dr_automation_service_service.create_manage_dr(
                instance_id='050ebe3b-13f4-4db8-8ece-501a3c13be80mh3',
                stand_by_redeploy='false',
                
                # Body parameters
                orchestrator_ha=True,
                orchestrator_location_type='off-premises',
                location_id='dal10',
                orchestrator_workspace_id='75cbf05b-78f6-406e-afe7-a904f646d798',
                orchestrator_name='drautomationprimarymh3',
                orchestrator_password='abcdefgh@123456',
                machine_type='s922',
                tier='tier1',
                guid='397dc20d-9f66-46dc-a750-d15392872023',
                secret_group='12345-1234-1234-1234-1234abcd',
                secret='abcd-1234-abcd-1234-1234abcd',
                region_id='us-south',
                api_key='apikey is required',
                # Standby fields (only for HA)
                standby_orchestrator_name='drautomationstandbymh3',
                standby_orchestrator_workspace_id='71027b79-0e31-44f6-a499-63eca1a66feb',
                standby_machine_type='s922',
                standby_tier='tier1',

                # MFA fields
                client_id='123abcd-abcd-4b14-bf62-123456abcdef',
                client_secret='abcdefgh123456abcdefg123456',
                tenant_name='xxx.ibm.com'
            )

            service_instance_manage_dr = response.get_result()

            print(json.dumps(service_instance_manage_dr, indent=2))

            # end-create_manage_dr_ha_with_secrets

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_manage_dr_nonha_with_sshkey_example(self):
        """
        create_manage_dr_nonha_with_sshkey request example
        """
        try:
            print('\ncreate_manage_dr_nonha_with_sshkey:')

            # begin-create_manage_dr_nonha_with_sshkey

            response = dr_automation_service_service.create_manage_dr(
                instance_id='050ebe3b-13f4-4db8-8ece-501a3c13be80mnh5',
                stand_by_redeploy='false',
                
                # Body parameters
                orchestrator_ha=False,
                orchestrator_location_type='off-premises',
                location_id='dal10',
                orchestrator_workspace_id='75cbf05b-78f6-406e-afe7-a904f646d798',
                orchestrator_name='drautomationprimarymnh5',
                orchestrator_password='abcdefgh@123456',
                machine_type='s922',
                tier='tier1',
                ssh_key_name='vijaykey',
                api_key='apikey is required',
                 # MFA fields
                client_id='123abcd-abcd-4b14-bf62-123456abcdef',
                client_secret='abcdefgh123456abcdefg123456',
                tenant_name='xxx.ibm.com'
            )

            service_instance_manage_dr = response.get_result()

            print(json.dumps(service_instance_manage_dr, indent=2))

            # end-create_manage_dr_nonha_with_sshkey

        except ApiException as e:
            pytest.fail(str(e))


    @needscredentials
    def test_create_manage_dr_nonha_with_secrets_example(self):
        """
        create_manage_dr_nonha_with_secrets request example
        """
        try:
            print('\ncreate_manage_dr_nonha_with_secrets:')

            # begin-create_manage_dr_nonha_with_secrets

            response = dr_automation_service_service.create_manage_dr(
                instance_id='050ebe3b-13f4-4db8-8ece-501a3c13be80mnh7',
                stand_by_redeploy='false',
                
                # Body parameters
                orchestrator_ha=False,
                orchestrator_location_type='off-premises',
                location_id='dal10',
                orchestrator_workspace_id='75cbf05b-78f6-406e-afe7-a904f646d798',
                orchestrator_name='drautomationprimarymnh7',
                orchestrator_password='abcdefgh@123456',
                machine_type='s922',
                tier='tier1',
                guid='397dc20d-9f66-46dc-a750-d15392872023',
                secret_group='12345-1234-1234-1234-1234abcd',
                secret='abcd-1234-abcd-1234-1234abcd',
                region_id='us-south',
                api_key='apikey is required',
                 # MFA fields
                client_id='123abcd-abcd-4b14-bf62-123456abcdef',
                client_secret='abcdefgh123456abcdefg123456',
                tenant_name='xxx.ibm.com'
            )

        
            service_instance_manage_dr = response.get_result()

            print(json.dumps(service_instance_manage_dr, indent=2))

            # end-create_manage_dr_nonha_with_secrets

        except ApiException as e:
            pytest.fail(str(e))


##############################################################################
# End of Examples for Service: DrAutomationServiceV1
##############################################################################
