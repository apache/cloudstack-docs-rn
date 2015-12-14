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
| addImageStoreS3                   | Adds S3 Image Store                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateVmNicIp                     | Update the default Ip of a VM Nic                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| updateNuageVspDevice              | Update a Nuage VSP device                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaStatement                    | Create a quota statement                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaBalance                      | Create a quota balance statement                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaSummary                      | Lists balance and quota usage for all accounts                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaUpdate                       |  Update quota calculations, alerts and statements                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaTariffList                   | Lists all quota tariff plans                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaTariffUpdate                 | Update the tariff plan for a resource                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaCredits                      | Add +-credits to an account                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaEmailTemplateList            | Lists all quota email templates                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaEmailTemplateUpdate          | Updates existing email templates for quota alerts                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| quotaIsEnabled                    | Return true if the plugin is enabled                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+


Updated API commands
--------------------

.. cssclass:: table-striped table-bordered table-hover

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
| startInternalLoadBalancerVM       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listInternalLoadBalancerVMs       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| stopInternalLoadBalancerVM        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listRouters                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| stopRouter                        | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| destroyRouter                     | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| rebootRouter                      | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| changeServiceForRouter            | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| startRouter                       | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: guestnetworkname, vpcname                                                 |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listAffinityGroups                | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``projectid`` (optional)                                                  |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: project, projectid                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| createAffinityGroup               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``projectid`` (optional)                                                  |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   | New parameters: project, projectid                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| deleteAffinityGroup               | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | New parameters: ``projectid`` (optional)                                                  |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| dedicatePublicIpRange             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   | Changed parameters: ``account`` (old version - required, new version - optional)          |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+


Removed API commands
--------------------

.. cssclass:: table-striped table-bordered table-hover

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
| addS3                             | Adds S3                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| listS3s                           | Lists S3s                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+


.. include:: global.rst
