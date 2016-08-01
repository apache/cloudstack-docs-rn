.. Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information#
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.


API Changes Introduced in |version|
===================================

For the complete list of API commands and params consult the `CloudStack Apidocs`_.


New API Commands
----------------

.. cssclass:: table-striped table-bordered table-hover

+---------------------------------------------+--------------------------------------------------------------------------------+
| Name                                        | Description                                                                    |
+=============================================+================================================================================+
| ``configureOutOfBandManagement``            | Configures a host's out-of-band management interface                           |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``disableOutOfBandManagementForZone``       | Disables out-of-band management for a zone                                     |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateRolePermission``                    | Updates a role permission order                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``ldapConfig``                              | Configure the LDAP context for this site.                                      |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createRole``                              | Creates a role                                                                 |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``deleteStratosphereSsp``                   | Removes stratosphere ssp server                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``searchLdap``                              | Searches LDAP based on the username attribute                                  |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``enableOutOfBandManagementForCluster``     | Enables out-of-band management for a cluster                                   |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``getPathForVolume``                        | Get the path associated with the provided volume UUID                          |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listRolePermissions``                     | Lists role permissions                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``changeOutOfBandManagementPassword``       | Changes out-of-band management interface password on the host and updates the  |
|                                             | interface configuration in CloudStack if the operation succeeds, else reverts  |
|                                             | the old password                                                               |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listRoles``                               | Lists dynamic roles in CloudStack                                              |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateRole``                              | Updates a role                                                                 |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createRolePermission``                    | Adds a API permission to a role                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``enableOutOfBandManagementForHost``        | Enables out-of-band management for a host                                      |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``disableOutOfBandManagementForCluster``    | Disables out-of-band management for a cluster                                  |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``deleteRolePermission``                    | Deletes a role permission                                                      |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``getVolumeiScsiName``                      | Get Volume's iSCSI Name                                                        |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``getVolumeSnapshotDetails``                | Get Volume Snapshot Details                                                    |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``notifyBaremetalProvisionDone``            | Notify provision has been done on a host. This api is for baremetal virtual    |
|                                             | router service, not for end user                                               |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``ldapRemove``                              | Remove the LDAP context for this site.                                         |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``deleteUcsManager``                        | Delete a Ucs manager                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``issueOutOfBandManagementPowerAction``     | Initiates the specified power action to the host's out-of-band management      |
|                                             | interface                                                                      |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``disableOutOfBandManagementForHost``       | Disables out-of-band management for a host                                     |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``deleteRole``                              | Deletes a role                                                                 |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``enableOutOfBandManagementForZone``        | Enables out-of-band management for a zone                                      |
+---------------------------------------------+--------------------------------------------------------------------------------+


Removed API Commands
--------------------

.. cssclass:: table-striped table-bordered table-hover

+---------------------------------------------+--------------------------------------------------------------------------------+
| Name                                        | Description                                                                    |
+=============================================+================================================================================+
| ``issueNuageVspResourceRequest``            | Issues a Nuage VSP REST API resource request                                   |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``getSolidFireVolumeIscsiName``             | Get SolidFire Volume's Iscsi Name                                              |
+---------------------------------------------+--------------------------------------------------------------------------------+


Parameters Changed API Commands
-------------------------------

.. cssclass:: table-striped table-bordered table-hover

+---------------------------------------------+--------------------------------------------------------------------------------+
| Name                                        | Description                                                                    |
+=============================================+================================================================================+
| ``reconnectHost``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``copyTemplate``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addNicToVirtualMachine``                  | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addCluster``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``resourcedetails``                                                          |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listVolumes``                             | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``ids`` (optional)                                                           |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``importLdapUsers``                         | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid`` (optional)                                                        |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``accounttype`` was 'required' and is now 'optional'                         |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createTemplate``                          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``migrateVolume``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``enableAccount``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listClusters``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``resourcedetails``                                                          |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``attachVolume``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``resetSSHKeyForVirtualMachine``            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateVmNicIp``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateVolume``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``cancelHostMaintenance``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addNuageVspDevice``                       | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``retrycount`` was 'required' and is now 'optional'                          |
|                                             | - ``retryinterval`` was 'required' and is now 'optional'                       |
|                                             | - ``apiversion`` was 'required' and is now 'optional'                          |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``cmsid``                                                                    |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addBaremetalHost``                        | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``resizeVolume``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``recoverVirtualMachine``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listCapabilities``                        | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``dynamicrolesenabled``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``deployVirtualMachine``                    | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``enableUser``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateAccount``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addHost``                                 | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateNuageVspDevice``                    | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``cmsid``                                                                    |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateHost``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``lockAccount``                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createUser``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``detachVolume``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listSnapshots``                           | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``ids`` (optional)                                                           |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``ldapCreateAccount``                       | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid`` (optional)                                                        |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``accounttype`` was 'required' and is now 'optional'                         |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``registerTemplate``                        | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createAccount``                           | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid`` (optional)                                                        |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``accounttype`` was 'required' and is now 'optional'                         |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``prepareHostForMaintenance``               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listNuageVspDevices``                     | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``cmsid``                                                                    |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``attachIso``                               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``getUser``                                 | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateCluster``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``resourcedetails``                                                          |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listTemplates``                           | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``ids`` (optional)                                                           |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``prepareTemplate``                         | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``rebootVirtualMachine``                    | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateVMAffinityGroup``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateUser``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateTemplate``                          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``disableUser``                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``removeNicFromVirtualMachine``             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateDefaultNicForVirtualMachine``       | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``registerIso``                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listExternalLoadBalancers``               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createVolume``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``resetPasswordForVirtualMachine``          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``changeServiceForVirtualMachine``          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``startVirtualMachine``                     | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``detachIso``                               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``disableAccount``                          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``migrateVirtualMachine``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listVMSnapshot``                          | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``vmsnapshotids`` (optional)                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``assignVirtualMachine``                    | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateVirtualMachine``                    | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``securitygroupids`` (optional)                                              |
|                                             | - ``securitygroupnames`` (optional)                                            |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``getSolidFireVolumeSize``                  | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``storageid``                                                                |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``restoreVirtualMachine``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``copyIso``                                 | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``uploadVolume``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``migrateVirtualMachineWithVolume``         | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``stopVirtualMachine``                      | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listAccounts``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateIso``                               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``destroyVirtualMachine``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``revertToVMSnapshot``                      | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``markDefaultZoneForAccount``               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``lockUser``                                | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listVirtualMachines``                     | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memoryintfreekbs``                                                         |
|                                             | - ``memorykbs``                                                                |
|                                             | - ``memorytargetkbs``                                                          |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listHosts``                               | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagementenabled`` (optional)                                    |
|                                             | - ``outofbandmanagementpowerstate`` (optional)                                 |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``outofbandmanagement``                                                      |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listUsers``                               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``roleid``                                                                   |
|                                             | - ``rolename``                                                                 |
|                                             | - ``roletype``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listIsos``                                | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``tags(*)``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+

.. include:: global.rst
