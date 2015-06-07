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
   
Compatibility Matrix
====================

Supported OS Versions for Management Server
-------------------------------------------

This section lists the operating systems that are supported for running
CloudStack Management Server. Note that specific versions of the
operating systems are tested, so compatibility with CentOS 6.3 may not
indicate compatibility with CentOS 6.2, 6.1 and so on.

-  RHEL versions 6.3, 6.5, 6.6 and 7.0
-  CentOS versions 6.6, 7.0
-  Ubuntu 14.04 LTS

Software Requirements
~~~~~~~~~~~~~~~~~~~~~

-  Java 1.7
-  MySQL 5.6 (RHEL 7)
-  MySQL 5.1 (RHEL 6.x)

Supported Hypervisor Versions
-----------------------------

CloudStack supports three hypervisor families, XenServer with XAPI, KVM,
and VMware with vSphere.

-  LXC Host Containers on RHEL 7
-  Windows Server 2012 R2 (with Hyper-V Role enabled)
-  Hyper-V 2012 R2
-  CentOS 6.2+ with KVM
-  Red Hat Enterprise Linux 6.2 with KVM
-  XenServer versions 6.1, 6.2 SP1 and 6.5 with latest hotfixes

      .. note:: It is now required to enable HA on the XenServer pool in order to recover from a pool-master failure. Please refer to the `XenServer documentation <http://docs.vmd.citrix.com/XenServer/6.5.0/1.0/en_gb/>`_.

-  VMware versions 5.0 Update 3a, 5.1 Update 2a, and 5.5 Update 2
-  Bare metal hosts are supported, which have no hypervisor. These hosts
   can run the following operating systems:

   -  RHEL or CentOS, v6.2 or 6.3

      .. note:: Use libvirt version 0.9.10 for CentOS 6.3

   -  Fedora 17
   -  Ubuntu 12.04

For more information, see the Hypervisor Compatibility Matrix in the
CloudStack Installation Guide.


Supported External Devices
--------------------------

-  Netscaler VPX and MPX versions 9.3, 10.1e and 10.5
-  Netscaler SDX version 9.3, 10.1e and 10.5
-  SRX (Model srx100b) versions 10.3 to 10.4 R7.5
-  F5 11.X
-  Force 10 Switch version S4810 for Baremetal Advanced Networks


Supported Browsers
------------------

The CloudStack Web-based UI should be compatible with any modern
browser, but it's possible that some browsers will not render portions
of the UI reliably, depending on their support of Web standards. For
best results, one of the following browsers recommended:

-  Internet Explorer versions 10 and 11

-  Firefox version 31 or later

-  Google Chrome version 36.0.1985

-  Safari 6+
