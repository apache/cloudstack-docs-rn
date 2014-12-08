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

Version |release| includes more than 180 bug fixes from previous release, the following new features and improvements.

.. contents::
   :local:
   :backlinks: top


Managed storage for KVM
-----------------------

   This adapter provides one to one mapping between SAN volume to VM's disk. This is to guarantee quality of services for performance sensitive applications. This adapter is based on nfs protocol.

   ====================== ============================================================================
   Supported hypervisors: KVM
   Link                   `CLOUDSTACK-7576 <https://issues.apache.org/jira/browse/CLOUDSTACK-7576>`_
   ====================== ============================================================================


Improvements
------------

-  [UI] keep advanced search parameters visible after search has been run
-  [UI] Add new vGPU types K160Q, K180Q, K280Q
-  [LXC] storage migration for LXC VMs fixed
-  MariaDB as cloudstack management server database
-  VM password reset when Router VM in stopped
-  [VR] Use ssh for commands sent to VR instead of xapi
-  Root volume detach support

.. _VR failure alerting functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Virtual+Router+Service+Failure+Alerting

