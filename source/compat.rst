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

-  RHEL versions 5.5, 6.2, 6.3, 6.4 and 7

-  CentOS versions 6.3, 6.4, 6.5 and 7

-  Ubuntu 12.04 LTS and 14.04 LTS

Supported Hypervisor Versions
-----------------------------

CloudStack supports three hypervisor families, XenServer with XAPI, KVM,
and VMware with vSphere.

-  Windows Server 2012 R2 (with Hyper-V Role enabled)

-  Hyper-V 2012 R2

-  CentOS 6.2 with KVM

-  CentOS 7 with KVM

-  Red Hat Enterprise Linux 6.2 with KVM

-  XenServer 6.0.2 (with Hotfix)

-  XenServer versions 6.1 and 6.2 SPI with latest hotfixes

-  VMware versions 5.0, 5.1, and 5.5

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

-  Netscaler VPX and MPX versions 9.3 and 10.e

-  Netscaler SDX version 9.3

-  SRX (Model srx100b) versions 10.3 or higher

-  F5 10.1.0 (Build 3341.1084)


Supported Browsers
------------------

The CloudStack Web-based UI should be compatible with any modern
browser, but it's possible that some browsers will not render portions
of the UI reliably, depending on their support of Web standards. For
best results, one of the following browsers recommended:

-  Internet Explorer versions 10 and 11

-  Firefox version 26 or lower

-  Google Chrome version 31

-  Safari 5