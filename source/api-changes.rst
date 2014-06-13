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

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
|  listNetworkACLs                  | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  reconnectHost                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listNiciraNvpDeviceNetworks      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addNicToVirtualMachine            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listNetworkOfferings              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: supportsstrechedl2subnet                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  createVpnConnection              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listVolumes                      | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid (optional), displayvolume (optional)                     |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname,                              |
|                                   |                                                                                           |
|                                   |   templatedisplaytext, templateid, templatename                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listLoadBalancers                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  importLdapUsers                  | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: account (optional)                                                      |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listLoadBalancerRuleInstances     | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: lbvmips (optional)                                                      |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: lbvmipaddresses, loadbalancerruleinstance                               |
|                                   |                                                                                           |
|                                   | Removed parameters:                                                                       |
|                                   |   id, account, cpunumber, cpuspeed, cpuused,                                              |
|                                   |                                                                                           |
|                                   |   created, details, diskioread, diskiowrite,diskkbsread, diskkbswrite,                    |
|                                   |                                                                                           |
|                                   |   displayname, displayvm, domain, domainid, forvirtualnetwork, group,                     |
|                                   |                                                                                           |
|                                   |   groupid,guestosid, haenable, hostid, hostname, hypervisor,                              |
|                                   |                                                                                           |
|                                   |   instancename, isdynamicallyscalable, isodisplaytext, isoid,isoname,                     |
|                                   |                                                                                           |
|                                   |   keypair, memory, name, networkkbsread, networkkbswrite, password,                       |
|                                   |                                                                                           |
|                                   |   passwordenabled, project,projectid, publicip, publicipid,                               |
|                                   |                                                                                           |
|                                   |   rootdeviceid, rootdevicetype, serviceofferingid, serviceofferingname,                   |
|                                   |                                                                                           |
|                                   |   servicestate, state, templatedisplaytext, templateid, templatename,                     |
|                                   |                                                                                           |
|                                   |   zoneid, zonename, affinitygroup(*),nic(*), securitygroup(*),                            |
|                                   |                                                                                           |
|                                   |   tags(*), jobid, jobstatus                                                               |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| migrateVolume                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname,                              |
|                                   |                                                                                           |
|                                   |   templatedisplaytext, templateid, templatename                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listAutoScaleVmGroups            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createNetwork                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| enableAccount                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listPublicIpAddresses            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| enableStorageMaintenance          | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: overprovisionfactor                                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listVpnGateways                   | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| attachVolume                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname,                              |
|                                   |                                                                                           |
|                                   |   templatedisplaytext, templateid, templatename                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVPCOffering                 | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: distributedvpcrouter, supportsregionLevelvpc                            |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| resetSSHKeyForVirtualMachine      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVolume                      | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo (optional), customid (optional)                               |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname,                              |
|                                   |                                                                                           |
|                                   |   templatedisplaytext, templateid, templatename                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listNetworks                      | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: displaynetwork (optional)                                               |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createAutoScaleVmProfile          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| cancelHostMaintenance             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateServiceOffering             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisorsnapshotreserve, iscustomizediops, maxiops, miniops           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateStoragePool                 | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: overprovisionfactor                                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addBaremetalHost                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| resizeVolume                      | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |  Changed parameters: id (old version - optional, new version - required)                  |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname, templatedisplaytext,         |
|                                   |                                                                                           |
|                                   |   templateid, templatename                                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createIpForwardingRule            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateDiskOffering                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: cacheMode, hypervisorsnapshotreserve                                    |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listNetworkACLLists               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| recoverVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listCapabilities                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: customdiskofferingminsize                                               |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVPC                         | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional), fordisplay (optional)                              |
|                                   |                                                                                           |
|                                   | Changed parameters: name (old version - required, new version - optional)                 |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: distributedvpcrouter, fordisplay, regionlevelvpc                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateAutoScaleVmProfile          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional), fordisplay (optional)                              |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updatePortForwardingRule          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: id (required), customid (optional), fordisplay (optional)               |
|                                   |                                                                                           |
|                                   | Changed parameters: privateport (old version - required, new version -                    |
|                                   |                                                                                           |
|                                   |    optional), protocol (old version -required, new version - optional),                   |
|                                   |                                                                                           |
|                                   |    ipaddressid (old version - required, new version - optional), publicport               |
|                                   |                                                                                           |
|                                   |    old version - required, new version - optional)                                        |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listPortForwardingRules           | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createLoadBalancer                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| cancelStorageMaintenance          | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: overprovisionfactor                                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deployVirtualMachine              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional), deploymentplanner (optional),                      |
|                                   |                                                                                           |
|                                   |   rootdisksize (optional)                                                                 |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createNetworkACLList              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createPortForwardingRule          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createVPCOffering                 | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: servicecapabilitylist (optional)                                        |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: distributedvpcrouter, supportsregionLevelvpc                            |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createEgressFirewallRule          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listUsageRecords                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: cpunumber, cpuspeed, memory                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateNetworkACLItem              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional), fordisplay (optional)                              |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateAccount                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listLBHealthCheckPolicies         | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addHost                           | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createAutoScaleVmGroup            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createLBHealthCheckPolicy         | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateHost                        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| lockAccount                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listDiskOfferings                 | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: cacheMode, hypervisorsnapshotreserve                                    |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| detachVolume                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname,                              |
|                                   |                                                                                           |
|                                   |   templatedisplaytext, templateid, templatename                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateLoadBalancerRule            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional), fordisplay (optional)                              |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createVpnGateway                  | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listF5LoadBalancerNetworks        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| ldapCreateAccount                 | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listRemoteAccessVpns              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| disableAutoScaleVmGroup           | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createAccount                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| prepareHostForMaintenance         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| attachIso                         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getUser                           | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: apikey (required)                                                       |
|                                   |                                                                                           |
|                                   | Removed parameters: userapikey                                                            |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listLoadBalancerRules             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| enableAutoScaleVmGroup            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listResourceDetails               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |  Changed parameters: resourceid (old version - required, new version - optional)          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listPaloAltoFirewallNetworks      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| restartNetwork                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| rebootVirtualMachine              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listLBStickinessPolicies          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listFirewallRules                 | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVMAffinityGroup             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listNics                          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional), networkid (optional)                             |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: deviceid, virtualmachineid                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createStoragePool                 | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: overprovisionfactor                                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listSrxFirewallNetworks           | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createServiceOffering             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customizediops (optional), hypervisorsnapshotreserve                    |
|                                   |                                                                                           |
|                                   |   (optional), maxiops (optional), miniops optional)                                       |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisorsnapshotreserve, iscustomizediops, maxiops, miniops           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| removeNicFromVirtualMachine       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateDefaultNicForVirtualMachine | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createNetworkACL                  | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createVPC                         | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: distributedvpcrouter, fordisplay, regionlevelvpc                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listOsTypes                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: isuserdefined                                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addResourceDetail                 | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listExternalLoadBalancers         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| resetPasswordForVirtualMachine    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createVolume                      | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional)                                                     |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname,                              |
|                                   |                                                                                           |
|                                   |   templatedisplaytext, templateid, templatename                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| assignToLoadBalancerRule          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: vmidipmap (optional)                                                    |
|                                   |                                                                                           |
|                                   | Changed parameters: virtualmachineids (old version - required,                            |
|                                   |                                                                                           |
|                                   |   new version - optional)                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| changeServiceForVirtualMachine    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listStoragePools                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: overprovisionfactor                                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| resetVpnConnection                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| startVirtualMachine               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: deploymentplanner (optional)                                            |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createRemoteAccessVpn             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| detachIso                         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| associateIpAddress                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| disableAccount                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| migrateVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| removeFromLoadBalancerRule        | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: vmidipmap (optional)                                                    |
|                                   |                                                                                           |
|                                   | Changed parameters: virtualmachineids (old version - required,                            |
|                                   |                                                                                           |
|                                   |   new version - optional)                                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listVPCs                          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |      New parameters: fordisplay (optional)                                                |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: distributedvpcrouter, fordisplay, regionlevelvpc                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| assignVirtualMachine              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVirtualMachine              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional), name (optional)                                    |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listServiceOfferings              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: hypervisorsnapshotreserve, iscustomizediops,                            |
|                                   |                                                                                           |
|                                   |   maxiops, miniops                                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createLoadBalancerRule            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| restoreVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createNetworkOffering             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: supportsstrechedl2subnet                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| uploadVolume                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: chaininfo, isodisplaytext, isoid, isoname, templatedisplaytext,         |
|                                   |                                                                                           |
|                                   |   templateid, templatename                                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listAutoScaleVmProfiles           | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional), serviceofferingid (optional),                    |
|                                   |                                                                                           |
|                                   |   zoneid (optional)                                                                       |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createLBStickinessPolicy          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| migrateVirtualMachineWithVolume   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| stopVirtualMachine                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listAccounts                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listIpForwardingRules             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| destroyVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateNetwork                     | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional)                                                     |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createDiskOffering                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: cacheMode, hypervisorsnapshotreserve                                    |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listNetscalerLoadBalancerNetworks | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: strechedl2subnet, zonesnetworkspans                                     |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createFirewallRule                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| revertToVMSnapshot                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| markDefaultZoneForAccount         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: groups                                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listVirtualMachines               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: displayvm (optional), ids (optional), serviceofferingid (optional)      |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid, diskofferingname, ostypeid, vgpu                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| restartVPC                        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: distributedvpcrouter, fordisplay, regionlevelvpc                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listEgressFirewallRules           | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateAutoScaleVmGroup            | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: customid (optional), fordisplay (optional)                              |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listHosts                         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: gpugroup(*)                                                             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listVpnConnections                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listVPCOfferings                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: distributedvpcrouter, supportsregionLevelvpc                            |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateNetworkOffering             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: supportsstrechedl2subnet                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| findStoragePoolsForMigration      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: overprovisionfactor                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------+
