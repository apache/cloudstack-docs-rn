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

Added API commands
------------------

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
| samlSso                           | SP initiated SAML Single Sign On                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| samlSlo                           | SAML Global Log Out API                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getSPMetadata                     | Returns SAML2 CloudStack Service Provider MetaData                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listHostTags                      | Lists host tags                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listStorageTags                   | Lists storage tags                                                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addBrocadeVcsDevice               | Adds a Brocade VCS Switch                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deleteBrocadeVcsDevice            | delete a Brocade VCS Switch                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listBrocadeVcsDevices             | Lists Brocade VCS Switches                                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listBrocadeVcsDeviceNetworks      | lists network that are using a brocade vcs switch                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addNuageVspDevice                 | Adds a Nuage VSP device                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deleteNuageVspDevice              | delete a nuage vsp device                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listNuageVspDevices               | Lists Nuage VSP devices                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| issueNuageVspResourceRequest      | Issues a Nuage VSP REST API resource request                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getSolidFireAccountId             | Get SolidFire Account ID                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getSolidFireVolumeSize            | Get the SF volume size including Hypervisor Snapshot Reserve                              |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getSolidFireVolumeAccessGroupId   | Get the SF Volume Access Group ID                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getSolidFireVolumeIscsiName       | Get SolidFire Volume's Iscsi Name                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addBaremetalRct                   | adds baremetal rack configuration text                                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deleteBaremetalRct                | deletes baremetal rack configuration text                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listBaremetalRct                  | list baremetal rack configuration                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createServiceInstance             | Creates a system virtual-machine that implements network services                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addOpenDaylightController         | Adds an OpenDyalight controler                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deleteOpenDaylightController      | Removes an OpenDyalight controler                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listOpenDaylightControllers       | Lists OpenDyalight controllers                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addGloboDnsHost                   | Adds the GloboDNS external host                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+


Updated API commands
--------------------

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
|  reconnectHost                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  addHost                          | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  updateHost                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  cancelHostMaintenance            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  prepareHostForMaintenance        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listHosts                        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listVolumes                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  migrateVolume                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  attachVolume                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  updateVolume                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  resizeVolume                     | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``maxiops`` (optional), ``miniops`` (optional)                          |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  detachVolume                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  createVolume                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  uploadVolume                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listUsageRecords                 | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: usageid (optional)                                                      |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  updateTrafficType                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``xenservernetworklabel`` (optional)                                    |
|                                   |                                                                                           |
|                                   |   Removed parameters: xennetworklabel                                                     |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: xenservernetworklabel                                                   |
|                                   |                                                                                           |
|                                   |   Removed parameters: xennetworklabel                                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  login                            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: registered                                                              |
|                                   |                                                                                           |
|                                   |   Removed parameters: password, timezoneoffset                                            |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  updateZone                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   Removed parameters: vlan                                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  createZone                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   Removed parameters: vlan                                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listZones                        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   Removed parameters: vlan                                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listBaremetalPxeServers          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``physicalnetworkid`` (required)                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listBaremetalDhcp                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``physicalnetworkid`` (required)                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  addBaremetalHost                 | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  addTrafficType                   | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``xenservernetworklabel`` (optional)                                    |
|                                   |                                                                                           |
|                                   |   Removed parameters: xennetworklabel                                                     |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: xenservernetworklabel                                                   |
|                                   |                                                                                           |
|                                   |   Removed parameters: xennetworklabel                                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listPublicIpAddresses            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``state`` (optional)                                                    |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  startInternalLoadBalancerVM      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listExternalLoadBalancers        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: details                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listInternalLoadBalancerVMs      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listLBHealthCheckPolicies        | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   Changed parameters: ``lbruleid`` (old version - optional, new version - required)       |
|                                   |                                                                                           |
|                                   |   Removed parameters: id                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  stopInternalLoadBalancerVM       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  updateVirtualMachine             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   Changed parameters: ``instancename`` (optional)                                         |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  createServiceOffering            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``provisioningtype`` (optional)                                         |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  updateServiceOffering            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listServiceOfferings             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  updateDiskOffering               | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listDiskOfferings                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  createDiskOffering               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: ``provisioningtype`` (optional)                                         |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: provisioningtype                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listRouters                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  stopRouter                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  destroyRouter                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  rebootRouter                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  startRouter                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  changeServiceForRouter           | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  changeServiceForSystemVm         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listSystemVms                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  destroySystemVm                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  stopSystemVm                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  startSystemVm                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  migrateSystemVm                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  rebootSystemVm                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  scaleSystemVm                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisor                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+

.. include:: global.rst
