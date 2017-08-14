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

Issues Fixed in |release|
-------------------------

.. cssclass:: table-striped table-bordered table-hover

+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| Branches                | Github   | Jira               | Type          | Priority | Description                                                |
+=========================+==========+====================+===============+==========+============================================================+
| 4.10                    | `#2162`_ | CLOUDSTACK-9980_   | Bug           | Blocker  | ACS Master: Internal DNS feature breaks on restart network |
|                         |          |                    |               |          | with cleanup                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2150`_ |                    |               |          | Two fixes for RC3 by @mike-tutkowski                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2089`_ |                    |               |          | vRouters fixes & performance improvement                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2100`_ | CLOUDSTACK-9907_   | Bug           | Major    | Physical size of snapshot is considered when usage is      |
|                         |          |                    |               |          | generated for snapshots.                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2135`_ | CLOUDSTACK-9860_   | Improvement   | Major    | CloudStack should be able to pass 'hard' shutdown          |
|                         |          |                    |               |          | instruction to hosts to force a guest instance shutdown    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1759`_ | CLOUDSTACK-9589_   | Bug           | Major    | vmName entries from host_details table for the VM's whose  |
|                         |          |                    |               |          | state is Expunging should be deleted during upgrade from   |
|                         |          |                    |               |          | older versions                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1726`_ | CLOUDSTACK-9560_   | Bug           | Major    | Root volume of deleted VM left unremoved                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1866`_ |                    |               |          | Advanced isolated network egress destination cidr support  |
|                         |          |                    |               |          | added                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2126`_ | CLOUDSTACK-9740_   | Bug           | Major    | Search for secondary IP of NIC that is attached to an      |
|                         |          |                    |               |          | instance is not working                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2132`_ | CLOUDSTACK-9935_   | Bug           | Major    | Search in VPN Customer Gateway not working                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1716`_ | CLOUDSTACK-9555_   | Bug           | Major    | when a template is deleted and then copied over again , it |
|                         |          |                    |               |          | is still marked as Removed in template_zone_ref table      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1725`_ | CLOUDSTACK-9559_   | Bug           | Major    | Deleting zone without deleting the secondary storage under |
|                         |          |                    |               |          | the zone should not be allowed                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1734`_ | CLOUDSTACK-9567_   | Bug           | Major    | Difference in the api call outputs for CAPACITY_TYPE_CPU = |
|                         |          |                    |               |          | 1                                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1756`_ | CLOUDSTACK-9585_   | Bug           | Major    | UI doesn't give an option to select the xentools version   |
|                         |          |                    |               |          | for non ROOT users                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1761`_ | CLOUDSTACK-9592_   | Bug           | Major    | Empty responses from site to site connection status are    |
|                         |          |                    |               |          | not handled propertly                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1776`_ | CLOUDSTACK-9603_   | Bug           | Minor    | 'concurrent.snapshots.threshold.perhost' parameter should  |
|                         |          |                    |               |          | not accept String                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1779`_ | CLOUDSTACK-9610_   | Bug           | Major    | Disabled Host Keeps Being up status after unmanaging       |
|                         |          |                    |               |          | cluster                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1841`_ | CLOUDSTACK-9684_   | Bug           | Major    | Invalid zone id error while listing vmware zone            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1850`_ | CLOUDSTACK-9694_   | Bug           | Major    | Unable to limit the Public IPs in VPC                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1862`_ | CLOUDSTACK-9704_   | Bug           | Major    | Remove dependency on VmwareContext object to fetch system  |
|                         |          |                    |               |          | VM key file                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1865`_ | CLOUDSTACK-9705_   | Bug           | Major    | Unauthenticated API allows Admin password reset            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1868`_ | CLOUDSTACK-9707_   | Bug           | Major    | deployVirtualMachine API should fail if hostid is          |
|                         |          |                    |               |          | specified and host doesn't have enough resources           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1869`_ | CLOUDSTACK-9701_   | Bug           | Major    | When host is disabled/removed, capacity_state for local    |
|                         |          |                    |               |          | storage in op_host_capacity is still enabled               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1900`_ | CLOUDSTACK-8862_   | Bug           | Major    | Issuing multiple attach-volume commands simultaneously can |
|                         |          |                    |               |          | be problematic                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2012`_ | CLOUDSTACK-9842_   | Bug           | Major    | Unable to map root volume usage to VM                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2015`_ | CLOUDSTACK-9843_   | Bug           | Major    | Performance improvement of deployVirtualMachine,           |
|                         |          |                    |               |          | createFirewallRule, createPortForwardingRule               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2086`_ | CLOUDSTACK-9905_   | Improvement   | Major    | VPN Gateway with Public Subnet                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2113`_ | CLOUDSTACK-9162_   | Bug           | Major    | Handle the vpn user add when vpn is not enabled on the     |
|                         |          |                    |               |          | account                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1894`_ | CLOUDSTACK-9700_   | Improvement   | Major    | Allow user to Register/Copy templates to multiple zones at |
|                         |          |                    |               |          | the same time                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#892`_  | CLOUDSTACK-8910_   | Bug           | Major    | The reserved_capacity field increases suddenly after a     |
|                         |          |                    |               |          | vmware host failure                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#899`_  | CLOUDSTACK-8921_   | Bug           | Major    | snapshot_store_ref table should store actual size of back  |
|                         |          |                    |               |          | snapshot in secondary storage                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#927`_  | CLOUDSTACK-9901_   | Bug           | Major    | secure and hidden config values are returned as plaintext  |
|                         |          |                    |               |          | string                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1867`_ | CLOUDSTACK-9706_   | Bug           | Major    | Retry deleting snapshot if deleteSnapshot command failed   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1996`_ | CLOUDSTACK-9099_   | Bug           | Major    | SecretKey is returned from the APIs                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2016`_ | CLOUDSTACK-9835_   | Bug           | Major    | To make management server and SSVM to be in time sync      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2108`_ | CLOUDSTACK-9860_   | Improvement   | Major    | CloudStack should be able to pass 'hard' shutdown          |
|                         |          |                    |               |          | instruction to hosts to force a guest instance shutdown    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2133`_ | CLOUDSTACK-9937_   | Bug           | Major    | dedicateCluster API response does not return correct       |
|                         |          |                    |               |          | detail in response                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1987`_ | CLOUDSTACK-9814_   | Bug           | Major    | Unable to edit a Sub domain, which has the same name in    |
|                         |          |                    |               |          | different domains                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2072`_ | CLOUDSTACK-9895_   | Improvement   | Major    | Support parallel volume creation from snapshot             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1967`_ | CLOUDSTACK-9638_   | Bug           | Major    | Problems caused when inputting double-byte numbers for     |
|                         |          |                    |               |          | custom compute offerings                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2082`_ | CLOUDSTACK-9017_   | Bug           | Major    | VPC VR DHCP broken for multihomed guest VMs                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2098`_ | CLOUDSTACK-9660_   | Bug           | Major    | NPE while destroying volumes during 1000 VMs deploy and    |
|                         |          |                    |               |          | destroy tests                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2121`_ | CLOUDSTACK-9641_   | Bug           | Major    | In KVM SSVM and CPVM may use the old cmdline data, if we   |
|                         |          |                    |               |          | fail to fetch the new cmdline in the first pass.           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2120`_ | CLOUDSTACK-9665_   | Bug           | Major    | List hosts api dose not report correct cpu and memory      |
|                         |          |                    |               |          | usage                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1824`_ | CLOUDSTACK-9657_   | Bug           | Major    | Ipset command fails for VM's with long internal name       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2103`_ | CLOUDSTACK-8647_   | Improvement   | Major    | LDAP Trust AD and Autoimport                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2080`_ |                    |               |          | Changing vlan to None since network offering being used    |
|                         |          |                    |               |          | has Specify Vlan set to False                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1908`_ | CLOUDSTACK-9317_   | Bug           | Major    | Disabling static NAT on many IPs can leave wrong IPs on    |
|                         |          |                    |               |          | the router                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#874`_  | CLOUDSTACK-8897_   | Bug           | Major    | baremetal:addHost:make host tag info mandtory in baremetal |
|                         |          |                    |               |          | addhost Api call                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2106`_ | CLOUDSTACK-9168_   | Task          | Major    | Testcase to check if wrong value is inserted into nics     |
|                         |          |                    |               |          | table netmask field when creating a VM                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2006`_ | CLOUDSTACK-9833_   | Bug           | Major    | Move configuration parameters from Config.java to use      |
|                         |          |                    |               |          | ConfigDepot                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1322`_ | CLOUDSTACK-9217_   | Test          | Major    | CloudStack should block volume migration to a pool in      |
|                         |          |                    |               |          | maintenance mode                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#868`_  | CLOUDSTACK-8894_   | Bug           | Major    | Dynamic scaling is not restricted when destination         |
|                         |          |                    |               |          | offering has changes in the vGPU type                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1971`_ | CLOUDSTACK-9726_   | Bug           | Major    | state of the rvr dose not change to update failed when     |
|                         |          |                    |               |          | updating rvrs in sequence to a new offering fails.         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1873`_ | CLOUDSTACK-9709_   | Bug           | Major    | DHCP/DNS offload: Use correct thread pool for IP fetch     |
|                         |          |                    |               |          | task                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1872`_ | CLOUDSTACK-3223_   | Bug           | Major    | Exception observed while creating CPVM in VMware Setup     |
|                         |          |                    |               |          | with DVS                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1842`_ | CLOUDSTACK-9686_   | Bug           | Major    | multiple entires for builtin template in template store    |
|                         |          |                    |               |          | ref table so builtin template is never downloaded          |
|                         |          |                    |               |          | completely                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1883`_ | CLOUDSTACK-9723_   | Bug           | Major    | Enable unique mac address across different deployments and |
|                         |          |                    |               |          | networks                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1968`_ | CLOUDSTACK-9666_   | Bug           | Major    | Add configuration validation for the config drive global   |
|                         |          |                    |               |          | settings                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1945`_ | CLOUDSTACK-9787_   | Bug           | Major    | No error message while change guest vm cidr to a large     |
|                         |          |                    |               |          | value                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2002`_ | CLOUDSTACK-9831_   | Bug           | Major    | Previous pod_id still remains in the vm_instance table     |
|                         |          |                    |               |          | after VM migration with migrateVirtualMachineWithVolume    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2027`_ | CLOUDSTACK-9918_   | Test          | Major    | Enable NIO test cases                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2018`_ | CLOUDSTACK-9848_   | Bug           | Major    | VR commands exist status is not checked in python config   |
|                         |          |                    |               |          | files                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2055`_ | CLOUDSTACK-9887_   | Bug           | Major    | A VM with dual shared/isolated network gets bogus GW       |
|                         |          |                    |               |          | assignment                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2070`_ | CLOUDSTACK-9904_   | Bug           | Major    | HyperV plugin created logs @AGENTLOG@                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1995`_ | CLOUDSTACK-9828_   | Bug           | Major    | .GetDomRVersionCommand failed while starting virtual       |
|                         |          |                    |               |          | router                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1870`_ | CLOUDSTACK-9708_   | Bug           | Major    | Router deployment failed due to two threads start VR       |
|                         |          |                    |               |          | simultaneosuly                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1840`_ | CLOUDSTACK-9685_   | Bug           | Major    | [Xen]Delete snapshot on primary when associated volume is  |
|                         |          |                    |               |          | deleted                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1849`_ | CLOUDSTACK-9690_   | Bug           | Major    | Scale CentOS7 VM fails with error                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2007`_ | CLOUDSTACK-9834_   | Bug           | Major    | prepareTemplate API call doesn't work well with XenServer  |
|                         |          |                    |               |          | & Local SR (Db_exn.Uniqueness_constraint_violation)        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1180`_ | CLOUDSTACK-9112_   | Bug           | Major    | deployVM thread is holding the global lock on network      |
|                         |          |                    |               |          | longer and cause delays and some improvements in the       |
|                         |          |                    |               |          | planner                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1992`_ | CLOUDSTACK-9824_   | Bug           | Major    | Resource count for Primary storage is considered twice -   |
|                         |          |                    |               |          | while creating and while attaching the disk.               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2075`_ | CLOUDSTACK-9900_   | Bug           | Major    | Fix high CPU deviation seen in Zone/Cluster metrics view   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2077`_ |                    |               |          | Honor network.dns.basiczone.updates setting when sending   |
|                         |          |                    |               |          | DHCP config …                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2062`_ | CLOUDSTACK-9878_   | Bug           | Blocker  | Remote Access VPN that losing connection when new network  |
|                         |          |                    |               |          | configs are introduced                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1949`_ |                    |               |          | Automated Cloudstack bugs 9277 9276 9275 9274 9273 9179    |
|                         |          |                    |               |          | 9178 9177                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1813`_ | CLOUDSTACK-9604_   | Improvement   | Major    | Root disk resize support for VMware and XenServer          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#803`_  | CLOUDSTACK-8833_   | Bug           | Major    | Generating url and migrate volume to another storage ,     |
|                         |          |                    |               |          | resulting two entry in UI and listvolume is not working    |
|                         |          |                    |               |          | for that volume                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1606`_ |                    |               |          | Allow CGN (RFC6598) to be used within a VPC                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2056`_ | CLOUDSTACK-8829_   | Bug           | Major    | Consecutive cold migration fails                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1810`_ | CLOUDSTACK-9647_   | Bug           | Major    | NIC adapter type becomes e1000 , even after changing the   |
|                         |          |                    |               |          | global parameter "vmware.systemvm.nic.device.type" to      |
|                         |          |                    |               |          | vmxnet3 for VPC VR                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2071`_ | CLOUDSTACK-9815_   | Improvement   | Major    | Application Container Service                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2030`_ | CLOUDSTACK-9864_   | Improvement   | Major    | cleanup stale worker VMs after job expiry time             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1792`_ | CLOUDSTACK-9623_   | Bug           | Major    | Deploying virtual machine fails due to "Couldn't find      |
|                         |          |                    |               |          | vlanId" in Basic Zone                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1970`_ | CLOUDSTACK-9725_   | Bug           | Major    | Failed to update VPC Network during N/w offering Upgrade   |
|                         |          |                    |               |          | which doesnt have ACL service Enabled.     check if acl    |
|                         |          |                    |               |          | service provider is configured when network is associated  |
|                         |          |                    |               |          | with a acl.                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1997`_ | CLOUDSTACK-9208_   | Bug           | Minor    | Assertion Error in VM_POWER_STATE handler.                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2066`_ | CLOUDSTACK-9893_   | Bug           | Minor    | smoke test test_deploy_virtio_scsi_vm fails                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2053`_ |                    |               |          | deb: Only build binary packages                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2069`_ | CLOUDSTACK-8793_   | Bug           | Major    | Project Site-2-Site VPN Connection Fails to Register       |
|                         |          |                    |               |          | Correctly                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2037`_ | CLOUDSTACK-9871_   | Bug           | Minor    | MySQL 5.7 compatibility                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1852`_ | CLOUDSTACK-9695_   | Improvement   | Minor    | For VM in stopped state, disable "Snapshot Memory" option  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1797`_ | CLOUDSTACK-9630_   | Bug           | Major    | Cannot use listNics API as advertised                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1918`_ |                    |               |          | Management Server UI (VM statistics page) CPU Utilized     |
|                         |          |                    |               |          | value is incorrect.                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2063`_ |                    |               |          | Fix typo on label.gpu                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1978`_ | CLOUDSTACK-9779_   | Bug           | Major    | Releasing secondary guest IP fails with error VM nic Ip    |
|                         |          |                    |               |          | x.x.x.x is mapped to load balancing rule                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1582`_ | CLOUDSTACK-9408_   | Improvement   | Blocker  | remove runtime references to http://download.cloud.com     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2009`_ | CLOUDSTACK-9369_   | Bug           | Critical | Security issue! Local login open with SAML implementation  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2060`_ |                    |               |          | Merge release branch 4.9 to master                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1819`_ | CLOUDSTACK-9653_   | Bug           | Major    | listCapacity API shows incorrect output when sortBy=usage  |
|                         |          |                    |               |          | option is added                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1879`_ | CLOUDSTACK-9719_   | Bug           | Major    | [VMware] VR loses DHCP settings and VMs cannot obtain IP   |
|                         |          |                    |               |          | after HA recovery                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1917`_ | CLOUDSTACK-9756_   | Bug           | Major    | IP address must not be allocated to other VR if releasing  |
|                         |          |                    |               |          | ip address is failed                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1993`_ | CLOUDSTACK-8931_   | Bug           | Major    | Fail to deploy VM instance when                            |
|                         |          |                    |               |          | use.system.public.ips=false                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1957`_ | CLOUDSTACK-9748_   | Bug           | Major    | VPN Users search functionality broken                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1956`_ | CLOUDSTACK-9796_   | Bug           | Minor    | Null Pointer Exception in VirtualMachineManagerImpl.java   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1903`_ | CLOUDSTACK-9356_   | Bug           | Critical | VPC add VPN User fails same error as CLOUDSTACK-8927       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1886`_ | CLOUDSTACK-9728_   | Bug           | Major    | query to traffic sentinel requesting for usage stats is    |
|                         |          |                    |               |          | too long resulting in traffic sentinel sending HTTP 414    |
|                         |          |                    |               |          | error response                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2024`_ | CLOUDSTACK-9857_   | Bug           | Critical | CloudStack KVM Agent Self Fencing  - improper systemd      |
|                         |          |                    |               |          | config                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1935`_ | CLOUDSTACK-9764_   | Bug           | Major    | Delete domain failure due to Account Cleanup task          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1889`_ | CLOUDSTACK-9718_   | Improvement   | Major    | Revamp the dropdown showing lists of hosts available for   |
|                         |          |                    |               |          | migration in a Zone                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1955`_ | CLOUDSTACK-8239_   | New Feature   | Critical | Add support for VirtIO-SCSI for KVM hypervisors            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1980`_ | CLOUDSTACK-9805_   | Bug           | Major    | Show VRs in a tab for a network in network detail view     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2051`_ | CLOUDSTACK-9858_   | Improvement   | Major    | Retirement of midonet plugin (disabling ticket)            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2043`_ | CLOUDSTACK-9876_   | Bug           | Major    | Remove test_01_test_vm_volume_snapshot in                  |
|                         |          |                    |               |          | test_vm_snapshots.py                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2036`_ | CLOUDSTACK-9858_   | Improvement   | Major    | Retirement of midonet plugin (disabling ticket)            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1771`_ | CLOUDSTACK-9611_   | Bug           | Major    | Dedicating a Guest VLAN range to Project does not work     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2033`_ | CLOUDSTACK-9462_   | Bug           | Major    | Systemd packaging for Ubuntu 16.04                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2023`_ | CLOUDSTACK-9808_   | Bug           | Blocker  | 4.9->4.10 upgrade does not upgrade global settings to      |
|                         |          |                    |               |          | point to new template                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2025`_ |                    |               |          | [4.10-blocker] Fix error in restart network in 4.10.0.0 RC |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2022`_ | CLOUDSTACK-9591_   | Bug           | Minor    | VMware dvSwitch Requires a Dummy, Standard vSwitch         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2032`_ | CLOUDSTACK-9783_   | Improvement   | Major    | Improve metrics view performance                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1880`_ | CLOUDSTACK-9720_   | Bug           | Major    | [VMware] template_spool_ref table is not getting updated   |
|                         |          |                    |               |          | with correct template physical size in template_size       |
|                         |          |                    |               |          | column.                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1944`_ | CLOUDSTACK-9783_   | Improvement   | Major    | Improve metrics view performance                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2021`_ | CLOUDSTACK-9854_   | Bug           | Major    | Fix test_primary_storage test failure due to live          |
|                         |          |                    |               |          | migration                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2019`_ | CLOUDSTACK-9851_   | Bug           | Major    | travis CI build failure after merge of PR#1953             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1994`_ | CLOUDSTACK-9827_   | Bug           | Blocker  | Storage tags stored in multiple places                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1961`_ |                    |               |          | Fix for test_snapshots.py using nfs2 instead of nfs        |
|                         |          |                    |               |          | template                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#2011`_ | CLOUDSTACK-9811_   | Bug           | Blocker  | VR will not start, looking to configure eth3 while no such |
|                         |          |                    |               |          | device exists on the VR. On KVM-CentOS6.8 physical host    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#2003`_ | CLOUDSTACK-9811_   | Bug           | Blocker  | VR will not start, looking to configure eth3 while no such |
|                         |          |                    |               |          | device exists on the VR. On KVM-CentOS6.8 physical host    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1923`_ | CLOUDSTACK-9765_   | Bug           | Major    | broken db.properties after upgrade                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#847`_  | CLOUDSTACK-8880_   | Bug           | Major    | Allocated memory more than total memory on a KVM host      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1953`_ | CLOUDSTACK-9794_   | Bug           | Major    | Unable to attach more than 14 devices to a VM              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1958`_ | CLOUDSTACK-5806_   | Bug           | Critical | Storage types other than NFS/VMFS can't overprovision      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1861`_ | CLOUDSTACK-9698_   | Bug           | Major    | Make the wait timeout for NIC adapter hotplug as           |
|                         |          |                    |               |          | configurable                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1856`_ | CLOUDSTACK-9569_   | Bug           | Critical | VR on shared network not starting on KVM                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1991`_ | CLOUDSTACK-9821_   | Bug           | Blocker  | Unable to deploy user VM in Basic Zone                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1982`_ | CLOUDSTACK-9807_   | Bug           | Blocker  | 4.5->4.10 upgrade fails. db upgrade script looking for     |
|                         |          |                    |               |          | ssvm template-4.6 when having 4.10 already installed.      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1942`_ | CLOUDSTACK-9784_   | Bug           | Major    | GPU detail not displayed in GPU tab of management server   |
|                         |          |                    |               |          | UI.                                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1914`_ | CLOUDSTACK-9753_   | Bug           | Minor    | Update L10N resource files with 4.10 strings from          |
|                         |          |                    |               |          | Transifex (20170121)                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1896`_ | CLOUDSTACK-9732_   | Improvement   | Minor    | Update L10N resource files with 4.9 strings from Transifex |
|                         |          |                    |               |          | (20170106)                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1768`_ |                    |               |          | CLOUDSTACK 9601: Upgrade: change logic for update path for |
|                         |          |                    |               |          | files                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1975`_ |                    |               |          | Fix build failure on master                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#815`_  | CLOUDSTACK-8841_   | Bug           | Major    | Storage XenMotion from XS 6.2 to XS 6.5 fails.             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#843`_  |                    |               |          | Security group ingress/egress issues with xenserver 6.2    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1825`_ | CLOUDSTACK-9660_   | Bug           | Major    | NPE while destroying volumes during 1000 VMs deploy and    |
|                         |          |                    |               |          | destroy tests                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1907`_ |                    |               |          | Fix public IPs not being removed from the VR when          |
|                         |          |                    |               |          | deprovisioned                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1922`_ | CLOUDSTACK-9757_   | Bug           | Major    | VPC traffic from vm to additional public subnet is not     |
|                         |          |                    |               |          | working                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1915`_ | CLOUDSTACK-9746_   | Bug           | Critical | system-vm: logrotate config causes critical failures       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1829`_ | CLOUDSTACK-9363_   | Bug           | Critical | Can't start a Xen HVM vm when more than 2 volumes attached |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1941`_ | CLOUDSTACK-8663_   | Improvement   | Major    | Snapshot Improvements                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1946`_ | CLOUDSTACK-9788_   | Bug           | Major    | Exception is throwed when list networks with pagesize is 0 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1948`_ | CLOUDSTACK-9793_   | Bug           | Major    | Unnecessary conversion from IPNetwork to list causes       |
|                         |          |                    |               |          | router slowdown when processing static Nat rules           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1954`_ | CLOUDSTACK-9795_   | Bug           | Minor    | VRs used as VPC Routers have logrotate in cron.daily       |
|                         |          |                    |               |          | instead of cron.hourly                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1927`_ |                    |               |          | ipv6: Set IPv6 CIDR and Gateway in 'nic' profile           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#838`_  | CLOUDSTACK-8857_   | Bug           | Major    | 'listProjects' doesn't return tags 'vmstopped' or          |
|                         |          |                    |               |          | 'vmrunning' when their value is zero                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#865`_  | CLOUDSTACK-8856_   | Bug           | Major    | Primary Storage Used(type tag with value 2) related tag is |
|                         |          |                    |               |          | not showing in listCapacity api response                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1947`_ | CLOUDSTACK-9789_   | Bug           | Major    | Releasing secondary guest IP fails with error VM nic Ip    |
|                         |          |                    |               |          | x.x.x.x is mapped to static nat                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1770`_ | CLOUDSTACK-9628_   | Bug           | Major    | Fix Template Size in Swift as Secondary Storage            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1379`_ | CLOUDSTACK-8324_   | New Feature   | Major    | DHCP/DNS offload and config drive support for adv shared   |
|                         |          |                    |               |          | network                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1885`_ | CLOUDSTACK-9724_   | Bug           | Major    | VPC tier network restart with cleanup, missing public ip   |
|                         |          |                    |               |          | on VR interface                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1882`_ | CLOUDSTACK-8737_   | Bug           | Major    | Remove out-of-band VR reboot code based on persistent VR   |
|                         |          |                    |               |          | configuration changes                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1881`_ | CLOUDSTACK-9721_   | Bug           | Major    | Remove deprecated/unused global configuration parameter -  |
|                         |          |                    |               |          | consoleproxy.loadscan.interval                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1926`_ | CLOUDSTACK-9768_   | Bug           | Major    | Time displayed for events in UI is incorrect               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1924`_ | CLOUDSTACK-9766_   | Bug           | Major    | Executing deleteSnapshot api with already deleted snapshot |
|                         |          |                    |               |          | does not throw any exception or failure message            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1874`_ | CLOUDSTACK-9711_   | Bug           | Major    | Remote Access vpn user add fail ignored when the VR in     |
|                         |          |                    |               |          | stopped state                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1333`_ | CLOUDSTACK-9228_   | Bug           | Major    | Network update with mistmatch in services require forced   |
|                         |          |                    |               |          | option                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1758`_ | CLOUDSTACK-9588_   | Bug           | Major    | Add Load Balancer functionality in Network page is         |
|                         |          |                    |               |          | redundant.                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1786`_ | CLOUDSTACK-9618_   | Bug           | Major    | Load Balancer configuration page does not have "Source"    |
|                         |          |                    |               |          | method in the drop down list                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1847`_ | CLOUDSTACK-9691_   | Bug           | Major    | unhandeled excetion in list snapshot command when a        |
|                         |          |                    |               |          | primary store is deleted                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1952`_ | CLOUDSTACK-9790_   | Bug           | Blocker  | Can't create a Basic Zone (networking problem)             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1838`_ | CLOUDSTACK-9682_   | Bug           | Major    | Block VM migration to a storage which is in maintainence   |
|                         |          |                    |               |          | mode                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1913`_ | CLOUDSTACK-9752_   | Improvement   | Major    | [Vmware] Optimization of volume attachness to vm           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1727`_ | CLOUDSTACK-9539_   | Bug           | Major    | Support changing Service offering for instance with VM     |
|                         |          |                    |               |          | Snapshots                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1834`_ | CLOUDSTACK-9679_   | Bug           | Major    | Allow master user to manage subordinate user uploaded      |
|                         |          |                    |               |          | template                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1747`_ | CLOUDSTACK-9574_   | Improvement   | Major    | Redesign storage views                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1833`_ | CLOUDSTACK-9678_   | Bug           | Major    | listNetworkOfferings API is listing all the offerings      |
|                         |          |                    |               |          | which has same prefix in their name                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1818`_ | CLOUDSTACK-9655_   | Bug           | Major    | The template which is registered in all zones will be      |
|                         |          |                    |               |          | deleted by deleting 1 template on any zone                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1939`_ | CLOUDSTACK-8886_   | Bug           | Major    | Limitations is listUsageRecords output - listUsageRecords  |
|                         |          |                    |               |          | does not return "domain"                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1741`_ |                    |               |          | Updated StrongSwan VPN Implementation                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#873`_  | CLOUDSTACK-8896_   | Bug           | Major    | Allocated percentage of storage can go beyond 100%         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1794`_ |                    |               |          | added more guest os                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1938`_ | CLOUDSTACK-9780_   | Bug           | Major    | Default to Java8 if JAVA_HOME is not set                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1876`_ | CLOUDSTACK-9715_   | Bug           | Major    | "somaxconn" value on VR is not reflecting value from       |
|                         |          |                    |               |          | /etc/sysctl.conf                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#928`_  | CLOUDSTACK-8950_   | Bug           | Major    | Hypervisor Parameter check is not performed  for           |
|                         |          |                    |               |          | registerTemplate and getUploadParamsForTemplate API's.     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1183`_ |                    |               |          | Marvin test to verify that adding TCP ports 500,4500 and   |
|                         |          |                    |               |          | 1701 in vpn should not fail                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1416`_ | CLOUDSTACK-8717_   | Bug           | Major    | Failed to start instance after restoring the running       |
|                         |          |                    |               |          | instance                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#844`_  | CLOUDSTACK-7985_   | Improvement   | Major    | assignVM in Advanced zone with Security Groups             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1929`_ | CLOUDSTACK-9770_   | Bug           | Critical | Virtual router / Network regression since 4.9.1.0 with     |
|                         |          |                    |               |          | public interface eth2                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1697`_ | CLOUDSTACK-4858_   | Bug           | Major    | Disable copy snapshot to secondary storage                 |
|                         |          |                    |               |          | snapshot.backup.rightafter                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1905`_ | CLOUDSTACK-9738_   | Improvement   | Major    | Optimize vm expunge process for instances with vm          |
|                         |          |                    |               |          | snapshots                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1767`_ | CLOUDSTACK-9457_   | Bug           | Minor    | Allow retrieval and modification of VM and template        |
|                         |          |                    |               |          | details via API and UI                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1892`_ | CLOUDSTACK-9731_   | Bug           | Major    | Hardcoded label appears on the Add zone wizard             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#775`_  | CLOUDSTACK-8805_   | Bug           | Major    | Domains become inactive automatically.                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1890`_ | CLOUDSTACK-9712_   | Bug           | Critical | Establishing Remote access VPN  is failing due to mismatch |
|                         |          |                    |               |          | of preshared secrets post Disable/Enable VPN.              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1871`_ | CLOUDSTACK-9692_   | Bug           | Major    | Reset password service is not running on Redundant virtual |
|                         |          |                    |               |          | routers.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1921`_ |                    |               |          | Dockerfile: Upgrade base distro to Ubuntu 16.04, fix       |
|                         |          |                    |               |          | support for JDK8                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1920`_ |                    |               |          | Change the README link for event page to the current ACS   |
|                         |          |                    |               |          | CCCs website                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#977`_  | CLOUDSTACK-8746_   | Improvement   | Major    | VM Snapshotting implementation for KVM                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1700`_ | CLOUDSTACK-9359_   | Sub-task      | Major    | Return ip6address in Basic Networking                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1749`_ | CLOUDSTACK-9619_   | Bug           | Major    | Fixes for PR 1600                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1904`_ | CLOUDSTACK-9729_   | Bug           | Blocker  | Spring 4.x support PR-1638 broke Nuage VSP plugin as of    |
|                         |          |                    |               |          | dependency to com.amazonaws.util.json.JSONException        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1888`_ | CLOUDSTACK-9710_   | Bug           | Major    | Switch to JDK 1.8                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1899`_ | CLOUDSTACK-9650_   | Improvement   | Major    | Allow starting VMs regardless of cpu/memory                |
|                         |          |                    |               |          | cluster.disablethreshold setting                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1887`_ |                    |               |          | schema: Fix upgrade issue for 4.9.1.0->4.9.2.0             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1863`_ |                    |               |          | Smoke tests xen:iscsi fix                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1638`_ | CLOUDSTACK-9456_   | Bug           | Major    | Migrate master to use Java8 and Spring4                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1854`_ |                    |               |          | 4.9 multiplex testing                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1858`_ |                    |               |          | README: Happy Christmas, happy holidays!                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1827`_ | CLOUDSTACK-9673_   | Bug           | Critical | Exception occured while creating the CPVM in the VmWare    |
|                         |          |                    |               |          | Setup over standard vSwitches                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1828`_ | CLOUDSTACK-9676_   | Bug           | Critical | Start instance fails after reverting to a VM snapshot,     |
|                         |          |                    |               |          | when there are child VM snapshots                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1764`_ | CLOUDSTACK-9597_   | Bug           | Major    | Incorrect updateResourceCount()                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1811`_ | CLOUDSTACK-9649_   | Bug           | Major    | In the management server log there is an error related to  |
|                         |          |                    |               |          | 0.0.0.0 IP address                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1804`_ | CLOUDSTACK-9639_   | Bug           | Major    | Unable to create shared network with vLan isolation        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1782`_ | CLOUDSTACK-9617_   | Bug           | Major    | Enabling Remote access Vpn Fails when there is a           |
|                         |          |                    |               |          | portforwarding rule of the reserved ports ( 1701 , 500 ,   |
|                         |          |                    |               |          | 4500) under TCP protocol.                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1783`_ | CLOUDSTACK-9615_   | Bug           | Major    | Ingress Firewall Rules with blank start and End ports      |
|                         |          |                    |               |          | doesnt get applied                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1711`_ |                    |               |          | XenServer 7 Support                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1851`_ |                    |               |          | schema: Upgrade path from 4.9.1.0 to 4.9.2.0               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1839`_ | CLOUDSTACK-9683_   | Bug           | Major    | system.vm.default.hypervisor Does Not Pin Hypervisor Type  |
|                         |          |                    |               |          | of Virtual Routers                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1846`_ | CLOUDSTACK-9688_   | Bug           | Major    | Fix smoke test failures for 4.9                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1831`_ | CLOUDSTACK-9671_   | Bug           | Major    | Unknown column 'image_store_details.display' in 'field     |
|                         |          |                    |               |          | list' when upgrade from 4.9.1.0 to 4.10.0.0 SNAPSHOT       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#896`_  | CLOUDSTACK-8908_   | Bug           | Major    | After copying the template charging for that template is   |
|                         |          |                    |               |          | stopped                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1796`_ | CLOUDSTACK-9626_   | Bug           | Major    | Instance fails to start after unsuccesful compute offering |
|                         |          |                    |               |          | upgrade.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1817`_ | CLOUDSTACK-9654_   | Bug           | Major    | Missing hypervisor mapping of various SUSE Linux guest os  |
|                         |          |                    |               |          | versions on VMware 6.0                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1396`_ | CLOUDSTACK-9269_   | Bug           | Major    | Missing field for Switch type for Management and Storage   |
|                         |          |                    |               |          | traffic types                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1820`_ | CLOUDSTACK-9656_   | Bug           | Blocker  | Usage does not gather if you have a project with usage     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1822`_ | CLOUDSTACK-9584_   | Bug           | Major    | Increase component tests coverage in Travis run            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1821`_ | CLOUDSTACK-9659_   | Bug           | Major    | mismatch in traffic type in ip_associations.json and       |
|                         |          |                    |               |          | ips.json                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1805`_ | CLOUDSTACK-9637_   | Bug           | Major    | Template create from snapshot does not populate            |
|                         |          |                    |               |          | vm_template_details                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1772`_ | CLOUDSTACK-9627_   | Bug           | Major    | Template Doens't get sync when using Swift as Secondary    |
|                         |          |                    |               |          | Storage                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1618`_ | CLOUDSTACK-9643_   | Improvement   | Major    | Add OS info to list snapshots response                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1622`_ | CLOUDSTACK-9644_   | Improvement   | Major    | Add bits field to template response                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1566`_ | CLOUDSTACK-9645_   | Improvement   | Major    | Add support for not restarting the management server after |
|                         |          |                    |               |          | setup                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1809`_ | CLOUDSTACK-9646_   | Bug           | Critical | [Usage] No usage is generated for uploaded                 |
|                         |          |                    |               |          | templates/volumes from local                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1579`_ | CLOUDSTACK-9403_   | Task          | Major    | Nuage VSP Plugin : Support for SharedNetwork fuctionality  |
|                         |          |                    |               |          | including Marvin test coverage                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1659`_ | CLOUDSTACK-9339_   | Bug           | Major    | Virtual Routers don't handle Multiple Public Interfaces    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1799`_ | CLOUDSTACK-9632_   | Bug           | Major    | Upgrade bountycastle to 1.55+                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1816`_ | CLOUDSTACK-9564_   | Bug           | Major    | Fix memory leak in VmwareContextPool                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1765`_ |                    |               |          | Cloudstack 9586: When using local storage with Xenserver   |
|                         |          |                    |               |          | prepareTemplate does not work with multiple primary store  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1729`_ | CLOUDSTACK-9564_   | Bug           | Major    | Fix memory leak in VmwareContextPool                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1808`_ | CLOUDSTACK-9648_   | Bug           | Major    | Checkstyle module version fails to update by build_asf.sh  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1802`_ | CLOUDSTACK-9635_   | Bug           | Major    | fix test_privategw_acl.py                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1806`_ |                    |               |          | travis: cleanup apt before installing packages             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1803`_ | CLOUDSTACK-9636_   | Bug           | Major    | The host alerts box should be named as hosts in Alerts.    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1800`_ | CLOUDSTACK-9633_   | Bug           | Major    | test_snapshot is failing due to incorrect string           |
|                         |          |                    |               |          | construction in utils.py                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#828`_  | CLOUDSTACK-8854_   | Bug           | Major    | Apple Mac OS/X VM get created without USB controller in    |
|                         |          |                    |               |          | ESXi hypervisors                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1801`_ |                    |               |          | fix marvin test failure test_router_dhcp_opts              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1793`_ | CLOUDSTACK-9624_   | Bug           | Major    | Incorrect hypervisor mapping of guest os Windows 2008      |
|                         |          |                    |               |          | Server R2 (64-bit) on VMware                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1710`_ | CLOUDSTACK-9538_   | Bug           | Major    | Deleting Snapshot From Primary Storage Fails on RBD        |
|                         |          |                    |               |          | Storage if you already delete vm's itself                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1755`_ | CLOUDSTACK-9584_   | Bug           | Major    | Increase component tests coverage in Travis run            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1791`_ | CLOUDSTACK-9622_   | Improvement   | Trivial  | Localisation for 'Project' label on the top of Web UI      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1789`_ |                    |               |          | Update L10N files from Transifex (2016-11-27) for the new  |
|                         |          |                    |               |          | release 4.10.0.0                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1785`_ | CLOUDSTACK-9416_   | Bug           | Major    | ACS master GUI: Enabling Static NAT on an associated       |
|                         |          |                    |               |          | Public IP to one of the NICs (networks) of a multi-NIC VM  |
|                         |          |                    |               |          | fails due to a wrong (default) Guest VM IP being selected  |
|                         |          |                    |               |          | in the GUI                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1788`_ |                    |               |          | systemvm: Fix regression from fwd-merging PR #1766         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1577`_ | CLOUDSTACK-9321_   | Bug           | Critical | Multiple Internal LB rules (more than one Internal LB rule |
|                         |          |                    |               |          | with same source IP address) are not getting resolved in   |
|                         |          |                    |               |          | the corresponding InternalLbVm instance's haproxy.cfg file |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1580`_ | CLOUDSTACK-9402_   | Task          | Major    | Nuage VSP Plugin : Support for underlay features (Source & |
|                         |          |                    |               |          | Static NAT to underlay) including Marvin test coverage on  |
|                         |          |                    |               |          | master                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1635`_ | CLOUDSTACK-9451_   | Bug           | Minor    | stopVirtualMachine ignores forced parameter                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1738`_ | CLOUDSTACK-9566_   | Bug           | Major    | instance-id metadata for baremetal VM returns ID           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1766`_ | CLOUDSTACK-9598_   | Bug           | Major    | wrong defaut gateway in guest VM with nics in isolated and |
|                         |          |                    |               |          | a shared network                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#756`_  | CLOUDSTACK-8781_   | Bug           | Trivial  | Superfluous field during VPC creation                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1542`_ | CLOUDSTACK-9379_   | Improvement   | Major    | Support nested virtualization at VM level on VMware        |
|                         |          |                    |               |          | Hypervisor                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1680`_ | CLOUDSTACK-9498_   | Bug           | Major    | VR CsFile search utility methods fail when search string   |
|                         |          |                    |               |          | has char *, + etc                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1681`_ | CLOUDSTACK-9491_   | Bug           | Major    | Vmware resource: incorrect parsing of device list to find  |
|                         |          |                    |               |          | ethener index of plugged nic                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1745`_ | CLOUDSTACK-9503_   | Bug           | Major    | The router script times out resulting in failure of        |
|                         |          |                    |               |          | deployment                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1757`_ | CLOUDSTACK-9583_   | Bug           | Major    | VR: In CsDhcp.py preseed both hostaname and localhost to   |
|                         |          |                    |               |          | resolve to 127.0.0.1                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1684`_ | CLOUDSTACK-9489_   | Bug           | Blocker  | When upgrading, Config.java new configuration are not      |
|                         |          |                    |               |          | updated.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1591`_ |                    |               |          | Updating Alert codes                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1674`_ | CLOUDSTACK-9460_   | Bug           | Major    | Graceful handling of Mysql server connection timeout       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1673`_ | CLOUDSTACK-9071_   | Bug           | Major    | stats.output.uri stops the server from starting if the uri |
|                         |          |                    |               |          | is malformed                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1676`_ | CLOUDSTACK-9502_   | Bug           | Major    | Target CLOUDSTACK-9386 into 4.9 release branch             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1677`_ | CLOUDSTACK-8830_   | Bug           | Major    | [VMware] VM snapshot fails for 12 min after instance       |
|                         |          |                    |               |          | creation                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1578`_ | CLOUDSTACK-9401_   | Task          | Major    | Nuage VSP Plugin : Support for InternalDns including       |
|                         |          |                    |               |          | Marvin test coverage                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1751`_ |                    |               |          | systemd: Fix semicolon missing in b75e69                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1743`_ | CLOUDSTACK-8326_   | Bug           | Major    | Bug in cloudstack virtual router (KVM) in Simple zone with |
|                         |          |                    |               |          | public ips / DHCP Debian Wheezy specific                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9, 4.10     | `#1744`_ | CLOUDSTACK-9183_   | Bug           | Major    | CS 4.7.0 bash: /opt/cloud/bin/getRouterAlerts.sh: No such  |
|                         |          |                    |               |          | file or directory                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1713`_ | CLOUDSTACK-9552_   | Bug           | Major    | KVM Security Groups do not allow DNS over TCP egress       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1746`_ |                    |               |          | SSVM downloader now handles redirects properly.            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1714`_ | CLOUDSTACK-9553_   | Bug           | Major    | Usage event is not getting recorded for snapshots in a     |
|                         |          |                    |               |          | specific scenario                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1715`_ | CLOUDSTACK-9554_   | Bug           | Major    | Juniper Contrail plug-in is publishing events to wrong     |
|                         |          |                    |               |          | message bus                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1705`_ |                    |               |          | Made the changes to improve logging.                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1728`_ | CLOUDSTACK-9551_   | Bug           | Major    | Pull KVM agent's tmp folder usage within its own folder    |
|                         |          |                    |               |          | structure                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1694`_ | CLOUDSTACK-9509_   | Bug           | Critical | KVM Hosts connect with no storage                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1600`_ |                    |               |          | Support Backup of Snapshots for Managed Storage            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1732`_ |                    |               |          | Switched to the official SolidFire SDK for Java            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1701`_ | CLOUDSTACK-9534_   | Bug           | Major    | Allow users to destroy VR when in running state            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1712`_ | CLOUDSTACK-9550_   | Bug           | Major    | Metrics view does not filter items based on                |
|                         |          |                    |               |          | zone/cluster/host it is in                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1742`_ | CLOUDSTACK-9544_   | Bug           | Major    | Account API keys vulnerability in Cloudstack with possible |
|                         |          |                    |               |          | privileges escalation                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1615`_ | CLOUDSTACK-9438_   | Improvement   | Major    | Fix for CLOUDSTACK-9252 - Make NFS version changeable in   |
|                         |          |                    |               |          | UI                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1731`_ | CLOUDSTACK-9565_   | Bug           | Major    | Fix intermittent failure in oobm test                      |
|                         |          |                    |               |          | test_oobm_zchange_password                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1642`_ | CLOUDSTACK-9504_   | Bug           | Major    | Fully support system VMs on managed storage                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1451`_ | CLOUDSTACK-9319_   | Bug           | Trivial  | Timeout is not passed to virtual router operations         |
|                         |          |                    |               |          | consistently                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1724`_ | CLOUDSTACK-9511_   | Bug           | Critical | fix test_privategw_acl.py to handle multiple physical      |
|                         |          |                    |               |          | networks                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1624`_ |                    |               |          | Fixes regarding VOLUME_DELETE events resulting from        |
|                         |          |                    |               |          | account deletion                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1692`_ |                    |               |          | Fix Smoke Test Failures                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1572`_ | CLOUDSTACK-9395_   | New Feature   | Major    | Add VirtIO Random Number Geneator to KVM Instances         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1464`_ | CLOUDSTACK-9337_   | Test          | Major    | [CI] Enhance vcenter library to add datacenter             |
|                         |          |                    |               |          | programmatically                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1548`_ |                    |               |          | Compabitility fix for Docker >= 1.11 (docker/docker#19490) |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1702`_ | CLOUDSTACK-9535_   | Improvement   | Major    | [API] listVMSnapshots improvement                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1698`_ | CLOUDSTACK-9525_   | Bug           | Major    | add support for windows 10 guest os in xenserver 6.5       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1699`_ | CLOUDSTACK-9513_   | Bug           | Major    | Migrate transifex workflow and format to json              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1696`_ | CLOUDSTACK-9364_   | Task          | Major    | Add Support for Ubuntu 16.04                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1690`_ |                    |               |          | Update L10N resource files with 4.10 strings from          |
|                         |          |                    |               |          | Transifex (20160925)                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1619`_ |                    |               |          | Add the Transifex config for next version of CS (4.10)     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1669`_ |                    |               |          | Make CloudStack JSP-free                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1693`_ | CLOUDSTACK-9505_   | Bug           | Major    | Fix test_deploy_vgpu_enabled tests cleanup                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1689`_ |                    |               |          | Switched to the official SolidFire SDK for Python          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1602`_ | CLOUDSTACK-9422_   | Bug           | Major    | Granular VMware vm's creation as full clones on HV         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1666`_ | CLOUDSTACK-9480_   | Bug           | Critical | Egress Firewall: Incorrect use of Allow/Deny for ICMP      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1645`_ |                    |               |          | On snapshot backup, this converts the rbd raw format on    |
|                         |          |                    |               |          | disk to qcow2 for compression.                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1661`_ |                    |               |          | Export UUID for zone creation event completion.            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1671`_ |                    |               |          | Adding support for cross-cluster storage migration for     |
|                         |          |                    |               |          | managed storage when using XenServer                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1560`_ | CLOUDSTACK-9386_   | Bug           | Major    | DS template copies don’t get deleted in VMware ESXi with   |
|                         |          |                    |               |          | multiple clusters and zone wide storage                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1658`_ |                    |               |          | Added an additional JSON diff output to the                |
|                         |          |                    |               |          | ApiXmlDocReader                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#866`_  | CLOUDSTACK-8751_   | Improvement   | Major    | Minimise VR downtime during network update                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1672`_ |                    |               |          | In comment, Add missing packages for Docker Ubuntu builds  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1605`_ | CLOUDSTACK-9428_   | Improvement   | Major    | Fix for CLOUDSTACK-9211 - Improve performance              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1665`_ |                    |               |          | Changes database upgrade script names to be consistent for |
|                         |          |                    |               |          | the 4.9.1.0 release                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1636`_ |                    |               |          | Fix a quote issue with Spanish L10N (from transifex        |
|                         |          |                    |               |          | translation)                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1670`_ | CLOUDSTACK-9481_   | Bug           | Major    | Convert MyISAM table to InnoDB for consistency             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1654`_ |                    |               |          | Updating pom.xml version numbers for release               |
|                         |          |                    |               |          | 4.8.2.0-SNAPSHOT                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1663`_ | CLOUDSTACK-6432_   | Bug           | Major    | Prevent VR from response to DNS request from outside of    |
|                         |          |                    |               |          | network                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1621`_ | CLOUDSTACK-9444_   | Bug           | Minor    | ERROR c.c.u.d.DriverLoader DB driver type null is not      |
|                         |          |                    |               |          | supported (during migration from 4.7.1 to 4.9)             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1648`_ |                    |               |          | test/integration: fix tearDown order in list_acl_ tests    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1647`_ | CLOUDSTACK-9462_   | Bug           | Major    | Systemd packaging for Ubuntu 16.04                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1657`_ | CLOUDSTACK-9467_   | Bug           | Blocker  | Fresh installation of cloudstack-usage server fails        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.8, 4.9, 4.10          | `#1656`_ | CLOUDSTACK-9466_   | Bug           | Major    | Upgrading to older CloudStack 4.0.x to 4.1.x causes sql    |
|                         |          |                    |               |          | contraint errors                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1634`_ | CLOUDSTACK-9452_   | Bug           | Blocker  | CentOS6 kvm hosts stop working after upgrade               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1599`_ |                    |               |          | Marvin: Fix codegenerator to work with API discovery       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1646`_ |                    |               |          | [4.9/LTS] Add upgrade path from 4.9.0 to 4.9.1, change     |
|                         |          |                    |               |          | version to 4.9.1.0-SNAPSHOT                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1630`_ |                    |               |          | Add projectid to project details page                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1649`_ | CLOUDSTACK-9463_   | Bug           | Major    | Dynamic roles migrate script fails with old                |
|                         |          |                    |               |          | commands.properties file format                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1620`_ |                    |               |          | oobm: simply change password transactional logic           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1641`_ | CLOUDSTACK-9459_   | Bug           | Critical | Database upgrade from 3.0.7 to 4.9.0 fails with a          |
|                         |          |                    |               |          | ResultSet closed exception                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1628`_ |                    |               |          | updated contributing.md                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9, 4.10               | `#1626`_ |                    |               |          | [blocker] Fix systemvm template build                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1631`_ |                    |               |          | Fix debian build error due to commit 3315eb5               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.7, 4.8, 4.9, 4.10     | `#1612`_ | CLOUDSTACK-9446_   | Bug           | Major    | Package marvin and integration-tests for making testing    |
|                         |          |                    |               |          | easier                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10                    | `#1625`_ |                    |               |          | [blocker] cloudstack: fix upgrade paths to 4.10.0          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+

.. _`#2162`: https://github.com/apache/cloudstack/pull/2162
.. _CLOUDSTACK-9980: https://issues.apache.org/jira/browse/CLOUDSTACK-9980
.. _`#2150`: https://github.com/apache/cloudstack/pull/2150
.. _`#2089`: https://github.com/apache/cloudstack/pull/2089
.. _`#2100`: https://github.com/apache/cloudstack/pull/2100
.. _CLOUDSTACK-9907: https://issues.apache.org/jira/browse/CLOUDSTACK-9907
.. _`#2135`: https://github.com/apache/cloudstack/pull/2135
.. _CLOUDSTACK-9860: https://issues.apache.org/jira/browse/CLOUDSTACK-9860
.. _`#1759`: https://github.com/apache/cloudstack/pull/1759
.. _CLOUDSTACK-9589: https://issues.apache.org/jira/browse/CLOUDSTACK-9589
.. _`#1726`: https://github.com/apache/cloudstack/pull/1726
.. _CLOUDSTACK-9560: https://issues.apache.org/jira/browse/CLOUDSTACK-9560
.. _`#1866`: https://github.com/apache/cloudstack/pull/1866
.. _`#2126`: https://github.com/apache/cloudstack/pull/2126
.. _CLOUDSTACK-9740: https://issues.apache.org/jira/browse/CLOUDSTACK-9740
.. _`#2132`: https://github.com/apache/cloudstack/pull/2132
.. _CLOUDSTACK-9935: https://issues.apache.org/jira/browse/CLOUDSTACK-9935
.. _`#1716`: https://github.com/apache/cloudstack/pull/1716
.. _CLOUDSTACK-9555: https://issues.apache.org/jira/browse/CLOUDSTACK-9555
.. _`#1725`: https://github.com/apache/cloudstack/pull/1725
.. _CLOUDSTACK-9559: https://issues.apache.org/jira/browse/CLOUDSTACK-9559
.. _`#1734`: https://github.com/apache/cloudstack/pull/1734
.. _CLOUDSTACK-9567: https://issues.apache.org/jira/browse/CLOUDSTACK-9567
.. _`#1756`: https://github.com/apache/cloudstack/pull/1756
.. _CLOUDSTACK-9585: https://issues.apache.org/jira/browse/CLOUDSTACK-9585
.. _`#1761`: https://github.com/apache/cloudstack/pull/1761
.. _CLOUDSTACK-9592: https://issues.apache.org/jira/browse/CLOUDSTACK-9592
.. _`#1776`: https://github.com/apache/cloudstack/pull/1776
.. _CLOUDSTACK-9603: https://issues.apache.org/jira/browse/CLOUDSTACK-9603
.. _`#1779`: https://github.com/apache/cloudstack/pull/1779
.. _CLOUDSTACK-9610: https://issues.apache.org/jira/browse/CLOUDSTACK-9610
.. _`#1841`: https://github.com/apache/cloudstack/pull/1841
.. _CLOUDSTACK-9684: https://issues.apache.org/jira/browse/CLOUDSTACK-9684
.. _`#1850`: https://github.com/apache/cloudstack/pull/1850
.. _CLOUDSTACK-9694: https://issues.apache.org/jira/browse/CLOUDSTACK-9694
.. _`#1862`: https://github.com/apache/cloudstack/pull/1862
.. _CLOUDSTACK-9704: https://issues.apache.org/jira/browse/CLOUDSTACK-9704
.. _`#1865`: https://github.com/apache/cloudstack/pull/1865
.. _CLOUDSTACK-9705: https://issues.apache.org/jira/browse/CLOUDSTACK-9705
.. _`#1868`: https://github.com/apache/cloudstack/pull/1868
.. _CLOUDSTACK-9707: https://issues.apache.org/jira/browse/CLOUDSTACK-9707
.. _`#1869`: https://github.com/apache/cloudstack/pull/1869
.. _CLOUDSTACK-9701: https://issues.apache.org/jira/browse/CLOUDSTACK-9701
.. _`#1900`: https://github.com/apache/cloudstack/pull/1900
.. _CLOUDSTACK-8862: https://issues.apache.org/jira/browse/CLOUDSTACK-8862
.. _`#2012`: https://github.com/apache/cloudstack/pull/2012
.. _CLOUDSTACK-9842: https://issues.apache.org/jira/browse/CLOUDSTACK-9842
.. _`#2015`: https://github.com/apache/cloudstack/pull/2015
.. _CLOUDSTACK-9843: https://issues.apache.org/jira/browse/CLOUDSTACK-9843
.. _`#2086`: https://github.com/apache/cloudstack/pull/2086
.. _CLOUDSTACK-9905: https://issues.apache.org/jira/browse/CLOUDSTACK-9905
.. _`#2113`: https://github.com/apache/cloudstack/pull/2113
.. _CLOUDSTACK-9162: https://issues.apache.org/jira/browse/CLOUDSTACK-9162
.. _`#1894`: https://github.com/apache/cloudstack/pull/1894
.. _CLOUDSTACK-9700: https://issues.apache.org/jira/browse/CLOUDSTACK-9700
.. _`#892`: https://github.com/apache/cloudstack/pull/892
.. _CLOUDSTACK-8910: https://issues.apache.org/jira/browse/CLOUDSTACK-8910
.. _`#899`: https://github.com/apache/cloudstack/pull/899
.. _CLOUDSTACK-8921: https://issues.apache.org/jira/browse/CLOUDSTACK-8921
.. _`#927`: https://github.com/apache/cloudstack/pull/927
.. _CLOUDSTACK-9901: https://issues.apache.org/jira/browse/CLOUDSTACK-9901
.. _`#1867`: https://github.com/apache/cloudstack/pull/1867
.. _CLOUDSTACK-9706: https://issues.apache.org/jira/browse/CLOUDSTACK-9706
.. _`#1996`: https://github.com/apache/cloudstack/pull/1996
.. _CLOUDSTACK-9099: https://issues.apache.org/jira/browse/CLOUDSTACK-9099
.. _`#2016`: https://github.com/apache/cloudstack/pull/2016
.. _CLOUDSTACK-9835: https://issues.apache.org/jira/browse/CLOUDSTACK-9835
.. _`#2108`: https://github.com/apache/cloudstack/pull/2108
.. _CLOUDSTACK-9860: https://issues.apache.org/jira/browse/CLOUDSTACK-9860
.. _`#2133`: https://github.com/apache/cloudstack/pull/2133
.. _CLOUDSTACK-9937: https://issues.apache.org/jira/browse/CLOUDSTACK-9937
.. _`#1987`: https://github.com/apache/cloudstack/pull/1987
.. _CLOUDSTACK-9814: https://issues.apache.org/jira/browse/CLOUDSTACK-9814
.. _`#2072`: https://github.com/apache/cloudstack/pull/2072
.. _CLOUDSTACK-9895: https://issues.apache.org/jira/browse/CLOUDSTACK-9895
.. _`#1967`: https://github.com/apache/cloudstack/pull/1967
.. _CLOUDSTACK-9638: https://issues.apache.org/jira/browse/CLOUDSTACK-9638
.. _`#2082`: https://github.com/apache/cloudstack/pull/2082
.. _CLOUDSTACK-9017: https://issues.apache.org/jira/browse/CLOUDSTACK-9017
.. _`#2098`: https://github.com/apache/cloudstack/pull/2098
.. _CLOUDSTACK-9660: https://issues.apache.org/jira/browse/CLOUDSTACK-9660
.. _`#2121`: https://github.com/apache/cloudstack/pull/2121
.. _CLOUDSTACK-9641: https://issues.apache.org/jira/browse/CLOUDSTACK-9641
.. _`#2120`: https://github.com/apache/cloudstack/pull/2120
.. _CLOUDSTACK-9665: https://issues.apache.org/jira/browse/CLOUDSTACK-9665
.. _`#1824`: https://github.com/apache/cloudstack/pull/1824
.. _CLOUDSTACK-9657: https://issues.apache.org/jira/browse/CLOUDSTACK-9657
.. _`#2103`: https://github.com/apache/cloudstack/pull/2103
.. _CLOUDSTACK-8647: https://issues.apache.org/jira/browse/CLOUDSTACK-8647
.. _`#2080`: https://github.com/apache/cloudstack/pull/2080
.. _`#1908`: https://github.com/apache/cloudstack/pull/1908
.. _CLOUDSTACK-9317: https://issues.apache.org/jira/browse/CLOUDSTACK-9317
.. _`#874`: https://github.com/apache/cloudstack/pull/874
.. _CLOUDSTACK-8897: https://issues.apache.org/jira/browse/CLOUDSTACK-8897
.. _`#2106`: https://github.com/apache/cloudstack/pull/2106
.. _CLOUDSTACK-9168: https://issues.apache.org/jira/browse/CLOUDSTACK-9168
.. _`#2006`: https://github.com/apache/cloudstack/pull/2006
.. _CLOUDSTACK-9833: https://issues.apache.org/jira/browse/CLOUDSTACK-9833
.. _`#1322`: https://github.com/apache/cloudstack/pull/1322
.. _CLOUDSTACK-9217: https://issues.apache.org/jira/browse/CLOUDSTACK-9217
.. _`#868`: https://github.com/apache/cloudstack/pull/868
.. _CLOUDSTACK-8894: https://issues.apache.org/jira/browse/CLOUDSTACK-8894
.. _`#1971`: https://github.com/apache/cloudstack/pull/1971
.. _CLOUDSTACK-9726: https://issues.apache.org/jira/browse/CLOUDSTACK-9726
.. _`#1873`: https://github.com/apache/cloudstack/pull/1873
.. _CLOUDSTACK-9709: https://issues.apache.org/jira/browse/CLOUDSTACK-9709
.. _`#1872`: https://github.com/apache/cloudstack/pull/1872
.. _CLOUDSTACK-3223: https://issues.apache.org/jira/browse/CLOUDSTACK-3223
.. _`#1842`: https://github.com/apache/cloudstack/pull/1842
.. _CLOUDSTACK-9686: https://issues.apache.org/jira/browse/CLOUDSTACK-9686
.. _`#1883`: https://github.com/apache/cloudstack/pull/1883
.. _CLOUDSTACK-9723: https://issues.apache.org/jira/browse/CLOUDSTACK-9723
.. _`#1968`: https://github.com/apache/cloudstack/pull/1968
.. _CLOUDSTACK-9666: https://issues.apache.org/jira/browse/CLOUDSTACK-9666
.. _`#1945`: https://github.com/apache/cloudstack/pull/1945
.. _CLOUDSTACK-9787: https://issues.apache.org/jira/browse/CLOUDSTACK-9787
.. _`#2002`: https://github.com/apache/cloudstack/pull/2002
.. _CLOUDSTACK-9831: https://issues.apache.org/jira/browse/CLOUDSTACK-9831
.. _`#2027`: https://github.com/apache/cloudstack/pull/2027
.. _CLOUDSTACK-9918: https://issues.apache.org/jira/browse/CLOUDSTACK-9918
.. _`#2018`: https://github.com/apache/cloudstack/pull/2018
.. _CLOUDSTACK-9848: https://issues.apache.org/jira/browse/CLOUDSTACK-9848
.. _`#2055`: https://github.com/apache/cloudstack/pull/2055
.. _CLOUDSTACK-9887: https://issues.apache.org/jira/browse/CLOUDSTACK-9887
.. _`#2070`: https://github.com/apache/cloudstack/pull/2070
.. _CLOUDSTACK-9904: https://issues.apache.org/jira/browse/CLOUDSTACK-9904
.. _`#1995`: https://github.com/apache/cloudstack/pull/1995
.. _CLOUDSTACK-9828: https://issues.apache.org/jira/browse/CLOUDSTACK-9828
.. _`#1870`: https://github.com/apache/cloudstack/pull/1870
.. _CLOUDSTACK-9708: https://issues.apache.org/jira/browse/CLOUDSTACK-9708
.. _`#1840`: https://github.com/apache/cloudstack/pull/1840
.. _CLOUDSTACK-9685: https://issues.apache.org/jira/browse/CLOUDSTACK-9685
.. _`#1849`: https://github.com/apache/cloudstack/pull/1849
.. _CLOUDSTACK-9690: https://issues.apache.org/jira/browse/CLOUDSTACK-9690
.. _`#2007`: https://github.com/apache/cloudstack/pull/2007
.. _CLOUDSTACK-9834: https://issues.apache.org/jira/browse/CLOUDSTACK-9834
.. _`#1180`: https://github.com/apache/cloudstack/pull/1180
.. _CLOUDSTACK-9112: https://issues.apache.org/jira/browse/CLOUDSTACK-9112
.. _`#1992`: https://github.com/apache/cloudstack/pull/1992
.. _CLOUDSTACK-9824: https://issues.apache.org/jira/browse/CLOUDSTACK-9824
.. _`#2075`: https://github.com/apache/cloudstack/pull/2075
.. _CLOUDSTACK-9900: https://issues.apache.org/jira/browse/CLOUDSTACK-9900
.. _`#2077`: https://github.com/apache/cloudstack/pull/2077
.. _`#2062`: https://github.com/apache/cloudstack/pull/2062
.. _CLOUDSTACK-9878: https://issues.apache.org/jira/browse/CLOUDSTACK-9878
.. _`#1949`: https://github.com/apache/cloudstack/pull/1949
.. _`#1813`: https://github.com/apache/cloudstack/pull/1813
.. _CLOUDSTACK-9604: https://issues.apache.org/jira/browse/CLOUDSTACK-9604
.. _`#803`: https://github.com/apache/cloudstack/pull/803
.. _CLOUDSTACK-8833: https://issues.apache.org/jira/browse/CLOUDSTACK-8833
.. _`#1606`: https://github.com/apache/cloudstack/pull/1606
.. _`#2056`: https://github.com/apache/cloudstack/pull/2056
.. _CLOUDSTACK-8829: https://issues.apache.org/jira/browse/CLOUDSTACK-8829
.. _`#1810`: https://github.com/apache/cloudstack/pull/1810
.. _CLOUDSTACK-9647: https://issues.apache.org/jira/browse/CLOUDSTACK-9647
.. _`#2071`: https://github.com/apache/cloudstack/pull/2071
.. _CLOUDSTACK-9815: https://issues.apache.org/jira/browse/CLOUDSTACK-9815
.. _`#2030`: https://github.com/apache/cloudstack/pull/2030
.. _CLOUDSTACK-9864: https://issues.apache.org/jira/browse/CLOUDSTACK-9864
.. _`#1792`: https://github.com/apache/cloudstack/pull/1792
.. _CLOUDSTACK-9623: https://issues.apache.org/jira/browse/CLOUDSTACK-9623
.. _`#1970`: https://github.com/apache/cloudstack/pull/1970
.. _CLOUDSTACK-9725: https://issues.apache.org/jira/browse/CLOUDSTACK-9725
.. _`#1997`: https://github.com/apache/cloudstack/pull/1997
.. _CLOUDSTACK-9208: https://issues.apache.org/jira/browse/CLOUDSTACK-9208
.. _`#2066`: https://github.com/apache/cloudstack/pull/2066
.. _CLOUDSTACK-9893: https://issues.apache.org/jira/browse/CLOUDSTACK-9893
.. _`#2053`: https://github.com/apache/cloudstack/pull/2053
.. _`#2069`: https://github.com/apache/cloudstack/pull/2069
.. _CLOUDSTACK-8793: https://issues.apache.org/jira/browse/CLOUDSTACK-8793
.. _`#2037`: https://github.com/apache/cloudstack/pull/2037
.. _CLOUDSTACK-9871: https://issues.apache.org/jira/browse/CLOUDSTACK-9871
.. _`#1852`: https://github.com/apache/cloudstack/pull/1852
.. _CLOUDSTACK-9695: https://issues.apache.org/jira/browse/CLOUDSTACK-9695
.. _`#1797`: https://github.com/apache/cloudstack/pull/1797
.. _CLOUDSTACK-9630: https://issues.apache.org/jira/browse/CLOUDSTACK-9630
.. _`#1918`: https://github.com/apache/cloudstack/pull/1918
.. _`#2063`: https://github.com/apache/cloudstack/pull/2063
.. _`#1978`: https://github.com/apache/cloudstack/pull/1978
.. _CLOUDSTACK-9779: https://issues.apache.org/jira/browse/CLOUDSTACK-9779
.. _`#1582`: https://github.com/apache/cloudstack/pull/1582
.. _CLOUDSTACK-9408: https://issues.apache.org/jira/browse/CLOUDSTACK-9408
.. _`#2009`: https://github.com/apache/cloudstack/pull/2009
.. _CLOUDSTACK-9369: https://issues.apache.org/jira/browse/CLOUDSTACK-9369
.. _`#2060`: https://github.com/apache/cloudstack/pull/2060
.. _`#1819`: https://github.com/apache/cloudstack/pull/1819
.. _CLOUDSTACK-9653: https://issues.apache.org/jira/browse/CLOUDSTACK-9653
.. _`#1879`: https://github.com/apache/cloudstack/pull/1879
.. _CLOUDSTACK-9719: https://issues.apache.org/jira/browse/CLOUDSTACK-9719
.. _`#1917`: https://github.com/apache/cloudstack/pull/1917
.. _CLOUDSTACK-9756: https://issues.apache.org/jira/browse/CLOUDSTACK-9756
.. _`#1993`: https://github.com/apache/cloudstack/pull/1993
.. _CLOUDSTACK-8931: https://issues.apache.org/jira/browse/CLOUDSTACK-8931
.. _`#1957`: https://github.com/apache/cloudstack/pull/1957
.. _CLOUDSTACK-9748: https://issues.apache.org/jira/browse/CLOUDSTACK-9748
.. _`#1956`: https://github.com/apache/cloudstack/pull/1956
.. _CLOUDSTACK-9796: https://issues.apache.org/jira/browse/CLOUDSTACK-9796
.. _`#1903`: https://github.com/apache/cloudstack/pull/1903
.. _CLOUDSTACK-9356: https://issues.apache.org/jira/browse/CLOUDSTACK-9356
.. _`#1886`: https://github.com/apache/cloudstack/pull/1886
.. _CLOUDSTACK-9728: https://issues.apache.org/jira/browse/CLOUDSTACK-9728
.. _`#2024`: https://github.com/apache/cloudstack/pull/2024
.. _CLOUDSTACK-9857: https://issues.apache.org/jira/browse/CLOUDSTACK-9857
.. _`#1935`: https://github.com/apache/cloudstack/pull/1935
.. _CLOUDSTACK-9764: https://issues.apache.org/jira/browse/CLOUDSTACK-9764
.. _`#1889`: https://github.com/apache/cloudstack/pull/1889
.. _CLOUDSTACK-9718: https://issues.apache.org/jira/browse/CLOUDSTACK-9718
.. _`#1955`: https://github.com/apache/cloudstack/pull/1955
.. _CLOUDSTACK-8239: https://issues.apache.org/jira/browse/CLOUDSTACK-8239
.. _`#1980`: https://github.com/apache/cloudstack/pull/1980
.. _CLOUDSTACK-9805: https://issues.apache.org/jira/browse/CLOUDSTACK-9805
.. _`#2051`: https://github.com/apache/cloudstack/pull/2051
.. _CLOUDSTACK-9858: https://issues.apache.org/jira/browse/CLOUDSTACK-9858
.. _`#2043`: https://github.com/apache/cloudstack/pull/2043
.. _CLOUDSTACK-9876: https://issues.apache.org/jira/browse/CLOUDSTACK-9876
.. _`#2036`: https://github.com/apache/cloudstack/pull/2036
.. _CLOUDSTACK-9858: https://issues.apache.org/jira/browse/CLOUDSTACK-9858
.. _`#1771`: https://github.com/apache/cloudstack/pull/1771
.. _CLOUDSTACK-9611: https://issues.apache.org/jira/browse/CLOUDSTACK-9611
.. _`#2033`: https://github.com/apache/cloudstack/pull/2033
.. _CLOUDSTACK-9462: https://issues.apache.org/jira/browse/CLOUDSTACK-9462
.. _`#2023`: https://github.com/apache/cloudstack/pull/2023
.. _CLOUDSTACK-9808: https://issues.apache.org/jira/browse/CLOUDSTACK-9808
.. _`#2025`: https://github.com/apache/cloudstack/pull/2025
.. _`#2022`: https://github.com/apache/cloudstack/pull/2022
.. _CLOUDSTACK-9591: https://issues.apache.org/jira/browse/CLOUDSTACK-9591
.. _`#2032`: https://github.com/apache/cloudstack/pull/2032
.. _CLOUDSTACK-9783: https://issues.apache.org/jira/browse/CLOUDSTACK-9783
.. _`#1880`: https://github.com/apache/cloudstack/pull/1880
.. _CLOUDSTACK-9720: https://issues.apache.org/jira/browse/CLOUDSTACK-9720
.. _`#1944`: https://github.com/apache/cloudstack/pull/1944
.. _CLOUDSTACK-9783: https://issues.apache.org/jira/browse/CLOUDSTACK-9783
.. _`#2021`: https://github.com/apache/cloudstack/pull/2021
.. _CLOUDSTACK-9854: https://issues.apache.org/jira/browse/CLOUDSTACK-9854
.. _`#2019`: https://github.com/apache/cloudstack/pull/2019
.. _CLOUDSTACK-9851: https://issues.apache.org/jira/browse/CLOUDSTACK-9851
.. _`#1994`: https://github.com/apache/cloudstack/pull/1994
.. _CLOUDSTACK-9827: https://issues.apache.org/jira/browse/CLOUDSTACK-9827
.. _`#1961`: https://github.com/apache/cloudstack/pull/1961
.. _`#2011`: https://github.com/apache/cloudstack/pull/2011
.. _CLOUDSTACK-9811: https://issues.apache.org/jira/browse/CLOUDSTACK-9811
.. _`#2003`: https://github.com/apache/cloudstack/pull/2003
.. _CLOUDSTACK-9811: https://issues.apache.org/jira/browse/CLOUDSTACK-9811
.. _`#1923`: https://github.com/apache/cloudstack/pull/1923
.. _CLOUDSTACK-9765: https://issues.apache.org/jira/browse/CLOUDSTACK-9765
.. _`#847`: https://github.com/apache/cloudstack/pull/847
.. _CLOUDSTACK-8880: https://issues.apache.org/jira/browse/CLOUDSTACK-8880
.. _`#1953`: https://github.com/apache/cloudstack/pull/1953
.. _CLOUDSTACK-9794: https://issues.apache.org/jira/browse/CLOUDSTACK-9794
.. _`#1958`: https://github.com/apache/cloudstack/pull/1958
.. _CLOUDSTACK-5806: https://issues.apache.org/jira/browse/CLOUDSTACK-5806
.. _`#1861`: https://github.com/apache/cloudstack/pull/1861
.. _CLOUDSTACK-9698: https://issues.apache.org/jira/browse/CLOUDSTACK-9698
.. _`#1856`: https://github.com/apache/cloudstack/pull/1856
.. _CLOUDSTACK-9569: https://issues.apache.org/jira/browse/CLOUDSTACK-9569
.. _`#1991`: https://github.com/apache/cloudstack/pull/1991
.. _CLOUDSTACK-9821: https://issues.apache.org/jira/browse/CLOUDSTACK-9821
.. _`#1982`: https://github.com/apache/cloudstack/pull/1982
.. _CLOUDSTACK-9807: https://issues.apache.org/jira/browse/CLOUDSTACK-9807
.. _`#1942`: https://github.com/apache/cloudstack/pull/1942
.. _CLOUDSTACK-9784: https://issues.apache.org/jira/browse/CLOUDSTACK-9784
.. _`#1914`: https://github.com/apache/cloudstack/pull/1914
.. _CLOUDSTACK-9753: https://issues.apache.org/jira/browse/CLOUDSTACK-9753
.. _`#1896`: https://github.com/apache/cloudstack/pull/1896
.. _CLOUDSTACK-9732: https://issues.apache.org/jira/browse/CLOUDSTACK-9732
.. _`#1768`: https://github.com/apache/cloudstack/pull/1768
.. _`#1975`: https://github.com/apache/cloudstack/pull/1975
.. _`#815`: https://github.com/apache/cloudstack/pull/815
.. _CLOUDSTACK-8841: https://issues.apache.org/jira/browse/CLOUDSTACK-8841
.. _`#843`: https://github.com/apache/cloudstack/pull/843
.. _`#1825`: https://github.com/apache/cloudstack/pull/1825
.. _CLOUDSTACK-9660: https://issues.apache.org/jira/browse/CLOUDSTACK-9660
.. _`#1907`: https://github.com/apache/cloudstack/pull/1907
.. _`#1922`: https://github.com/apache/cloudstack/pull/1922
.. _CLOUDSTACK-9757: https://issues.apache.org/jira/browse/CLOUDSTACK-9757
.. _`#1915`: https://github.com/apache/cloudstack/pull/1915
.. _CLOUDSTACK-9746: https://issues.apache.org/jira/browse/CLOUDSTACK-9746
.. _`#1829`: https://github.com/apache/cloudstack/pull/1829
.. _CLOUDSTACK-9363: https://issues.apache.org/jira/browse/CLOUDSTACK-9363
.. _`#1941`: https://github.com/apache/cloudstack/pull/1941
.. _CLOUDSTACK-8663: https://issues.apache.org/jira/browse/CLOUDSTACK-8663
.. _`#1946`: https://github.com/apache/cloudstack/pull/1946
.. _CLOUDSTACK-9788: https://issues.apache.org/jira/browse/CLOUDSTACK-9788
.. _`#1948`: https://github.com/apache/cloudstack/pull/1948
.. _CLOUDSTACK-9793: https://issues.apache.org/jira/browse/CLOUDSTACK-9793
.. _`#1954`: https://github.com/apache/cloudstack/pull/1954
.. _CLOUDSTACK-9795: https://issues.apache.org/jira/browse/CLOUDSTACK-9795
.. _`#1927`: https://github.com/apache/cloudstack/pull/1927
.. _`#838`: https://github.com/apache/cloudstack/pull/838
.. _CLOUDSTACK-8857: https://issues.apache.org/jira/browse/CLOUDSTACK-8857
.. _`#865`: https://github.com/apache/cloudstack/pull/865
.. _CLOUDSTACK-8856: https://issues.apache.org/jira/browse/CLOUDSTACK-8856
.. _`#1947`: https://github.com/apache/cloudstack/pull/1947
.. _CLOUDSTACK-9789: https://issues.apache.org/jira/browse/CLOUDSTACK-9789
.. _`#1770`: https://github.com/apache/cloudstack/pull/1770
.. _CLOUDSTACK-9628: https://issues.apache.org/jira/browse/CLOUDSTACK-9628
.. _`#1379`: https://github.com/apache/cloudstack/pull/1379
.. _CLOUDSTACK-8324: https://issues.apache.org/jira/browse/CLOUDSTACK-8324
.. _`#1885`: https://github.com/apache/cloudstack/pull/1885
.. _CLOUDSTACK-9724: https://issues.apache.org/jira/browse/CLOUDSTACK-9724
.. _`#1882`: https://github.com/apache/cloudstack/pull/1882
.. _CLOUDSTACK-8737: https://issues.apache.org/jira/browse/CLOUDSTACK-8737
.. _`#1881`: https://github.com/apache/cloudstack/pull/1881
.. _CLOUDSTACK-9721: https://issues.apache.org/jira/browse/CLOUDSTACK-9721
.. _`#1926`: https://github.com/apache/cloudstack/pull/1926
.. _CLOUDSTACK-9768: https://issues.apache.org/jira/browse/CLOUDSTACK-9768
.. _`#1924`: https://github.com/apache/cloudstack/pull/1924
.. _CLOUDSTACK-9766: https://issues.apache.org/jira/browse/CLOUDSTACK-9766
.. _`#1874`: https://github.com/apache/cloudstack/pull/1874
.. _CLOUDSTACK-9711: https://issues.apache.org/jira/browse/CLOUDSTACK-9711
.. _`#1333`: https://github.com/apache/cloudstack/pull/1333
.. _CLOUDSTACK-9228: https://issues.apache.org/jira/browse/CLOUDSTACK-9228
.. _`#1758`: https://github.com/apache/cloudstack/pull/1758
.. _CLOUDSTACK-9588: https://issues.apache.org/jira/browse/CLOUDSTACK-9588
.. _`#1786`: https://github.com/apache/cloudstack/pull/1786
.. _CLOUDSTACK-9618: https://issues.apache.org/jira/browse/CLOUDSTACK-9618
.. _`#1847`: https://github.com/apache/cloudstack/pull/1847
.. _CLOUDSTACK-9691: https://issues.apache.org/jira/browse/CLOUDSTACK-9691
.. _`#1952`: https://github.com/apache/cloudstack/pull/1952
.. _CLOUDSTACK-9790: https://issues.apache.org/jira/browse/CLOUDSTACK-9790
.. _`#1838`: https://github.com/apache/cloudstack/pull/1838
.. _CLOUDSTACK-9682: https://issues.apache.org/jira/browse/CLOUDSTACK-9682
.. _`#1913`: https://github.com/apache/cloudstack/pull/1913
.. _CLOUDSTACK-9752: https://issues.apache.org/jira/browse/CLOUDSTACK-9752
.. _`#1727`: https://github.com/apache/cloudstack/pull/1727
.. _CLOUDSTACK-9539: https://issues.apache.org/jira/browse/CLOUDSTACK-9539
.. _`#1834`: https://github.com/apache/cloudstack/pull/1834
.. _CLOUDSTACK-9679: https://issues.apache.org/jira/browse/CLOUDSTACK-9679
.. _`#1747`: https://github.com/apache/cloudstack/pull/1747
.. _CLOUDSTACK-9574: https://issues.apache.org/jira/browse/CLOUDSTACK-9574
.. _`#1833`: https://github.com/apache/cloudstack/pull/1833
.. _CLOUDSTACK-9678: https://issues.apache.org/jira/browse/CLOUDSTACK-9678
.. _`#1818`: https://github.com/apache/cloudstack/pull/1818
.. _CLOUDSTACK-9655: https://issues.apache.org/jira/browse/CLOUDSTACK-9655
.. _`#1939`: https://github.com/apache/cloudstack/pull/1939
.. _CLOUDSTACK-8886: https://issues.apache.org/jira/browse/CLOUDSTACK-8886
.. _`#1741`: https://github.com/apache/cloudstack/pull/1741
.. _`#873`: https://github.com/apache/cloudstack/pull/873
.. _CLOUDSTACK-8896: https://issues.apache.org/jira/browse/CLOUDSTACK-8896
.. _`#1794`: https://github.com/apache/cloudstack/pull/1794
.. _`#1938`: https://github.com/apache/cloudstack/pull/1938
.. _CLOUDSTACK-9780: https://issues.apache.org/jira/browse/CLOUDSTACK-9780
.. _`#1876`: https://github.com/apache/cloudstack/pull/1876
.. _CLOUDSTACK-9715: https://issues.apache.org/jira/browse/CLOUDSTACK-9715
.. _`#928`: https://github.com/apache/cloudstack/pull/928
.. _CLOUDSTACK-8950: https://issues.apache.org/jira/browse/CLOUDSTACK-8950
.. _`#1183`: https://github.com/apache/cloudstack/pull/1183
.. _`#1416`: https://github.com/apache/cloudstack/pull/1416
.. _CLOUDSTACK-8717: https://issues.apache.org/jira/browse/CLOUDSTACK-8717
.. _`#844`: https://github.com/apache/cloudstack/pull/844
.. _CLOUDSTACK-7985: https://issues.apache.org/jira/browse/CLOUDSTACK-7985
.. _`#1929`: https://github.com/apache/cloudstack/pull/1929
.. _CLOUDSTACK-9770: https://issues.apache.org/jira/browse/CLOUDSTACK-9770
.. _`#1697`: https://github.com/apache/cloudstack/pull/1697
.. _CLOUDSTACK-4858: https://issues.apache.org/jira/browse/CLOUDSTACK-4858
.. _`#1905`: https://github.com/apache/cloudstack/pull/1905
.. _CLOUDSTACK-9738: https://issues.apache.org/jira/browse/CLOUDSTACK-9738
.. _`#1767`: https://github.com/apache/cloudstack/pull/1767
.. _CLOUDSTACK-9457: https://issues.apache.org/jira/browse/CLOUDSTACK-9457
.. _`#1892`: https://github.com/apache/cloudstack/pull/1892
.. _CLOUDSTACK-9731: https://issues.apache.org/jira/browse/CLOUDSTACK-9731
.. _`#775`: https://github.com/apache/cloudstack/pull/775
.. _CLOUDSTACK-8805: https://issues.apache.org/jira/browse/CLOUDSTACK-8805
.. _`#1890`: https://github.com/apache/cloudstack/pull/1890
.. _CLOUDSTACK-9712: https://issues.apache.org/jira/browse/CLOUDSTACK-9712
.. _`#1871`: https://github.com/apache/cloudstack/pull/1871
.. _CLOUDSTACK-9692: https://issues.apache.org/jira/browse/CLOUDSTACK-9692
.. _`#1921`: https://github.com/apache/cloudstack/pull/1921
.. _`#1920`: https://github.com/apache/cloudstack/pull/1920
.. _`#977`: https://github.com/apache/cloudstack/pull/977
.. _CLOUDSTACK-8746: https://issues.apache.org/jira/browse/CLOUDSTACK-8746
.. _`#1700`: https://github.com/apache/cloudstack/pull/1700
.. _CLOUDSTACK-9359: https://issues.apache.org/jira/browse/CLOUDSTACK-9359
.. _`#1749`: https://github.com/apache/cloudstack/pull/1749
.. _CLOUDSTACK-9619: https://issues.apache.org/jira/browse/CLOUDSTACK-9619
.. _`#1904`: https://github.com/apache/cloudstack/pull/1904
.. _CLOUDSTACK-9729: https://issues.apache.org/jira/browse/CLOUDSTACK-9729
.. _`#1888`: https://github.com/apache/cloudstack/pull/1888
.. _CLOUDSTACK-9710: https://issues.apache.org/jira/browse/CLOUDSTACK-9710
.. _`#1899`: https://github.com/apache/cloudstack/pull/1899
.. _CLOUDSTACK-9650: https://issues.apache.org/jira/browse/CLOUDSTACK-9650
.. _`#1887`: https://github.com/apache/cloudstack/pull/1887
.. _`#1863`: https://github.com/apache/cloudstack/pull/1863
.. _`#1638`: https://github.com/apache/cloudstack/pull/1638
.. _CLOUDSTACK-9456: https://issues.apache.org/jira/browse/CLOUDSTACK-9456
.. _`#1854`: https://github.com/apache/cloudstack/pull/1854
.. _`#1858`: https://github.com/apache/cloudstack/pull/1858
.. _`#1827`: https://github.com/apache/cloudstack/pull/1827
.. _CLOUDSTACK-9673: https://issues.apache.org/jira/browse/CLOUDSTACK-9673
.. _`#1828`: https://github.com/apache/cloudstack/pull/1828
.. _CLOUDSTACK-9676: https://issues.apache.org/jira/browse/CLOUDSTACK-9676
.. _`#1764`: https://github.com/apache/cloudstack/pull/1764
.. _CLOUDSTACK-9597: https://issues.apache.org/jira/browse/CLOUDSTACK-9597
.. _`#1811`: https://github.com/apache/cloudstack/pull/1811
.. _CLOUDSTACK-9649: https://issues.apache.org/jira/browse/CLOUDSTACK-9649
.. _`#1804`: https://github.com/apache/cloudstack/pull/1804
.. _CLOUDSTACK-9639: https://issues.apache.org/jira/browse/CLOUDSTACK-9639
.. _`#1782`: https://github.com/apache/cloudstack/pull/1782
.. _CLOUDSTACK-9617: https://issues.apache.org/jira/browse/CLOUDSTACK-9617
.. _`#1783`: https://github.com/apache/cloudstack/pull/1783
.. _CLOUDSTACK-9615: https://issues.apache.org/jira/browse/CLOUDSTACK-9615
.. _`#1711`: https://github.com/apache/cloudstack/pull/1711
.. _`#1851`: https://github.com/apache/cloudstack/pull/1851
.. _`#1839`: https://github.com/apache/cloudstack/pull/1839
.. _CLOUDSTACK-9683: https://issues.apache.org/jira/browse/CLOUDSTACK-9683
.. _`#1846`: https://github.com/apache/cloudstack/pull/1846
.. _CLOUDSTACK-9688: https://issues.apache.org/jira/browse/CLOUDSTACK-9688
.. _`#1831`: https://github.com/apache/cloudstack/pull/1831
.. _CLOUDSTACK-9671: https://issues.apache.org/jira/browse/CLOUDSTACK-9671
.. _`#896`: https://github.com/apache/cloudstack/pull/896
.. _CLOUDSTACK-8908: https://issues.apache.org/jira/browse/CLOUDSTACK-8908
.. _`#1796`: https://github.com/apache/cloudstack/pull/1796
.. _CLOUDSTACK-9626: https://issues.apache.org/jira/browse/CLOUDSTACK-9626
.. _`#1815`: https://github.com/apache/cloudstack/pull/1815
.. _`#1823`: https://github.com/apache/cloudstack/pull/1823
.. _`#1817`: https://github.com/apache/cloudstack/pull/1817
.. _CLOUDSTACK-9654: https://issues.apache.org/jira/browse/CLOUDSTACK-9654
.. _`#1763`: https://github.com/apache/cloudstack/pull/1763
.. _`#1396`: https://github.com/apache/cloudstack/pull/1396
.. _CLOUDSTACK-9269: https://issues.apache.org/jira/browse/CLOUDSTACK-9269
.. _`#1820`: https://github.com/apache/cloudstack/pull/1820
.. _CLOUDSTACK-9656: https://issues.apache.org/jira/browse/CLOUDSTACK-9656
.. _`#1822`: https://github.com/apache/cloudstack/pull/1822
.. _CLOUDSTACK-9584: https://issues.apache.org/jira/browse/CLOUDSTACK-9584
.. _`#1821`: https://github.com/apache/cloudstack/pull/1821
.. _CLOUDSTACK-9659: https://issues.apache.org/jira/browse/CLOUDSTACK-9659
.. _`#1805`: https://github.com/apache/cloudstack/pull/1805
.. _CLOUDSTACK-9637: https://issues.apache.org/jira/browse/CLOUDSTACK-9637
.. _`#1772`: https://github.com/apache/cloudstack/pull/1772
.. _CLOUDSTACK-9627: https://issues.apache.org/jira/browse/CLOUDSTACK-9627
.. _`#1618`: https://github.com/apache/cloudstack/pull/1618
.. _CLOUDSTACK-9643: https://issues.apache.org/jira/browse/CLOUDSTACK-9643
.. _`#1622`: https://github.com/apache/cloudstack/pull/1622
.. _CLOUDSTACK-9644: https://issues.apache.org/jira/browse/CLOUDSTACK-9644
.. _`#1566`: https://github.com/apache/cloudstack/pull/1566
.. _CLOUDSTACK-9645: https://issues.apache.org/jira/browse/CLOUDSTACK-9645
.. _`#1809`: https://github.com/apache/cloudstack/pull/1809
.. _CLOUDSTACK-9646: https://issues.apache.org/jira/browse/CLOUDSTACK-9646
.. _`#1579`: https://github.com/apache/cloudstack/pull/1579
.. _CLOUDSTACK-9403: https://issues.apache.org/jira/browse/CLOUDSTACK-9403
.. _`#1659`: https://github.com/apache/cloudstack/pull/1659
.. _CLOUDSTACK-9339: https://issues.apache.org/jira/browse/CLOUDSTACK-9339
.. _`#1799`: https://github.com/apache/cloudstack/pull/1799
.. _CLOUDSTACK-9632: https://issues.apache.org/jira/browse/CLOUDSTACK-9632
.. _`#1816`: https://github.com/apache/cloudstack/pull/1816
.. _CLOUDSTACK-9564: https://issues.apache.org/jira/browse/CLOUDSTACK-9564
.. _`#1765`: https://github.com/apache/cloudstack/pull/1765
.. _`#1729`: https://github.com/apache/cloudstack/pull/1729
.. _CLOUDSTACK-9564: https://issues.apache.org/jira/browse/CLOUDSTACK-9564
.. _`#1808`: https://github.com/apache/cloudstack/pull/1808
.. _CLOUDSTACK-9648: https://issues.apache.org/jira/browse/CLOUDSTACK-9648
.. _`#1802`: https://github.com/apache/cloudstack/pull/1802
.. _CLOUDSTACK-9635: https://issues.apache.org/jira/browse/CLOUDSTACK-9635
.. _`#1806`: https://github.com/apache/cloudstack/pull/1806
.. _`#1803`: https://github.com/apache/cloudstack/pull/1803
.. _CLOUDSTACK-9636: https://issues.apache.org/jira/browse/CLOUDSTACK-9636
.. _`#1800`: https://github.com/apache/cloudstack/pull/1800
.. _CLOUDSTACK-9633: https://issues.apache.org/jira/browse/CLOUDSTACK-9633
.. _`#828`: https://github.com/apache/cloudstack/pull/828
.. _CLOUDSTACK-8854: https://issues.apache.org/jira/browse/CLOUDSTACK-8854
.. _`#1801`: https://github.com/apache/cloudstack/pull/1801
.. _`#1793`: https://github.com/apache/cloudstack/pull/1793
.. _CLOUDSTACK-9624: https://issues.apache.org/jira/browse/CLOUDSTACK-9624
.. _`#1710`: https://github.com/apache/cloudstack/pull/1710
.. _CLOUDSTACK-9538: https://issues.apache.org/jira/browse/CLOUDSTACK-9538
.. _`#1755`: https://github.com/apache/cloudstack/pull/1755
.. _CLOUDSTACK-9584: https://issues.apache.org/jira/browse/CLOUDSTACK-9584
.. _`#1791`: https://github.com/apache/cloudstack/pull/1791
.. _CLOUDSTACK-9622: https://issues.apache.org/jira/browse/CLOUDSTACK-9622
.. _`#1789`: https://github.com/apache/cloudstack/pull/1789
.. _`#1785`: https://github.com/apache/cloudstack/pull/1785
.. _CLOUDSTACK-9416: https://issues.apache.org/jira/browse/CLOUDSTACK-9416
.. _`#1788`: https://github.com/apache/cloudstack/pull/1788
.. _`#1577`: https://github.com/apache/cloudstack/pull/1577
.. _CLOUDSTACK-9321: https://issues.apache.org/jira/browse/CLOUDSTACK-9321
.. _`#1580`: https://github.com/apache/cloudstack/pull/1580
.. _CLOUDSTACK-9402: https://issues.apache.org/jira/browse/CLOUDSTACK-9402
.. _`#1635`: https://github.com/apache/cloudstack/pull/1635
.. _CLOUDSTACK-9451: https://issues.apache.org/jira/browse/CLOUDSTACK-9451
.. _`#1738`: https://github.com/apache/cloudstack/pull/1738
.. _CLOUDSTACK-9566: https://issues.apache.org/jira/browse/CLOUDSTACK-9566
.. _`#1766`: https://github.com/apache/cloudstack/pull/1766
.. _CLOUDSTACK-9598: https://issues.apache.org/jira/browse/CLOUDSTACK-9598
.. _`#756`: https://github.com/apache/cloudstack/pull/756
.. _CLOUDSTACK-8781: https://issues.apache.org/jira/browse/CLOUDSTACK-8781
.. _`#1542`: https://github.com/apache/cloudstack/pull/1542
.. _CLOUDSTACK-9379: https://issues.apache.org/jira/browse/CLOUDSTACK-9379
.. _`#1680`: https://github.com/apache/cloudstack/pull/1680
.. _CLOUDSTACK-9498: https://issues.apache.org/jira/browse/CLOUDSTACK-9498
.. _`#1681`: https://github.com/apache/cloudstack/pull/1681
.. _CLOUDSTACK-9491: https://issues.apache.org/jira/browse/CLOUDSTACK-9491
.. _`#1745`: https://github.com/apache/cloudstack/pull/1745
.. _CLOUDSTACK-9503: https://issues.apache.org/jira/browse/CLOUDSTACK-9503
.. _`#1757`: https://github.com/apache/cloudstack/pull/1757
.. _CLOUDSTACK-9583: https://issues.apache.org/jira/browse/CLOUDSTACK-9583
.. _`#1684`: https://github.com/apache/cloudstack/pull/1684
.. _CLOUDSTACK-9489: https://issues.apache.org/jira/browse/CLOUDSTACK-9489
.. _`#1591`: https://github.com/apache/cloudstack/pull/1591
.. _`#1674`: https://github.com/apache/cloudstack/pull/1674
.. _CLOUDSTACK-9460: https://issues.apache.org/jira/browse/CLOUDSTACK-9460
.. _`#1673`: https://github.com/apache/cloudstack/pull/1673
.. _CLOUDSTACK-9071: https://issues.apache.org/jira/browse/CLOUDSTACK-9071
.. _`#1676`: https://github.com/apache/cloudstack/pull/1676
.. _CLOUDSTACK-9502: https://issues.apache.org/jira/browse/CLOUDSTACK-9502
.. _`#1677`: https://github.com/apache/cloudstack/pull/1677
.. _CLOUDSTACK-8830: https://issues.apache.org/jira/browse/CLOUDSTACK-8830
.. _`#1578`: https://github.com/apache/cloudstack/pull/1578
.. _CLOUDSTACK-9401: https://issues.apache.org/jira/browse/CLOUDSTACK-9401
.. _`#1751`: https://github.com/apache/cloudstack/pull/1751
.. _`#1743`: https://github.com/apache/cloudstack/pull/1743
.. _CLOUDSTACK-8326: https://issues.apache.org/jira/browse/CLOUDSTACK-8326
.. _`#1744`: https://github.com/apache/cloudstack/pull/1744
.. _CLOUDSTACK-9183: https://issues.apache.org/jira/browse/CLOUDSTACK-9183
.. _`#1713`: https://github.com/apache/cloudstack/pull/1713
.. _CLOUDSTACK-9552: https://issues.apache.org/jira/browse/CLOUDSTACK-9552
.. _`#1746`: https://github.com/apache/cloudstack/pull/1746
.. _`#1714`: https://github.com/apache/cloudstack/pull/1714
.. _CLOUDSTACK-9553: https://issues.apache.org/jira/browse/CLOUDSTACK-9553
.. _`#1715`: https://github.com/apache/cloudstack/pull/1715
.. _CLOUDSTACK-9554: https://issues.apache.org/jira/browse/CLOUDSTACK-9554
.. _`#1705`: https://github.com/apache/cloudstack/pull/1705
.. _`#1728`: https://github.com/apache/cloudstack/pull/1728
.. _CLOUDSTACK-9551: https://issues.apache.org/jira/browse/CLOUDSTACK-9551
.. _`#1694`: https://github.com/apache/cloudstack/pull/1694
.. _CLOUDSTACK-9509: https://issues.apache.org/jira/browse/CLOUDSTACK-9509
.. _`#1600`: https://github.com/apache/cloudstack/pull/1600
.. _`#1732`: https://github.com/apache/cloudstack/pull/1732
.. _`#1701`: https://github.com/apache/cloudstack/pull/1701
.. _CLOUDSTACK-9534: https://issues.apache.org/jira/browse/CLOUDSTACK-9534
.. _`#1712`: https://github.com/apache/cloudstack/pull/1712
.. _CLOUDSTACK-9550: https://issues.apache.org/jira/browse/CLOUDSTACK-9550
.. _`#1742`: https://github.com/apache/cloudstack/pull/1742
.. _CLOUDSTACK-9544: https://issues.apache.org/jira/browse/CLOUDSTACK-9544
.. _`#1615`: https://github.com/apache/cloudstack/pull/1615
.. _CLOUDSTACK-9438: https://issues.apache.org/jira/browse/CLOUDSTACK-9438
.. _`#1731`: https://github.com/apache/cloudstack/pull/1731
.. _CLOUDSTACK-9565: https://issues.apache.org/jira/browse/CLOUDSTACK-9565
.. _`#1642`: https://github.com/apache/cloudstack/pull/1642
.. _CLOUDSTACK-9504: https://issues.apache.org/jira/browse/CLOUDSTACK-9504
.. _`#1451`: https://github.com/apache/cloudstack/pull/1451
.. _CLOUDSTACK-9319: https://issues.apache.org/jira/browse/CLOUDSTACK-9319
.. _`#1724`: https://github.com/apache/cloudstack/pull/1724
.. _CLOUDSTACK-9511: https://issues.apache.org/jira/browse/CLOUDSTACK-9511
.. _`#1624`: https://github.com/apache/cloudstack/pull/1624
.. _`#1692`: https://github.com/apache/cloudstack/pull/1692
.. _`#1572`: https://github.com/apache/cloudstack/pull/1572
.. _CLOUDSTACK-9395: https://issues.apache.org/jira/browse/CLOUDSTACK-9395
.. _`#1464`: https://github.com/apache/cloudstack/pull/1464
.. _CLOUDSTACK-9337: https://issues.apache.org/jira/browse/CLOUDSTACK-9337
.. _`#1548`: https://github.com/apache/cloudstack/pull/1548
.. _`#1702`: https://github.com/apache/cloudstack/pull/1702
.. _CLOUDSTACK-9535: https://issues.apache.org/jira/browse/CLOUDSTACK-9535
.. _`#1698`: https://github.com/apache/cloudstack/pull/1698
.. _CLOUDSTACK-9525: https://issues.apache.org/jira/browse/CLOUDSTACK-9525
.. _`#1699`: https://github.com/apache/cloudstack/pull/1699
.. _CLOUDSTACK-9513: https://issues.apache.org/jira/browse/CLOUDSTACK-9513
.. _`#1696`: https://github.com/apache/cloudstack/pull/1696
.. _CLOUDSTACK-9364: https://issues.apache.org/jira/browse/CLOUDSTACK-9364
.. _`#1690`: https://github.com/apache/cloudstack/pull/1690
.. _`#1619`: https://github.com/apache/cloudstack/pull/1619
.. _`#1669`: https://github.com/apache/cloudstack/pull/1669
.. _`#1693`: https://github.com/apache/cloudstack/pull/1693
.. _CLOUDSTACK-9505: https://issues.apache.org/jira/browse/CLOUDSTACK-9505
.. _`#1689`: https://github.com/apache/cloudstack/pull/1689
.. _`#1602`: https://github.com/apache/cloudstack/pull/1602
.. _CLOUDSTACK-9422: https://issues.apache.org/jira/browse/CLOUDSTACK-9422
.. _`#1666`: https://github.com/apache/cloudstack/pull/1666
.. _CLOUDSTACK-9480: https://issues.apache.org/jira/browse/CLOUDSTACK-9480
.. _`#1645`: https://github.com/apache/cloudstack/pull/1645
.. _`#1661`: https://github.com/apache/cloudstack/pull/1661
.. _`#1671`: https://github.com/apache/cloudstack/pull/1671
.. _`#1560`: https://github.com/apache/cloudstack/pull/1560
.. _CLOUDSTACK-9386: https://issues.apache.org/jira/browse/CLOUDSTACK-9386
.. _`#1658`: https://github.com/apache/cloudstack/pull/1658
.. _`#866`: https://github.com/apache/cloudstack/pull/866
.. _CLOUDSTACK-8751: https://issues.apache.org/jira/browse/CLOUDSTACK-8751
.. _`#1672`: https://github.com/apache/cloudstack/pull/1672
.. _`#1605`: https://github.com/apache/cloudstack/pull/1605
.. _CLOUDSTACK-9428: https://issues.apache.org/jira/browse/CLOUDSTACK-9428
.. _`#1665`: https://github.com/apache/cloudstack/pull/1665
.. _`#1636`: https://github.com/apache/cloudstack/pull/1636
.. _`#1670`: https://github.com/apache/cloudstack/pull/1670
.. _CLOUDSTACK-9481: https://issues.apache.org/jira/browse/CLOUDSTACK-9481
.. _`#1654`: https://github.com/apache/cloudstack/pull/1654
.. _`#1663`: https://github.com/apache/cloudstack/pull/1663
.. _CLOUDSTACK-6432: https://issues.apache.org/jira/browse/CLOUDSTACK-6432
.. _`#1621`: https://github.com/apache/cloudstack/pull/1621
.. _CLOUDSTACK-9444: https://issues.apache.org/jira/browse/CLOUDSTACK-9444
.. _`#1648`: https://github.com/apache/cloudstack/pull/1648
.. _`#1647`: https://github.com/apache/cloudstack/pull/1647
.. _CLOUDSTACK-9462: https://issues.apache.org/jira/browse/CLOUDSTACK-9462
.. _`#1657`: https://github.com/apache/cloudstack/pull/1657
.. _CLOUDSTACK-9467: https://issues.apache.org/jira/browse/CLOUDSTACK-9467
.. _`#1656`: https://github.com/apache/cloudstack/pull/1656
.. _CLOUDSTACK-9466: https://issues.apache.org/jira/browse/CLOUDSTACK-9466
.. _`#1634`: https://github.com/apache/cloudstack/pull/1634
.. _CLOUDSTACK-9452: https://issues.apache.org/jira/browse/CLOUDSTACK-9452
.. _`#1599`: https://github.com/apache/cloudstack/pull/1599
.. _`#1646`: https://github.com/apache/cloudstack/pull/1646
.. _`#1630`: https://github.com/apache/cloudstack/pull/1630
.. _`#1649`: https://github.com/apache/cloudstack/pull/1649
.. _CLOUDSTACK-9463: https://issues.apache.org/jira/browse/CLOUDSTACK-9463
.. _`#1620`: https://github.com/apache/cloudstack/pull/1620
.. _`#1641`: https://github.com/apache/cloudstack/pull/1641
.. _CLOUDSTACK-9459: https://issues.apache.org/jira/browse/CLOUDSTACK-9459
.. _`#1628`: https://github.com/apache/cloudstack/pull/1628
.. _`#1626`: https://github.com/apache/cloudstack/pull/1626
.. _`#1631`: https://github.com/apache/cloudstack/pull/1631
.. _`#1612`: https://github.com/apache/cloudstack/pull/1612
.. _CLOUDSTACK-9446: https://issues.apache.org/jira/browse/CLOUDSTACK-9446
.. _`#1625`: https://github.com/apache/cloudstack/pull/1625

