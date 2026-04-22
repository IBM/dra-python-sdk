import json
import pytest
import time
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibm_platform_services import GlobalCatalogV1, ResourceControllerV2

#
# Example for Powerha automation provisioning and deprovisioning a service instance
#


class TestResourceControllerV2Examples:
    """
    Example Test Class for ResourceControllerV2 with explicit API key
    """

    @classmethod
    def setup_class(cls):
        global resource_controller_service, catalog_service

        # Set API key as variable here
        api_key = "<apikey>"  # <-- Replace with your IBM Cloud API key

        authenticator = IAMAuthenticator(api_key)

        # Initialize services with explicit authenticator
        resource_controller_service = ResourceControllerV2(authenticator=authenticator)
        catalog_service = GlobalCatalogV1(authenticator=authenticator)

        assert resource_controller_service is not None
        assert catalog_service is not None

        print("Setup complete.")

    def test_create_resource_instance_with_parameters(self):
        """
        Create a resource instance with dynamic plan lookup and parameters
        """
        try:
            # Configurable values
            service_name = "power-dr-automation"
            plan_name = "powerha-aix-powervs"  # Mention your plan name for your service to create the provision.
            resource_group_id = "8d445dfd58484a4892207123456"  # Replace with your RG ID
            resource_instance_name = "phasdktestmp123"
            target_region = "us-east"

            # Step 1: Find service entry
            search_result = catalog_service.list_catalog_entries(q=f"name:{service_name}", complete=True).get_result()

            if len(search_result["resources"]) == 0:
                pytest.fail(f"Service {service_name} not found in catalog")

            service_entry_id = search_result["resources"][0]["id"]

            # Step 2: Use global catalog to fetch the plan ID from the given plan name
            child_result = catalog_service.get_child_objects(id=service_entry_id, kind="*", complete=True).get_result()
            # Found the plan id from the user given plan name.
            plan_id = None
            for child in child_result["resources"]:
                if child.get("name") == plan_name:
                    plan_id = child["id"]
                    break

            if not plan_id:
                pytest.fail(f"Plan {plan_name} not found for service {service_name}")

            print(f"Found Plan ID: {plan_id}")

            # Step 3: Create resource instance with parameters

            create_response = resource_controller_service.create_resource_instance(
                name=resource_instance_name,
                target=target_region,
                resource_group=resource_group_id,
                resource_plan_id=plan_id,
            )

            resource_instance = create_response.get_result()
            print("\nCreateResourceInstance() result:")
            print(json.dumps(resource_instance, indent=2))

            # Save GUID for later delete
            global created_instance_guid
            created_instance_guid = resource_instance["guid"]

            # Step 4: Fetch instance details
            instance_details = resource_controller_service.get_resource_instance(id=created_instance_guid).get_result()

            print("\nGetResourceInstance() result:")
            print(json.dumps(instance_details, indent=2))

        except ApiException as e:
            pytest.fail(f"API exception: {str(e)}")

    # Example: Deprovision (delete) a previously provisioned resource instance. This prints the instance details that will be used in the delete request.
    def test_delete_resource_instance(self):
        """
        Delete a resource instance by GUID
        """
        try:
            # Use the instance GUID from create step OR hardcode one
            instance_guid = globals().get(
                "created_instance_guid",
                "crn:v1:bluemix:public:power-dr-automation:us-east:a/12345674d444c9bd95efca704cf033:a19b6293-9f76-46d8-81b0-7a443db51887::",
            )

            print(f"\nDeleting resource instance: {instance_guid}")

            delete_response = resource_controller_service.delete_resource_instance(id=instance_guid, recursive=False)

            print(f"DeleteResourceInstance() response status: {delete_response.get_status_code()}")

            time.sleep(10)

            assert delete_response.get_status_code() in [202, 204]

        except ApiException as e:
            pytest.fail(f"API exception: {str(e)}")
