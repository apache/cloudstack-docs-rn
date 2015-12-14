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
   

What's New in |version|
=======================

Version |release| includes more than 100 bug fixes from previous release and some
significant UI improvements. Here are key new features and improvements:


Metrics Views
-------------

WebUI now offer visibility of performance metrics from various levels of the cloud
infrastructure. As admin it is now easier to identify problematic resources.
Allow hierarchical navigation to triage issue, sort and refresh.

Under Infrastructure, Instance and Storage as "Metric" button.

|metric-view.png|

====================== ============================================================================
Supported hypervisors: Any
Link                   `Metric View spec`_
====================== ============================================================================


Affinity groups within projects
-------------------------------

It is now possible to use anti-affinity groups in projects.

====================== ============================================================================
Supported hypervisors: Any
Link                   `CLOUDSTACK-6276`_
====================== ============================================================================


AWS SDK updated to 1.10.34
--------------------------

AWS SDK used for Secondary Storage to S3 has been updated to latest SDK, 1.10.34.

====================== ============================================================================
Supported hypervisors: Any
Link                   `CLOUDSTACK-9062`_
====================== ============================================================================


Quota Service
-------------

Quota service extends the functionality of usage server to provide a measurement
for the resources used by the accounts and domains using a common unit referred
to as cloud currency. It can be configured to ensure that your usage won’t
exceed the budget allocated to accounts/domain in cloud currency.

====================== ============================================================================
Supported hypervisors: Any
Link                   `Quota Service spec`_
====================== ============================================================================


SDN
---

* Nicira plugins updated
* Nuage plugins updated


Build dependency
----------------

When building Apache CloudStack with ``noredist``, it now require the file
``deps/vim25_55.jar`` available from vSphere SDK 5.5,
VMware-vSphere-SDK-5.5.0-1284541.zip.


.. _Metric View spec : https://cwiki.apache.org/confluence/display/CLOUDSTACK/Metrics+Views+for+CloudStack+UI
.. _CLOUDSTACK-6276 : https://issues.apache.org/jira/browse/CLOUDSTACK-6276
.. _CLOUDSTACK-9062 : https://issues.apache.org/jira/browse/CLOUDSTACK-9062
.. _Quota Service spec : https://cwiki.apache.org/confluence/display/CLOUDSTACK/Quota+Service+-+FS

.. |metric-view.png| image:: _static/images/metric-view.png
   :alt: Metrics from Instance view