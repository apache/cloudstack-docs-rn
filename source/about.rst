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

CloudStack |version| includes the following new features and improvements.


 
[Storage] Support managed storage for root disks
------------------------------------------------

Use of Primary Storage Plug-in for Root disks. See `Configuring a Storage Plug-in <http://docs.cloudstack.apache.org/projects/cloudstack-installation/en/master/configuration.html#configuring-a-storage-plug-in>`_

Supported hypervisors: XenServer, VMware

[Storage] Root disk resize
------------------------------------------------

Allow Root disk resize which remove need to have multiple templates of the same Operating System for different disk size.

Supported hypervisor: KVM

`Root resize Functional spec <https://cwiki.apache.org/confluence/display/CLOUDSTACK/Root+Resize+Support>`_

[Storage] Per primary Storage OverProvisioning
------------------------------------------------

Added per Primary Storage ``storage.overprovisioning.factor`` setting to overseed the Global Settings value.

- admin can update an existing primary store by setting ``storage.overprovisioning.factor`` in the per primary setting.
- This value will override the value at the global level. This leverages the granularity of global parameters introduced in 4.2
- To fall back to the global value, null value can be passed.
- To disable overprovision a value of 1 will be passed.

`Storage Over Prov. Functional spec <https://cwiki.apache.org/confluence/display/CLOUDSTACK/Storage+OverProvisioning+as+Per+Primary+Basis>`_


[Hypervisor] VMWare Support for DRS
------------------------------------------------

VMware DRS(Distributed Resource Scheduler), VM HA(High Availability): Provide highly available resources to your workloads. Balance workloads for optimal performance. Scale and manage computing resources without service disruption.

- **Load Balancing**: distribution and usage of CPU and memory resources for all hosts and VMs in the cluster are continuously monitored and compared to ideal resource utilization given the attributes of the cluster’s resource pools and VMs, the current demand, and the imbalance target. It then performs (or recommends) virtual machine migrations accordingly. Also, when a VM is powered on in the cluster, DRS attempts to maintain proper load balancing by either placing the VM on an appropriate host or making a recommendation.
- **Power Management**: When the vSphere Distributed Power Management (DPM) feature is enabled, DRS compares cluster- and host-level capacity to the demands of the cluster’s VMs, including recent historical demand. It places (or recommends placing) hosts in standby power mode if sufficient excess capacity is found or powering on hosts if capacity is needed. Depending on the resulting host power state recommendations, VMs might need to be migrated to and from the hosts as well.
- **Affinity Rules**: control the placement of virtual machines on hosts within a cluster, by assigning affinity rules 

`DRS Functional spec <https://cwiki.apache.org/confluence/display/CLOUDSTACK/VMWare+Enhancements+-+Support+for+DRS+and+VM+HA>`_

[Hypervisor] Zone Wide Primary Store in Hyper-V
------------------------------------------------

SMB share as zone wide primary store.


[Management Server] CloudStack on Windows
------------------------------------------------

Windowsfication of CloudStack Management Server, remove dependency on cygwin in order to run CloudStack Management Server on Windows based Operating System.

`CLOUDSTACK-6105 <https://issues.apache.org/jira/browse/CLOUDSTACK-6105>`_



