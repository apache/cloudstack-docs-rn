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

Version |release| includes more than 20 bug fixes from previous release.

Part of a new release process 4.8.0 got released 2 months after 4.7.0.

Lot's of UI and VPC improvements and fixes where merged into this release.


SDN
---

* Nicira plugins updated
* Nuage plugins updated


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


Build dependency
----------------

When building Apache CloudStack with ``noredist``, it now require the file
``deps/vim25_55.jar`` available from vSphere SDK 5.5,
VMware-vSphere-SDK-5.5.0-1284541.zip.


.. _Metric View spec : https://cwiki.apache.org/confluence/display/CLOUDSTACK/Metrics+Views+for+CloudStack+UI

.. |metric-view.png| image:: _static/images/metric-view.png
   :alt: Metrics from Instance view