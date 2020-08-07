#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_mysql_db_system_actions
short_description: Perform actions on a DbSystem resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DbSystem resource in Oracle Cloud Infrastructure
    - For I(action=restart), restarts the specified DB System.
    - For I(action=start), start the specified DB System.
    - For I(action=stop), stops the specified DB System.
      A stopped DB System is not billed.
version_added: "2.9"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    shutdown_type:
        description:
            - "The InnoDB shutdown mode to use, following the option
              \\"L(innodb_fast_shutdown,https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_fast_shutdown)\\"."
            - Required for I(action=restart), I(action=stop).
        type: str
        choices:
            - "IMMEDIATE"
            - "FAST"
            - "SLOW"
    action:
        description:
            - The action to perform on the DbSystem.
        type: str
        required: true
        choices:
            - "restart"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action restart on db_system
  oci_mysql_db_system_actions:
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
    shutdown_type: IMMEDIATE
    action: restart

- name: Perform action start on db_system
  oci_mysql_db_system_actions:
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
    action: start

- name: Perform action stop on db_system
  oci_mysql_db_system_actions:
    db_system_id: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
    shutdown_type: IMMEDIATE
    action: stop

"""

RETURN = """
db_system:
    description:
        - Details of the DbSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the DB System.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-friendly name for the DB System. It does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - User-provided data about the DB System.
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment the DB System belongs in.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        subnet_id:
            description:
                - The OCID of the subnet the DB System is associated with.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        availability_domain:
            description:
                - The Availability Domain where the primary DB System should be located.
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The name of the Fault Domain the DB System is located in.
            returned: on success
            type: string
            sample: fault_domain_example
        shape_name:
            description:
                - "The shape of the primary instances of the DB System. The shape
                  determines resources allocated to a DB System - CPU cores
                  and memory for VM shapes; CPU cores, memory and storage for non-VM
                  (or bare metal) shapes. To get a list of shapes, use (the
                  L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/mysql/20181021/ShapeSummary/ListShapes) operation."
            returned: on success
            type: string
            sample: shape_name_example
        mysql_version:
            description:
                - Name of the MySQL Version in use for the DB System.
            returned: on success
            type: string
            sample: mysql_version_example
        backup_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - If automated backups are enabled or disabled.
                    returned: on success
                    type: bool
                    sample: true
                window_start_time:
                    description:
                        - The start of a 30-minute window of time in which daily, automated backups occur.
                        - "This should be in the format of the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be
                          truncated to zero."
                        - At some point in the window, the system may incur a brief service disruption as the backup is performed.
                        - "If not defined, a window is selected from the following Region-based time-spans:
                          - eu-frankfurt-1: 20:00 - 04:00 UTC
                          - us-ashburn-1: 03:00 - 11:00 UTC
                          - uk-london-1: 06:00 - 14:00 UTC
                          - ap-tokyo-1: 13:00 - 21:00
                          - us-phoenix-1: 06:00 - 14:00"
                    returned: on success
                    type: string
                    sample: window_start_time_example
                retention_in_days:
                    description:
                        - The number of days automated backups are retained.
                    returned: on success
                    type: int
                    sample: 56
                freeform_tags:
                    description:
                        - Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                        - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                        - "Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                        - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                        - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The specific source identifier.
                    returned: on success
                    type: string
                    sample: NONE
                backup_id:
                    description:
                        - The OCID of the backup to be used as the source for the new DB System.
                    returned: on success
                    type: string
                    sample: ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx
        configuration_id:
            description:
                - The OCID of the Configuration to be used for Instances in this DB System.
            returned: on success
            type: string
            sample: ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx
        data_storage_size_in_gbs:
            description:
                - Initial size of the data volume in GiBs that will be created and attached.
            returned: on success
            type: int
            sample: 56
        hostname_label:
            description:
                - "The hostname for the primary endpoint of the DB System. Used for DNS.
                  The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
                  (for example, \\"dbsystem-1\\" in FQDN \\"dbsystem-1.subnet123.vcn1.oraclevcn.com\\").
                  Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123."
            returned: on success
            type: string
            sample: hostname_label_example
        ip_address:
            description:
                - "The IP address the DB System is configured to listen on. A private
                  IP address of the primary endpoint of the DB System. Must be an
                  available IP address within the subnet's CIDR. This will be a
                  \\"dotted-quad\\" style IPv4 address."
            returned: on success
            type: string
            sample: ip_address_example
        port:
            description:
                - The port for primary endpoint of the DB System to listen on.
            returned: on success
            type: int
            sample: 56
        port_x:
            description:
                - The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.
            returned: on success
            type: int
            sample: 56
        endpoints:
            description:
                - The network endpoints available for this DB System.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The network address of the DB System.
                    returned: on success
                    type: string
                    sample: hostname_example
                ip_address:
                    description:
                        - The IP address the DB System is configured to listen on.
                    returned: on success
                    type: string
                    sample: ip_address_example
                port:
                    description:
                        - The port the MySQL instance listens on.
                    returned: on success
                    type: int
                    sample: 56
                port_x:
                    description:
                        - The network port where to connect to use this endpoint using the X protocol.
                    returned: on success
                    type: int
                    sample: 56
                modes:
                    description:
                        - The access modes from the client that this endpoint supports.
                    returned: on success
                    type: list
                    sample: []
                status:
                    description:
                        - The state of the endpoints, as far as it can seen from the DB System.
                          There may be some inconsistency with the actual state of the MySQL service.
                    returned: on success
                    type: string
                    sample: ACTIVE
                status_details:
                    description:
                        - Additional information about the current endpoint status.
                    returned: on success
                    type: string
                    sample: status_details_example
        lifecycle_state:
            description:
                - The current state of the DB System.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
        maintenance:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                window_start_time:
                    description:
                        - The start time of the maintenance window.
                        - "This string is of the format: \\"{day-of-week} {time-of-day}\\"."
                        - "\\"{day-of-week}\\" is a case-insensitive string like \\"mon\\", \\"tue\\", &c."
                        - "\\"{time-of-day}\\" is the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated
                          to zero."
                    returned: on success
                    type: string
                    sample: window_start_time_example
        time_created:
            description:
                - The date and time the DB System was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the DB System was last updated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "fault_domain_example",
        "shape_name": "shape_name_example",
        "mysql_version": "mysql_version_example",
        "backup_policy": {
            "is_enabled": true,
            "window_start_time": "window_start_time_example",
            "retention_in_days": 56,
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        },
        "source": {
            "source_type": "NONE",
            "backup_id": "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "configuration_id": "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx",
        "data_storage_size_in_gbs": 56,
        "hostname_label": "hostname_label_example",
        "ip_address": "ip_address_example",
        "port": 56,
        "port_x": 56,
        "endpoints": [{
            "hostname": "hostname_example",
            "ip_address": "ip_address_example",
            "port": 56,
            "port_x": 56,
            "modes": [],
            "status": "ACTIVE",
            "status_details": "status_details_example"
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "maintenance": {
            "window_start_time": "window_start_time_example"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.mysql import DbSystemClient
    from oci.mysql.models import RestartDbSystemDetails
    from oci.mysql.models import StopDbSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlDbSystemActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        restart
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_db_system

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def restart(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestartDbSystemDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restart_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                restart_db_system_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(db_system_id=self.module.params.get("db_system_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StopDbSystemDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                stop_db_system_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlDbSystemActionsHelperCustom = get_custom_class("MysqlDbSystemActionsHelperCustom")


class ResourceHelper(MysqlDbSystemActionsHelperCustom, MysqlDbSystemActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            db_system_id=dict(aliases=["id"], type="str", required=True),
            shutdown_type=dict(type="str", choices=["IMMEDIATE", "FAST", "SLOW"]),
            action=dict(
                type="str", required=True, choices=["restart", "start", "stop"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_system",
        service_client_class=DbSystemClient,
        namespace="mysql",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
