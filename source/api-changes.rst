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
| ``listVirtualMachinesMetrics``              | Lists VM metrics                                                               |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listHostsMetrics``                        | Lists hosts metrics                                                            |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listClustersMetrics``                     | Lists clusters metrics                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listNuageUnderlayVlanIpRanges``           | enable Nuage underlay on vlan ip range                                         |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listVolumesMetrics``                      | Lists volume metrics                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``disableNuageUnderlayVlanIpRange``         | disable Nuage underlay on vlan ip range                                        |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``enableNuageUnderlayVlanIpRange``          | enable Nuage underlay on vlan ip range                                         |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listStoragePoolsMetrics``                 | Lists storage pool metrics                                                     |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createSnapshotFromVMSnapshot``            | Creates an instant snapshot of a volume from existing vm snapshot.             |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``getUserKeys``                             | This command allows the user to query the seceret and API keys for the account |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listInfrastructure``                      | Lists infrastructure                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listZonesMetrics``                        | Lists zone metrics                                                             |
+---------------------------------------------+--------------------------------------------------------------------------------+


Parameters Changed API Commands
-------------------------------

.. cssclass:: table-striped table-bordered table-hover

+---------------------------------------------+--------------------------------------------------------------------------------+
| Name                                        | Description                                                                    |
+=============================================+================================================================================+
| ``copyIso``                                 | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destzoneids`` (optional)                                                   |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``destzoneid`` was 'required' and is now 'optional'                          |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listHosts``                               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateFirewallRule``                      | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destcidrlist``                                                             |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateGuestOs``                           | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``details`` (required)                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateHost``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createEgressFirewallRule``                | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destcidrlist`` (optional)                                                  |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destcidrlist``                                                             |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addSwift``                                | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listEgressFirewallRules``                 | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destcidrlist``                                                             |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listSecondaryStagingStores``              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listTemplates``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listFirewallRules``                       | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destcidrlist``                                                             |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createSecondaryStagingStore``             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateNetworkOffering``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``supportspublicaccess``                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createNetworkOffering``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``supportspublicaccess``                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listSnapshots``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``locationtype``                                                             |
|                                             | - ``osdisplayname``                                                            |
|                                             | - ``ostypeid``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listConfigurations``                      | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``imagestoreuuid`` (optional)                                                |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addIpToNic``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``secondaryip``                                                              |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createProject``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``projectaccountname``                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createSnapshot``                          | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``locationtype`` (optional)                                                  |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``locationtype``                                                             |
|                                             | - ``osdisplayname``                                                            |
|                                             | - ``ostypeid``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``findHostsForMigration``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``dedicateGuestVlanRange``                  | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``account`` was 'required' and is now 'optional'                             |
|                                             | - ``domainid`` was 'required' and is now 'optional'                            |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateIso``                               | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``cleanupdetails`` (optional)                                                |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listExternalLoadBalancers``               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``prepareTemplate``                         | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``samlSso``                                 | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``timezoneoffset``                                                           |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``login``                                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``timezoneoffset``                                                           |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addImageStore``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``copyTemplate``                            | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destzoneids`` (optional)                                                   |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``destzoneid`` was 'required' and is now 'optional'                          |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``assignVirtualMachine``                    | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``projectid`` (optional)                                                     |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``account`` was 'required' and is now 'optional'                             |
|                                             | - ``domainid`` was 'required' and is now 'optional'                            |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateTemplate``                          | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``cleanupdetails`` (optional)                                                |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addSecondaryStorage``                     | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateVirtualMachine``                    | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``cleanupdetails`` (optional)                                                |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateNetwork``                           | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``forced`` (optional)                                                        |
|                                             | - ``updateinsequence`` (optional)                                              |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createTemplate``                          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``prepareHostForMaintenance``               | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listProjects``                            | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``projectaccountname``                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addGuestOs``                              | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``details`` (required)                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``registerIso``                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``cancelHostMaintenance``                   | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listProjectAccounts``                     | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``projectaccountname``                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listNetworkOfferings``                    | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``supportspublicaccess``                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addHost``                                 | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateProject``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``projectaccountname``                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listIsos``                                | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateCloudToUseObjectStore``             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateConfiguration``                     | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``imagestoreuuid`` (optional)                                                |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``revertSnapshot``                          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``locationtype``                                                             |
|                                             | - ``osdisplayname``                                                            |
|                                             | - ``ostypeid``                                                                 |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listSwifts``                              | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``suspendProject``                          | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``projectaccountname``                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``registerTemplate``                        | **Request:**                                                                   |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``zoneids`` (optional)                                                       |
|                                             |                                                                                |
|                                             | *Changed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``zoneid`` was 'required' and is now 'optional'                              |
|                                             |                                                                                |
|                                             | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``bits``                                                                     |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addImageStoreS3``                         | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``createFirewallRule``                      | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destcidrlist``                                                             |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``listImageStores``                         | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *Removed Parameters:*                                                          |
|                                             |                                                                                |
|                                             | - ``details``                                                                  |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``activateProject``                         | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``projectaccountname``                                                       |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``reconnectHost``                           | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``addBaremetalHost``                        | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``memorywithoverprovisioning``                                               |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+
| ``updateEgressFirewallRule``                | **Response:**                                                                  |
|                                             |                                                                                |
|                                             | *New Parameters:*                                                              |
|                                             |                                                                                |
|                                             | - ``destcidrlist``                                                             |
|                                             |                                                                                |
+---------------------------------------------+--------------------------------------------------------------------------------+


