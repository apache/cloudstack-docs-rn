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

Version |release| includes more than 20 bug fixes from previous release, the
following new features and improvements.


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


VMware vSphere dependency upgrade
---------------------------------

When building Apache CloudStack with ``noredist``, it now require the file
``deps/vim25_55.jar`` available from vSphere SDK 5.5,
VMware-vSphere-SDK-5.5.0-1284541.zip.


AWS SDK updated to 1.10.34
--------------------------

AWS SDK used for Secondary Storage to S3 has been updated to latest SDK, 1.10.34.

====================== ============================================================================
Supported hypervisors: Any
Link                   `CLOUDSTACK-9062`_
====================== ============================================================================


.. _Metric View spec : https://cwiki.apache.org/confluence/display/CLOUDSTACK/Metrics+Views+for+CloudStack+UI
.. _CLOUDSTACK-6276 : https://issues.apache.org/jira/browse/CLOUDSTACK-6276
.. _CLOUDSTACK-9062 : https://issues.apache.org/jira/browse/CLOUDSTACK-9062

.. |metric-view.png| image:: _static/images/metric-view.png
   :alt: Metrics from Instance view
