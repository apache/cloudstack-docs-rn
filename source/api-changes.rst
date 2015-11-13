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

.. cssclass:: table-striped table-bordered table-hover

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
| listIdps                          | Returns list of discovered SAML Identity Providers                                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| authorizeSamlSso                  | Allow or disallow a user to use SAML SSO                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listSamlAuthorization             | Lists authorized users who can used SAML SSO                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listAndSwitchSamlAccount          | Lists and switches to other SAML accounts owned by the SAML user                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| removeRawUsageRecords             | Safely removes raw records from cloud_usage table                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addBigSwitchBcfDevice             | Adds a BigSwitch BCF Controller device                                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deleteBigSwitchBcfDevice          |  delete a BigSwitch BCF Controller device                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listBigSwitchBcfDevices           | Lists BigSwitch BCF Controller devices                                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| linkDomainToLdap                  | link an existing cloudstack domain to group or OU in ldap                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getUploadParamsForVolume          | Upload a data disk to the cloudstack cloud.                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| getUploadParamsForTemplate        | upload an existing template into the CloudStack cloud.                                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+


Updated API commands
--------------------

.. cssclass:: table-striped table-bordered table-hover

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
| addNicToVirtualMachine            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addCluster                        | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``ovm3cluster`` (optional), ``ovm3pool`` (optional),                      |
|                                   | ``ovm3vip`` (optional)                                                                    |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: ovm3vip                                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createTemplate                    | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``projectid`` (optional)                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| registerSSHKeyPair                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: account, domain, domainid                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listClusters                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: ovm3vip                                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| resetSSHKeyForVirtualMachine      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createSecurityGroup               | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: virtualmachinecount, virtualmachineids                                    |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateStoragePool                 | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``enabled`` (optional)                                                    |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateHostPassword                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``update_passwd_on_host`` (optional)                                      |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listSSHKeyPairs                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: account, domain, domainid                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| recoverVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listCapabilities                  | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: allowuserexpungerecovervm, allowuserviewdestroyedvm                       |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVPC                         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: redundantvpcrouter                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updatePortForwardingRule          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``vmguestip`` (optional)                                                  |
|                                   |                                                                                           |
|                                   | Removed parameters: ipaddressid, privateip, protocol, publicport                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deployVirtualMachine              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateTrafficType                 | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``ovm3networklabel`` (optional), ``xennetworklabel`` (optional)           |
|                                   |                                                                                           |
|                                   | Removed parameters: xenservernetworklabel                                                 |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: ovm3networklabel, xennetworklabel                                         |
|                                   |                                                                                           |
|                                   | Removed parameters: xenservernetworklabel                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createDomain                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: cpuavailable, cpulimit, cputotal, ipavailable, iplimit, iptotal,          |
|                                   | memoryavailable, memorylimit, memorytotal, networkavailable, networklimit, networktotal,  |
|                                   | primarystorageavailable, primarystoragelimit, primarystoragetotal, projectavailable,      |
|                                   | projectlimit, projecttotal, secondarystorageavailable, secondarystoragelimit,             |
|                                   | secondarystoragetotal, snapshotavailable, snapshotlimit, snapshottotal, state,            |
|                                   | templateavailable, templatelimit, templatetotal, vmavailable, vmlimit, vmtotal,           |
|                                   | volumeavailable, volumelimit, volumetotal, vpcavailable, vpclimit, vpctotal               |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listLBHealthCheckPolicies         | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``id`` (optional)                                                         |
|                                   |                                                                                           |
|                                   | Changed parameters: lbruleid (old version - required, new version - optional)             |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listDiskOfferings                 | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``isrecursive`` (optional), ``listall`` (optional)                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listSnapshots                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: physicalsize                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addS3                             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``connectionttl`` (optional), ``usetcpkeepalive`` (optional)              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| attachIso                         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listDomains                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: cpuavailable, cpulimit, cputotal, ipavailable, iplimit, iptotal,          |
|                                   | memoryavailable, memorylimit, memorytotal, networkavailable, networklimit, networktotal,  |
|                                   | primarystorageavailable, primarystoragelimit, primarystoragetotal, projectavailable,      |
|                                   | projectlimit, projecttotal, secondarystorageavailable, secondarystoragelimit,             |
|                                   | secondarystoragetotal, snapshotavailable, snapshotlimit, snapshottotal, state,            |
|                                   | templateavailable, templatelimit, templatetotal, vmavailable, vmlimit, vmtotal,           |
|                                   | volumeavailable, volumelimit, volumetotal, vpcavailable, vpclimit, vpctotal               |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateCluster                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: ovm3vip                                                                   |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| prepareTemplate                   | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``storageid`` (optional)                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| rebootVirtualMachine              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listSecurityGroups                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: virtualmachinecount, virtualmachineids                                    |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVMAffinityGroup             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| addTrafficType                    | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``ovm3networklabel`` (optional), ``xennetworklabel`` (optional)           |
|                                   |                                                                                           |
|                                   | Removed parameters: xenservernetworklabel                                                 |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: ovm3networklabel, xennetworklabel                                         |
|                                   |                                                                                           |
|                                   | Removed parameters: xenservernetworklabel                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateTemplate                    | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``requireshvm`` (optional)                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| removeNicFromVirtualMachine       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateDefaultNicForVirtualMachine | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createVPC                         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: redundantvpcrouter                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| resetPasswordForVirtualMachine    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| changeServiceForVirtualMachine    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| startVirtualMachine               | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| detachIso                         | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| migrateVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateDomain                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: cpuavailable, cpulimit, cputotal, ipavailable, iplimit, iptotal,          |
|                                   | memoryavailable, memorylimit, memorytotal, networkavailable, networklimit, networktotal,  |
|                                   | primarystorageavailable, primarystoragelimit, primarystoragetotal, projectavailable,      |
|                                   | projectlimit, projecttotal, secondarystorageavailable, secondarystoragelimit,             |
|                                   | secondarystoragetotal, snapshotavailable, snapshotlimit, snapshottotal, state,            |
|                                   | templateavailable, templatelimit, templatetotal, vmavailable, vmlimit, vmtotal,           |
|                                   | volumeavailable, volumelimit, volumetotal, vpcavailable, vpclimit, vpctotal               |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listVPCs                          | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: redundantvpcrouter                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| assignVirtualMachine              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVirtualMachine              | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listServiceOfferings              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``isrecursive`` (optional), ``listall`` (optional)                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| samlSso                           | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``idpid`` (required)                                                      |
|                                   |                                                                                           |
|                                   | Removed parameters: idpurl                                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| restoreVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listDomainChildren                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: cpuavailable, cpulimit, cputotal, ipavailable, iplimit, iptotal,          |
|                                   | memoryavailable, memorylimit, memorytotal, networkavailable, networklimit, networktotal,  |
|                                   | primarystorageavailable, primarystoragelimit, primarystoragetotal, projectavailable,      |
|                                   | projectlimit, projecttotal, secondarystorageavailable, secondarystoragelimit,             |
|                                   | secondarystoragetotal, snapshotavailable, snapshotlimit, snapshottotal, state,            |
|                                   | templateavailable, templatelimit, templatetotal, vmavailable, vmlimit, vmtotal,           |
|                                   | volumeavailable, volumelimit, volumetotal, vpcavailable, vpclimit, vpctotal               |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| migrateVirtualMachineWithVolume   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| stopVirtualMachine                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createSnapshot                    | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``name`` (optional)                                                       |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: physicalsize                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateIso                         | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``requireshvm`` (optional)                                                |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| destroyVirtualMachine             | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| revertToVMSnapshot                | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listVirtualMachines               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``keypair`` (optional), ``userid`` (optional)                             |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: userid, username                                                          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| restartVPC                        | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``cleanup`` (optional), ``makeredundant`` (optional)                      |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: redundantvpcrouter                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| revertSnapshot                    | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: physicalsize                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createVpnCustomerGateway          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``projectid`` (optional)                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+


.. include:: global.rst
