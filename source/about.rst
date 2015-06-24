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

Version |release| of Apache CloudStack is a bugfix release and does not add new features to |version|. Here is the list of new features and improvements introduce in |version|:

.. contents::
   :local:
   :backlinks: top

Virtual Router Out of Band reboots configurable
-----------------------------------------------

   As of Apache CloudStack 4.4.4 it is now configurable how Out of Band reboots of Virtual Routers should be treated.
   A new setting ``router.reboot.when.outofband.migrated`` is introduced wich defaults to  ``false``.

   This behaviour changed in Apache CloudStack 4.4.3, and to restore that behaviour the setting should be set to ``true``.

   - ``false`` will not force a reboot of the router(s) if a reboot is detected.
   - ``true`` will force a reboot of the router(s) if a reboot is detected.

Duplicate SSH Keys are no longer allowed
----------------------------------------

In previous versions you could register the same SSH Public Key more than once in the same account.
This is no longer allowed as of Apache CloudStack 4.4.4 and throws an error if tried.


Java version upgraded to Java 1.7
---------------------------------

Apache CloudStack |version| is now using Java 1.7 for the management-server, cloudstack-usage, kvm agent and in system-VMs.


Support managed storage for root disks
--------------------------------------

   Use of Primary Storage Plug-in for Root disks. See `Configuring a Storage Plug-in
   <http://docs.cloudstack.apache.org/projects/cloudstack-installation/en/master/configuration.html#configuring-a-storage-plug-in>`_

   ====================== ============================================================================
   Supported hypervisors: XenServer, VMware
   ====================== ============================================================================


Root disk resize
----------------

   Allow Root disk resize which remove need to have multiple templates of the
   same Operating System for different disk size.

   ====================== ============================================================================
   Supported hypervisor:  KVM
   Link                   `Root resize Functional spec`_
   ====================== ============================================================================


Per primary Storage OverProvisioning
------------------------------------

   Added per Primary Storage ``storage.overprovisioning.factor`` setting to
   overseed the Global Settings value.

   -  admin can update an existing primary store by setting
      ``storage.overprovisioning.factor`` in the per primary setting.

   -  This value will override the value at the global level. This leverages
      the granularity of global parameters introduced in 4.2

   -  To fall back to the global value, null value can be passed.

   -  To disable overprovision a value of 1 will be passed.

   ====================== ============================================================================
   Supported hypervisor:  KVM
   link                   `Storage Over Prov. Functional spec`_
   ====================== ============================================================================


VMWare Support for DRS
----------------------

   VMware DRS(Distributed Resource Scheduler), VM HA(High Availability):
   Provide highly available resources to your workloads. Balance workloads for
   optimal performance. Scale and manage computing resources without service
   disruption.

   -  **Load Balancing**: distribution and usage of CPU and memory resources
      for all hosts and VMs in the cluster are continuously monitored and
      compared to ideal resource utilization given the attributes of the
      cluster’s resource pools and VMs, the current demand, and the imbalance
      target. It then performs (or recommends) virtual machine migrations
      accordingly. Also, when a VM is powered on in the cluster, DRS attempts
      to maintain proper load balancing by either placing the VM on an
      appropriate host or making a recommendation.

   -  **Power Management**: When the vSphere Distributed Power Management
      (DPM) feature is enabled, DRS compares cluster- and host-level capacity
      to the demands of the cluster’s VMs, including recent historical demand.
      It places (or recommends placing) hosts in standby  power mode if
      sufficient excess capacity is found or powering on hosts if capacity is
      needed. Depending on the resulting host power state  recommendations,
      VMs might need to be migrated to and from the hosts as well.

   -  **Affinity Rules**: control the placement of virtual machines on hosts
      within a cluster, by assigning affinity rules

   ====================== ============================================================================
   Supported hypervisors: VMware
   Link                   `DRS functional spec`_
   ====================== ============================================================================


Region wide Guest networks and VPC
----------------------------------

   Region level Guest networks and VPC deployment. Allowing VPC tiers and guest
   networks accessibility across zones.

   ====================== ============================================================================
   Supported hypervisors: N/A
   Link                   `VPC region functional spec`_
   ====================== ============================================================================


Virtual Router Service Failure Alerting
---------------------------------------

   Send failure alerts to management server to notify admins using `Monitoring
   VR services <https://cwiki.apache.org/confluence/display/CLOUDSTACK/Monitoring+VR+services>`_
   introduced in CloudStack 4.3.

   ====================== ============================================================================
   Supported hypervisors: xenserver, kvm, vmware
   Link                   `VR failure alerting functional spec`_
   ====================== ============================================================================


Distributed routing and network ACL with OVS plug-in
----------------------------------------------------

   Support distributed routing and network ACL with OVS plug-in.

   ====================== ============================================================================
   Supported hypervisors: xenserver, kvm, vmware
   Link                   `CLOUDSTACK-6161 <https://issues.apache.org/jira/browse/CLOUDSTACK-6161>`_
   ====================== ============================================================================


Hyper-V support improvements
----------------------------

Zone Wide Primary Store in Hyper-V
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   SMB share as zone wide primary storage.

   ====================== ============================================================================
   Supported hypervisors: Hyper-V
   Link                   `Hyper-V zone wide storage functional spec`_
   ====================== ============================================================================


VPC support on Hyper-V
~~~~~~~~~~~~~~~~~~~~~~

   Provide VPC capability on Hyper-V hypervisor.

   ====================== ============================================================================
   Supported hypervisors: Hyper-V
   Link                   `VPC support on Hyper-V functional spec`_
   ====================== ============================================================================


Storage Live-Migration support for Hyper-V
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Hyper-V 2012 R2 allows migration of volumes (virtual disks) of a virtual
   machine from one storage to another, while the virtual machine continues to
   run. It also allows live migration of a virtual machine and its volumes to
   another host and storage without any downtime.

   The intend of this feature is to enable support of live migration of a
   virtual machines with its volumes across hosts and storage pools. It'll
   also migration of volumes across storage pools while the volume stays
   attached to a running virtual machine.

   ====================== ============================================================================
   Supported hypervisors: Hyper-V
   Link                   `Hyper-V storage motion functional spec`_
   ====================== ============================================================================


.. _Hyper-V storage motion functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Storage+motion+for+Hyper-V
.. _Hyper-V zone wide storage functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Zone+wide+primary+storage+for+Hyper-V
.. _VPC support on Hyper-V functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/VPC+support+on+Hyper-V
.. _VR failure alerting functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Virtual+Router+Service+Failure+Alerting
.. _VPC region Functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Region+level+VPC+and+guest+network+spanning+multiple+zones
.. _Storage Over Prov. Functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Storage+OverProvisioning+as+Per+Primary+Basis
.. _Root resize functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Root+Resize+Support
.. _DRS functional spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/VMWare+Enhancements+-+Support+for+DRS+and+VM+HA
