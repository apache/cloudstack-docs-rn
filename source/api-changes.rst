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

List Instances
--------------

+---------------------+-------------------------------------------------------------------+
| API                 | Description                                                       |
+=====================+===================================================================+
| listVirtualMachines | For this existing API, the following request parameters has       |
|                     | been added                                                        |
|                     |                                                                   |
|                     | - ids : comma seperated VM ID's                                   |
+---------------------+-------------------------------------------------------------------+

https://issues.apache.org/jira/browse/CLOUDSTACK-6052


API support for retrieving UserData
-----------------------------------




Hyper-V
-------

+-------------------+-------------------------------------------------------------------+
| API               | Description                                                       |
+===================+===================================================================+
| addPrimaryStorage | To this existing API, the following field has been added: smb     |
+-------------------+-------------------------------------------------------------------+
| addImageStore     | To this existing API, the following field has been added: smb     |
+-------------------+-------------------------------------------------------------------+

Reporting CPU Sockets
---------------------

+----------+-------------------------------------------------------------------+
| API      | Description                                                       |
+==========+===================================================================+
| listhost | To this existing API, the following request parameter has been    |
|          | added: hypervisor.                                                |
|          |                                                                   |
|          | The new response parameter added is: cpusockets                   |
+----------+-------------------------------------------------------------------+

Publishing Alerts Using the Web ROOT Admin API
----------------------------------------------

+---------------+-------------------------------------------------------------------+
| API           | Description                                                       |
+===============+===================================================================+
| generateAlert | A new API has been added to generate and publish alerts for usage |
|               | services. The usage services can be installed on a different host |
|               | or the same host where the Management Server is running. This API |
|               | is available only to the Root Admin.                              |
+---------------+-------------------------------------------------------------------+
| listAlerts    | To this existing API, a new response parameter has been added:    |
|               | name. An alert can be searched on the basis of alert name.        |
+---------------+-------------------------------------------------------------------+

Dynamic Compute Offering
------------------------

+-----------------+-------------------------------------------------------------------+
| API             | Description                                                       |
+=================+===================================================================+
| DeployVM        | To this existing API, the following request parameter has been    |
|                 | added: details.                                                   |
+-----------------+-------------------------------------------------------------------+
| ScaleVM         | To this existing API, the following request parameter has been    |
|                 | added: details.                                                   |
+-----------------+-------------------------------------------------------------------+
| ScaleSystemVM   | To this existing API, the following request parameter has been    |
|                 | added: details.                                                   |
|                 |                                                                   |
+-----------------+-------------------------------------------------------------------+
| UpgradeVM       | To this existing API, the following request parameter has been    |
|                 | added: details.                                                   |
+-----------------+-------------------------------------------------------------------+
| UpgradeSystemVM | To this existing API, the following request parameter has been    |
|                 | added: details.                                                   |
|                 |                                                                   |
+-----------------+-------------------------------------------------------------------+

Enhanced Upgrade for Virtual Routers
------------------------------------

+-----------------------+-------------------------------------------------------------------+
| API                   | Description                                                       |
+=======================+===================================================================+
| upgradeRouterTemplate | This is a new API which has been added in this release.           |
|                       |                                                                   |
|                       | The following are the request parameters:                         |
|                       |                                                                   |
|                       | -  id: Upgrade the specified VR                                   |
|                       |                                                                   |
|                       | -  zone\_id : Upgrade the VRs in the specified zone.              |
|                       |                                                                   |
|                       | -  pod\_id : Upgrade the VRs in the specified pod.                |
|                       |                                                                   |
|                       | -  cluster\_id : Upgrade the VRs in the specified cluster.        |
|                       |                                                                   |
|                       | -  domain\_id : Upgrade the VRs belonging to the specified        |
|                       |    domain.                                                        |
|                       |                                                                   |
|                       | -  account\_id : Upgrade the VRs belonging to the specified       |
|                       |    account.                                                       |
|                       |                                                                   |                                  
+-----------------------+-------------------------------------------------------------------+
| listRouters           | For this existing API, the following request parameters has been  |
|                       | added:                                                            |
|                       |                                                                   |
|                       | -  version: Lists routers by specified version.                   |
|                       |                                                                   |
|                       | -  zone\_id : lists routers in specified zone.                    |
|                       |                                                                   |
|                       | -  pod\_id : Lists routers in the specified pod.                  |
|                       |                                                                   |
|                       | -  cluster\_id : Lists routers in the specified cluster.          |
|                       |                                                                   |
|                       | -  domain\_id : Lists routers owned by specified domain.          |
|                       |                                                                   |
|                       | -  account: Lists routers owned by specified account.             |
|                       |                                                                   |
|                       | The following response parameters has been added:                 |
|                       |                                                                   |
|                       | -  version : (String) The router version. For example, |release|. |
|                       |                                                                   |
|                       | -  requiresupgrade: (Boolean) The flag to indicate if the router  |
|                       |    template requires an upgrade.                                  |
|                       |                                                                   |
+-----------------------+-------------------------------------------------------------------+
