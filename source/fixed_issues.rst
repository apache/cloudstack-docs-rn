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


Issues Fixed in |version|
=========================

Apache CloudStack uses `Jira <https://issues.apache.org/jira/browse/CLOUDSTACK>`_ 
to track its issues and `Github <https://github.com/apache/cloudstack/pulls>`_ for 
pull requests. All new features and bugs for |release| have been merged through
Github pull requests.  A subset of these changes are tracked in Jira, which have a 
standard naming convention of "CLOUDSTACK-NNNN" where "NNNN" is the issue number.

Issues Fixed in 4.9.3.0
-----------------------

.. cssclass:: table-striped table-bordered table-hover

+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| Branches           |  Jira              | Type          | Priority | Description                                                |
+====================+====================+===============+==========+============================================================+
| 4.9                | CLOUDSTACK-3223_   | Bug           | Major    | Exception observed while creating CPVM in VMware Setup wit |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-4858_   | Bug           | Major    | Disable copy snapshot to secondary storage snapshot.backup |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8186_   | Bug           | Critical | setRemoved(null) does not work as expected                 |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8663_   | Improvement   | Major    | Snapshot Improvements                                      |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8805_   | Bug           | Major    | Domains become inactive automatically.                     |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8829_   | Bug           | Major    | Consecutive cold migration fails                           |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8833_   | Bug           | Major    | Generating url and migrate volume to another storage , res |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8841_   | Bug           | Major    | Storage XenMotion from XS 6.2 to XS 6.5 fails.             |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8857_   | Bug           | Major    |  'listProjects' doesn't return tags 'vmstopped' or 'vmrunn |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8871_   | Bug           | Major    | Basic zone security group ingress/egress rules are not wor |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8896_   | Bug           | Major    | Allocated percentage of storage can go beyond 100%         |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8910_   | Bug           | Major    | The reserved_capacity field increases suddenly after a vmw |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8931_   | Bug           | Major    | Fail to deploy VM instance when use.system.public.ips=fals |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8950_   | Bug           | Major    | Hypervisor Parameter check is not performed  for registerT |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-8958_   | Improvement   | Major    | add dedicated ips to domain                                |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9017_   | Bug           | Major    | VPC VR DHCP broken for multihomed guest VMs                |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9136_   | Bug           | Major    | SSH keypairs are left and cannot be removed after removing |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9208_   | Bug           | Minor    | Assertion Error in VM_POWER_STATE handler.                 |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9321_   | Bug           | Critical | Multiple Internal LB rules (more than one Internal LB rule |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9356_   | Bug           | Critical | VPC add VPN User fails same error as CLOUDSTACK-8927       |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9369_   | Bug           | Critical | Security issue! Local login open with SAML implementation  |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9555_   | Bug           | Major    | when a template is deleted and then copied over again , it |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9560_   | Bug           | Major    | Root volume of deleted VM left unremoved                   |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9567_   | Bug           | Major    | Difference in the api call outputs for CAPACITY_TYPE_CPU = |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9569_   | Bug           | Critical | VR on shared network not starting on KVM                   |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9591_   | Bug           | Minor    | VMware dvSwitch Requires a Dummy, Standard vSwitch         |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9592_   | Bug           | Major    | Empty responses from site to site connection status are no |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9610_   | Bug           | Major    | Disabled Host Keeps Being up status after unmanaging clust |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9611_   | Bug           | Major    | Dedicating a Guest VLAN range to Project does not work     |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9623_   | Bug           | Major    | Deploying virtual machine fails due to "Couldn't find vlan |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9628_   | Bug           | Major    | Fix Template Size in Swift as Secondary Storage            |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9630_   | Bug           | Major    | Cannot use listNics API as advertised                      |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9631_   | Bug           | Major    | updateVMAffinityGroup must require one of the list paramet |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9638_   | Bug           | Major    |  Problems caused when inputting double-byte numbers for cu |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9647_   | Bug           | Major    | NIC adapter type becomes e1000 , even after changing the g |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9655_   | Bug           | Major    | The template which is registered in all zones will be dele |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9666_   | Bug           | Major    | Add configuration validation for the config drive global s |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9668_   | Bug           | Major    | disksizeallocated of PrimaryStorage is different from the  |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9682_   | Bug           | Major    | Block VM migration to a storage which is in maintainence m |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9684_   | Bug           | Major    | Invalid zone id error while listing vmware zone            |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9685_   | Bug           | Major    | [Xen]Delete snapshot on primary when associated volume is  |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9686_   | Bug           | Major    | multiple entires for builtin template in template store re |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9691_   | Bug           | Major    | unhandeled excetion in list snapshot command when a primar |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9692_   | Bug           | Major    | Reset password service is not running on Redundant virtual |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9694_   | Bug           | Major    | Unable to limit the Public IPs in VPC                      |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9701_   | Bug           | Major    | When host is disabled/removed, capacity_state for local st |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9705_   | Bug           | Major    | Unauthenticated API allows Admin password reset            |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9708_   | Bug           | Major    | Router deployment failed due to two threads start VR simul |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9715_   | Bug           | Major    | "somaxconn" value on VR is not reflecting value from /etc/ |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9719_   | Bug           | Major    | [VMware] VR loses DHCP settings and VMs cannot obtain IP a |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9720_   | Bug           | Major    | [VMware] template_spool_ref table is not getting updated w |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9725_   | Bug           | Major    | Failed to update VPC Network during N/w offering Upgrade w |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9728_   | Bug           | Major    | query to traffic sentinel requesting for usage stats is to |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9731_   | Bug           | Major    | Hardcoded label appears on the Add zone wizard             |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9746_   | Bug           | Critical | system-vm: logrotate config causes critical failures       |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9748_   | Bug           | Major    | VPN Users search functionality broken                      |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9751_   | Bug           | Major    | if a public IP is assigned to a VM when VR is in starting  |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9752_   | Improvement   | Major    | [Vmware] Optimization of volume attachness to vm           |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9757_   | Bug           | Major    | VPC traffic from vm to additional public subnet is not wor |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9765_   | Bug           | Major    | broken db.properties after upgrade                         |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9770_   | Bug           | Critical | Virtual router / Network regression since 4.9.1.0 with pub |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9783_   | Improvement   | Major    | Improve metrics view performance                           |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9784_   | Bug           | Major    | GPU detail not displayed in GPU tab of management server U |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9787_   | Bug           | Major    | No error message while change guest vm cidr to a large val |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9788_   | Bug           | Major    | Exception is throwed when list networks with pagesize is 0 |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9789_   | Bug           | Major    | Releasing secondary guest IP fails with error VM nic Ip x. |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9792_   | Bug           | Major    | Add 4.9.3.0 Upgrade path                                   |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9793_   | Bug           | Major    | Unnecessary conversion from IPNetwork to list causes route |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9794_   | Bug           | Major    | Unable to attach more than 14 devices to a VM              |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9796_   | Bug           | Minor    | Null Pointer Exception in VirtualMachineManagerImpl.java   |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9801_   | Bug           | Critical | IPSec VPN does not work after vRouter reboot or recreate   |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9805_   | Bug           | Major    | Show VRs in a tab for a network in network detail view     |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9811_   | Bug           | Blocker  | VR will not start, looking to configure eth3 while no such |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9814_   | Bug           | Major    | Unable to edit a Sub domain, which has the same name in di |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9821_   | Bug           | Blocker  | Unable to deploy user VM in Basic Zone                     |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9828_   | Bug           | Major    | .GetDomRVersionCommand failed while starting virtual route |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9830_   | Bug           | Minor    | QuotaAlertManagerTest fails testGetDifferenceDays on day b |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9831_   | Bug           | Major    | Previous pod_id still remains in the vm_instance table aft |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9834_   | Bug           | Major    | prepareTemplate API call doesn't work well with XenServer  |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9838_   | Bug           | Minor    | When 2 VMs have SNAT IPs assigned, they cannot communicate |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9842_   | Bug           | Major    | Unable to map root volume usage to VM                      |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9843_   | Bug           | Major    | Performance improvement of deployVirtualMachine, createFir |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9851_   | Bug           | Major    | travis CI build failure after merge of PR#1953             |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9857_   | Bug           | Critical | CloudStack KVM Agent Self Fencing  - improper systemd conf |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9860_   | Improvement   | Major    | CloudStack should be able to pass 'hard' shutdown instruct |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9871_   | Bug           | Minor    | MySQL 5.7 compatibility                                    |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9876_   | Bug           | Major    | Remove test_01_test_vm_volume_snapshot in test_vm_snapshot |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9900_   | Bug           | Major    | Fix high CPU deviation seen in Zone/Cluster metrics view   |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9904_   | Bug           | Major    | HyperV plugin created logs @AGENTLOG@                      |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9929_   | Bug           | Major    | Disk statistics fail to collect on Ubuntu 16.04            |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9935_   | Bug           | Major    | Search in VPN Customer Gateway not working                 |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9937_   | Bug           | Major    | dedicateCluster API response does not return correct detai |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9983_   | Bug           | Major    | Don't return username/password details in the listClusters |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-9985_   | Bug           | Major    | Allow admins to create roles with previously deleted role' |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-10011_  | Bug           | Minor    | Several issues with logrotation for CS Agents on Debians   |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-10016_  | Bug           | Major    | VPC VR doesn't respond to DNS requests from remote access  |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for router.aggregation.comman |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-10042_  | Bug           | Major    | UI doesn't show ICMP Type and Code for Security Group rule |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | CLOUDSTACK-10052_  | Bug           | Major    | Upgrading to 4.9.2 causes confusion/issues around dynamic  |
+--------------------+--------------------+---------------+----------+------------------------------------------------------------+

Issues Fixed in 4.9.2.0
-----------------------

.. cssclass:: table-striped table-bordered table-hover

+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| Branches           | Github   | Jira               | Type          | Priority | Description                                                |
+====================+==========+====================+===============+==========+============================================================+
| 4.9                | `#1764`_ | CLOUDSTACK-9597_   | Bug           | Major    | Incorrect updateResourceCount()                            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1781`_ | CLOUDSTACK-9612_   | Bug           | Major    | Restart Network with clean up fails for networks whose off |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1783`_ | CLOUDSTACK-9615_   | Bug           | Major    | Ingress Firewall Rules with blank start and End ports does |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1782`_ | CLOUDSTACK-9617_   | Bug           | Major    | Enabling Remote access Vpn Fails when there is a portforwa |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1804`_ | CLOUDSTACK-9639_   | Bug           | Major    | Unable to create shared network with vLan isolation        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1811`_ | CLOUDSTACK-9649_   | Bug           | Major    | In the management server log there is an error related to  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9662_   | Improvement   | Major    | Adding XenServer 7 support to Cloudstack                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1827`_ | CLOUDSTACK-9673_   | Bug           | Critical | Exception occured while creating the CPVM in the VmWare Se |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1828`_ | CLOUDSTACK-9676_   | Bug           | Critical | Start instance fails after reverting to a VM snapshot, whe |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1839`_ | CLOUDSTACK-9683_   | Bug           | Major    | system.vm.default.hypervisor Does Not Pin Hypervisor Type  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1846`_ | CLOUDSTACK-9688_   | Bug           | Major    | Fix smoke test failures for 4.9                            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+

Issues Fixed in 4.9.1.0
-----------------------

.. cssclass:: table-striped table-bordered table-hover

+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| Branches           | Github   | Jira               | Type          | Priority | Description                                                |
+====================+==========+====================+===============+==========+============================================================+
| 4.9                | `#1663`_ | CLOUDSTACK-6432_   | Bug           | Major    | Prevent VR from response to DNS request from outside of ne |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1743`_ | CLOUDSTACK-8326_   | Bug           | Major    | Bug in cloudstack virtual router (KVM) in Simple zone with |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#798`_  | CLOUDSTACK-8830_   | Bug           | Major    | [VMware] VM snapshot fails for 12 min after instance creat |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#828`_  | CLOUDSTACK-8854_   | Bug           | Major    | Apple Mac OS/X VM get created without USB controller in ES |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#896`_  | CLOUDSTACK-8908_   | Bug           | Major    | After copying the template charging for that template is s |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1673`_ | CLOUDSTACK-9071_   | Bug           | Major    | stats.output.uri stops the server from starting if the uri |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1240`_ | CLOUDSTACK-9161_   | Bug           | Critical | Quota Service: fix marvin test                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1744`_ | CLOUDSTACK-9183_   | Bug           | Major    | CS 4.7.0 bash: /opt/cloud/bin/getRouterAlerts.sh: No such  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1396`_ | CLOUDSTACK-9269_   | Bug           | Major    | Missing field for Switch type for Management and Storage t |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1659`_ | CLOUDSTACK-9339_   | Bug           | Major    | Virtual Routers don't handle Multiple Public Interfaces    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1696`_ | CLOUDSTACK-9364_   | Task          | Major    | Add Support for Ubuntu 16.04                               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9376_   | Bug           | Major    | Using the listTemplates API with the "templatefilter=all"  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1560`_ | CLOUDSTACK-9386_   | Bug           | Major    | DS template copies don’t get deleted in VMware ESXi with m |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1586`_ | CLOUDSTACK-9410_   | Bug           | Minor    | Data Disk shown as "detached" in XS                        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1785`_ | CLOUDSTACK-9416_   | Bug           | Major    | ACS master GUI: Enabling Static NAT on an associated Publi |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1621`_ | CLOUDSTACK-9444_   | Bug           | Minor    | ERROR c.c.u.d.DriverLoader DB driver type null is not supp |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9447_   | Bug           | Major    | Fix systemvm template build failure                        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1646`_ | CLOUDSTACK-9449_   | Bug           | Major    | Dynamic roles default user description typo and column iss |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1635`_ | CLOUDSTACK-9451_   | Bug           | Minor    | stopVirtualMachine ignores forced parameter                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1634`_ | CLOUDSTACK-9452_   | Bug           | Blocker  | CentOS6 kvm hosts stop working after upgrade               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1641`_ | CLOUDSTACK-9459_   | Bug           | Critical | Database upgrade from 3.0.7 to 4.9.0 fails with a ResultSe |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1674`_ | CLOUDSTACK-9460_   | Bug           | Major    | Graceful handling of Mysql server connection timeout       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1647`_ | CLOUDSTACK-9462_   | Bug           | Major    | Systemd packaging for Ubuntu 16.04                         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1649`_ | CLOUDSTACK-9463_   | Bug           | Major    | Dynamic roles migrate script fails with old commands.prope |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1656`_ | CLOUDSTACK-9466_   | Bug           | Major    | Upgrading to older CloudStack 4.0.x to 4.1.x causes sql co |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1657`_ | CLOUDSTACK-9467_   | Bug           | Blocker  | Fresh installation of cloudstack-usage server fails        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9468_   | Improvement   | Minor    | Alert code documentation out of sync with responses        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1660`_ | CLOUDSTACK-9470_   | Improvement   | Major    | [BLOCKER] Bug in SshHelper affecting interaction with vRou |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1666`_ | CLOUDSTACK-9480_   | Bug           | Critical | Egress Firewall: Incorrect use of Allow/Deny for ICMP      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1670`_ | CLOUDSTACK-9481_   | Bug           | Major    | Convert MyISAM table to InnoDB for consistency             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1684`_ | CLOUDSTACK-9489_   | Bug           | Blocker  | When upgrading, Config.java new configuration are not upda |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1681`_ | CLOUDSTACK-9491_   | Bug           | Major    | Vmware resource: incorrect parsing of device list to find  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9495_   | Bug           | Critical | Egress rules functionalty broken when protocol=all specifi |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1680`_ | CLOUDSTACK-9498_   | Bug           | Major    | VR CsFile search utility methods fail when search string h |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1676`_ | CLOUDSTACK-9502_   | Bug           | Major    | Target CLOUDSTACK-9386 into 4.9 release branch             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1745`_ | CLOUDSTACK-9503_   | Bug           | Major    | The router script times out resulting in failure of deploy |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1694`_ | CLOUDSTACK-9509_   | Bug           | Critical | KVM Hosts connect with no storage                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1724`_ | CLOUDSTACK-9511_   | Bug           | Critical | fix test_privategw_acl.py to handle multiple physical netw |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9514_   | Bug           | Critical | MarvinTests: some host credentials are hardcoded, make the |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9515_   | Bug           | Critical | internal LB vm is not handled when parsing cmd_line.json,  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9522_   | Bug           | Major    | Marvin common.py setNonContiguousVlanIds does not hanlde m |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9524_   | Bug           | Major    | Some marvin tests don't check hypervisor before executing  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9526_   | Bug           | Major    | Marvin test_deploy_vgpu_enabled_vm.py - Fix a hardcoded us |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9527_   | Bug           | Major    | test_01_test_vm_volume_snapshot making test negative again |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9529_   | Bug           | Major    | Marvin Tests do not clean up properly                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9531_   | Bug           | Major    | Fix tearDown issue in test_vpc_vpn.py                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9532_   | Bug           | Major    | Use macchinina as a template for failing tests             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9533_   | Bug           | Major    | gateway of public IP is not handled correctly when parsing |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1701`_ | CLOUDSTACK-9534_   | Bug           | Major    | Allow users to destroy VR when in running state            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1702`_ | CLOUDSTACK-9535_   | Improvement   | Major    | [API] listVMSnapshots improvement                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1710`_ | CLOUDSTACK-9538_   | Bug           | Major    | Deleting Snapshot From Primary Storage Fails on RBD Storag |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1742`_ | CLOUDSTACK-9544_   | Bug           | Major    | Account API keys vulnerability in Cloudstack with possible |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1712`_ | CLOUDSTACK-9550_   | Bug           | Major    | Metrics view does not filter items based on zone/cluster/h |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1728`_ | CLOUDSTACK-9551_   | Bug           | Major    | Pull KVM agent's tmp folder usage within its own folder st |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1713`_ | CLOUDSTACK-9552_   | Bug           | Major    | KVM Security Groups do not allow DNS over TCP egress       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1714`_ | CLOUDSTACK-9553_   | Bug           | Major    | Usage event is not getting recorded for snapshots in a spe |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1715`_ | CLOUDSTACK-9554_   | Bug           | Major    | Juniper Contrail plug-in is publishing events to wrong mes |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1737`_ | CLOUDSTACK-9561_   | Bug           | Major    | After domain/account deletion, snapshot taken by the domai |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1729`_ | CLOUDSTACK-9564_   | Bug           | Major    | Fix memory leak in VmwareContextPool                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1731`_ | CLOUDSTACK-9565_   | Bug           | Major    | Fix intermittent failure in oobm test test_oobm_zchange_pa |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1738`_ | CLOUDSTACK-9566_   | Bug           | Major    | instance-id metadata for baremetal VM returns ID           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1757`_ | CLOUDSTACK-9583_   | Bug           | Major    | VR: In CsDhcp.py preseed both hostaname and localhost to r |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1755`_ | CLOUDSTACK-9584_   | Bug           | Major    | Increase component tests coverage in Travis run            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1766`_ | CLOUDSTACK-9598_   | Bug           | Major    | wrong defaut gateway in guest VM with nics in isolated and |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1791`_ | CLOUDSTACK-9622_   | Improvement   | Trivial  | Localisation for 'Project' label on the top of Web UI      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1793`_ | CLOUDSTACK-9624_   | Bug           | Major    | Incorrect hypervisor mapping of guest os Windows 2008 Serv |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1796`_ | CLOUDSTACK-9626_   | Bug           | Major    | Instance fails to start after unsuccesful compute offering |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1799`_ | CLOUDSTACK-9632_   | Bug           | Major    | Upgrade bountycastle to 1.55+                              |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9634_   | Bug           | Major    | fix marvin test test_router_dhcp_opts failure              |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1802`_ | CLOUDSTACK-9635_   | Bug           | Major    | fix test_privategw_acl.py                                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                |          | CLOUDSTACK-9636_   | Bug           | Major    | The host alerts box should be named as hosts in Alerts.    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1805`_ | CLOUDSTACK-9637_   | Bug           | Major    | Template create from snapshot does not populate vm_templat |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1809`_ | CLOUDSTACK-9646_   | Bug           | Critical | [Usage] No usage is generated for uploaded templates/volum |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1808`_ | CLOUDSTACK-9648_   | Bug           | Major    | Checkstyle module version fails to update by build_asf.sh  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1817`_ | CLOUDSTACK-9654_   | Bug           | Major    | Missing hypervisor mapping of various SUSE Linux guest os  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1820`_ | CLOUDSTACK-9656_   | Bug           | Blocker  | Usage does not gather if you have a project with usage     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1821`_ | CLOUDSTACK-9659_   | Bug           | Major    | mismatch in traffic type in ip_associations.json and ips.j |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+


Issues Fixed in 4.9.0
-------------------------

.. cssclass:: table-striped table-bordered table-hover

+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| Branches           | Github   | Jira               | Type          | Priority | Description                                                |
+====================+==========+====================+===============+==========+============================================================+
| 4.9                | `#1616`_ |                    |               |          | Added missing rules on router config, fixed ordering of    |
|                    |          |                    |               |          | multiple rules                                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1613`_ | CLOUDSTACK-9436_   | Bug           | Major    | ``vm_network_map`` table cleanup on expunge command        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1583`_ |                    |               |          | Update L10N resource files with 4.9 strings from Transifex |
|                    |          |                    |               |          | (20160607)                                                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1610`_ |                    |               |          | Packaging: Add ``db.X.driver=jdbc:mysql`` to               |
|                    |          |                    |               |          | ``db.properties`` on upgrade                               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1609`_ | CLOUDSTACK-9430_   | Bug           | Major    | Adding a network ACL rule adds it in the wrong order for   |
|                    |          |                    |               |          | VPCs                                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1608`_ |                    |               |          | Cleanup RBD contexts after exceptions to prevent potential |
|                    |          |                    |               |          | agent crash                                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1601`_ | CLOUDSTACK-9348_   | Bug           | Major    | CloudStack Server degrades when a lot of connections on    |
|                    |          |                    |               |          | port 8250                                                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1595`_ |                    |               |          | UI: Show resize volume button to all users                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1455`_ | CLOUDSTACK-9328_   | Test          | Major    | Fix VLAN issues from test suite ``test_privategw_acl.py``  |
|                    |          |                    |               |          | in BVT                                                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1480`_ | CLOUDSTACK-9342_   | Bug           | Critical | PFS not being set correctly for S2S VPN Tunnel             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1598`_ | CLOUDSTACK-9423_   | Bug           | Major    | Object storage should get the correct size for compressed  |
|                    |          |                    |               |          | templates                                                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1547`_ |                    |               |          | Fixes for VirtualRouters in Basic Networking, especially   |
|                    |          |                    |               |          | with multiple ranges in VLANs                              |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1596`_ | CLOUDSTACK-9353_   | Bug           | Critical | NullPointerException when migrating VMs with local storage |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1581`_ | CLOUDSTACK-9404_   | Bug           | Major    | Network ACL rules in VPCs are applied in an inverted order |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1585`_ | CLOUDSTACK-9399_   | Bug           | Major    | NullPointerException when deleting Host                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1584`_ | CLOUDSTACK-9409_   | Bug           | Blocker  | Usage server fails to work with 4.9 due to missing         |
|                    |          |                    |               |          | ``role_id`` column                                         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1574`_ |                    |               |          | Make sure that the DB drivers are loaded before creating   |
|                    |          |                    |               |          | connections                                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1570`_ |                    |               |          | Travis: Use ``ipmitool`` from Ubuntu repository            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1569`_ |                    |               |          | Fix noredist build because of missing maven dependency of  |
|                    |          |                    |               |          | vmware 6.0 lib                                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1423`_ | CLOUDSTACK-9296_   | Bug           | Major    | IPsec doesn't get started when enabling client VPN gateway |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1251`_ | CLOUDSTACK-9180_   | Bug           | Major    | Optimize concurrent VM deployment operation on same        |
|                    |          |                    |               |          | network                                                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1567`_ | CLOUDSTACK-9238_   | Bug           | Major    | URL fields in database are to small. Cause malformed URLs  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1565`_ |                    |               |          | Add ``lsb-release`` dependency to mgmt server and agent on |
|                    |          |                    |               |          | Debian/Ubuntu.                                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1564`_ |                    |               |          | Emit template UUID and class type over event bus when      |
|                    |          |                    |               |          | deleting templates                                         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1561`_ | CLOUDSTACK-9388_   | Test          | Major    | Remove string conversion in Assertion statement            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1471`_ |                    |               |          | Lower the time we wait for interfaces to appear            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1518`_ | CLOUDSTACK-9368_   | Bug           | Major    | Fix for Support configurable NFS version for Secondary     |
|                    |          |                    |               |          | Storage mounts                                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1424`_ | CLOUDSTACK-8973_   | Bug           | Minor    | Unusual response when creating a template from a snapshot  |
|                    |          |                    |               |          | with Swift as secondary storage                            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1360`_ |                    |               |          | Re-factor system VM default network creation               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1552`_ |                    |               |          | Add DHCP lease folders for Ubuntu                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1556`_ |                    |               |          | Hyper-V communication broken by change in variable names   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1553`_ |                    |               |          | Dynamically load drivers before creating our DB            |
|                    |          |                    |               |          | connections                                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1297`_ | CLOUDSTACK-9203_   | New Feature   | Minor    | [API] extend ``updateVirtualMachine`` to support updating  |
|                    |          |                    |               |          | security groups                                            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1550`_ | CLOUDSTACK-9380_   | Bug           | Critical | ``listDomains`` API returns NPE if there is a failure in   |
|                    |          |                    |               |          | deleting domains                                           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1494`_ | CLOUDSTACK-9294_   | Bug           | Major    | Nuage Plugin: VR doesn't get removed from the VSD when     |
|                    |          |                    |               |          | destroying a VPC                                           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1555`_ |                    |               |          | Add Java Default Certificate Authorities into the keystore |
|                    |          |                    |               |          | if using a custom cert SSL                                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1533`_ |                    |               |          | Convert patchviasocket to python (removes perl dependency  |
|                    |          |                    |               |          | for KVM agent)                                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1503`_ | CLOUDSTACK-9358_   | Bug           | Critical | ``StringIndexOutOfBoundsException`` when publishing events |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#956`_  | CLOUDSTACK-8970_   | Bug           | Major    | CentOS 6.{1,2,3,4,5} guest OS mapping for VMware is not    |
|                    |          |                    |               |          | available                                                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#846`_  | CLOUDSTACK-8870_   | Bug           | Major    | External network device usage monitor runs even when there |
|                    |          |                    |               |          | are no external devices                                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1514`_ | CLOUDSTACK-6975_   | Bug           | Major    | Service monitoring starts ``dnsmasq`` on backup router     |
|                    |          |                    |               |          | when using redundant VRs                                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1410`_ | CLOUDSTACK-6928_   | Bug           | Critical | IOPS throttling setting isn't applied to a dynamically     |
|                    |          |                    |               |          | attached volume                                            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1549`_ | CLOUDSTACK-9348_   | Bug           | Major    | NioConnection improvements                                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1523`_ | CLOUDSTACK-9365_   | Bug           | Major    | ``updateVirtualMachine`` with ``userdata`` should not      |
|                    |          |                    |               |          | error when a VM is attached to multiple networks from      |
|                    |          |                    |               |          | which one or more doesn't support ``userdata``             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1403`_ |                    |               |          | Taking fast and efficient volume snapshots with XenServer  |
|                    |          |                    |               |          | (and your storage provider)                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1516`_ | CLOUDSTACK-9366_   | Bug           | Major    | Disable a host also disables storage pool capacity         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1551`_ |                    |               |          | Dynamic Roles: packaging improvements                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1540`_ | CLOUDSTACK-9377_   | Bug           | Major    | Metrics data incorrectly calculated in zone/cluster        |
|                    |          |                    |               |          | metrics view                                               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1414`_ |                    |               |          | SystemVM cleanups                                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9           | `#1513`_ | CLOUDSTACK-9362_   | Bug           | Major    | Migrating a VM using VXLANs and bridges fails              |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1331`_ |                    |               |          | Fix Sync of template.properties in Swift                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1486`_ |                    |               |          | Re-implement ``router.redundant.vrrp.interval`` setting    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1532`_ |                    |               |          | DAO: Hit the cache for entity flagged as removed too       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1537`_ |                    |               |          | Remove extraneous log directory and add ``catalina.out``   |
|                    |          |                    |               |          | log rotation                                               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1520`_ |                    |               |          | CPU socket count reporting correction                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1280`_ | CLOUDSTACK-9199_   | Bug           | Major    | ``deployVirtualMachine`` API does not throw an error when  |
|                    |          |                    |               |          | ``cpunumber`` is specified for static compute offering     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1376`_ |                    |               |          | L10n update master 20160127                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1543`_ |                    |               |          | Fix Nio/CPU issue and CI failures                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1536`_ |                    |               |          | Honour GS ``use_ext_dns`` and redundant VR VIP             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1460`_ | CLOUDSTACK-9334_   | Improvement   | Minor    | Support jenv and pyenv to manage Java and Python versions  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1444`_ | CLOUDSTACK-8800_   | Bug           | Major    | Improve the ``listVirtualMachines`` API call to include    |
|                    |          |                    |               |          | memory utilization information for a VM                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1453`_ |                    |               |          | Remove classes with no references                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1456`_ |                    |               |          | writeIfNotHere requires an array of strings, not a string  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1385`_ | CLOUDSTACK-9265_   | Bug           | Trivial  | Some java classes use ``commons-httpclient`` where         |
|                    |          |                    |               |          | ``httpcomponents`` is intended                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1528`_ | CLOUDSTACK-9373_   | Bug           | Major    | Marvin issue with class and instance methods named the     |
|                    |          |                    |               |          | same                                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#816`_  |                    |               |          | Notify listeners when a host has been added to a cluster,  |
|                    |          |                    |               |          | is about to be removed from a cluster, or has been removed |
|                    |          |                    |               |          | from a cluster                                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1502`_ | CLOUDSTACK-9299_   | New Feature   | Major    | Out-of-band Management for CloudStack                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1474`_ |                    |               |          | Handle private gateways more reliably                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1472`_ |                    |               |          | Apply static routes on change to master state              |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1483`_ | CLOUDSTACK-9287_   | Bug           | Critical | As an User I want to use Private Gateways with Redundant   |
|                    |          |                    |               |          | VPCs                                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1489`_ | CLOUDSTACK-8562_   | New Feature   | Major    | User Definable Roles                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1477`_ |                    |               |          | When no zone name is available display a default           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#880`_  | CLOUDSTACK-8901_   | Bug           | Major    | PrepareTemplate job thread hard-coded to max 8 threads     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1529`_ |                    |               |          | Marvin: Replace a ``timer.sleep(30)`` with pulling logic   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1466`_ | CLOUDSTACK-9340_   | Improvement   | Major    | General DB Optimization                                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1488`_ |                    |               |          | Agent: Enable IPv6 connectivity for KVM Agent to           |
|                    |          |                    |               |          | Management Server                                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1054`_ | CLOUDSTACK-8818_   | Improvement   | Major    | Python scripts should depend on ``mysql.connector``        |
|                    |          |                    |               |          | instead of ``MySQLdb``                                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1428`_ | CLOUDSTACK-9300_   | Bug           | Minor    | MySQL HA feature StaticStrategy throws exception           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1440`_ |                    |               |          | Removed Unused Void Class                                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1497`_ | CLOUDSTACK-9351_   | Improvement   | Major    | Add ids parameter to resource listing API calls            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1496`_ | CLOUDSTACK-9350_   | Bug           | Major    | Local storage hosts get HA tasks, cause issues             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1124`_ |                    |               |          | CID-1338387: Deletion of method                            |
|                    |          |                    |               |          | ``endPointSelector.selectHypervisorHost``                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9           | `#1515`_ |                    |               |          | L10n update 4.8 20160422                                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1527`_ |                    |               |          | Update L10N resource files with 4.7 strings from Transifex |
|                    |          |                    |               |          | (20160502)                                                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1408`_ |                    |               |          | KVM: Acquire lock when running security group Python       |
|                    |          |                    |               |          | script                                                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1463`_ | CLOUDSTACK-9336_   | Bug           | Trivial  | Run ``baremetal-vr.py`` only in (normal) routers           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1350`_ |                    |               |          | Quota: Consolidated lockable account check to a method.    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1230`_ | CLOUDSTACK-8302_   | Bug           | Critical | Cleanup snapshot on KVM with RBD                           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1433`_ | CLOUDSTACK-9305_   | Bug           | Major    | CloudStack Usage breaks with DB HA                         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1485`_ |                    |               |          | Set default networkDomain to empty instead of username     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1473`_ |                    |               |          | Bump ssh retries to prevent false positives of             |
|                    |          |                    |               |          | ``test_loadbalance``                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1321`_ | CLOUDSTACK-8847_   | Bug           | Major    | ``ListServiceOfferings`` is returning incompatible tagged  |
|                    |          |                    |               |          | offerings when called with VM id                           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1490`_ |                    |               |          | Installing bzip2 since it is required for extracting       |
|                    |          |                    |               |          | templates                                                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1365`_ |                    |               |          | [4.7] VMware: Improve support for disks                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1409`_ | CLOUDSTACK-9283_   | Bug           | Major    | ``cloudstack-usage`` fails to start throwing Integer       |
|                    |          |                    |               |          | exception during PID                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1517`_ |                    |               |          | Engine/Schema: Fix upgrade path to work with MySQL 5.7     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1454`_ | CLOUDSTACK-9323_   | Bug           | Major    | Canceling host maintenance results in "Internal error      |
|                    |          |                    |               |          | canceling maintenance."                                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1500`_ | CLOUDSTACK-9349_   | Bug           | Minor    | Unable to detach root volume when using Hypervisor Type    |
|                    |          |                    |               |          | KVM                                                        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1270`_ | CLOUDSTACK-9194_   | Bug           | Major    | Allow re-sizable windows in IE for VM console              |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1522`_ |                    |               |          | Log asynchronous responses in the API log                  |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1510`_ |                    |               |          | 4.9 mvn version safeupgradeonly                            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1348`_ | CLOUDSTACK-9142_   | Bug           | Critical | Migrate VM changes ``xmlDesc`` in an unsafe way            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#826`_  |                    |               |          | Fixed: Error given when creating VPN user in one network   |
|                    |          |                    |               |          | if VR for an other network is stopped.                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1498`_ | CLOUDSTACK-9352_   | Test          | Minor    | Test fails in Windows as the file separator "/" is         |
|                    |          |                    |               |          | different from "\"                                         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1458`_ | CLOUDSTACK-9331_   | Bug           | Major    | Automation: Prepare and add the baremetal cfg to           |
|                    |          |                    |               |          | marvin/config folder &marvin frame work changes to support |
|                    |          |                    |               |          | baremetal advanced testcase                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1452`_ | CLOUDSTACK-9322_   | Task          | Major    | Support for Internal LB functionality with Nuage VSP SDN   |
|                    |          |                    |               |          | Plugin including Marvin test coverage                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1271`_ | CLOUDSTACK-9164_   | Bug           | Major    | Consoleproxy does not prevent Firefox Quicksearch when     |
|                    |          |                    |               |          | typing slash                                               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#713`_  | CLOUDSTACK-8745_   | Bug           | Major    | After a volume is migrated; the usage table still shows    |
|                    |          |                    |               |          | the old volume id                                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1459`_ | CLOUDSTACK-8611_   | Bug           | Major    | CS waits indefinitely for                                  |
|                    |          |                    |               |          | ``CheckS2SVpnConnectionsCommand`` to return                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1308`_ |                    |               |          | Test to create VPN customer gateway with hostname          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1326`_ |                    |               |          | New test to validate starting VM after NIC removal and     |
|                    |          |                    |               |          | attach                                                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1126`_ | CLOUDSTACK-9088_   | Bug           | Major    | ``migrateto`` parameter associated with                    |
|                    |          |                    |               |          | ``migrateVirtualMachineWithVolume`` API needs an example   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1323`_ | CLOUDSTACK-9218_   | Test          | Major    | Test to verify restart network after master VR destroyed   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1501`_ |                    |               |          | Fixing an issue in Marvin around creating a template from  |
|                    |          |                    |               |          | a snapshot                                                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1200`_ | CLOUDSTACK-9130_   | Bug           | Major    | Make ``RebootCommand`` similar to start/stop/migrate agent |
|                    |          |                    |               |          | commands w.r.t. "execute in sequence" flag                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1505`_ | CLOUDSTACK-9172_   | Bug           | Major    | Templates registered with CrossZones cannot be deleted in  |
|                    |          |                    |               |          | UI                                                         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1402`_ |                    |               |          | Check the existence of ``forceencap`` parameter before use |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1420`_ |                    |               |          | systemvm: preserve file permissions, set default umask     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1157`_ | CLOUDSTACK-9100_   | Bug           | Major    | ISO.CREATE/TEMPLATE.CREATE event missing for usage_event   |
|                    |          |                    |               |          | by template sync thread                                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1398`_ | CLOUDSTACK-9270_   | Bug           | Major    | UI alignment gone bad in multiple places - VM Instance,    |
|                    |          |                    |               |          | Network, Egress rules                                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1399`_ | CLOUDSTACK-9272_   | Bug           | Major    | No option in UI to add GSLB with service type "HTTP"       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1394`_ | CLOUDSTACK-9268_   | Bug           | Major    | Display VM in Load balancing rule in UI                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1262`_ |                    |               |          | Removed unnecessary code from getGuestOsType in            |
|                    |          |                    |               |          | CitrixResourceBase                                         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1363`_ | CLOUDSTACK-9251_   | Bug           | Major    | Error while change instance offering to custom offering    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1263`_ |                    |               |          | Removed unused code from ``com.cloud.api.ApiServer``       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1445`_ |                    |               |          | Fixed Profiler's unit tests bugs.                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1487`_ |                    |               |          | Speedup iptables by prefetching the variables              |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1479`_ | CLOUDSTACK-9285_   | Bug           | Blocker  | CloudStack 4.8 can't connect to XEN and KVM hosts          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1287`_ |                    |               |          | ``SecurityGroupRulesCmd`` code cleanup                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1422`_ |                    |               |          | Improve ordering of fields of VPC router detail tab        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1441`_ | CLOUDSTACK-9297_   | Bug           | Major    | Delete snapshot without id is failing with Unable to       |
|                    |          |                    |               |          | determine the storage pool of the snapshot                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1462`_ | CLOUDSTACK-9335_   | Bug           | Minor    | CloudStack UI has a typo and does not send                 |
|                    |          |                    |               |          | ``fetchlatest=true`` correctly to ``listCapacity``         |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1316`_ | CLOUDSTACK-9215_   | Test          | Major    | Marvin test to check VM deployment in VPC tier if NIC type |
|                    |          |                    |               |          | is ``vmxnet3``                                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1481`_ |                    |               |          | Travis: Increase build verbosity                           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1457`_ | CLOUDSTACK-9333_   | Bug           | Major    | Exclude clusters from OVF operations                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1254`_ | CLOUDSTACK-9174_   | Bug           | Critical | Quota Service: When a account/user is deleted with low     |
|                    |          |                    |               |          | quota, quota service still tries to alert the user         |
|                    |          |                    |               |          | resulting in NPE                                           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1461`_ |                    |               |          | Travis: Fix simulator tests and optimize default global    |
|                    |          |                    |               |          | configs                                                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1332`_ |                    |               |          | Add ability to download templates in Swift                 |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1425`_ | CLOUDSTACK-9298_   | Improvement   | Major    | Improve performance of resource retrieval that have tags   |
|                    |          |                    |               |          | associated and target volumes, VMs and templates           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1438`_ |                    |               |          | Fix new error found in findbugs slow build #3455           |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1430`_ | CLOUDSTACK-9285_   | Bug           | Blocker  | CloudStack 4.8 can't connect to XEN and KVM hosts          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1431`_ | CLOUDSTACK-9304_   | Task          | Major    | Add nuagevsp userdata testcase (Cloudstack-9095) &         |
|                    |          |                    |               |          | Refactor existing testcases                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1434`_ |                    |               |          | Change variable ``ROOK_DISK_CONTROLLER`` to                |
|                    |          |                    |               |          | ``ROOT_DISK_CONTROLLER``                                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1426`_ |                    |               |          | ADD be explicit about the underlying limitation - OpenSwan |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1390`_ | CLOUDSTACK-9267_   | Bug           | Major    | String is not localized on create instance wizards.        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1078`_ | CLOUDSTACK-9066_   | Improvement   | Major    | Update testpath to delete account after deleting VM's of   |
|                    |          |                    |               |          | that account                                               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1361`_ | CLOUDSTACK-9252_   | Bug           | Major    | Support configurable NFS version for Secondary Storage     |
|                    |          |                    |               |          | mounts                                                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1218`_ | CLOUDSTACK-9140_   | Test          | Major    | Testcase to verify if Dedicated cluster is used for        |
|                    |          |                    |               |          | virtual routers that belong to non-dedicated account       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1310`_ | CLOUDSTACK-9211_   | Bug           | Major    | Support passing vRAM size over to Esxi hypervisor to       |
|                    |          |                    |               |          | support 3D GPU on VMware                                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1031`_ | CLOUDSTACK-9026_   | Improvement   | Major    | Modifying testpath for adding missing parameter            |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1130`_ | CLOUDSTACK-9091_   | Improvement   | Major    | Update testpath for parameter issues                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1199`_ | CLOUDSTACK-9128_   | Bug           | Major    | Testcase to verify if ``snapshot_store_ref`` table stores  |
|                    |          |                    |               |          | actual size of back snapshot in secondary storage          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#684`_  | CLOUDSTACK-8728_   | Test          | Major    | Testcase to Verify if VRs IP changes if it is destroyed    |
|                    |          |                    |               |          | and re-created in Basic Zone                               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1190`_ | CLOUDSTACK-9121_   | Improvement   | Major    | Adding VmSnapshot validation in                            |
|                    |          |                    |               |          | ``testpath_revert_snap.py``                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#869`_  | CLOUDSTACK-8895_   | Test          | Major    | Verify if storage can be selected when attaching uploaded  |
|                    |          |                    |               |          | data volume to VM                                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1386`_ | CLOUDSTACK-9266_   | Bug           | Critical | Delete static route on private gateway doesn't actually    |
|                    |          |                    |               |          | delete it on the router                                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1383`_ | CLOUDSTACK-9264_   | Bug           | Critical | Create of /32 static route on private gateway fails        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1384`_ |                    |               |          | Display hostname the VPC router runs on                    |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1387`_ | CLOUDSTACK-8300_   | Bug           | Minor    | Add index on archived field in ``cloud.event`` table       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.6, 4.7, 4.8, 4.9 | `#1342`_ | CLOUDSTACK-6181_   | New Feature   | Major    | Root resize                                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1288`_ |                    |               |          | Trailing commas in javascripts removed                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1274`_ | CLOUDSTACK-9196_   | Bug           | Major    | ``NullPointerException`` in some scenarios while syncing   |
|                    |          |                    |               |          | VM metadata                                                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1261`_ |                    |               |          | Removed unused variables from ``NetworkStateListener``     |
|                    |          |                    |               |          | class                                                      |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1048`_ | CLOUDSTACK-8731_   | Test          | Major    | Automation: Checking usage event generation for delete     |
|                    |          |                    |               |          | volume                                                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1044`_ | CLOUDSTACK-5822_   | Bug           | Major    | SSH keypairs are removed after rebooting VM                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#969`_  |                    |               |          | Fixed return type ``Void`` to ``void`` in                  |
|                    |          |                    |               |          | ``DataMotionStrategy``                                     |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#855`_  |                    |               |          | Removal of class                                           |
|                    |          |                    |               |          | ``AgentBasedStandaloneConsoleProxyManager``                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#831`_  | CLOUDSTACK-8850_   | Bug           | Major    | ``revertSnapshot`` command does not work                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#830`_  | CLOUDSTACK-8858_   | Bug           | Major    | ``listVolumes`` API fails for a particular domain with NPE |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1256`_ | CLOUDSTACK-9185_   | Bug           | Major    | [VMware DRS] VM sync failed with exception due to          |
|                    |          |                    |               |          | out-of-band changes                                        |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1240`_ | CLOUDSTACK-9161_   | Bug           | Critical | Quota Service: Fix marvin test                             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1289`_ |                    |               |          | Quota: findbug fixes                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1364`_ | CLOUDSTACK-9256_   | Bug           | Major    | Static routes get lost after network restart               |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1369`_ |                    |               |          | Set version to 4.9.0-SNAPSHOT in master branch             |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9           | `#1368`_ |                    |               |          | Set version to 4.8.1-SNAPSHOT in 4.8 branch                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1367`_ |                    |               |          | Set version to 4.7.2-SNAPSHOT in 4.7 branch                |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1358`_ | CLOUDSTACK-9245_   | Improvement   | Major    | As an User I want to be able to delete non-attached ACL    |
|                    |          |                    |               |          | lists that contain items                                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1362`_ | CLOUDSTACK-9254_   | Bug           | Major    | Name of logged in user in UI is not always lined out       |
|                    |          |                    |               |          | properly                                                   |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9                | `#1354`_ |                    |               |          | UI: improve filter dropdown width                          |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9      | `#1356`_ |                    |               |          | More VR performance!                                       |
+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+

.. _`#1616`: https://github.com/apache/cloudstack/pull/1616
.. _`#1613`: https://github.com/apache/cloudstack/pull/1613
.. _CLOUDSTACK-9436: https://issues.apache.org/jira/browse/CLOUDSTACK-9436
.. _`#1583`: https://github.com/apache/cloudstack/pull/1583
.. _`#1610`: https://github.com/apache/cloudstack/pull/1610
.. _`#1609`: https://github.com/apache/cloudstack/pull/1609
.. _CLOUDSTACK-9430: https://issues.apache.org/jira/browse/CLOUDSTACK-9430
.. _`#1608`: https://github.com/apache/cloudstack/pull/1608
.. _`#1601`: https://github.com/apache/cloudstack/pull/1601
.. _CLOUDSTACK-9348: https://issues.apache.org/jira/browse/CLOUDSTACK-9348
.. _`#1595`: https://github.com/apache/cloudstack/pull/1595
.. _`#1455`: https://github.com/apache/cloudstack/pull/1455
.. _CLOUDSTACK-9328: https://issues.apache.org/jira/browse/CLOUDSTACK-9328
.. _`#1480`: https://github.com/apache/cloudstack/pull/1480
.. _CLOUDSTACK-9342: https://issues.apache.org/jira/browse/CLOUDSTACK-9342
.. _`#1598`: https://github.com/apache/cloudstack/pull/1598
.. _CLOUDSTACK-9423: https://issues.apache.org/jira/browse/CLOUDSTACK-9423
.. _`#1547`: https://github.com/apache/cloudstack/pull/1547
.. _`#1596`: https://github.com/apache/cloudstack/pull/1596
.. _CLOUDSTACK-9353: https://issues.apache.org/jira/browse/CLOUDSTACK-9353
.. _`#1581`: https://github.com/apache/cloudstack/pull/1581
.. _CLOUDSTACK-9404: https://issues.apache.org/jira/browse/CLOUDSTACK-9404
.. _`#1585`: https://github.com/apache/cloudstack/pull/1585
.. _CLOUDSTACK-9399: https://issues.apache.org/jira/browse/CLOUDSTACK-9399
.. _`#1584`: https://github.com/apache/cloudstack/pull/1584
.. _CLOUDSTACK-9409: https://issues.apache.org/jira/browse/CLOUDSTACK-9409
.. _`#1574`: https://github.com/apache/cloudstack/pull/1574
.. _`#1570`: https://github.com/apache/cloudstack/pull/1570
.. _`#1569`: https://github.com/apache/cloudstack/pull/1569
.. _`#1423`: https://github.com/apache/cloudstack/pull/1423
.. _CLOUDSTACK-9296: https://issues.apache.org/jira/browse/CLOUDSTACK-9296
.. _`#1251`: https://github.com/apache/cloudstack/pull/1251
.. _CLOUDSTACK-9180: https://issues.apache.org/jira/browse/CLOUDSTACK-9180
.. _`#1567`: https://github.com/apache/cloudstack/pull/1567
.. _CLOUDSTACK-9238: https://issues.apache.org/jira/browse/CLOUDSTACK-9238
.. _`#1565`: https://github.com/apache/cloudstack/pull/1565
.. _`#1564`: https://github.com/apache/cloudstack/pull/1564
.. _`#1561`: https://github.com/apache/cloudstack/pull/1561
.. _CLOUDSTACK-9388: https://issues.apache.org/jira/browse/CLOUDSTACK-9388
.. _`#1471`: https://github.com/apache/cloudstack/pull/1471
.. _`#1518`: https://github.com/apache/cloudstack/pull/1518
.. _CLOUDSTACK-9368: https://issues.apache.org/jira/browse/CLOUDSTACK-9368
.. _`#1424`: https://github.com/apache/cloudstack/pull/1424
.. _CLOUDSTACK-8973: https://issues.apache.org/jira/browse/CLOUDSTACK-8973
.. _`#1360`: https://github.com/apache/cloudstack/pull/1360
.. _`#1552`: https://github.com/apache/cloudstack/pull/1552
.. _`#1556`: https://github.com/apache/cloudstack/pull/1556
.. _`#1553`: https://github.com/apache/cloudstack/pull/1553
.. _`#1297`: https://github.com/apache/cloudstack/pull/1297
.. _CLOUDSTACK-9203: https://issues.apache.org/jira/browse/CLOUDSTACK-9203
.. _`#1550`: https://github.com/apache/cloudstack/pull/1550
.. _CLOUDSTACK-9380: https://issues.apache.org/jira/browse/CLOUDSTACK-9380
.. _`#1494`: https://github.com/apache/cloudstack/pull/1494
.. _CLOUDSTACK-9294: https://issues.apache.org/jira/browse/CLOUDSTACK-9294
.. _`#1555`: https://github.com/apache/cloudstack/pull/1555
.. _`#1533`: https://github.com/apache/cloudstack/pull/1533
.. _`#1503`: https://github.com/apache/cloudstack/pull/1503
.. _CLOUDSTACK-9358: https://issues.apache.org/jira/browse/CLOUDSTACK-9358
.. _`#956`: https://github.com/apache/cloudstack/pull/956
.. _CLOUDSTACK-8970: https://issues.apache.org/jira/browse/CLOUDSTACK-8970
.. _`#846`: https://github.com/apache/cloudstack/pull/846
.. _CLOUDSTACK-8870: https://issues.apache.org/jira/browse/CLOUDSTACK-8870
.. _`#1514`: https://github.com/apache/cloudstack/pull/1514
.. _CLOUDSTACK-6975: https://issues.apache.org/jira/browse/CLOUDSTACK-6975
.. _`#1410`: https://github.com/apache/cloudstack/pull/1410
.. _CLOUDSTACK-6928: https://issues.apache.org/jira/browse/CLOUDSTACK-6928
.. _`#1549`: https://github.com/apache/cloudstack/pull/1549
.. _CLOUDSTACK-9348: https://issues.apache.org/jira/browse/CLOUDSTACK-9348
.. _`#1523`: https://github.com/apache/cloudstack/pull/1523
.. _CLOUDSTACK-9365: https://issues.apache.org/jira/browse/CLOUDSTACK-9365
.. _`#1403`: https://github.com/apache/cloudstack/pull/1403
.. _`#1516`: https://github.com/apache/cloudstack/pull/1516
.. _CLOUDSTACK-9366: https://issues.apache.org/jira/browse/CLOUDSTACK-9366
.. _`#1551`: https://github.com/apache/cloudstack/pull/1551
.. _`#1540`: https://github.com/apache/cloudstack/pull/1540
.. _CLOUDSTACK-9377: https://issues.apache.org/jira/browse/CLOUDSTACK-9377
.. _`#1414`: https://github.com/apache/cloudstack/pull/1414
.. _`#1513`: https://github.com/apache/cloudstack/pull/1513
.. _CLOUDSTACK-9362: https://issues.apache.org/jira/browse/CLOUDSTACK-9362
.. _`#1331`: https://github.com/apache/cloudstack/pull/1331
.. _`#1486`: https://github.com/apache/cloudstack/pull/1486
.. _`#1495`: https://github.com/apache/cloudstack/pull/1495
.. _`#1532`: https://github.com/apache/cloudstack/pull/1532
.. _`#1537`: https://github.com/apache/cloudstack/pull/1537
.. _`#1520`: https://github.com/apache/cloudstack/pull/1520
.. _`#1280`: https://github.com/apache/cloudstack/pull/1280
.. _CLOUDSTACK-9199: https://issues.apache.org/jira/browse/CLOUDSTACK-9199
.. _`#1376`: https://github.com/apache/cloudstack/pull/1376
.. _`#1543`: https://github.com/apache/cloudstack/pull/1543
.. _`#1536`: https://github.com/apache/cloudstack/pull/1536
.. _`#1460`: https://github.com/apache/cloudstack/pull/1460
.. _CLOUDSTACK-9334: https://issues.apache.org/jira/browse/CLOUDSTACK-9334
.. _`#1444`: https://github.com/apache/cloudstack/pull/1444
.. _CLOUDSTACK-8800: https://issues.apache.org/jira/browse/CLOUDSTACK-8800
.. _`#1453`: https://github.com/apache/cloudstack/pull/1453
.. _`#1456`: https://github.com/apache/cloudstack/pull/1456
.. _`#1385`: https://github.com/apache/cloudstack/pull/1385
.. _CLOUDSTACK-9265: https://issues.apache.org/jira/browse/CLOUDSTACK-9265
.. _`#1528`: https://github.com/apache/cloudstack/pull/1528
.. _CLOUDSTACK-9373: https://issues.apache.org/jira/browse/CLOUDSTACK-9373
.. _`#816`: https://github.com/apache/cloudstack/pull/816
.. _`#1502`: https://github.com/apache/cloudstack/pull/1502
.. _CLOUDSTACK-9299: https://issues.apache.org/jira/browse/CLOUDSTACK-9299
.. _`#1474`: https://github.com/apache/cloudstack/pull/1474
.. _`#1472`: https://github.com/apache/cloudstack/pull/1472
.. _`#1483`: https://github.com/apache/cloudstack/pull/1483
.. _CLOUDSTACK-9287: https://issues.apache.org/jira/browse/CLOUDSTACK-9287
.. _`#1489`: https://github.com/apache/cloudstack/pull/1489
.. _CLOUDSTACK-8562: https://issues.apache.org/jira/browse/CLOUDSTACK-8562
.. _`#1477`: https://github.com/apache/cloudstack/pull/1477
.. _`#880`: https://github.com/apache/cloudstack/pull/880
.. _CLOUDSTACK-8901: https://issues.apache.org/jira/browse/CLOUDSTACK-8901
.. _`#1529`: https://github.com/apache/cloudstack/pull/1529
.. _`#1466`: https://github.com/apache/cloudstack/pull/1466
.. _CLOUDSTACK-9340: https://issues.apache.org/jira/browse/CLOUDSTACK-9340
.. _`#1488`: https://github.com/apache/cloudstack/pull/1488
.. _`#1054`: https://github.com/apache/cloudstack/pull/1054
.. _CLOUDSTACK-8818: https://issues.apache.org/jira/browse/CLOUDSTACK-8818
.. _`#1428`: https://github.com/apache/cloudstack/pull/1428
.. _CLOUDSTACK-9300: https://issues.apache.org/jira/browse/CLOUDSTACK-9300
.. _`#1440`: https://github.com/apache/cloudstack/pull/1440
.. _`#1497`: https://github.com/apache/cloudstack/pull/1497
.. _CLOUDSTACK-9351: https://issues.apache.org/jira/browse/CLOUDSTACK-9351
.. _`#1496`: https://github.com/apache/cloudstack/pull/1496
.. _CLOUDSTACK-9350: https://issues.apache.org/jira/browse/CLOUDSTACK-9350
.. _`#1124`: https://github.com/apache/cloudstack/pull/1124
.. _`#1515`: https://github.com/apache/cloudstack/pull/1515
.. _`#1527`: https://github.com/apache/cloudstack/pull/1527
.. _`#1408`: https://github.com/apache/cloudstack/pull/1408
.. _`#1463`: https://github.com/apache/cloudstack/pull/1463
.. _CLOUDSTACK-9336: https://issues.apache.org/jira/browse/CLOUDSTACK-9336
.. _`#1350`: https://github.com/apache/cloudstack/pull/1350
.. _`#1230`: https://github.com/apache/cloudstack/pull/1230
.. _CLOUDSTACK-8302: https://issues.apache.org/jira/browse/CLOUDSTACK-8302
.. _`#1433`: https://github.com/apache/cloudstack/pull/1433
.. _CLOUDSTACK-9305: https://issues.apache.org/jira/browse/CLOUDSTACK-9305
.. _`#1485`: https://github.com/apache/cloudstack/pull/1485
.. _`#1473`: https://github.com/apache/cloudstack/pull/1473
.. _`#1321`: https://github.com/apache/cloudstack/pull/1321
.. _CLOUDSTACK-8847: https://issues.apache.org/jira/browse/CLOUDSTACK-8847
.. _`#1490`: https://github.com/apache/cloudstack/pull/1490
.. _`#1365`: https://github.com/apache/cloudstack/pull/1365
.. _`#1409`: https://github.com/apache/cloudstack/pull/1409
.. _CLOUDSTACK-9283: https://issues.apache.org/jira/browse/CLOUDSTACK-9283
.. _`#1517`: https://github.com/apache/cloudstack/pull/1517
.. _`#1454`: https://github.com/apache/cloudstack/pull/1454
.. _CLOUDSTACK-9323: https://issues.apache.org/jira/browse/CLOUDSTACK-9323
.. _`#1500`: https://github.com/apache/cloudstack/pull/1500
.. _CLOUDSTACK-9349: https://issues.apache.org/jira/browse/CLOUDSTACK-9349
.. _`#1270`: https://github.com/apache/cloudstack/pull/1270
.. _CLOUDSTACK-9194: https://issues.apache.org/jira/browse/CLOUDSTACK-9194
.. _`#1522`: https://github.com/apache/cloudstack/pull/1522
.. _`#1510`: https://github.com/apache/cloudstack/pull/1510
.. _`#1348`: https://github.com/apache/cloudstack/pull/1348
.. _CLOUDSTACK-9142: https://issues.apache.org/jira/browse/CLOUDSTACK-9142
.. _`#826`: https://github.com/apache/cloudstack/pull/826
.. _`#1498`: https://github.com/apache/cloudstack/pull/1498
.. _CLOUDSTACK-9352: https://issues.apache.org/jira/browse/CLOUDSTACK-9352
.. _`#1458`: https://github.com/apache/cloudstack/pull/1458
.. _CLOUDSTACK-9331: https://issues.apache.org/jira/browse/CLOUDSTACK-9331
.. _`#1452`: https://github.com/apache/cloudstack/pull/1452
.. _CLOUDSTACK-9322: https://issues.apache.org/jira/browse/CLOUDSTACK-9322
.. _`#1271`: https://github.com/apache/cloudstack/pull/1271
.. _CLOUDSTACK-9164: https://issues.apache.org/jira/browse/CLOUDSTACK-9164
.. _`#713`: https://github.com/apache/cloudstack/pull/713
.. _CLOUDSTACK-8745: https://issues.apache.org/jira/browse/CLOUDSTACK-8745
.. _`#1459`: https://github.com/apache/cloudstack/pull/1459
.. _CLOUDSTACK-8611: https://issues.apache.org/jira/browse/CLOUDSTACK-8611
.. _`#1308`: https://github.com/apache/cloudstack/pull/1308
.. _`#1326`: https://github.com/apache/cloudstack/pull/1326
.. _`#1126`: https://github.com/apache/cloudstack/pull/1126
.. _CLOUDSTACK-9088: https://issues.apache.org/jira/browse/CLOUDSTACK-9088
.. _`#1323`: https://github.com/apache/cloudstack/pull/1323
.. _CLOUDSTACK-9218: https://issues.apache.org/jira/browse/CLOUDSTACK-9218
.. _`#1501`: https://github.com/apache/cloudstack/pull/1501
.. _`#1200`: https://github.com/apache/cloudstack/pull/1200
.. _CLOUDSTACK-9130: https://issues.apache.org/jira/browse/CLOUDSTACK-9130
.. _`#1505`: https://github.com/apache/cloudstack/pull/1505
.. _CLOUDSTACK-9172: https://issues.apache.org/jira/browse/CLOUDSTACK-9172
.. _`#1402`: https://github.com/apache/cloudstack/pull/1402
.. _`#1420`: https://github.com/apache/cloudstack/pull/1420
.. _`#1157`: https://github.com/apache/cloudstack/pull/1157
.. _CLOUDSTACK-9100: https://issues.apache.org/jira/browse/CLOUDSTACK-9100
.. _`#1398`: https://github.com/apache/cloudstack/pull/1398
.. _CLOUDSTACK-9270: https://issues.apache.org/jira/browse/CLOUDSTACK-9270
.. _`#1399`: https://github.com/apache/cloudstack/pull/1399
.. _CLOUDSTACK-9272: https://issues.apache.org/jira/browse/CLOUDSTACK-9272
.. _`#1394`: https://github.com/apache/cloudstack/pull/1394
.. _CLOUDSTACK-9268: https://issues.apache.org/jira/browse/CLOUDSTACK-9268
.. _`#1262`: https://github.com/apache/cloudstack/pull/1262
.. _`#1363`: https://github.com/apache/cloudstack/pull/1363
.. _CLOUDSTACK-9251: https://issues.apache.org/jira/browse/CLOUDSTACK-9251
.. _`#1263`: https://github.com/apache/cloudstack/pull/1263
.. _`#1445`: https://github.com/apache/cloudstack/pull/1445
.. _`#1487`: https://github.com/apache/cloudstack/pull/1487
.. _`#1479`: https://github.com/apache/cloudstack/pull/1479
.. _CLOUDSTACK-9285: https://issues.apache.org/jira/browse/CLOUDSTACK-9285
.. _`#1287`: https://github.com/apache/cloudstack/pull/1287
.. _`#1422`: https://github.com/apache/cloudstack/pull/1422
.. _`#1441`: https://github.com/apache/cloudstack/pull/1441
.. _CLOUDSTACK-9297: https://issues.apache.org/jira/browse/CLOUDSTACK-9297
.. _`#1462`: https://github.com/apache/cloudstack/pull/1462
.. _CLOUDSTACK-9335: https://issues.apache.org/jira/browse/CLOUDSTACK-9335
.. _`#1316`: https://github.com/apache/cloudstack/pull/1316
.. _CLOUDSTACK-9215: https://issues.apache.org/jira/browse/CLOUDSTACK-9215
.. _`#1481`: https://github.com/apache/cloudstack/pull/1481
.. _`#1457`: https://github.com/apache/cloudstack/pull/1457
.. _CLOUDSTACK-9333: https://issues.apache.org/jira/browse/CLOUDSTACK-9333
.. _`#1254`: https://github.com/apache/cloudstack/pull/1254
.. _CLOUDSTACK-9174: https://issues.apache.org/jira/browse/CLOUDSTACK-9174
.. _`#1461`: https://github.com/apache/cloudstack/pull/1461
.. _`#1332`: https://github.com/apache/cloudstack/pull/1332
.. _`#1425`: https://github.com/apache/cloudstack/pull/1425
.. _CLOUDSTACK-9298: https://issues.apache.org/jira/browse/CLOUDSTACK-9298
.. _`#1438`: https://github.com/apache/cloudstack/pull/1438
.. _`#1430`: https://github.com/apache/cloudstack/pull/1430
.. _CLOUDSTACK-9285: https://issues.apache.org/jira/browse/CLOUDSTACK-9285
.. _`#1431`: https://github.com/apache/cloudstack/pull/1431
.. _CLOUDSTACK-9304: https://issues.apache.org/jira/browse/CLOUDSTACK-9304
.. _`#1434`: https://github.com/apache/cloudstack/pull/1434
.. _`#1426`: https://github.com/apache/cloudstack/pull/1426
.. _`#1390`: https://github.com/apache/cloudstack/pull/1390
.. _CLOUDSTACK-9267: https://issues.apache.org/jira/browse/CLOUDSTACK-9267
.. _`#1078`: https://github.com/apache/cloudstack/pull/1078
.. _CLOUDSTACK-9066: https://issues.apache.org/jira/browse/CLOUDSTACK-9066
.. _`#1361`: https://github.com/apache/cloudstack/pull/1361
.. _CLOUDSTACK-9252: https://issues.apache.org/jira/browse/CLOUDSTACK-9252
.. _`#1218`: https://github.com/apache/cloudstack/pull/1218
.. _CLOUDSTACK-9140: https://issues.apache.org/jira/browse/CLOUDSTACK-9140
.. _`#1310`: https://github.com/apache/cloudstack/pull/1310
.. _CLOUDSTACK-9211: https://issues.apache.org/jira/browse/CLOUDSTACK-9211
.. _`#1031`: https://github.com/apache/cloudstack/pull/1031
.. _CLOUDSTACK-9026: https://issues.apache.org/jira/browse/CLOUDSTACK-9026
.. _`#1130`: https://github.com/apache/cloudstack/pull/1130
.. _CLOUDSTACK-9091: https://issues.apache.org/jira/browse/CLOUDSTACK-9091
.. _`#1199`: https://github.com/apache/cloudstack/pull/1199
.. _CLOUDSTACK-9128: https://issues.apache.org/jira/browse/CLOUDSTACK-9128
.. _`#684`: https://github.com/apache/cloudstack/pull/684
.. _CLOUDSTACK-8728: https://issues.apache.org/jira/browse/CLOUDSTACK-8728
.. _`#1190`: https://github.com/apache/cloudstack/pull/1190
.. _CLOUDSTACK-9121: https://issues.apache.org/jira/browse/CLOUDSTACK-9121
.. _`#869`: https://github.com/apache/cloudstack/pull/869
.. _CLOUDSTACK-8895: https://issues.apache.org/jira/browse/CLOUDSTACK-8895
.. _`#1386`: https://github.com/apache/cloudstack/pull/1386
.. _CLOUDSTACK-9266: https://issues.apache.org/jira/browse/CLOUDSTACK-9266
.. _`#1383`: https://github.com/apache/cloudstack/pull/1383
.. _CLOUDSTACK-9264: https://issues.apache.org/jira/browse/CLOUDSTACK-9264
.. _`#1384`: https://github.com/apache/cloudstack/pull/1384
.. _`#1387`: https://github.com/apache/cloudstack/pull/1387
.. _CLOUDSTACK-8300: https://issues.apache.org/jira/browse/CLOUDSTACK-8300
.. _`#1342`: https://github.com/apache/cloudstack/pull/1342
.. _CLOUDSTACK-6181: https://issues.apache.org/jira/browse/CLOUDSTACK-6181
.. _`#1288`: https://github.com/apache/cloudstack/pull/1288
.. _`#1274`: https://github.com/apache/cloudstack/pull/1274
.. _CLOUDSTACK-9196: https://issues.apache.org/jira/browse/CLOUDSTACK-9196
.. _`#1261`: https://github.com/apache/cloudstack/pull/1261
.. _`#1048`: https://github.com/apache/cloudstack/pull/1048
.. _CLOUDSTACK-8731: https://issues.apache.org/jira/browse/CLOUDSTACK-8731
.. _`#1044`: https://github.com/apache/cloudstack/pull/1044
.. _CLOUDSTACK-5822: https://issues.apache.org/jira/browse/CLOUDSTACK-5822
.. _`#969`: https://github.com/apache/cloudstack/pull/969
.. _`#855`: https://github.com/apache/cloudstack/pull/855
.. _`#831`: https://github.com/apache/cloudstack/pull/831
.. _CLOUDSTACK-8850: https://issues.apache.org/jira/browse/CLOUDSTACK-8850
.. _`#830`: https://github.com/apache/cloudstack/pull/830
.. _CLOUDSTACK-8858: https://issues.apache.org/jira/browse/CLOUDSTACK-8858
.. _`#1256`: https://github.com/apache/cloudstack/pull/1256
.. _CLOUDSTACK-9185: https://issues.apache.org/jira/browse/CLOUDSTACK-9185
.. _`#1240`: https://github.com/apache/cloudstack/pull/1240
.. _CLOUDSTACK-9161: https://issues.apache.org/jira/browse/CLOUDSTACK-9161
.. _`#1289`: https://github.com/apache/cloudstack/pull/1289
.. _`#1364`: https://github.com/apache/cloudstack/pull/1364
.. _CLOUDSTACK-9256: https://issues.apache.org/jira/browse/CLOUDSTACK-9256
.. _`#1369`: https://github.com/apache/cloudstack/pull/1369
.. _`#1368`: https://github.com/apache/cloudstack/pull/1368
.. _`#1367`: https://github.com/apache/cloudstack/pull/1367
.. _`#1358`: https://github.com/apache/cloudstack/pull/1358
.. _CLOUDSTACK-9245: https://issues.apache.org/jira/browse/CLOUDSTACK-9245
.. _`#1362`: https://github.com/apache/cloudstack/pull/1362
.. _CLOUDSTACK-9254: https://issues.apache.org/jira/browse/CLOUDSTACK-9254
.. _`#1354`: https://github.com/apache/cloudstack/pull/1354
.. _`#1356`: https://github.com/apache/cloudstack/pull/1356
.. _CLOUDSTACK-6432: https://issues.apache.org/jira/browse/CLOUDSTACK-6432
.. _CLOUDSTACK-8326: https://issues.apache.org/jira/browse/CLOUDSTACK-8326
.. _CLOUDSTACK-8830: https://issues.apache.org/jira/browse/CLOUDSTACK-8830
.. _CLOUDSTACK-8854: https://issues.apache.org/jira/browse/CLOUDSTACK-8854
.. _CLOUDSTACK-8908: https://issues.apache.org/jira/browse/CLOUDSTACK-8908
.. _CLOUDSTACK-9071: https://issues.apache.org/jira/browse/CLOUDSTACK-9071
.. _CLOUDSTACK-9161: https://issues.apache.org/jira/browse/CLOUDSTACK-9161
.. _CLOUDSTACK-9183: https://issues.apache.org/jira/browse/CLOUDSTACK-9183
.. _CLOUDSTACK-9269: https://issues.apache.org/jira/browse/CLOUDSTACK-9269
.. _CLOUDSTACK-9339: https://issues.apache.org/jira/browse/CLOUDSTACK-9339
.. _CLOUDSTACK-9364: https://issues.apache.org/jira/browse/CLOUDSTACK-9364
.. _CLOUDSTACK-9376: https://issues.apache.org/jira/browse/CLOUDSTACK-9376
.. _CLOUDSTACK-9386: https://issues.apache.org/jira/browse/CLOUDSTACK-9386
.. _CLOUDSTACK-9410: https://issues.apache.org/jira/browse/CLOUDSTACK-9410
.. _CLOUDSTACK-9416: https://issues.apache.org/jira/browse/CLOUDSTACK-9416
.. _CLOUDSTACK-9444: https://issues.apache.org/jira/browse/CLOUDSTACK-9444
.. _CLOUDSTACK-9447: https://issues.apache.org/jira/browse/CLOUDSTACK-9447
.. _CLOUDSTACK-9449: https://issues.apache.org/jira/browse/CLOUDSTACK-9449
.. _CLOUDSTACK-9451: https://issues.apache.org/jira/browse/CLOUDSTACK-9451
.. _CLOUDSTACK-9452: https://issues.apache.org/jira/browse/CLOUDSTACK-9452
.. _CLOUDSTACK-9459: https://issues.apache.org/jira/browse/CLOUDSTACK-9459
.. _CLOUDSTACK-9460: https://issues.apache.org/jira/browse/CLOUDSTACK-9460
.. _CLOUDSTACK-9462: https://issues.apache.org/jira/browse/CLOUDSTACK-9462
.. _CLOUDSTACK-9463: https://issues.apache.org/jira/browse/CLOUDSTACK-9463
.. _CLOUDSTACK-9466: https://issues.apache.org/jira/browse/CLOUDSTACK-9466
.. _CLOUDSTACK-9467: https://issues.apache.org/jira/browse/CLOUDSTACK-9467
.. _CLOUDSTACK-9468: https://issues.apache.org/jira/browse/CLOUDSTACK-9468
.. _CLOUDSTACK-9470: https://issues.apache.org/jira/browse/CLOUDSTACK-9470
.. _CLOUDSTACK-9480: https://issues.apache.org/jira/browse/CLOUDSTACK-9480
.. _CLOUDSTACK-9481: https://issues.apache.org/jira/browse/CLOUDSTACK-9481
.. _CLOUDSTACK-9489: https://issues.apache.org/jira/browse/CLOUDSTACK-9489
.. _CLOUDSTACK-9491: https://issues.apache.org/jira/browse/CLOUDSTACK-9491
.. _CLOUDSTACK-9495: https://issues.apache.org/jira/browse/CLOUDSTACK-9495
.. _CLOUDSTACK-9498: https://issues.apache.org/jira/browse/CLOUDSTACK-9498
.. _CLOUDSTACK-9502: https://issues.apache.org/jira/browse/CLOUDSTACK-9502
.. _CLOUDSTACK-9503: https://issues.apache.org/jira/browse/CLOUDSTACK-9503
.. _CLOUDSTACK-9509: https://issues.apache.org/jira/browse/CLOUDSTACK-9509
.. _CLOUDSTACK-9511: https://issues.apache.org/jira/browse/CLOUDSTACK-9511
.. _CLOUDSTACK-9514: https://issues.apache.org/jira/browse/CLOUDSTACK-9514
.. _CLOUDSTACK-9515: https://issues.apache.org/jira/browse/CLOUDSTACK-9515
.. _CLOUDSTACK-9522: https://issues.apache.org/jira/browse/CLOUDSTACK-9522
.. _CLOUDSTACK-9524: https://issues.apache.org/jira/browse/CLOUDSTACK-9524
.. _CLOUDSTACK-9526: https://issues.apache.org/jira/browse/CLOUDSTACK-9526
.. _CLOUDSTACK-9527: https://issues.apache.org/jira/browse/CLOUDSTACK-9527
.. _CLOUDSTACK-9529: https://issues.apache.org/jira/browse/CLOUDSTACK-9529
.. _CLOUDSTACK-9531: https://issues.apache.org/jira/browse/CLOUDSTACK-9531
.. _CLOUDSTACK-9532: https://issues.apache.org/jira/browse/CLOUDSTACK-9532
.. _CLOUDSTACK-9533: https://issues.apache.org/jira/browse/CLOUDSTACK-9533
.. _CLOUDSTACK-9534: https://issues.apache.org/jira/browse/CLOUDSTACK-9534
.. _CLOUDSTACK-9535: https://issues.apache.org/jira/browse/CLOUDSTACK-9535
.. _CLOUDSTACK-9538: https://issues.apache.org/jira/browse/CLOUDSTACK-9538
.. _CLOUDSTACK-9544: https://issues.apache.org/jira/browse/CLOUDSTACK-9544
.. _CLOUDSTACK-9550: https://issues.apache.org/jira/browse/CLOUDSTACK-9550
.. _CLOUDSTACK-9551: https://issues.apache.org/jira/browse/CLOUDSTACK-9551
.. _CLOUDSTACK-9552: https://issues.apache.org/jira/browse/CLOUDSTACK-9552
.. _CLOUDSTACK-9553: https://issues.apache.org/jira/browse/CLOUDSTACK-9553
.. _CLOUDSTACK-9554: https://issues.apache.org/jira/browse/CLOUDSTACK-9554
.. _CLOUDSTACK-9561: https://issues.apache.org/jira/browse/CLOUDSTACK-9561
.. _CLOUDSTACK-9564: https://issues.apache.org/jira/browse/CLOUDSTACK-9564
.. _CLOUDSTACK-9565: https://issues.apache.org/jira/browse/CLOUDSTACK-9565
.. _CLOUDSTACK-9566: https://issues.apache.org/jira/browse/CLOUDSTACK-9566
.. _CLOUDSTACK-9583: https://issues.apache.org/jira/browse/CLOUDSTACK-9583
.. _CLOUDSTACK-9584: https://issues.apache.org/jira/browse/CLOUDSTACK-9584
.. _CLOUDSTACK-9594: https://issues.apache.org/jira/browse/CLOUDSTACK-9594
.. _CLOUDSTACK-9598: https://issues.apache.org/jira/browse/CLOUDSTACK-9598
.. _CLOUDSTACK-9622: https://issues.apache.org/jira/browse/CLOUDSTACK-9622
.. _CLOUDSTACK-9624: https://issues.apache.org/jira/browse/CLOUDSTACK-9624
.. _CLOUDSTACK-9626: https://issues.apache.org/jira/browse/CLOUDSTACK-9626
.. _CLOUDSTACK-9632: https://issues.apache.org/jira/browse/CLOUDSTACK-9632
.. _CLOUDSTACK-9634: https://issues.apache.org/jira/browse/CLOUDSTACK-9634
.. _CLOUDSTACK-9635: https://issues.apache.org/jira/browse/CLOUDSTACK-9635
.. _CLOUDSTACK-9636: https://issues.apache.org/jira/browse/CLOUDSTACK-9636
.. _CLOUDSTACK-9637: https://issues.apache.org/jira/browse/CLOUDSTACK-9637
.. _CLOUDSTACK-9646: https://issues.apache.org/jira/browse/CLOUDSTACK-9646
.. _CLOUDSTACK-9648: https://issues.apache.org/jira/browse/CLOUDSTACK-9648
.. _CLOUDSTACK-9654: https://issues.apache.org/jira/browse/CLOUDSTACK-9654
.. _CLOUDSTACK-9656: https://issues.apache.org/jira/browse/CLOUDSTACK-9656
.. _CLOUDSTACK-9659: https://issues.apache.org/jira/browse/CLOUDSTACK-9659
.. _`#1663`: https://github.com/apache/cloudstack/pull/1663
.. _`#1743`: https://github.com/apache/cloudstack/pull/1743
.. _`#798`: https://github.com/apache/cloudstack/pull/798
.. _`#828`: https://github.com/apache/cloudstack/pull/828
.. _`#896`: https://github.com/apache/cloudstack/pull/896
.. _`#1673`: https://github.com/apache/cloudstack/pull/1673
.. _`#1240`: https://github.com/apache/cloudstack/pull/1240
.. _`#1744`: https://github.com/apache/cloudstack/pull/1744
.. _`#1396`: https://github.com/apache/cloudstack/pull/1396
.. _`#1659`: https://github.com/apache/cloudstack/pull/1659
.. _`#1696`: https://github.com/apache/cloudstack/pull/1696
.. _`#1560`: https://github.com/apache/cloudstack/pull/1560
.. _`#1586`: https://github.com/apache/cloudstack/pull/1586
.. _`#1785`: https://github.com/apache/cloudstack/pull/1785
.. _`#1621`: https://github.com/apache/cloudstack/pull/1621
.. _`#1646`: https://github.com/apache/cloudstack/pull/1646
.. _`#1635`: https://github.com/apache/cloudstack/pull/1635
.. _`#1634`: https://github.com/apache/cloudstack/pull/1634
.. _`#1641`: https://github.com/apache/cloudstack/pull/1641
.. _`#1674`: https://github.com/apache/cloudstack/pull/1674
.. _`#1647`: https://github.com/apache/cloudstack/pull/1647
.. _`#1649`: https://github.com/apache/cloudstack/pull/1649
.. _`#1656`: https://github.com/apache/cloudstack/pull/1656
.. _`#1657`: https://github.com/apache/cloudstack/pull/1657
.. _`#1660`: https://github.com/apache/cloudstack/pull/1660
.. _`#1666`: https://github.com/apache/cloudstack/pull/1666
.. _`#1670`: https://github.com/apache/cloudstack/pull/1670
.. _`#1684`: https://github.com/apache/cloudstack/pull/1684
.. _`#1681`: https://github.com/apache/cloudstack/pull/1681
.. _`#1680`: https://github.com/apache/cloudstack/pull/1680
.. _`#1676`: https://github.com/apache/cloudstack/pull/1676
.. _`#1745`: https://github.com/apache/cloudstack/pull/1745
.. _`#1694`: https://github.com/apache/cloudstack/pull/1694
.. _`#1724`: https://github.com/apache/cloudstack/pull/1724
.. _`#1701`: https://github.com/apache/cloudstack/pull/1701
.. _`#1702`: https://github.com/apache/cloudstack/pull/1702
.. _`#1710`: https://github.com/apache/cloudstack/pull/1710
.. _`#1742`: https://github.com/apache/cloudstack/pull/1742
.. _`#1712`: https://github.com/apache/cloudstack/pull/1712
.. _`#1728`: https://github.com/apache/cloudstack/pull/1728
.. _`#1713`: https://github.com/apache/cloudstack/pull/1713
.. _`#1714`: https://github.com/apache/cloudstack/pull/1714
.. _`#1715`: https://github.com/apache/cloudstack/pull/1715
.. _`#1737`: https://github.com/apache/cloudstack/pull/1737
.. _`#1729`: https://github.com/apache/cloudstack/pull/1729
.. _`#1731`: https://github.com/apache/cloudstack/pull/1731
.. _`#1738`: https://github.com/apache/cloudstack/pull/1738
.. _`#1757`: https://github.com/apache/cloudstack/pull/1757
.. _`#1755`: https://github.com/apache/cloudstack/pull/1755
.. _`#1766`: https://github.com/apache/cloudstack/pull/1766
.. _`#1791`: https://github.com/apache/cloudstack/pull/1791
.. _`#1793`: https://github.com/apache/cloudstack/pull/1793
.. _`#1796`: https://github.com/apache/cloudstack/pull/1796
.. _`#1799`: https://github.com/apache/cloudstack/pull/1799
.. _`#1802`: https://github.com/apache/cloudstack/pull/1802
.. _`#1805`: https://github.com/apache/cloudstack/pull/1805
.. _`#1809`: https://github.com/apache/cloudstack/pull/1809
.. _`#1808`: https://github.com/apache/cloudstack/pull/1808
.. _`#1817`: https://github.com/apache/cloudstack/pull/1817
.. _`#1820`: https://github.com/apache/cloudstack/pull/1820
.. _`#1821`: https://github.com/apache/cloudstack/pull/1821
.. _CLOUDSTACK-9597: https://issues.apache.org/jira/browse/CLOUDSTACK-9597
.. _CLOUDSTACK-9612: https://issues.apache.org/jira/browse/CLOUDSTACK-9612
.. _CLOUDSTACK-9615: https://issues.apache.org/jira/browse/CLOUDSTACK-9615
.. _CLOUDSTACK-9617: https://issues.apache.org/jira/browse/CLOUDSTACK-9617
.. _CLOUDSTACK-9639: https://issues.apache.org/jira/browse/CLOUDSTACK-9639
.. _CLOUDSTACK-9649: https://issues.apache.org/jira/browse/CLOUDSTACK-9649
.. _CLOUDSTACK-9662: https://issues.apache.org/jira/browse/CLOUDSTACK-9662
.. _CLOUDSTACK-9673: https://issues.apache.org/jira/browse/CLOUDSTACK-9673
.. _CLOUDSTACK-9676: https://issues.apache.org/jira/browse/CLOUDSTACK-9676
.. _CLOUDSTACK-9683: https://issues.apache.org/jira/browse/CLOUDSTACK-9683
.. _CLOUDSTACK-9688: https://issues.apache.org/jira/browse/CLOUDSTACK-9688
.. _`#1764`: https://github.com/apache/cloudstack/pull/1764
.. _`#1781`: https://github.com/apache/cloudstack/pull/1781
.. _`#1783`: https://github.com/apache/cloudstack/pull/1783
.. _`#1782`: https://github.com/apache/cloudstack/pull/1782
.. _`#1804`: https://github.com/apache/cloudstack/pull/1804
.. _`#1811`: https://github.com/apache/cloudstack/pull/1811
.. _`#1827`: https://github.com/apache/cloudstack/pull/1827
.. _`#1828`: https://github.com/apache/cloudstack/pull/1828
.. _`#1839`: https://github.com/apache/cloudstack/pull/1839
.. _`#1846`: https://github.com/apache/cloudstack/pull/1846
.. _CLOUDSTACK-10011: https://issues.apache.org/jira/browse/CLOUDSTACK-10011
.. _CLOUDSTACK-10016: https://issues.apache.org/jira/browse/CLOUDSTACK-10016
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _CLOUDSTACK-10042: https://issues.apache.org/jira/browse/CLOUDSTACK-10042
.. _CLOUDSTACK-10052: https://issues.apache.org/jira/browse/CLOUDSTACK-10052
.. _CLOUDSTACK-3223: https://issues.apache.org/jira/browse/CLOUDSTACK-3223
.. _CLOUDSTACK-4858: https://issues.apache.org/jira/browse/CLOUDSTACK-4858
.. _CLOUDSTACK-8186: https://issues.apache.org/jira/browse/CLOUDSTACK-8186
.. _CLOUDSTACK-8663: https://issues.apache.org/jira/browse/CLOUDSTACK-8663
.. _CLOUDSTACK-8805: https://issues.apache.org/jira/browse/CLOUDSTACK-8805
.. _CLOUDSTACK-8829: https://issues.apache.org/jira/browse/CLOUDSTACK-8829
.. _CLOUDSTACK-8833: https://issues.apache.org/jira/browse/CLOUDSTACK-8833
.. _CLOUDSTACK-8841: https://issues.apache.org/jira/browse/CLOUDSTACK-8841
.. _CLOUDSTACK-8857: https://issues.apache.org/jira/browse/CLOUDSTACK-8857
.. _CLOUDSTACK-8871: https://issues.apache.org/jira/browse/CLOUDSTACK-8871
.. _CLOUDSTACK-8896: https://issues.apache.org/jira/browse/CLOUDSTACK-8896
.. _CLOUDSTACK-8910: https://issues.apache.org/jira/browse/CLOUDSTACK-8910
.. _CLOUDSTACK-8931: https://issues.apache.org/jira/browse/CLOUDSTACK-8931
.. _CLOUDSTACK-8950: https://issues.apache.org/jira/browse/CLOUDSTACK-8950
.. _CLOUDSTACK-8958: https://issues.apache.org/jira/browse/CLOUDSTACK-8958
.. _CLOUDSTACK-9017: https://issues.apache.org/jira/browse/CLOUDSTACK-9017
.. _CLOUDSTACK-9136: https://issues.apache.org/jira/browse/CLOUDSTACK-9136
.. _CLOUDSTACK-9208: https://issues.apache.org/jira/browse/CLOUDSTACK-9208
.. _CLOUDSTACK-9321: https://issues.apache.org/jira/browse/CLOUDSTACK-9321
.. _CLOUDSTACK-9356: https://issues.apache.org/jira/browse/CLOUDSTACK-9356
.. _CLOUDSTACK-9369: https://issues.apache.org/jira/browse/CLOUDSTACK-9369
.. _CLOUDSTACK-9555: https://issues.apache.org/jira/browse/CLOUDSTACK-9555
.. _CLOUDSTACK-9560: https://issues.apache.org/jira/browse/CLOUDSTACK-9560
.. _CLOUDSTACK-9567: https://issues.apache.org/jira/browse/CLOUDSTACK-9567
.. _CLOUDSTACK-9569: https://issues.apache.org/jira/browse/CLOUDSTACK-9569
.. _CLOUDSTACK-9591: https://issues.apache.org/jira/browse/CLOUDSTACK-9591
.. _CLOUDSTACK-9592: https://issues.apache.org/jira/browse/CLOUDSTACK-9592
.. _CLOUDSTACK-9610: https://issues.apache.org/jira/browse/CLOUDSTACK-9610
.. _CLOUDSTACK-9611: https://issues.apache.org/jira/browse/CLOUDSTACK-9611
.. _CLOUDSTACK-9623: https://issues.apache.org/jira/browse/CLOUDSTACK-9623
.. _CLOUDSTACK-9628: https://issues.apache.org/jira/browse/CLOUDSTACK-9628
.. _CLOUDSTACK-9630: https://issues.apache.org/jira/browse/CLOUDSTACK-9630
.. _CLOUDSTACK-9631: https://issues.apache.org/jira/browse/CLOUDSTACK-9631
.. _CLOUDSTACK-9638: https://issues.apache.org/jira/browse/CLOUDSTACK-9638
.. _CLOUDSTACK-9647: https://issues.apache.org/jira/browse/CLOUDSTACK-9647
.. _CLOUDSTACK-9655: https://issues.apache.org/jira/browse/CLOUDSTACK-9655
.. _CLOUDSTACK-9666: https://issues.apache.org/jira/browse/CLOUDSTACK-9666
.. _CLOUDSTACK-9668: https://issues.apache.org/jira/browse/CLOUDSTACK-9668
.. _CLOUDSTACK-9682: https://issues.apache.org/jira/browse/CLOUDSTACK-9682
.. _CLOUDSTACK-9684: https://issues.apache.org/jira/browse/CLOUDSTACK-9684
.. _CLOUDSTACK-9685: https://issues.apache.org/jira/browse/CLOUDSTACK-9685
.. _CLOUDSTACK-9686: https://issues.apache.org/jira/browse/CLOUDSTACK-9686
.. _CLOUDSTACK-9691: https://issues.apache.org/jira/browse/CLOUDSTACK-9691
.. _CLOUDSTACK-9692: https://issues.apache.org/jira/browse/CLOUDSTACK-9692
.. _CLOUDSTACK-9694: https://issues.apache.org/jira/browse/CLOUDSTACK-9694
.. _CLOUDSTACK-9701: https://issues.apache.org/jira/browse/CLOUDSTACK-9701
.. _CLOUDSTACK-9705: https://issues.apache.org/jira/browse/CLOUDSTACK-9705
.. _CLOUDSTACK-9708: https://issues.apache.org/jira/browse/CLOUDSTACK-9708
.. _CLOUDSTACK-9715: https://issues.apache.org/jira/browse/CLOUDSTACK-9715
.. _CLOUDSTACK-9719: https://issues.apache.org/jira/browse/CLOUDSTACK-9719
.. _CLOUDSTACK-9720: https://issues.apache.org/jira/browse/CLOUDSTACK-9720
.. _CLOUDSTACK-9725: https://issues.apache.org/jira/browse/CLOUDSTACK-9725
.. _CLOUDSTACK-9728: https://issues.apache.org/jira/browse/CLOUDSTACK-9728
.. _CLOUDSTACK-9731: https://issues.apache.org/jira/browse/CLOUDSTACK-9731
.. _CLOUDSTACK-9746: https://issues.apache.org/jira/browse/CLOUDSTACK-9746
.. _CLOUDSTACK-9748: https://issues.apache.org/jira/browse/CLOUDSTACK-9748
.. _CLOUDSTACK-9751: https://issues.apache.org/jira/browse/CLOUDSTACK-9751
.. _CLOUDSTACK-9752: https://issues.apache.org/jira/browse/CLOUDSTACK-9752
.. _CLOUDSTACK-9757: https://issues.apache.org/jira/browse/CLOUDSTACK-9757
.. _CLOUDSTACK-9765: https://issues.apache.org/jira/browse/CLOUDSTACK-9765
.. _CLOUDSTACK-9770: https://issues.apache.org/jira/browse/CLOUDSTACK-9770
.. _CLOUDSTACK-9783: https://issues.apache.org/jira/browse/CLOUDSTACK-9783
.. _CLOUDSTACK-9784: https://issues.apache.org/jira/browse/CLOUDSTACK-9784
.. _CLOUDSTACK-9787: https://issues.apache.org/jira/browse/CLOUDSTACK-9787
.. _CLOUDSTACK-9788: https://issues.apache.org/jira/browse/CLOUDSTACK-9788
.. _CLOUDSTACK-9789: https://issues.apache.org/jira/browse/CLOUDSTACK-9789
.. _CLOUDSTACK-9792: https://issues.apache.org/jira/browse/CLOUDSTACK-9792
.. _CLOUDSTACK-9793: https://issues.apache.org/jira/browse/CLOUDSTACK-9793
.. _CLOUDSTACK-9794: https://issues.apache.org/jira/browse/CLOUDSTACK-9794
.. _CLOUDSTACK-9796: https://issues.apache.org/jira/browse/CLOUDSTACK-9796
.. _CLOUDSTACK-9801: https://issues.apache.org/jira/browse/CLOUDSTACK-9801
.. _CLOUDSTACK-9805: https://issues.apache.org/jira/browse/CLOUDSTACK-9805
.. _CLOUDSTACK-9811: https://issues.apache.org/jira/browse/CLOUDSTACK-9811
.. _CLOUDSTACK-9814: https://issues.apache.org/jira/browse/CLOUDSTACK-9814
.. _CLOUDSTACK-9821: https://issues.apache.org/jira/browse/CLOUDSTACK-9821
.. _CLOUDSTACK-9828: https://issues.apache.org/jira/browse/CLOUDSTACK-9828
.. _CLOUDSTACK-9830: https://issues.apache.org/jira/browse/CLOUDSTACK-9830
.. _CLOUDSTACK-9831: https://issues.apache.org/jira/browse/CLOUDSTACK-9831
.. _CLOUDSTACK-9834: https://issues.apache.org/jira/browse/CLOUDSTACK-9834
.. _CLOUDSTACK-9838: https://issues.apache.org/jira/browse/CLOUDSTACK-9838
.. _CLOUDSTACK-9842: https://issues.apache.org/jira/browse/CLOUDSTACK-9842
.. _CLOUDSTACK-9843: https://issues.apache.org/jira/browse/CLOUDSTACK-9843
.. _CLOUDSTACK-9851: https://issues.apache.org/jira/browse/CLOUDSTACK-9851
.. _CLOUDSTACK-9857: https://issues.apache.org/jira/browse/CLOUDSTACK-9857
.. _CLOUDSTACK-9860: https://issues.apache.org/jira/browse/CLOUDSTACK-9860
.. _CLOUDSTACK-9871: https://issues.apache.org/jira/browse/CLOUDSTACK-9871
.. _CLOUDSTACK-9876: https://issues.apache.org/jira/browse/CLOUDSTACK-9876
.. _CLOUDSTACK-9900: https://issues.apache.org/jira/browse/CLOUDSTACK-9900
.. _CLOUDSTACK-9904: https://issues.apache.org/jira/browse/CLOUDSTACK-9904
.. _CLOUDSTACK-9929: https://issues.apache.org/jira/browse/CLOUDSTACK-9929
.. _CLOUDSTACK-9935: https://issues.apache.org/jira/browse/CLOUDSTACK-9935
.. _CLOUDSTACK-9937: https://issues.apache.org/jira/browse/CLOUDSTACK-9937
.. _CLOUDSTACK-9983: https://issues.apache.org/jira/browse/CLOUDSTACK-9983
.. _CLOUDSTACK-9985: https://issues.apache.org/jira/browse/CLOUDSTACK-9985
