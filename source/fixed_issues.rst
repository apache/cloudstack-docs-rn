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
| master                  | `#2097`_ | CLOUDSTACK-9813_   | New Feature   | Major    | Use configdrive for userdata, metadata & password          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2146`_ | CLOUDSTACK-4757_   | New Feature   | Minor    | Support OVA files with multiple disks for templates        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2394`_ | CLOUDSTACK-10109_  | New Feature   | Major    | Enable dedication of public IPs to SSVM and CPVM           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2295`_ | CLOUDSTACK-10109_  | New Feature   | Major    | Enable dedication of public IPs to SSVM and CPVM           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2381`_ | CLOUDSTACK-10117_  | New Feature   | Major    | LDAP mapping on domain level                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2368`_ | CLOUDSTACK-10126_  | New Feature   | Major    | Separate Subnet for CPVM and SSVM                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2046`_ | CLOUDSTACK-7958_   | New Feature   | Minor    | Limit user login to specific subnets                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2374`_ | CLOUDSTACK-10024_  | New Feature   | Major    | Physical Networking Migration                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2301`_ | CLOUDSTACK-10121_  | New Feature   | Major    | move user API                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2360`_ | CLOUDSTACK-10189_  | New Feature   | Major    | Support for "VSD managed" networks with Nuage Networks     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2281`_ | CLOUDSTACK-10102_  | New Feature   | Major    | New Network Type (L2)                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2048`_ | CLOUDSTACK-9880_   | New Feature   | Major    | Expansion of Management IP Range.                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2294`_ | CLOUDSTACK-10039_  | New Feature   | Major    | Adding IOPS/GB offering                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2356`_ | CLOUDSTACK-8313_   | New Feature   | Major    | Local Storage overprovisioning should be possible          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2028`_ | CLOUDSTACK-9853_   | New Feature   | Major    | IPv6 Prefix Delegation support in Basic Networking         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1981`_ | CLOUDSTACK-9806_   | New Feature   | Major    | Nuage domain template selection per VPC                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2325`_ | CLOUDSTACK-9998_   | New Feature   | Major    | CloudStack exporter for Prometheus                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2284`_ | CLOUDSTACK-10103_  | New Feature   | Major    | Cloudian Connector for CloudStack                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2297`_ | CLOUDSTACK-9957_   | New Feature   | Major    | Annotations on entities                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2181`_ | CLOUDSTACK-9957_   | New Feature   | Major    | Annotations on entities                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2286`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2287`_ | CLOUDSTACK-9998_   | New Feature   | Major    | CloudStack exporter for Prometheus                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2278`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1707`_ | CLOUDSTACK-9397_   | New Feature   | Major    | Add Watchdog timer to KVM Instances                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2143`_ | CLOUDSTACK-9949_   | New Feature   | Minor    | add ability to specify mac address when                    |
|                         |          |                    |               |          | deployVirtualMachine or addNicToVirtualMachine is called   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2256`_ | CLOUDSTACK-9782_   | New Feature   | Major    | Host HA                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2239`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2222`_ | CLOUDSTACK-10022_  | New Feature   | Minor    | Allow domain admin to create and delete subdomains         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2026`_ | CLOUDSTACK-9861_   | New Feature   | Major    | Expire VM snapshots after configured duration              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2218`_ | CLOUDSTACK-9782_   | New Feature   | Major    | Host HA                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.11*                   | `#2407`_ | CLOUDSTACK-10227_  | Bug           | Blocker  | Stabilization fixes for master/4.11                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2403`_ | CLOUDSTACK-10227_  | Bug           | Blocker  | Stabilization fixes for master/4.11                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2396`_ | CLOUDSTACK-10220_  | Bug           | Major    | IPv4 NIC alias is not added on Virtual Router in Basic     |
|                         |          |                    |               |          | Networking when NIC has IPv6 address                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2362`_ | CLOUDSTACK-10188_  | Bug           | Major    | Resource Accounting for primary storage is Broken          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2393`_ | CLOUDSTACK-10217_  | Bug           | Major    | When IPv4 address of Instance is updated DHCP data is not  |
|                         |          |                    |               |          | cleared on VR                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2388`_ | CLOUDSTACK-10212_  | Bug           | Major    | Changing IPv4 Address of NIC in Basic Networking does not  |
|                         |          |                    |               |          | update the gateway                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2379`_ | CLOUDSTACK-10146_  | Bug           | Major    | Bypass Secondary Storage for KVM templates                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2391`_ | CLOUDSTACK-10215_  | Bug           | Major    | Excessive log4j debug level in CPVM, SSVM could lead to FS |
|                         |          |                    |               |          | overflow                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2139`_ | CLOUDSTACK-9921_   | Bug           | Major    | NPE when garbage collector is running                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2088`_ | CLOUDSTACK-9892_   | Bug           | Critical | Primary storage resource check is broken when using root   |
|                         |          |                    |               |          | disk size override to deploy VM                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2365`_ | CLOUDSTACK-10197_  | Bug           | Major    | XenServer 7.1: Cannot mount  xentool iso from cloudstack   |
|                         |          |                    |               |          | on VMs                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2073`_ | CLOUDSTACK-9896_   | Bug           | Minor    | ListDedicatedXXX doesn't respect pagination                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2386`_ | CLOUDSTACK-9632_   | Bug           | Major    | Upgrade bountycastle to 1.55+                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2315`_ | CLOUDSTACK-9025_   | Bug           | Critical | Unable to deploy VM instance from template if template     |
|                         |          |                    |               |          | spin from linked clone snapshot                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2274`_ | CLOUDSTACK-10096_  | Bug           | Major    | Can't reset api.integration.port and                       |
|                         |          |                    |               |          | usage.sanity.check.interval back to null                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2282`_ | CLOUDSTACK-10104_  | Bug           | Major    | Optimize database transactions in ListDomain API to        |
|                         |          |                    |               |          | improve performance                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2385`_ | CLOUDSTACK-10211_  | Bug           | Major    | test_nuage_public_sharednetwork_userdata fails due to      |
|                         |          |                    |               |          | errortext changed                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2260`_ | CLOUDSTACK-10065_  | Bug           | Major    | Optimize SQL queries in listTemplate API to improve        |
|                         |          |                    |               |          | performance.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1740`_ | CLOUDSTACK-9572_   | Bug           | Major    | Snapshot on primary storage not cleaned up after Storage   |
|                         |          |                    |               |          | migration                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2104`_ | CLOUDSTACK-9908_   | Bug           | Major    | Primary Storage allocated capacity goes very high after VM |
|                         |          |                    |               |          | snapshot                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2378`_ | CLOUDSTACK-10205_  | Bug           | Major    | LinkDomainToLdap returns internal id                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1773`_ | CLOUDSTACK-9607_   | Bug           | Major    | Preventing template deletion when template is in use.      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2149`_ | CLOUDSTACK-9932_   | Bug           | Major    | Snapshot is getting deleted while volume creation from the |
|                         |          |                    |               |          | snapshot is in progress                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2156`_ | CLOUDSTACK-9971_   | Bug           | Minor    | Bugfix/listaccounts parameter consistency                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2373`_ | CLOUDSTACK-10202_  | Bug           | Major    | createSnapshotPolicy API create multiple entries in DB for |
|                         |          |                    |               |          | same volume.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2344`_ | CLOUDSTACK-10163_  | Bug           | Major    | Component tests health check                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1760`_ | CLOUDSTACK-9593_   | Bug           | Major    | User data check is inconsistent with python                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2352`_ | CLOUDSTACK-10175_  | Bug           | Major    | Listing VPCs with a domain account and project id -1       |
|                         |          |                    |               |          | returns all the VPCs in the syste                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2347`_ | CLOUDSTACK-10166_  | Bug           | Minor    | Cannot add a tag to a NetworkACL (rule not list) in CS     |
|                         |          |                    |               |          | with a user in a project or in an account                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2375`_ | CLOUDSTACK-9456_   | Bug           | Major    | Migrate master to use Java8 and Spring4                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2211`_ | CLOUDSTACK-10013_  | Bug           | Major    | Migrate to Debian9 systemvmtemplate                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2304`_ | CLOUDSTACK-10127_  | Bug           | Critical | 4.9 / 4.10 KVM + openvswitch + vpc + static nat /          |
|                         |          |                    |               |          | secondary ip on eth2?                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2208`_ | CLOUDSTACK-9542_   | Bug           | Major    | listNics API does not return data as per API documentation |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2351`_ | CLOUDSTACK-10173_  | Bug           | Major    | Guest/Public nics on VR should pick network rate from      |
|                         |          |                    |               |          | network offering                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2370`_ | CLOUDSTACK-9595_   | Bug           | Major    | Transactions are not getting retried in case of database   |
|                         |          |                    |               |          | deadlock errors                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2366`_ | CLOUDSTACK-10168_  | Bug           | Major    | VR duplicate entries in /etc/hosts when reusing VM name    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2042`_ | CLOUDSTACK-9875_   | Bug           | Major    | Unable to re-apply Explicit dedication to VM               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2364`_ | CLOUDSTACK-10195_  | Bug           | Minor    | CloudStack MySQL HA problem -- No database selected        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2361`_ | CLOUDSTACK-10190_  | Bug           | Major    | Duplicate public VLAN for two different admin accounts.    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2247`_ | CLOUDSTACK-10012_  | Bug           | Major    | Migrate to Embedded Jetty based mgmt server                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1964`_ | CLOUDSTACK-9800_   | Bug           | Major    | Enable inline mode for NetScaler device                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1762`_ | CLOUDSTACK-9595_   | Bug           | Major    | Transactions are not getting retried in case of database   |
|                         |          |                    |               |          | deadlock errors                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2308`_ | CLOUDSTACK-8908_   | Bug           | Major    | After copying the template charging for that template is   |
|                         |          |                    |               |          | stopped                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2354`_ | CLOUDSTACK-10176_  | Bug           | Major    | VM Start Api Job returns success for failed Job            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2353`_ | CLOUDSTACK-9986_   | Bug           | Major    | Consider overcommit ratios with total/threshold values in  |
|                         |          |                    |               |          | Metrics View                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2358`_ | CLOUDSTACK-9736_   | Bug           | Minor    | Incoherent validation and error message when you change    |
|                         |          |                    |               |          | the vm.password.length configuration parameter             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2326`_ | CLOUDSTACK-10184_  | Bug           | Major    | Re-work method QuotaResponseBuilderImpl.startOfNextDay and |
|                         |          |                    |               |          | its test cases                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2267`_ | CLOUDSTACK-10077_  | Bug           | Major    | Allow account to use the same site-2-site VPN gateway with |
|                         |          |                    |               |          | different configs for several VPCs                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2337`_ | CLOUDSTACK-10157_  | Bug           | Major    | Wrong notification while migration                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2355`_ | CLOUDSTACK-10177_  | Bug           | Major    | NPE when programming Security Groups with KVM              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2349`_ | CLOUDSTACK-10070_  | Bug           | Major    | Extend travis run to include more component tests          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2312`_ | CLOUDSTACK-7793_   | Bug           | Critical | [Snapshots]Create Snaphot with "quiesce" option set to     |
|                         |          |                    |               |          | true fails with "InvalidParameterValueException: can't     |
|                         |          |                    |               |          | handle quiescevm equal true for volume snapshot"           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2345`_ | CLOUDSTACK-10164_  | Bug           | Blocker  | UI - not able to create a VPC                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2263`_ | CLOUDSTACK-10070_  | Bug           | Major    | Extend travis run to include more component tests          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2342`_ | CLOUDSTACK-9586_   | Bug           | Critical | When using local storage with Xenserver prepareTemplate    |
|                         |          |                    |               |          | does not work with multiple primary store                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2124`_ | CLOUDSTACK-9432_   | Bug           | Critical | Dedicate Cluster to Domain always creates an affinity      |
|                         |          |                    |               |          | group owned by the root domain                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2322`_ | CLOUDSTACK-10140_  | Bug           | Critical | When template is created from snapshot template.properties |
|                         |          |                    |               |          | are corrupted                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2335`_ | CLOUDSTACK-10154_  | Bug           | Major    | test failures in smoketest                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2341`_ | CLOUDSTACK-10160_  | Bug           | Major    | KVM VirtIO-SCSI not defined properly in Libvirt XML        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2321`_ | CLOUDSTACK-10138_  | Bug           | Major    | Load br_netfilter in security_group management script      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2334`_ | CLOUDSTACK-10152_  | Bug           | Major    | egress destination cidr with 0.0.0.0/0 is failing          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2310`_ | CLOUDSTACK-10133_  | Bug           | Major    | Local storage overprovisioning for ext file system         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2303`_ | CLOUDSTACK-10123_  | Bug           | Major    | VmWork job gets deleted before the parent job had time to  |
|                         |          |                    |               |          | fetch its result                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2329`_ | CLOUDSTACK-10012_  | Bug           | Major    | Migrate to Embedded Jetty based mgmt server                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2327`_ | CLOUDSTACK-10129_  | Bug           | Trivial  | Show instances attached to a network/VR via navigation     |
|                         |          |                    |               |          | from VRs->instances                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2316`_ | CLOUDSTACK-10137_  | Bug           | Major    | Re-installation fails for cloudstack-management            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2157`_ | CLOUDSTACK-9961_   | Bug           | Major    | Accept domain name for gateway while creating              |
|                         |          |                    |               |          | Vpncustomergateway                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2306`_ | CLOUDSTACK-10129_  | Bug           | Trivial  | Show instances attached to a network/VR via navigation     |
|                         |          |                    |               |          | from VRs->instances                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2273`_ | CLOUDSTACK-10090_  | Bug           | Major    | createPortForwardingRule api call accepts 'halt' as        |
|                         |          |                    |               |          | Protocol which Stops VR                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2240`_ | CLOUDSTACK-10051_  | Bug           | Major    | Mouse Scrolling is not working in instance VM console      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2291`_ | CLOUDSTACK-10111_  | Bug           | Minor    | Fix validation for parameter "vm.password.length"          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2302`_ | CLOUDSTACK-10122_  | Bug           | Major    | Unrelated error message                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2250`_ | CLOUDSTACK-10057_  | Bug           | Major    | ListNetworkOfferingsCmd does not return the correct count  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2268`_ | CLOUDSTACK-10081_  | Bug           | Major    | CloudUtils getDevInfo function only checks for KVM         |
|                         |          |                    |               |          | bridgePort and not OVS                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2293`_ | CLOUDSTACK-10047_  | Bug           | Major    | DVSwitch improvements                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2288`_ | CLOUDSTACK-10107_  | Bug           | Major    | VMware VM fails to start if it has more than 7 nics        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2257`_ | CLOUDSTACK-10060_  | Bug           | Minor    | ListUsage API always displays the Virtual size as '0' for  |
|                         |          |                    |               |          | Usage type=9 (snapshot)                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2246`_ | CLOUDSTACK-10046_  | Bug           | Major    | checksum is not verified during registerTemplate           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2074`_ | CLOUDSTACK-9899_   | Bug           | Major    | allow download without checking first for MS behind        |
|                         |          |                    |               |          | firewall                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2279`_ | CLOUDSTACK-9584_   | Bug           | Major    | Increase component tests coverage in Travis run            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2277`_ | CLOUDSTACK-10099_  | Bug           | Major    | GUI invokes migrateVirtualMachine instead of               |
|                         |          |                    |               |          | migrateVirtualMachineWithVolume                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2269`_ | CLOUDSTACK-10083_  | Bug           | Minor    | SSH keys are not created when starting from maintenance    |
|                         |          |                    |               |          | mode                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#876`_  | CLOUDSTACK-8865_   | Bug           | Major    | Adding SR doesn't create Storage_pool_host_ref entry for   |
|                         |          |                    |               |          | disabled host                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1252`_ | CLOUDSTACK-9182_   | Bug           | Major    | Some running VMs turned off on manual migration when auto  |
|                         |          |                    |               |          | migration failed while host preparing for maintenance      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2153`_ | CLOUDSTACK-9956_   | Bug           | Major    | File search on the vmware datastore may select wrong file  |
|                         |          |                    |               |          | if there are multiple files with same name                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2078`_ | CLOUDSTACK-9902_   | Bug           | Minor    | consoleproxy.sslEnabled global config variable is not      |
|                         |          |                    |               |          | present in default install                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2252`_ | CLOUDSTACK-10067_  | Bug           | Major    | Fix a case where a user 'ro' or 'roo' exists on the system |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2248`_ | CLOUDSTACK-10056_  | Bug           | Minor    | Cannot specify root disk controller when creating VM       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2243`_ | CLOUDSTACK-10019_  | Bug           | Major    | template.properties has hardcoded id                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2261`_ | CLOUDSTACK-10068_  | Bug           | Major    | smoketest/test_iso.py reports assertion failure            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2054`_ | CLOUDSTACK-9886_   | Bug           | Major    | After restarting cloudstack-management , It takes time to  |
|                         |          |                    |               |          | connect hosts                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#955`_  | CLOUDSTACK-8969_   | Bug           | Major    | VPN customer gateway can't be registered with hostname     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2262`_ | CLOUDSTACK-10069_  | Bug           | Major    | During release add sha512 suffix to sha 512 checksum/file  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2253`_ | CLOUDSTACK-10061_  | Bug           | Major    | When starting a VM, make sure it has the correct volume    |
|                         |          |                    |               |          | access group                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2254`_ | CLOUDSTACK-10058_  | Bug           | Major    | Error while opening the Settings tab in Secondary storage  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1733`_ | CLOUDSTACK-9563_   | Bug           | Major    | ExtractTemplate returns malformed URL after migrating NFS  |
|                         |          |                    |               |          | to s3                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2188`_ | CLOUDSTACK-10004_  | Bug           | Major    | On deletion, Vmware volume snapshots are left behind with  |
|                         |          |                    |               |          | message 'the snapshot has child, can't delete it on the    |
|                         |          |                    |               |          | storage'                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#914`_  | CLOUDSTACK-8939_   | Bug           | Major    | VM Snapshot size with memory is not correctly calculated   |
|                         |          |                    |               |          | in cloud.usage_event (XenServer)                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1985`_ | CLOUDSTACK-9812_   | Bug           | Major    | Update "updatePortForwardingRule" pi to include additional |
|                         |          |                    |               |          | parameter to update the end port in case of port range     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2224`_ | CLOUDSTACK-10032_  | Bug           | Major    | Database entries for templates created from snapshots      |
|                         |          |                    |               |          | disappear after management-server service restart          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2109`_ | CLOUDSTACK-9922_   | Bug           | Major    | Unable  to use 8081 port for Load balancing                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2216`_ | CLOUDSTACK-10027_  | Bug           | Minor    | Repeating the same list for Internal LB in VPC             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2174`_ | CLOUDSTACK-9996_   | Bug           | Major    | bug in network resource that juniper srx firewall          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2186`_ | CLOUDSTACK-10002_  | Bug           | Major    | Restart network with cleanup spawns Redundant Routers(In   |
|                         |          |                    |               |          | Default Network Offering)                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1246`_ | CLOUDSTACK-9165_   | Bug           | Major    | unable to use reserved IP range in a network for external  |
|                         |          |                    |               |          | VMs                                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2241`_ | CLOUDSTACK-10052_  | Bug           | Major    | Upgrading to 4.9.2 causes confusion/issues around dynamic  |
|                         |          |                    |               |          | roles usage                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2221`_ | CLOUDSTACK-10030_  | Bug           | Minor    | Public IPs assgined to the VPC are not reacheable from     |
|                         |          |                    |               |          | inside VPC                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2154`_ | CLOUDSTACK-9967_   | Bug           | Major    | [VPC] static nat on additional public subnet ip is not     |
|                         |          |                    |               |          | working.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1878`_ | CLOUDSTACK-9717_   | Bug           | Major    | [VMware] RVRs have mismatching MAC addresses for extra     |
|                         |          |                    |               |          | public NICs                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2013`_ | CLOUDSTACK-9734_   | Bug           | Major    | Destroy VM Fails sometimes                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2159`_ | CLOUDSTACK-9964_   | Bug           | Critical | Snapahots are getting deleted if VM is assigned to another |
|                         |          |                    |               |          | user                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2163`_ | CLOUDSTACK-9939_   | Bug           | Major    | Volumes stuck in Creating state while restarting the       |
|                         |          |                    |               |          | Management Server when the volume creation is in progress  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1919`_ | CLOUDSTACK-9763_   | Bug           | Major    | vpc: can not ssh to instance after vpc restart             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2215`_ | CLOUDSTACK-10026_  | Bug           | Major    | Page for Internal LB VM stucking while loading             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2180`_ | CLOUDSTACK-9999_   | Bug           | Major    | vpc tiers do not work if vpc has more than 8 tiers         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2182`_ | CLOUDSTACK-10000_  | Bug           | Major    | Remote access vpn user does not work if user password      |
|                         |          |                    |               |          | contains '#'                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2233`_ | CLOUDSTACK-10042_  | Bug           | Major    | UI doesn't show ICMP Type and Code for Security Group      |
|                         |          |                    |               |          | rules                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2228`_ | CLOUDSTACK-10036_  | Bug           | Major    | Decrease timeout of failing unit test                      |
|                         |          |                    |               |          | HypervisorUtilsTest.java                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1774`_ | CLOUDSTACK-9608_   | Bug           | Major    | Errored State and Abandoned state Templates are not        |
|                         |          |                    |               |          | displayed on UI                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2144`_ | CLOUDSTACK-9955_   | Bug           | Minor    | Featured Templates/Iso's created by Root/admin user are    |
|                         |          |                    |               |          | not visible to Domain Admin users                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1966`_ | CLOUDSTACK-9801_   | Bug           | Critical | IPSec VPN does not work after vRouter reboot or recreate   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2220`_ | CLOUDSTACK-9708_   | Bug           | Major    | Router deployment failed due to two threads start VR       |
|                         |          |                    |               |          | simultaneosuly                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1912`_ | CLOUDSTACK-9749_   | Bug           | Critical | cloudstack master vpc_internal_lb feature is broken as     |
|                         |          |                    |               |          | port 8080 is in use by password server on lb VM            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2138`_ | CLOUDSTACK-9944_   | Bug           | Major    | In clustered Management Server, Sometimes hosts stays in   |
|                         |          |                    |               |          | disconnected state.                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#883`_  | CLOUDSTACK-8906_   | Bug           | Major    | /var/log/cloud/ doesn't get logrotated on xenserver        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2119`_ | CLOUDSTACK-9925_   | Bug           | Minor    | Quota: fix tariff description for memory. Tariff value is  |
|                         |          |                    |               |          | for 1MB of RAM used per month (not hour).                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2145`_ | CLOUDSTACK-9697_   | Bug           | Major    | Better error message on UI user if tries to shrink the VM  |
|                         |          |                    |               |          | ROOT volume size                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2137`_ | CLOUDSTACK-9950_   | Bug           | Major    | listUsageRecords doesnt return required fields             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2008`_ | CLOUDSTACK-9840_   | Bug           | Major    | Datetime format of snapshot events is inconsistent with    |
|                         |          |                    |               |          | other events                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2142`_ | CLOUDSTACK-9954_   | Bug           | Major    | Unable to create service offering with networkrate=0       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2171`_ | CLOUDSTACK-9990_   | Bug           | Minor    | Account name is giving null in event tab after successful  |
|                         |          |                    |               |          | creation of account                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1925`_ | CLOUDSTACK-9751_   | Bug           | Major    | if a public IP is assigned to a VM when VR is in starting  |
|                         |          |                    |               |          | state, it does not get applied to the vport in Nuage VSD   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1798`_ | CLOUDSTACK-9631_   | Bug           | Major    | updateVMAffinityGroup must require one of the list         |
|                         |          |                    |               |          | parameter                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2201`_ | CLOUDSTACK-10016_  | Bug           | Major    | VPC VR doesn't respond to DNS requests from remote access  |
|                         |          |                    |               |          | vpn clients                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1959`_ | CLOUDSTACK-9786_   | Bug           | Major    | API reference guide entry for associateIpAddress needs a   |
|                         |          |                    |               |          | fix                                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1933`_ | CLOUDSTACK-9569_   | Bug           | Critical | VR on shared network not starting on KVM                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+




.. cssclass:: table-striped table-bordered table-hover

+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| Branches                | Github   | Jira               | Type          | Priority | Description                                                |
+=========================+==========+====================+===============+==========+============================================================+
| master                  | `#2097`_ | CLOUDSTACK-9813_   | New Feature   | Major    | Use configdrive for userdata, metadata & password          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2146`_ | CLOUDSTACK-4757_   | New Feature   | Minor    | Support OVA files with multiple disks for templates        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2394`_ | CLOUDSTACK-10109_  | New Feature   | Major    | Enable dedication of public IPs to SSVM and CPVM           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2295`_ | CLOUDSTACK-10109_  | New Feature   | Major    | Enable dedication of public IPs to SSVM and CPVM           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2381`_ | CLOUDSTACK-10117_  | New Feature   | Major    | LDAP mapping on domain level                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2368`_ | CLOUDSTACK-10126_  | New Feature   | Major    | Separate Subnet for CPVM and SSVM                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2046`_ | CLOUDSTACK-7958_   | New Feature   | Minor    | Limit user login to specific subnets                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2374`_ | CLOUDSTACK-10024_  | New Feature   | Major    | Physical Networking Migration                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2301`_ | CLOUDSTACK-10121_  | New Feature   | Major    | move user API                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2360`_ | CLOUDSTACK-10189_  | New Feature   | Major    | Support for "VSD managed" networks with Nuage Networks     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2281`_ | CLOUDSTACK-10102_  | New Feature   | Major    | New Network Type (L2)                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2048`_ | CLOUDSTACK-9880_   | New Feature   | Major    | Expansion of Management IP Range.                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2294`_ | CLOUDSTACK-10039_  | New Feature   | Major    | Adding IOPS/GB offering                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2356`_ | CLOUDSTACK-8313_   | New Feature   | Major    | Local Storage overprovisioning should be possible          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2028`_ | CLOUDSTACK-9853_   | New Feature   | Major    | IPv6 Prefix Delegation support in Basic Networking         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1981`_ | CLOUDSTACK-9806_   | New Feature   | Major    | Nuage domain template selection per VPC                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2325`_ | CLOUDSTACK-9998_   | New Feature   | Major    | CloudStack exporter for Prometheus                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2284`_ | CLOUDSTACK-10103_  | New Feature   | Major    | Cloudian Connector for CloudStack                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2297`_ | CLOUDSTACK-9957_   | New Feature   | Major    | Annotations on entities                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2181`_ | CLOUDSTACK-9957_   | New Feature   | Major    | Annotations on entities                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2286`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2287`_ | CLOUDSTACK-9998_   | New Feature   | Major    | CloudStack exporter for Prometheus                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2278`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1707`_ | CLOUDSTACK-9397_   | New Feature   | Major    | Add Watchdog timer to KVM Instances                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2143`_ | CLOUDSTACK-9949_   | New Feature   | Minor    | add ability to specify mac address when                    |
|                         |          |                    |               |          | deployVirtualMachine or addNicToVirtualMachine is called   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2256`_ | CLOUDSTACK-9782_   | New Feature   | Major    | Host HA                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2239`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2222`_ | CLOUDSTACK-10022_  | New Feature   | Minor    | Allow domain admin to create and delete subdomains         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2026`_ | CLOUDSTACK-9861_   | New Feature   | Major    | Expire VM snapshots after configured duration              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2218`_ | CLOUDSTACK-9782_   | New Feature   | Major    | Host HA                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.11*                   | `#2407`_ | CLOUDSTACK-10227_  | Bug           | Blocker  | Stabilization fixes for master/4.11                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2403`_ | CLOUDSTACK-10227_  | Bug           | Blocker  | Stabilization fixes for master/4.11                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2396`_ | CLOUDSTACK-10220_  | Bug           | Major    | IPv4 NIC alias is not added on Virtual Router in Basic     |
|                         |          |                    |               |          | Networking when NIC has IPv6 address                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2362`_ | CLOUDSTACK-10188_  | Bug           | Major    | Resource Accounting for primary storage is Broken          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2393`_ | CLOUDSTACK-10217_  | Bug           | Major    | When IPv4 address of Instance is updated DHCP data is not  |
|                         |          |                    |               |          | cleared on VR                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2388`_ | CLOUDSTACK-10212_  | Bug           | Major    | Changing IPv4 Address of NIC in Basic Networking does not  |
|                         |          |                    |               |          | update the gateway                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2379`_ | CLOUDSTACK-10146_  | Bug           | Major    | Bypass Secondary Storage for KVM templates                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2391`_ | CLOUDSTACK-10215_  | Bug           | Major    | Excessive log4j debug level in CPVM, SSVM could lead to FS |
|                         |          |                    |               |          | overflow                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2139`_ | CLOUDSTACK-9921_   | Bug           | Major    | NPE when garbage collector is running                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2088`_ | CLOUDSTACK-9892_   | Bug           | Critical | Primary storage resource check is broken when using root   |
|                         |          |                    |               |          | disk size override to deploy VM                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2365`_ | CLOUDSTACK-10197_  | Bug           | Major    | XenServer 7.1: Cannot mount  xentool iso from cloudstack   |
|                         |          |                    |               |          | on VMs                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2073`_ | CLOUDSTACK-9896_   | Bug           | Minor    | ListDedicatedXXX doesn't respect pagination                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2386`_ | CLOUDSTACK-9632_   | Bug           | Major    | Upgrade bountycastle to 1.55+                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2315`_ | CLOUDSTACK-9025_   | Bug           | Critical | Unable to deploy VM instance from template if template     |
|                         |          |                    |               |          | spin from linked clone snapshot                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2274`_ | CLOUDSTACK-10096_  | Bug           | Major    | Can't reset api.integration.port and                       |
|                         |          |                    |               |          | usage.sanity.check.interval back to null                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2282`_ | CLOUDSTACK-10104_  | Bug           | Major    | Optimize database transactions in ListDomain API to        |
|                         |          |                    |               |          | improve performance                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2385`_ | CLOUDSTACK-10211_  | Bug           | Major    | test_nuage_public_sharednetwork_userdata fails due to      |
|                         |          |                    |               |          | errortext changed                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2260`_ | CLOUDSTACK-10065_  | Bug           | Major    | Optimize SQL queries in listTemplate API to improve        |
|                         |          |                    |               |          | performance.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1740`_ | CLOUDSTACK-9572_   | Bug           | Major    | Snapshot on primary storage not cleaned up after Storage   |
|                         |          |                    |               |          | migration                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2104`_ | CLOUDSTACK-9908_   | Bug           | Major    | Primary Storage allocated capacity goes very high after VM |
|                         |          |                    |               |          | snapshot                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2378`_ | CLOUDSTACK-10205_  | Bug           | Major    | LinkDomainToLdap returns internal id                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1773`_ | CLOUDSTACK-9607_   | Bug           | Major    | Preventing template deletion when template is in use.      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2149`_ | CLOUDSTACK-9932_   | Bug           | Major    | Snapshot is getting deleted while volume creation from the |
|                         |          |                    |               |          | snapshot is in progress                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2156`_ | CLOUDSTACK-9971_   | Bug           | Minor    | Bugfix/listaccounts parameter consistency                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2373`_ | CLOUDSTACK-10202_  | Bug           | Major    | createSnapshotPolicy API create multiple entries in DB for |
|                         |          |                    |               |          | same volume.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2344`_ | CLOUDSTACK-10163_  | Bug           | Major    | Component tests health check                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1760`_ | CLOUDSTACK-9593_   | Bug           | Major    | User data check is inconsistent with python                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2352`_ | CLOUDSTACK-10175_  | Bug           | Major    | Listing VPCs with a domain account and project id -1       |
|                         |          |                    |               |          | returns all the VPCs in the syste                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2347`_ | CLOUDSTACK-10166_  | Bug           | Minor    | Cannot add a tag to a NetworkACL (rule not list) in CS     |
|                         |          |                    |               |          | with a user in a project or in an account                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2375`_ | CLOUDSTACK-9456_   | Bug           | Major    | Migrate master to use Java8 and Spring4                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2211`_ | CLOUDSTACK-10013_  | Bug           | Major    | Migrate to Debian9 systemvmtemplate                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2304`_ | CLOUDSTACK-10127_  | Bug           | Critical | 4.9 / 4.10 KVM + openvswitch + vpc + static nat /          |
|                         |          |                    |               |          | secondary ip on eth2?                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2208`_ | CLOUDSTACK-9542_   | Bug           | Major    | listNics API does not return data as per API documentation |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2351`_ | CLOUDSTACK-10173_  | Bug           | Major    | Guest/Public nics on VR should pick network rate from      |
|                         |          |                    |               |          | network offering                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2370`_ | CLOUDSTACK-9595_   | Bug           | Major    | Transactions are not getting retried in case of database   |
|                         |          |                    |               |          | deadlock errors                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2366`_ | CLOUDSTACK-10168_  | Bug           | Major    | VR duplicate entries in /etc/hosts when reusing VM name    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2042`_ | CLOUDSTACK-9875_   | Bug           | Major    | Unable to re-apply Explicit dedication to VM               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2364`_ | CLOUDSTACK-10195_  | Bug           | Minor    | CloudStack MySQL HA problem -- No database selected        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2361`_ | CLOUDSTACK-10190_  | Bug           | Major    | Duplicate public VLAN for two different admin accounts.    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2247`_ | CLOUDSTACK-10012_  | Bug           | Major    | Migrate to Embedded Jetty based mgmt server                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1964`_ | CLOUDSTACK-9800_   | Bug           | Major    | Enable inline mode for NetScaler device                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1762`_ | CLOUDSTACK-9595_   | Bug           | Major    | Transactions are not getting retried in case of database   |
|                         |          |                    |               |          | deadlock errors                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2308`_ | CLOUDSTACK-8908_   | Bug           | Major    | After copying the template charging for that template is   |
|                         |          |                    |               |          | stopped                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2354`_ | CLOUDSTACK-10176_  | Bug           | Major    | VM Start Api Job returns success for failed Job            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2353`_ | CLOUDSTACK-9986_   | Bug           | Major    | Consider overcommit ratios with total/threshold values in  |
|                         |          |                    |               |          | Metrics View                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2358`_ | CLOUDSTACK-9736_   | Bug           | Minor    | Incoherent validation and error message when you change    |
|                         |          |                    |               |          | the vm.password.length configuration parameter             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2326`_ | CLOUDSTACK-10184_  | Bug           | Major    | Re-work method QuotaResponseBuilderImpl.startOfNextDay and |
|                         |          |                    |               |          | its test cases                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2267`_ | CLOUDSTACK-10077_  | Bug           | Major    | Allow account to use the same site-2-site VPN gateway with |
|                         |          |                    |               |          | different configs for several VPCs                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2337`_ | CLOUDSTACK-10157_  | Bug           | Major    | Wrong notification while migration                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2355`_ | CLOUDSTACK-10177_  | Bug           | Major    | NPE when programming Security Groups with KVM              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2349`_ | CLOUDSTACK-10070_  | Bug           | Major    | Extend travis run to include more component tests          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2312`_ | CLOUDSTACK-7793_   | Bug           | Critical | [Snapshots]Create Snaphot with "quiesce" option set to     |
|                         |          |                    |               |          | true fails with "InvalidParameterValueException: can't     |
|                         |          |                    |               |          | handle quiescevm equal true for volume snapshot"           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2345`_ | CLOUDSTACK-10164_  | Bug           | Blocker  | UI - not able to create a VPC                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2263`_ | CLOUDSTACK-10070_  | Bug           | Major    | Extend travis run to include more component tests          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2342`_ | CLOUDSTACK-9586_   | Bug           | Critical | When using local storage with Xenserver prepareTemplate    |
|                         |          |                    |               |          | does not work with multiple primary store                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2124`_ | CLOUDSTACK-9432_   | Bug           | Critical | Dedicate Cluster to Domain always creates an affinity      |
|                         |          |                    |               |          | group owned by the root domain                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2322`_ | CLOUDSTACK-10140_  | Bug           | Critical | When template is created from snapshot template.properties |
|                         |          |                    |               |          | are corrupted                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2335`_ | CLOUDSTACK-10154_  | Bug           | Major    | test failures in smoketest                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2341`_ | CLOUDSTACK-10160_  | Bug           | Major    | KVM VirtIO-SCSI not defined properly in Libvirt XML        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2321`_ | CLOUDSTACK-10138_  | Bug           | Major    | Load br_netfilter in security_group management script      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2334`_ | CLOUDSTACK-10152_  | Bug           | Major    | egress destination cidr with 0.0.0.0/0 is failing          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2310`_ | CLOUDSTACK-10133_  | Bug           | Major    | Local storage overprovisioning for ext file system         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2303`_ | CLOUDSTACK-10123_  | Bug           | Major    | VmWork job gets deleted before the parent job had time to  |
|                         |          |                    |               |          | fetch its result                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2329`_ | CLOUDSTACK-10012_  | Bug           | Major    | Migrate to Embedded Jetty based mgmt server                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2327`_ | CLOUDSTACK-10129_  | Bug           | Trivial  | Show instances attached to a network/VR via navigation     |
|                         |          |                    |               |          | from VRs->instances                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2316`_ | CLOUDSTACK-10137_  | Bug           | Major    | Re-installation fails for cloudstack-management            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2157`_ | CLOUDSTACK-9961_   | Bug           | Major    | Accept domain name for gateway while creating              |
|                         |          |                    |               |          | Vpncustomergateway                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2306`_ | CLOUDSTACK-10129_  | Bug           | Trivial  | Show instances attached to a network/VR via navigation     |
|                         |          |                    |               |          | from VRs->instances                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2273`_ | CLOUDSTACK-10090_  | Bug           | Major    | createPortForwardingRule api call accepts 'halt' as        |
|                         |          |                    |               |          | Protocol which Stops VR                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2240`_ | CLOUDSTACK-10051_  | Bug           | Major    | Mouse Scrolling is not working in instance VM console      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2291`_ | CLOUDSTACK-10111_  | Bug           | Minor    | Fix validation for parameter "vm.password.length"          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2302`_ | CLOUDSTACK-10122_  | Bug           | Major    | Unrelated error message                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2250`_ | CLOUDSTACK-10057_  | Bug           | Major    | ListNetworkOfferingsCmd does not return the correct count  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2268`_ | CLOUDSTACK-10081_  | Bug           | Major    | CloudUtils getDevInfo function only checks for KVM         |
|                         |          |                    |               |          | bridgePort and not OVS                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2293`_ | CLOUDSTACK-10047_  | Bug           | Major    | DVSwitch improvements                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2288`_ | CLOUDSTACK-10107_  | Bug           | Major    | VMware VM fails to start if it has more than 7 nics        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2257`_ | CLOUDSTACK-10060_  | Bug           | Minor    | ListUsage API always displays the Virtual size as '0' for  |
|                         |          |                    |               |          | Usage type=9 (snapshot)                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2246`_ | CLOUDSTACK-10046_  | Bug           | Major    | checksum is not verified during registerTemplate           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2074`_ | CLOUDSTACK-9899_   | Bug           | Major    | allow download without checking first for MS behind        |
|                         |          |                    |               |          | firewall                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2279`_ | CLOUDSTACK-9584_   | Bug           | Major    | Increase component tests coverage in Travis run            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2277`_ | CLOUDSTACK-10099_  | Bug           | Major    | GUI invokes migrateVirtualMachine instead of               |
|                         |          |                    |               |          | migrateVirtualMachineWithVolume                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2269`_ | CLOUDSTACK-10083_  | Bug           | Minor    | SSH keys are not created when starting from maintenance    |
|                         |          |                    |               |          | mode                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#876`_  | CLOUDSTACK-8865_   | Bug           | Major    | Adding SR doesn't create Storage_pool_host_ref entry for   |
|                         |          |                    |               |          | disabled host                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1252`_ | CLOUDSTACK-9182_   | Bug           | Major    | Some running VMs turned off on manual migration when auto  |
|                         |          |                    |               |          | migration failed while host preparing for maintenance      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2153`_ | CLOUDSTACK-9956_   | Bug           | Major    | File search on the vmware datastore may select wrong file  |
|                         |          |                    |               |          | if there are multiple files with same name                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2078`_ | CLOUDSTACK-9902_   | Bug           | Minor    | consoleproxy.sslEnabled global config variable is not      |
|                         |          |                    |               |          | present in default install                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2252`_ | CLOUDSTACK-10067_  | Bug           | Major    | Fix a case where a user 'ro' or 'roo' exists on the system |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2248`_ | CLOUDSTACK-10056_  | Bug           | Minor    | Cannot specify root disk controller when creating VM       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2243`_ | CLOUDSTACK-10019_  | Bug           | Major    | template.properties has hardcoded id                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2261`_ | CLOUDSTACK-10068_  | Bug           | Major    | smoketest/test_iso.py reports assertion failure            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2054`_ | CLOUDSTACK-9886_   | Bug           | Major    | After restarting cloudstack-management , It takes time to  |
|                         |          |                    |               |          | connect hosts                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#955`_  | CLOUDSTACK-8969_   | Bug           | Major    | VPN customer gateway can't be registered with hostname     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2262`_ | CLOUDSTACK-10069_  | Bug           | Major    | During release add sha512 suffix to sha 512 checksum/file  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2253`_ | CLOUDSTACK-10061_  | Bug           | Major    | When starting a VM, make sure it has the correct volume    |
|                         |          |                    |               |          | access group                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2254`_ | CLOUDSTACK-10058_  | Bug           | Major    | Error while opening the Settings tab in Secondary storage  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1733`_ | CLOUDSTACK-9563_   | Bug           | Major    | ExtractTemplate returns malformed URL after migrating NFS  |
|                         |          |                    |               |          | to s3                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2188`_ | CLOUDSTACK-10004_  | Bug           | Major    | On deletion, Vmware volume snapshots are left behind with  |
|                         |          |                    |               |          | message 'the snapshot has child, can't delete it on the    |
|                         |          |                    |               |          | storage'                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#914`_  | CLOUDSTACK-8939_   | Bug           | Major    | VM Snapshot size with memory is not correctly calculated   |
|                         |          |                    |               |          | in cloud.usage_event (XenServer)                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1985`_ | CLOUDSTACK-9812_   | Bug           | Major    | Update "updatePortForwardingRule" pi to include additional |
|                         |          |                    |               |          | parameter to update the end port in case of port range     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2224`_ | CLOUDSTACK-10032_  | Bug           | Major    | Database entries for templates created from snapshots      |
|                         |          |                    |               |          | disappear after management-server service restart          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2109`_ | CLOUDSTACK-9922_   | Bug           | Major    | Unable  to use 8081 port for Load balancing                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2216`_ | CLOUDSTACK-10027_  | Bug           | Minor    | Repeating the same list for Internal LB in VPC             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2174`_ | CLOUDSTACK-9996_   | Bug           | Major    | bug in network resource that juniper srx firewall          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2186`_ | CLOUDSTACK-10002_  | Bug           | Major    | Restart network with cleanup spawns Redundant Routers(In   |
|                         |          |                    |               |          | Default Network Offering)                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1246`_ | CLOUDSTACK-9165_   | Bug           | Major    | unable to use reserved IP range in a network for external  |
|                         |          |                    |               |          | VMs                                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2241`_ | CLOUDSTACK-10052_  | Bug           | Major    | Upgrading to 4.9.2 causes confusion/issues around dynamic  |
|                         |          |                    |               |          | roles usage                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2221`_ | CLOUDSTACK-10030_  | Bug           | Minor    | Public IPs assgined to the VPC are not reacheable from     |
|                         |          |                    |               |          | inside VPC                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2154`_ | CLOUDSTACK-9967_   | Bug           | Major    | [VPC] static nat on additional public subnet ip is not     |
|                         |          |                    |               |          | working.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1878`_ | CLOUDSTACK-9717_   | Bug           | Major    | [VMware] RVRs have mismatching MAC addresses for extra     |
|                         |          |                    |               |          | public NICs                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2013`_ | CLOUDSTACK-9734_   | Bug           | Major    | Destroy VM Fails sometimes                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2159`_ | CLOUDSTACK-9964_   | Bug           | Critical | Snapahots are getting deleted if VM is assigned to another |
|                         |          |                    |               |          | user                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2163`_ | CLOUDSTACK-9939_   | Bug           | Major    | Volumes stuck in Creating state while restarting the       |
|                         |          |                    |               |          | Management Server when the volume creation is in progress  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1919`_ | CLOUDSTACK-9763_   | Bug           | Major    | vpc: can not ssh to instance after vpc restart             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2215`_ | CLOUDSTACK-10026_  | Bug           | Major    | Page for Internal LB VM stucking while loading             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2180`_ | CLOUDSTACK-9999_   | Bug           | Major    | vpc tiers do not work if vpc has more than 8 tiers         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2182`_ | CLOUDSTACK-10000_  | Bug           | Major    | Remote access vpn user does not work if user password      |
|                         |          |                    |               |          | contains '#'                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2233`_ | CLOUDSTACK-10042_  | Bug           | Major    | UI doesn't show ICMP Type and Code for Security Group      |
|                         |          |                    |               |          | rules                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2228`_ | CLOUDSTACK-10036_  | Bug           | Major    | Decrease timeout of failing unit test                      |
|                         |          |                    |               |          | HypervisorUtilsTest.java                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1774`_ | CLOUDSTACK-9608_   | Bug           | Major    | Errored State and Abandoned state Templates are not        |
|                         |          |                    |               |          | displayed on UI                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2144`_ | CLOUDSTACK-9955_   | Bug           | Minor    | Featured Templates/Iso's created by Root/admin user are    |
|                         |          |                    |               |          | not visible to Domain Admin users                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1966`_ | CLOUDSTACK-9801_   | Bug           | Critical | IPSec VPN does not work after vRouter reboot or recreate   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2220`_ | CLOUDSTACK-9708_   | Bug           | Major    | Router deployment failed due to two threads start VR       |
|                         |          |                    |               |          | simultaneosuly                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1912`_ | CLOUDSTACK-9749_   | Bug           | Critical | cloudstack master vpc_internal_lb feature is broken as     |
|                         |          |                    |               |          | port 8080 is in use by password server on lb VM            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2138`_ | CLOUDSTACK-9944_   | Bug           | Major    | In clustered Management Server, Sometimes hosts stays in   |
|                         |          |                    |               |          | disconnected state.                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#883`_  | CLOUDSTACK-8906_   | Bug           | Major    | /var/log/cloud/ doesn't get logrotated on xenserver        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2119`_ | CLOUDSTACK-9925_   | Bug           | Minor    | Quota: fix tariff description for memory. Tariff value is  |
|                         |          |                    |               |          | for 1MB of RAM used per month (not hour).                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2145`_ | CLOUDSTACK-9697_   | Bug           | Major    | Better error message on UI user if tries to shrink the VM  |
|                         |          |                    |               |          | ROOT volume size                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2137`_ | CLOUDSTACK-9950_   | Bug           | Major    | listUsageRecords doesnt return required fields             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2008`_ | CLOUDSTACK-9840_   | Bug           | Major    | Datetime format of snapshot events is inconsistent with    |
|                         |          |                    |               |          | other events                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2142`_ | CLOUDSTACK-9954_   | Bug           | Major    | Unable to create service offering with networkrate=0       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2171`_ | CLOUDSTACK-9990_   | Bug           | Minor    | Account name is giving null in event tab after successful  |
|                         |          |                    |               |          | creation of account                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1925`_ | CLOUDSTACK-9751_   | Bug           | Major    | if a public IP is assigned to a VM when VR is in starting  |
|                         |          |                    |               |          | state, it does not get applied to the vport in Nuage VSD   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1798`_ | CLOUDSTACK-9631_   | Bug           | Major    | updateVMAffinityGroup must require one of the list         |
|                         |          |                    |               |          | parameter                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2201`_ | CLOUDSTACK-10016_  | Bug           | Major    | VPC VR doesn't respond to DNS requests from remote access  |
|                         |          |                    |               |          | vpn clients                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1959`_ | CLOUDSTACK-9786_   | Bug           | Major    | API reference guide entry for associateIpAddress needs a   |
|                         |          |                    |               |          | fix                                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1933`_ | CLOUDSTACK-9569_   | Bug           | Critical | VR on shared network not starting on KVM                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2298`_ | CLOUDSTACK-9620_   | Improvement   | Major    | Improvements for Managed Storage                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2152`_ | CLOUDSTACK-10229_  | Improvement   | Trivial  | SSVM logging improvement when using Swift as               |
|                         |          |                    |               |          | secondary-storage                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2389`_ | CLOUDSTACK-10213_  | Improvement   | Major    | Allow specify SSH key lengh                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2292`_ | CLOUDSTACK-10108_  | Improvement   | Minor    | ConfigKey based approach for reading 'ping' configuaration |
|                         |          |                    |               |          | for Management Server                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2384`_ | CLOUDSTACK-10210_  | Improvement   | Trivial  | remove test file                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1554`_ | CLOUDSTACK-9602_   | Improvement   | Major    | Add resource type name in response                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2035`_ | CLOUDSTACK-9867_   | Improvement   | Major    | VM snapshots - not charged for the primary storage they    |
|                         |          |                    |               |          | use up                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1934`_ | CLOUDSTACK-9772_   | Improvement   | Major    | Perform HEAD request to retrieve header information        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2348`_ | CLOUDSTACK-10196_  | Improvement   | Minor    | Remove ejb-api 3.0 dependency                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2184`_ | CLOUDSTACK-10003_  | Improvement   | Major    | automatic configure juniper srx/vsrx nat loopback          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2332`_ | CLOUDSTACK-10156_  | Improvement   | Minor    | Fix Coverity new problems CID(1349987, 1349986, 1347248)   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2219`_ | CLOUDSTACK-9989_   | Improvement   | Major    | Extend smoketests suite                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2005`_ | CLOUDSTACK-9450_   | Improvement   | Major    | Network Offering for VPC based on DB flag                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2242`_ | CLOUDSTACK-9958_   | Improvement   | Major    | Include tags of resources in listUsageRecords API          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2158`_ | CLOUDSTACK-9972_   | Improvement   | Major    | Enhance listVolume API to include physical size and        |
|                         |          |                    |               |          | utilization.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2004`_ | CLOUDSTACK-9832_   | Improvement   | Major    | Do not assign public IP NIC to the VPC VR when the VPC     |
|                         |          |                    |               |          | offering does not contain VpcVirtualRouter as a SourceNat  |
|                         |          |                    |               |          | provider                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2238`_ | CLOUDSTACK-10053_  | Improvement   | Major    | Performance improvement: Caching of external id's          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2296`_ | CLOUDSTACK-10007_  | Improvement   | Major    | Isolation methods are hard coded enum, replace by registry |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2280`_ | CLOUDSTACK-10101_  | Improvement   | Major    | Present the full domain name when listing user's domains   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2285`_ | CLOUDSTACK-9859_   | Improvement   | Major    | Retirement of midonet plugin (final removal ticket)        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2266`_ | CLOUDSTACK-10073_  | Improvement   | Trivial  | KVM host RAM overprovisioning                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2249`_ | CLOUDSTACK-10007_  | Improvement   | Major    | Isolation methods are hard coded enum, replace by registry |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1443`_ | CLOUDSTACK-9314_   | Improvement   | Trivial  | Remove unused code from XenServerStorageProcessor and      |
|                         |          |                    |               |          | change methods access level                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2044`_ | CLOUDSTACK-9877_   | Improvement   | Major    | remove fully cloned deleted templates from primary storage |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2101`_ | CLOUDSTACK-9915_   | Improvement   | Major    | ListSnapshots API does not provide virtual size            |
|                         |          |                    |               |          | information of the snapshots                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2123`_ | CLOUDSTACK-9914_   | Improvement   | Trivial  | Alter quota_tariff to support currency values up to 5      |
|                         |          |                    |               |          | decimal places                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1936`_ | CLOUDSTACK-9773_   | Improvement   | Major    | Don't break API output with non-printable characters       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2236`_ | CLOUDSTACK-10044_  | Improvement   | Major    | Update rule permission of a role permission                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2193`_ | CLOUDSTACK-10007_  | Improvement   | Major    | Isolation methods are hard coded enum, replace by registry |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2130`_ | CLOUDSTACK-8961_   | Improvement   | Major    | Making the VPN user management more intutive               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2200`_ | CLOUDSTACK-10015_  | Improvement   | Minor    | Return storage provider with call to list storage pools    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+




.. cssclass:: table-striped table-bordered table-hover

+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| Branches                | Github   | Jira               | Type          | Priority | Description                                                |
+=========================+==========+====================+===============+==========+============================================================+
| master                  | `#2097`_ | CLOUDSTACK-9813_   | New Feature   | Major    | Use configdrive for userdata, metadata & password          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2146`_ | CLOUDSTACK-4757_   | New Feature   | Minor    | Support OVA files with multiple disks for templates        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2394`_ | CLOUDSTACK-10109_  | New Feature   | Major    | Enable dedication of public IPs to SSVM and CPVM           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2295`_ | CLOUDSTACK-10109_  | New Feature   | Major    | Enable dedication of public IPs to SSVM and CPVM           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2381`_ | CLOUDSTACK-10117_  | New Feature   | Major    | LDAP mapping on domain level                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2368`_ | CLOUDSTACK-10126_  | New Feature   | Major    | Separate Subnet for CPVM and SSVM                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2046`_ | CLOUDSTACK-7958_   | New Feature   | Minor    | Limit user login to specific subnets                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2374`_ | CLOUDSTACK-10024_  | New Feature   | Major    | Physical Networking Migration                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2301`_ | CLOUDSTACK-10121_  | New Feature   | Major    | move user API                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2360`_ | CLOUDSTACK-10189_  | New Feature   | Major    | Support for "VSD managed" networks with Nuage Networks     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2281`_ | CLOUDSTACK-10102_  | New Feature   | Major    | New Network Type (L2)                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2048`_ | CLOUDSTACK-9880_   | New Feature   | Major    | Expansion of Management IP Range.                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2294`_ | CLOUDSTACK-10039_  | New Feature   | Major    | Adding IOPS/GB offering                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2356`_ | CLOUDSTACK-8313_   | New Feature   | Major    | Local Storage overprovisioning should be possible          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2028`_ | CLOUDSTACK-9853_   | New Feature   | Major    | IPv6 Prefix Delegation support in Basic Networking         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1981`_ | CLOUDSTACK-9806_   | New Feature   | Major    | Nuage domain template selection per VPC                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2325`_ | CLOUDSTACK-9998_   | New Feature   | Major    | CloudStack exporter for Prometheus                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2284`_ | CLOUDSTACK-10103_  | New Feature   | Major    | Cloudian Connector for CloudStack                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2297`_ | CLOUDSTACK-9957_   | New Feature   | Major    | Annotations on entities                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2181`_ | CLOUDSTACK-9957_   | New Feature   | Major    | Annotations on entities                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2286`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2287`_ | CLOUDSTACK-9998_   | New Feature   | Major    | CloudStack exporter for Prometheus                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2278`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1707`_ | CLOUDSTACK-9397_   | New Feature   | Major    | Add Watchdog timer to KVM Instances                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2143`_ | CLOUDSTACK-9949_   | New Feature   | Minor    | add ability to specify mac address when                    |
|                         |          |                    |               |          | deployVirtualMachine or addNicToVirtualMachine is called   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2256`_ | CLOUDSTACK-9782_   | New Feature   | Major    | Host HA                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2239`_ | CLOUDSTACK-9993_   | New Feature   | Major    | Secure Agent Communications                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2222`_ | CLOUDSTACK-10022_  | New Feature   | Minor    | Allow domain admin to create and delete subdomains         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2026`_ | CLOUDSTACK-9861_   | New Feature   | Major    | Expire VM snapshots after configured duration              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2218`_ | CLOUDSTACK-9782_   | New Feature   | Major    | Host HA                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.11*                   | `#2407`_ | CLOUDSTACK-10227_  | Bug           | Blocker  | Stabilization fixes for master/4.11                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2403`_ | CLOUDSTACK-10227_  | Bug           | Blocker  | Stabilization fixes for master/4.11                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2396`_ | CLOUDSTACK-10220_  | Bug           | Major    | IPv4 NIC alias is not added on Virtual Router in Basic     |
|                         |          |                    |               |          | Networking when NIC has IPv6 address                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2362`_ | CLOUDSTACK-10188_  | Bug           | Major    | Resource Accounting for primary storage is Broken          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2393`_ | CLOUDSTACK-10217_  | Bug           | Major    | When IPv4 address of Instance is updated DHCP data is not  |
|                         |          |                    |               |          | cleared on VR                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2388`_ | CLOUDSTACK-10212_  | Bug           | Major    | Changing IPv4 Address of NIC in Basic Networking does not  |
|                         |          |                    |               |          | update the gateway                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2379`_ | CLOUDSTACK-10146_  | Bug           | Major    | Bypass Secondary Storage for KVM templates                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2391`_ | CLOUDSTACK-10215_  | Bug           | Major    | Excessive log4j debug level in CPVM, SSVM could lead to FS |
|                         |          |                    |               |          | overflow                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2139`_ | CLOUDSTACK-9921_   | Bug           | Major    | NPE when garbage collector is running                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2088`_ | CLOUDSTACK-9892_   | Bug           | Critical | Primary storage resource check is broken when using root   |
|                         |          |                    |               |          | disk size override to deploy VM                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2365`_ | CLOUDSTACK-10197_  | Bug           | Major    | XenServer 7.1: Cannot mount  xentool iso from cloudstack   |
|                         |          |                    |               |          | on VMs                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2073`_ | CLOUDSTACK-9896_   | Bug           | Minor    | ListDedicatedXXX doesn't respect pagination                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2386`_ | CLOUDSTACK-9632_   | Bug           | Major    | Upgrade bountycastle to 1.55+                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2315`_ | CLOUDSTACK-9025_   | Bug           | Critical | Unable to deploy VM instance from template if template     |
|                         |          |                    |               |          | spin from linked clone snapshot                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2274`_ | CLOUDSTACK-10096_  | Bug           | Major    | Can't reset api.integration.port and                       |
|                         |          |                    |               |          | usage.sanity.check.interval back to null                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2282`_ | CLOUDSTACK-10104_  | Bug           | Major    | Optimize database transactions in ListDomain API to        |
|                         |          |                    |               |          | improve performance                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2385`_ | CLOUDSTACK-10211_  | Bug           | Major    | test_nuage_public_sharednetwork_userdata fails due to      |
|                         |          |                    |               |          | errortext changed                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2260`_ | CLOUDSTACK-10065_  | Bug           | Major    | Optimize SQL queries in listTemplate API to improve        |
|                         |          |                    |               |          | performance.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1740`_ | CLOUDSTACK-9572_   | Bug           | Major    | Snapshot on primary storage not cleaned up after Storage   |
|                         |          |                    |               |          | migration                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2104`_ | CLOUDSTACK-9908_   | Bug           | Major    | Primary Storage allocated capacity goes very high after VM |
|                         |          |                    |               |          | snapshot                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2378`_ | CLOUDSTACK-10205_  | Bug           | Major    | LinkDomainToLdap returns internal id                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1773`_ | CLOUDSTACK-9607_   | Bug           | Major    | Preventing template deletion when template is in use.      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2149`_ | CLOUDSTACK-9932_   | Bug           | Major    | Snapshot is getting deleted while volume creation from the |
|                         |          |                    |               |          | snapshot is in progress                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2156`_ | CLOUDSTACK-9971_   | Bug           | Minor    | Bugfix/listaccounts parameter consistency                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2373`_ | CLOUDSTACK-10202_  | Bug           | Major    | createSnapshotPolicy API create multiple entries in DB for |
|                         |          |                    |               |          | same volume.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2344`_ | CLOUDSTACK-10163_  | Bug           | Major    | Component tests health check                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1760`_ | CLOUDSTACK-9593_   | Bug           | Major    | User data check is inconsistent with python                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2352`_ | CLOUDSTACK-10175_  | Bug           | Major    | Listing VPCs with a domain account and project id -1       |
|                         |          |                    |               |          | returns all the VPCs in the syste                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2347`_ | CLOUDSTACK-10166_  | Bug           | Minor    | Cannot add a tag to a NetworkACL (rule not list) in CS     |
|                         |          |                    |               |          | with a user in a project or in an account                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2375`_ | CLOUDSTACK-9456_   | Bug           | Major    | Migrate master to use Java8 and Spring4                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2211`_ | CLOUDSTACK-10013_  | Bug           | Major    | Migrate to Debian9 systemvmtemplate                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2304`_ | CLOUDSTACK-10127_  | Bug           | Critical | 4.9 / 4.10 KVM + openvswitch + vpc + static nat /          |
|                         |          |                    |               |          | secondary ip on eth2?                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2208`_ | CLOUDSTACK-9542_   | Bug           | Major    | listNics API does not return data as per API documentation |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2351`_ | CLOUDSTACK-10173_  | Bug           | Major    | Guest/Public nics on VR should pick network rate from      |
|                         |          |                    |               |          | network offering                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2370`_ | CLOUDSTACK-9595_   | Bug           | Major    | Transactions are not getting retried in case of database   |
|                         |          |                    |               |          | deadlock errors                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2366`_ | CLOUDSTACK-10168_  | Bug           | Major    | VR duplicate entries in /etc/hosts when reusing VM name    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2042`_ | CLOUDSTACK-9875_   | Bug           | Major    | Unable to re-apply Explicit dedication to VM               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2364`_ | CLOUDSTACK-10195_  | Bug           | Minor    | CloudStack MySQL HA problem -- No database selected        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2361`_ | CLOUDSTACK-10190_  | Bug           | Major    | Duplicate public VLAN for two different admin accounts.    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2247`_ | CLOUDSTACK-10012_  | Bug           | Major    | Migrate to Embedded Jetty based mgmt server                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1964`_ | CLOUDSTACK-9800_   | Bug           | Major    | Enable inline mode for NetScaler device                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1762`_ | CLOUDSTACK-9595_   | Bug           | Major    | Transactions are not getting retried in case of database   |
|                         |          |                    |               |          | deadlock errors                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2308`_ | CLOUDSTACK-8908_   | Bug           | Major    | After copying the template charging for that template is   |
|                         |          |                    |               |          | stopped                                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2354`_ | CLOUDSTACK-10176_  | Bug           | Major    | VM Start Api Job returns success for failed Job            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2353`_ | CLOUDSTACK-9986_   | Bug           | Major    | Consider overcommit ratios with total/threshold values in  |
|                         |          |                    |               |          | Metrics View                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2358`_ | CLOUDSTACK-9736_   | Bug           | Minor    | Incoherent validation and error message when you change    |
|                         |          |                    |               |          | the vm.password.length configuration parameter             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2326`_ | CLOUDSTACK-10184_  | Bug           | Major    | Re-work method QuotaResponseBuilderImpl.startOfNextDay and |
|                         |          |                    |               |          | its test cases                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2267`_ | CLOUDSTACK-10077_  | Bug           | Major    | Allow account to use the same site-2-site VPN gateway with |
|                         |          |                    |               |          | different configs for several VPCs                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2337`_ | CLOUDSTACK-10157_  | Bug           | Major    | Wrong notification while migration                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2355`_ | CLOUDSTACK-10177_  | Bug           | Major    | NPE when programming Security Groups with KVM              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2349`_ | CLOUDSTACK-10070_  | Bug           | Major    | Extend travis run to include more component tests          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2312`_ | CLOUDSTACK-7793_   | Bug           | Critical | [Snapshots]Create Snaphot with "quiesce" option set to     |
|                         |          |                    |               |          | true fails with "InvalidParameterValueException: can't     |
|                         |          |                    |               |          | handle quiescevm equal true for volume snapshot"           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2345`_ | CLOUDSTACK-10164_  | Bug           | Blocker  | UI - not able to create a VPC                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2263`_ | CLOUDSTACK-10070_  | Bug           | Major    | Extend travis run to include more component tests          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2342`_ | CLOUDSTACK-9586_   | Bug           | Critical | When using local storage with Xenserver prepareTemplate    |
|                         |          |                    |               |          | does not work with multiple primary store                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2124`_ | CLOUDSTACK-9432_   | Bug           | Critical | Dedicate Cluster to Domain always creates an affinity      |
|                         |          |                    |               |          | group owned by the root domain                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2322`_ | CLOUDSTACK-10140_  | Bug           | Critical | When template is created from snapshot template.properties |
|                         |          |                    |               |          | are corrupted                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2335`_ | CLOUDSTACK-10154_  | Bug           | Major    | test failures in smoketest                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2341`_ | CLOUDSTACK-10160_  | Bug           | Major    | KVM VirtIO-SCSI not defined properly in Libvirt XML        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2321`_ | CLOUDSTACK-10138_  | Bug           | Major    | Load br_netfilter in security_group management script      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2334`_ | CLOUDSTACK-10152_  | Bug           | Major    | egress destination cidr with 0.0.0.0/0 is failing          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2310`_ | CLOUDSTACK-10133_  | Bug           | Major    | Local storage overprovisioning for ext file system         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2303`_ | CLOUDSTACK-10123_  | Bug           | Major    | VmWork job gets deleted before the parent job had time to  |
|                         |          |                    |               |          | fetch its result                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2329`_ | CLOUDSTACK-10012_  | Bug           | Major    | Migrate to Embedded Jetty based mgmt server                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2327`_ | CLOUDSTACK-10129_  | Bug           | Trivial  | Show instances attached to a network/VR via navigation     |
|                         |          |                    |               |          | from VRs->instances                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2313`_ | CLOUDSTACK-10135_  | Bug           | Major    | ACL rules order is not maintained for ACL_OUTBOUND in VPC  |
|                         |          |                    |               |          | VR                                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2316`_ | CLOUDSTACK-10137_  | Bug           | Major    | Re-installation fails for cloudstack-management            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2157`_ | CLOUDSTACK-9961_   | Bug           | Major    | Accept domain name for gateway while creating              |
|                         |          |                    |               |          | Vpncustomergateway                                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2306`_ | CLOUDSTACK-10129_  | Bug           | Trivial  | Show instances attached to a network/VR via navigation     |
|                         |          |                    |               |          | from VRs->instances                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2273`_ | CLOUDSTACK-10090_  | Bug           | Major    | createPortForwardingRule api call accepts 'halt' as        |
|                         |          |                    |               |          | Protocol which Stops VR                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2240`_ | CLOUDSTACK-10051_  | Bug           | Major    | Mouse Scrolling is not working in instance VM console      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2291`_ | CLOUDSTACK-10111_  | Bug           | Minor    | Fix validation for parameter "vm.password.length"          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2302`_ | CLOUDSTACK-10122_  | Bug           | Major    | Unrelated error message                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2250`_ | CLOUDSTACK-10057_  | Bug           | Major    | ListNetworkOfferingsCmd does not return the correct count  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2268`_ | CLOUDSTACK-10081_  | Bug           | Major    | CloudUtils getDevInfo function only checks for KVM         |
|                         |          |                    |               |          | bridgePort and not OVS                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2293`_ | CLOUDSTACK-10047_  | Bug           | Major    | DVSwitch improvements                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2288`_ | CLOUDSTACK-10107_  | Bug           | Major    | VMware VM fails to start if it has more than 7 nics        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2257`_ | CLOUDSTACK-10060_  | Bug           | Minor    | ListUsage API always displays the Virtual size as '0' for  |
|                         |          |                    |               |          | Usage type=9 (snapshot)                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2246`_ | CLOUDSTACK-10046_  | Bug           | Major    | checksum is not verified during registerTemplate           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2074`_ | CLOUDSTACK-9899_   | Bug           | Major    | allow download without checking first for MS behind        |
|                         |          |                    |               |          | firewall                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2279`_ | CLOUDSTACK-9584_   | Bug           | Major    | Increase component tests coverage in Travis run            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2277`_ | CLOUDSTACK-10099_  | Bug           | Major    | GUI invokes migrateVirtualMachine instead of               |
|                         |          |                    |               |          | migrateVirtualMachineWithVolume                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2269`_ | CLOUDSTACK-10083_  | Bug           | Minor    | SSH keys are not created when starting from maintenance    |
|                         |          |                    |               |          | mode                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#876`_  | CLOUDSTACK-8865_   | Bug           | Major    | Adding SR doesn't create Storage_pool_host_ref entry for   |
|                         |          |                    |               |          | disabled host                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1252`_ | CLOUDSTACK-9182_   | Bug           | Major    | Some running VMs turned off on manual migration when auto  |
|                         |          |                    |               |          | migration failed while host preparing for maintenance      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2153`_ | CLOUDSTACK-9956_   | Bug           | Major    | File search on the vmware datastore may select wrong file  |
|                         |          |                    |               |          | if there are multiple files with same name                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2078`_ | CLOUDSTACK-9902_   | Bug           | Minor    | consoleproxy.sslEnabled global config variable is not      |
|                         |          |                    |               |          | present in default install                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2252`_ | CLOUDSTACK-10067_  | Bug           | Major    | Fix a case where a user 'ro' or 'roo' exists on the system |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2248`_ | CLOUDSTACK-10056_  | Bug           | Minor    | Cannot specify root disk controller when creating VM       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2243`_ | CLOUDSTACK-10019_  | Bug           | Major    | template.properties has hardcoded id                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2261`_ | CLOUDSTACK-10068_  | Bug           | Major    | smoketest/test_iso.py reports assertion failure            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2054`_ | CLOUDSTACK-9886_   | Bug           | Major    | After restarting cloudstack-management , It takes time to  |
|                         |          |                    |               |          | connect hosts                                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#955`_  | CLOUDSTACK-8969_   | Bug           | Major    | VPN customer gateway can't be registered with hostname     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2262`_ | CLOUDSTACK-10069_  | Bug           | Major    | During release add sha512 suffix to sha 512 checksum/file  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2253`_ | CLOUDSTACK-10061_  | Bug           | Major    | When starting a VM, make sure it has the correct volume    |
|                         |          |                    |               |          | access group                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2254`_ | CLOUDSTACK-10058_  | Bug           | Major    | Error while opening the Settings tab in Secondary storage  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1733`_ | CLOUDSTACK-9563_   | Bug           | Major    | ExtractTemplate returns malformed URL after migrating NFS  |
|                         |          |                    |               |          | to s3                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2188`_ | CLOUDSTACK-10004_  | Bug           | Major    | On deletion, Vmware volume snapshots are left behind with  |
|                         |          |                    |               |          | message 'the snapshot has child, can't delete it on the    |
|                         |          |                    |               |          | storage'                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#914`_  | CLOUDSTACK-8939_   | Bug           | Major    | VM Snapshot size with memory is not correctly calculated   |
|                         |          |                    |               |          | in cloud.usage_event (XenServer)                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1985`_ | CLOUDSTACK-9812_   | Bug           | Major    | Update "updatePortForwardingRule" pi to include additional |
|                         |          |                    |               |          | parameter to update the end port in case of port range     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2224`_ | CLOUDSTACK-10032_  | Bug           | Major    | Database entries for templates created from snapshots      |
|                         |          |                    |               |          | disappear after management-server service restart          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2109`_ | CLOUDSTACK-9922_   | Bug           | Major    | Unable  to use 8081 port for Load balancing                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2216`_ | CLOUDSTACK-10027_  | Bug           | Minor    | Repeating the same list for Internal LB in VPC             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2174`_ | CLOUDSTACK-9996_   | Bug           | Major    | bug in network resource that juniper srx firewall          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2186`_ | CLOUDSTACK-10002_  | Bug           | Major    | Restart network with cleanup spawns Redundant Routers(In   |
|                         |          |                    |               |          | Default Network Offering)                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1246`_ | CLOUDSTACK-9165_   | Bug           | Major    | unable to use reserved IP range in a network for external  |
|                         |          |                    |               |          | VMs                                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2241`_ | CLOUDSTACK-10052_  | Bug           | Major    | Upgrading to 4.9.2 causes confusion/issues around dynamic  |
|                         |          |                    |               |          | roles usage                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2221`_ | CLOUDSTACK-10030_  | Bug           | Minor    | Public IPs assgined to the VPC are not reacheable from     |
|                         |          |                    |               |          | inside VPC                                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2154`_ | CLOUDSTACK-9967_   | Bug           | Major    | [VPC] static nat on additional public subnet ip is not     |
|                         |          |                    |               |          | working.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1878`_ | CLOUDSTACK-9717_   | Bug           | Major    | [VMware] RVRs have mismatching MAC addresses for extra     |
|                         |          |                    |               |          | public NICs                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2013`_ | CLOUDSTACK-9734_   | Bug           | Major    | Destroy VM Fails sometimes                                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2159`_ | CLOUDSTACK-9964_   | Bug           | Critical | Snapahots are getting deleted if VM is assigned to another |
|                         |          |                    |               |          | user                                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2163`_ | CLOUDSTACK-9939_   | Bug           | Major    | Volumes stuck in Creating state while restarting the       |
|                         |          |                    |               |          | Management Server when the volume creation is in progress  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1919`_ | CLOUDSTACK-9763_   | Bug           | Major    | vpc: can not ssh to instance after vpc restart             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2215`_ | CLOUDSTACK-10026_  | Bug           | Major    | Page for Internal LB VM stucking while loading             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2180`_ | CLOUDSTACK-9999_   | Bug           | Major    | vpc tiers do not work if vpc has more than 8 tiers         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2223`_ | CLOUDSTACK-10031_  | Bug           | Major    | change default configuration for                           |
|                         |          |                    |               |          | router.aggregation.command.each.timeout from 3 to 600      |
|                         |          |                    |               |          | seconds.                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2182`_ | CLOUDSTACK-10000_  | Bug           | Major    | Remote access vpn user does not work if user password      |
|                         |          |                    |               |          | contains '#'                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2233`_ | CLOUDSTACK-10042_  | Bug           | Major    | UI doesn't show ICMP Type and Code for Security Group      |
|                         |          |                    |               |          | rules                                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2228`_ | CLOUDSTACK-10036_  | Bug           | Major    | Decrease timeout of failing unit test                      |
|                         |          |                    |               |          | HypervisorUtilsTest.java                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1774`_ | CLOUDSTACK-9608_   | Bug           | Major    | Errored State and Abandoned state Templates are not        |
|                         |          |                    |               |          | displayed on UI                                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2144`_ | CLOUDSTACK-9955_   | Bug           | Minor    | Featured Templates/Iso's created by Root/admin user are    |
|                         |          |                    |               |          | not visible to Domain Admin users                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1966`_ | CLOUDSTACK-9801_   | Bug           | Critical | IPSec VPN does not work after vRouter reboot or recreate   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2220`_ | CLOUDSTACK-9708_   | Bug           | Major    | Router deployment failed due to two threads start VR       |
|                         |          |                    |               |          | simultaneosuly                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1912`_ | CLOUDSTACK-9749_   | Bug           | Critical | cloudstack master vpc_internal_lb feature is broken as     |
|                         |          |                    |               |          | port 8080 is in use by password server on lb VM            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2138`_ | CLOUDSTACK-9944_   | Bug           | Major    | In clustered Management Server, Sometimes hosts stays in   |
|                         |          |                    |               |          | disconnected state.                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#883`_  | CLOUDSTACK-8906_   | Bug           | Major    | /var/log/cloud/ doesn't get logrotated on xenserver        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2119`_ | CLOUDSTACK-9925_   | Bug           | Minor    | Quota: fix tariff description for memory. Tariff value is  |
|                         |          |                    |               |          | for 1MB of RAM used per month (not hour).                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2145`_ | CLOUDSTACK-9697_   | Bug           | Major    | Better error message on UI user if tries to shrink the VM  |
|                         |          |                    |               |          | ROOT volume size                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2137`_ | CLOUDSTACK-9950_   | Bug           | Major    | listUsageRecords doesnt return required fields             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2008`_ | CLOUDSTACK-9840_   | Bug           | Major    | Datetime format of snapshot events is inconsistent with    |
|                         |          |                    |               |          | other events                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2142`_ | CLOUDSTACK-9954_   | Bug           | Major    | Unable to create service offering with networkrate=0       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2171`_ | CLOUDSTACK-9990_   | Bug           | Minor    | Account name is giving null in event tab after successful  |
|                         |          |                    |               |          | creation of account                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1925`_ | CLOUDSTACK-9751_   | Bug           | Major    | if a public IP is assigned to a VM when VR is in starting  |
|                         |          |                    |               |          | state, it does not get applied to the vport in Nuage VSD   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1798`_ | CLOUDSTACK-9631_   | Bug           | Major    | updateVMAffinityGroup must require one of the list         |
|                         |          |                    |               |          | parameter                                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2201`_ | CLOUDSTACK-10016_  | Bug           | Major    | VPC VR doesn't respond to DNS requests from remote access  |
|                         |          |                    |               |          | vpn clients                                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1959`_ | CLOUDSTACK-9786_   | Bug           | Major    | API reference guide entry for associateIpAddress needs a   |
|                         |          |                    |               |          | fix                                                        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#1933`_ | CLOUDSTACK-9569_   | Bug           | Critical | VR on shared network not starting on KVM                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2298`_ | CLOUDSTACK-9620_   | Improvement   | Major    | Improvements for Managed Storage                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2152`_ | CLOUDSTACK-10229_  | Improvement   | Trivial  | SSVM logging improvement when using Swift as               |
|                         |          |                    |               |          | secondary-storage                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2389`_ | CLOUDSTACK-10213_  | Improvement   | Major    | Allow specify SSH key lengh                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2292`_ | CLOUDSTACK-10108_  | Improvement   | Minor    | ConfigKey based approach for reading 'ping' configuaration |
|                         |          |                    |               |          | for Management Server                                      |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2384`_ | CLOUDSTACK-10210_  | Improvement   | Trivial  | remove test file                                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1554`_ | CLOUDSTACK-9602_   | Improvement   | Major    | Add resource type name in response                         |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2035`_ | CLOUDSTACK-9867_   | Improvement   | Major    | VM snapshots - not charged for the primary storage they    |
|                         |          |                    |               |          | use up                                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1934`_ | CLOUDSTACK-9772_   | Improvement   | Major    | Perform HEAD request to retrieve header information        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2348`_ | CLOUDSTACK-10196_  | Improvement   | Minor    | Remove ejb-api 3.0 dependency                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2184`_ | CLOUDSTACK-10003_  | Improvement   | Major    | automatic configure juniper srx/vsrx nat loopback          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2332`_ | CLOUDSTACK-10156_  | Improvement   | Minor    | Fix Coverity new problems CID(1349987, 1349986, 1347248)   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2219`_ | CLOUDSTACK-9989_   | Improvement   | Major    | Extend smoketests suite                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2005`_ | CLOUDSTACK-9450_   | Improvement   | Major    | Network Offering for VPC based on DB flag                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2242`_ | CLOUDSTACK-9958_   | Improvement   | Major    | Include tags of resources in listUsageRecords API          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2158`_ | CLOUDSTACK-9972_   | Improvement   | Major    | Enhance listVolume API to include physical size and        |
|                         |          |                    |               |          | utilization.                                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2004`_ | CLOUDSTACK-9832_   | Improvement   | Major    | Do not assign public IP NIC to the VPC VR when the VPC     |
|                         |          |                    |               |          | offering does not contain VpcVirtualRouter as a SourceNat  |
|                         |          |                    |               |          | provider                                                   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2238`_ | CLOUDSTACK-10053_  | Improvement   | Major    | Performance improvement: Caching of external id's          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2296`_ | CLOUDSTACK-10007_  | Improvement   | Major    | Isolation methods are hard coded enum, replace by registry |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2280`_ | CLOUDSTACK-10101_  | Improvement   | Major    | Present the full domain name when listing user's domains   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2285`_ | CLOUDSTACK-9859_   | Improvement   | Major    | Retirement of midonet plugin (final removal ticket)        |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2266`_ | CLOUDSTACK-10073_  | Improvement   | Trivial  | KVM host RAM overprovisioning                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2249`_ | CLOUDSTACK-10007_  | Improvement   | Major    | Isolation methods are hard coded enum, replace by registry |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1443`_ | CLOUDSTACK-9314_   | Improvement   | Trivial  | Remove unused code from XenServerStorageProcessor and      |
|                         |          |                    |               |          | change methods access level                                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2044`_ | CLOUDSTACK-9877_   | Improvement   | Major    | remove fully cloned deleted templates from primary storage |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2101`_ | CLOUDSTACK-9915_   | Improvement   | Major    | ListSnapshots API does not provide virtual size            |
|                         |          |                    |               |          | information of the snapshots                               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2123`_ | CLOUDSTACK-9914_   | Improvement   | Trivial  | Alter quota_tariff to support currency values up to 5      |
|                         |          |                    |               |          | decimal places                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1936`_ | CLOUDSTACK-9773_   | Improvement   | Major    | Don't break API output with non-printable characters       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2236`_ | CLOUDSTACK-10044_  | Improvement   | Major    | Update rule permission of a role permission                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2193`_ | CLOUDSTACK-10007_  | Improvement   | Major    | Isolation methods are hard coded enum, replace by registry |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2130`_ | CLOUDSTACK-8961_   | Improvement   | Major    | Making the VPN user management more intutive               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2200`_ | CLOUDSTACK-10015_  | Improvement   | Minor    | Return storage provider with call to list storage pools    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2350`_ |                    |               |          | Cloudstack 10170 - fixes resource tags security bugs and   |
|                         |          |                    |               |          | adds account tags support                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2383`_ |                    |               |          | "isdynamicallyscalable" Field to UpdateTemplate Response   |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2045`_ |                    |               |          | Fix snmptrap alert bug                                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2258`_ |                    |               |          | Cloudstack 10064: Secondary storage Usage for              |
|                         |          |                    |               |          | uploadedVolume is not collected                            |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1637`_ |                    |               |          | Command route not available on CentOS 7                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2367`_ |                    |               |          | Fix ACL_INBOUND/OUTBOUND rules for PrivateGateway          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2371`_ |                    |               |          | README: Happy Holidays, may the cloud be with you in 2018! |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1437`_ |                    |               |          | removed unused HypervDummyResourceBase class               |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2346`_ |                    |               |          | Add XenServer 7.1 and 7.2 interoperablility                |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2359`_ |                    |               |          | doc: replace virutal by virtual (typo)                     |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2324`_ |                    |               |          | Remove annotation and "depends-on" declaration not needed  |
|                         |          |                    |               |          | at cloud-engine-storage-image                              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1723`_ |                    |               |          | Fix GroupBy (+ having) condition and tests                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2307`_ |                    |               |          | packging: Raise compat mode to 9                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2245`_ |                    |               |          | increased jetty timeout                                    |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2235`_ |                    |               |          | repo has moved                                             |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2039`_ |                    |               |          | rbd: Use libvirt to create new volumes and not rados-java  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2094`_ |                    |               |          | Agent logrotation                                          |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.9*                    | `#2212`_ |                    |               |          | appliance: fix progress version in Gemfile                 |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2205`_ |                    |               |          | Add NULL checks for various objects in SolidFire           |
|                         |          |                    |               |          | integration test API                                       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1784`_ |                    |               |          | CS-505: Marvin test to check VR internal DNS Service       |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#1655`_ |                    |               |          | Fix ajaxviewer.js to solve console on Firefox              |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| master                  | `#2175`_ |                    |               |          | 4.10 to 4.11 upgrade path                                  |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+
| 4.10*                   | `#2176`_ |                    |               |          | Travis: use oraclejdk8 for 4.10+                           |
+-------------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+

.. _`#2407`: https://github.com/apache/cloudstack/pull/2407
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2403`: https://github.com/apache/cloudstack/pull/2403
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2298`: https://github.com/apache/cloudstack/pull/2298
.. _CLOUDSTACK-9620: https://issues.apache.org/jira/browse/CLOUDSTACK-9620
.. _`#2396`: https://github.com/apache/cloudstack/pull/2396
.. _CLOUDSTACK-10220: https://issues.apache.org/jira/browse/CLOUDSTACK-10220
.. _`#2152`: https://github.com/apache/cloudstack/pull/2152
.. _CLOUDSTACK-10229: https://issues.apache.org/jira/browse/CLOUDSTACK-10229
.. _`#2097`: https://github.com/apache/cloudstack/pull/2097
.. _CLOUDSTACK-9813: https://issues.apache.org/jira/browse/CLOUDSTACK-9813
.. _`#2362`: https://github.com/apache/cloudstack/pull/2362
.. _CLOUDSTACK-10188: https://issues.apache.org/jira/browse/CLOUDSTACK-10188
.. _`#2146`: https://github.com/apache/cloudstack/pull/2146
.. _CLOUDSTACK-4757: https://issues.apache.org/jira/browse/CLOUDSTACK-4757
.. _`#2394`: https://github.com/apache/cloudstack/pull/2394
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2393`: https://github.com/apache/cloudstack/pull/2393
.. _CLOUDSTACK-10217: https://issues.apache.org/jira/browse/CLOUDSTACK-10217
.. _`#2350`: https://github.com/apache/cloudstack/pull/2350
.. _`#2388`: https://github.com/apache/cloudstack/pull/2388
.. _CLOUDSTACK-10212: https://issues.apache.org/jira/browse/CLOUDSTACK-10212
.. _`#2379`: https://github.com/apache/cloudstack/pull/2379
.. _CLOUDSTACK-10146: https://issues.apache.org/jira/browse/CLOUDSTACK-10146
.. _`#2389`: https://github.com/apache/cloudstack/pull/2389
.. _CLOUDSTACK-10213: https://issues.apache.org/jira/browse/CLOUDSTACK-10213
.. _`#2391`: https://github.com/apache/cloudstack/pull/2391
.. _CLOUDSTACK-10215: https://issues.apache.org/jira/browse/CLOUDSTACK-10215
.. _`#2139`: https://github.com/apache/cloudstack/pull/2139
.. _CLOUDSTACK-9921: https://issues.apache.org/jira/browse/CLOUDSTACK-9921
.. _`#2088`: https://github.com/apache/cloudstack/pull/2088
.. _CLOUDSTACK-9892: https://issues.apache.org/jira/browse/CLOUDSTACK-9892
.. _`#2365`: https://github.com/apache/cloudstack/pull/2365
.. _CLOUDSTACK-10197: https://issues.apache.org/jira/browse/CLOUDSTACK-10197
.. _`#2073`: https://github.com/apache/cloudstack/pull/2073
.. _CLOUDSTACK-9896: https://issues.apache.org/jira/browse/CLOUDSTACK-9896
.. _`#2386`: https://github.com/apache/cloudstack/pull/2386
.. _CLOUDSTACK-9632: https://issues.apache.org/jira/browse/CLOUDSTACK-9632
.. _`#2295`: https://github.com/apache/cloudstack/pull/2295
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2381`: https://github.com/apache/cloudstack/pull/2381
.. _CLOUDSTACK-10117: https://issues.apache.org/jira/browse/CLOUDSTACK-10117
.. _`#2315`: https://github.com/apache/cloudstack/pull/2315
.. _CLOUDSTACK-9025: https://issues.apache.org/jira/browse/CLOUDSTACK-9025
.. _`#2274`: https://github.com/apache/cloudstack/pull/2274
.. _CLOUDSTACK-10096: https://issues.apache.org/jira/browse/CLOUDSTACK-10096
.. _`#2282`: https://github.com/apache/cloudstack/pull/2282
.. _CLOUDSTACK-10104: https://issues.apache.org/jira/browse/CLOUDSTACK-10104
.. _`#2368`: https://github.com/apache/cloudstack/pull/2368
.. _CLOUDSTACK-10126: https://issues.apache.org/jira/browse/CLOUDSTACK-10126
.. _`#2385`: https://github.com/apache/cloudstack/pull/2385
.. _CLOUDSTACK-10211: https://issues.apache.org/jira/browse/CLOUDSTACK-10211
.. _`#2260`: https://github.com/apache/cloudstack/pull/2260
.. _CLOUDSTACK-10065: https://issues.apache.org/jira/browse/CLOUDSTACK-10065
.. _`#2292`: https://github.com/apache/cloudstack/pull/2292
.. _CLOUDSTACK-10108: https://issues.apache.org/jira/browse/CLOUDSTACK-10108
.. _`#1740`: https://github.com/apache/cloudstack/pull/1740
.. _CLOUDSTACK-9572: https://issues.apache.org/jira/browse/CLOUDSTACK-9572
.. _`#2104`: https://github.com/apache/cloudstack/pull/2104
.. _CLOUDSTACK-9908: https://issues.apache.org/jira/browse/CLOUDSTACK-9908
.. _`#2384`: https://github.com/apache/cloudstack/pull/2384
.. _CLOUDSTACK-10210: https://issues.apache.org/jira/browse/CLOUDSTACK-10210
.. _`#2378`: https://github.com/apache/cloudstack/pull/2378
.. _CLOUDSTACK-10205: https://issues.apache.org/jira/browse/CLOUDSTACK-10205
.. _`#2383`: https://github.com/apache/cloudstack/pull/2383
.. _`#1773`: https://github.com/apache/cloudstack/pull/1773
.. _CLOUDSTACK-9607: https://issues.apache.org/jira/browse/CLOUDSTACK-9607
.. _`#2046`: https://github.com/apache/cloudstack/pull/2046
.. _CLOUDSTACK-7958: https://issues.apache.org/jira/browse/CLOUDSTACK-7958
.. _`#2149`: https://github.com/apache/cloudstack/pull/2149
.. _CLOUDSTACK-9932: https://issues.apache.org/jira/browse/CLOUDSTACK-9932
.. _`#2156`: https://github.com/apache/cloudstack/pull/2156
.. _CLOUDSTACK-9971: https://issues.apache.org/jira/browse/CLOUDSTACK-9971
.. _`#2374`: https://github.com/apache/cloudstack/pull/2374
.. _CLOUDSTACK-10024: https://issues.apache.org/jira/browse/CLOUDSTACK-10024
.. _`#2373`: https://github.com/apache/cloudstack/pull/2373
.. _CLOUDSTACK-10202: https://issues.apache.org/jira/browse/CLOUDSTACK-10202
.. _`#2344`: https://github.com/apache/cloudstack/pull/2344
.. _CLOUDSTACK-10163: https://issues.apache.org/jira/browse/CLOUDSTACK-10163
.. _`#2301`: https://github.com/apache/cloudstack/pull/2301
.. _CLOUDSTACK-10121: https://issues.apache.org/jira/browse/CLOUDSTACK-10121
.. _`#1554`: https://github.com/apache/cloudstack/pull/1554
.. _CLOUDSTACK-9602: https://issues.apache.org/jira/browse/CLOUDSTACK-9602
.. _`#1760`: https://github.com/apache/cloudstack/pull/1760
.. _CLOUDSTACK-9593: https://issues.apache.org/jira/browse/CLOUDSTACK-9593
.. _`#2035`: https://github.com/apache/cloudstack/pull/2035
.. _CLOUDSTACK-9867: https://issues.apache.org/jira/browse/CLOUDSTACK-9867
.. _`#2360`: https://github.com/apache/cloudstack/pull/2360
.. _CLOUDSTACK-10189: https://issues.apache.org/jira/browse/CLOUDSTACK-10189
.. _`#2352`: https://github.com/apache/cloudstack/pull/2352
.. _CLOUDSTACK-10175: https://issues.apache.org/jira/browse/CLOUDSTACK-10175
.. _`#2045`: https://github.com/apache/cloudstack/pull/2045
.. _`#1934`: https://github.com/apache/cloudstack/pull/1934
.. _CLOUDSTACK-9772: https://issues.apache.org/jira/browse/CLOUDSTACK-9772
.. _`#2258`: https://github.com/apache/cloudstack/pull/2258
.. _`#2347`: https://github.com/apache/cloudstack/pull/2347
.. _CLOUDSTACK-10166: https://issues.apache.org/jira/browse/CLOUDSTACK-10166
.. _`#2375`: https://github.com/apache/cloudstack/pull/2375
.. _CLOUDSTACK-9456: https://issues.apache.org/jira/browse/CLOUDSTACK-9456
.. _`#2211`: https://github.com/apache/cloudstack/pull/2211
.. _CLOUDSTACK-10013: https://issues.apache.org/jira/browse/CLOUDSTACK-10013
.. _`#1637`: https://github.com/apache/cloudstack/pull/1637
.. _`#2304`: https://github.com/apache/cloudstack/pull/2304
.. _CLOUDSTACK-10127: https://issues.apache.org/jira/browse/CLOUDSTACK-10127
.. _`#2208`: https://github.com/apache/cloudstack/pull/2208
.. _CLOUDSTACK-9542: https://issues.apache.org/jira/browse/CLOUDSTACK-9542
.. _`#2351`: https://github.com/apache/cloudstack/pull/2351
.. _CLOUDSTACK-10173: https://issues.apache.org/jira/browse/CLOUDSTACK-10173
.. _`#2367`: https://github.com/apache/cloudstack/pull/2367
.. _`#2370`: https://github.com/apache/cloudstack/pull/2370
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2366`: https://github.com/apache/cloudstack/pull/2366
.. _CLOUDSTACK-10168: https://issues.apache.org/jira/browse/CLOUDSTACK-10168
.. _`#2371`: https://github.com/apache/cloudstack/pull/2371
.. _`#2042`: https://github.com/apache/cloudstack/pull/2042
.. _CLOUDSTACK-9875: https://issues.apache.org/jira/browse/CLOUDSTACK-9875
.. _`#2281`: https://github.com/apache/cloudstack/pull/2281
.. _CLOUDSTACK-10102: https://issues.apache.org/jira/browse/CLOUDSTACK-10102
.. _`#2048`: https://github.com/apache/cloudstack/pull/2048
.. _CLOUDSTACK-9880: https://issues.apache.org/jira/browse/CLOUDSTACK-9880
.. _`#2364`: https://github.com/apache/cloudstack/pull/2364
.. _CLOUDSTACK-10195: https://issues.apache.org/jira/browse/CLOUDSTACK-10195
.. _`#2361`: https://github.com/apache/cloudstack/pull/2361
.. _CLOUDSTACK-10190: https://issues.apache.org/jira/browse/CLOUDSTACK-10190
.. _`#1437`: https://github.com/apache/cloudstack/pull/1437
.. _`#2247`: https://github.com/apache/cloudstack/pull/2247
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1964`: https://github.com/apache/cloudstack/pull/1964
.. _CLOUDSTACK-9800: https://issues.apache.org/jira/browse/CLOUDSTACK-9800
.. _`#1762`: https://github.com/apache/cloudstack/pull/1762
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2348`: https://github.com/apache/cloudstack/pull/2348
.. _CLOUDSTACK-10196: https://issues.apache.org/jira/browse/CLOUDSTACK-10196
.. _`#2184`: https://github.com/apache/cloudstack/pull/2184
.. _CLOUDSTACK-10003: https://issues.apache.org/jira/browse/CLOUDSTACK-10003
.. _`#2308`: https://github.com/apache/cloudstack/pull/2308
.. _CLOUDSTACK-8908: https://issues.apache.org/jira/browse/CLOUDSTACK-8908
.. _`#2294`: https://github.com/apache/cloudstack/pull/2294
.. _CLOUDSTACK-10039: https://issues.apache.org/jira/browse/CLOUDSTACK-10039
.. _`#2346`: https://github.com/apache/cloudstack/pull/2346
.. _`#2354`: https://github.com/apache/cloudstack/pull/2354
.. _CLOUDSTACK-10176: https://issues.apache.org/jira/browse/CLOUDSTACK-10176
.. _`#2353`: https://github.com/apache/cloudstack/pull/2353
.. _CLOUDSTACK-9986: https://issues.apache.org/jira/browse/CLOUDSTACK-9986
.. _`#2359`: https://github.com/apache/cloudstack/pull/2359
.. _`#2356`: https://github.com/apache/cloudstack/pull/2356
.. _CLOUDSTACK-8313: https://issues.apache.org/jira/browse/CLOUDSTACK-8313
.. _`#2358`: https://github.com/apache/cloudstack/pull/2358
.. _CLOUDSTACK-9736: https://issues.apache.org/jira/browse/CLOUDSTACK-9736
.. _`#2326`: https://github.com/apache/cloudstack/pull/2326
.. _CLOUDSTACK-10184: https://issues.apache.org/jira/browse/CLOUDSTACK-10184
.. _`#2267`: https://github.com/apache/cloudstack/pull/2267
.. _CLOUDSTACK-10077: https://issues.apache.org/jira/browse/CLOUDSTACK-10077
.. _`#2337`: https://github.com/apache/cloudstack/pull/2337
.. _CLOUDSTACK-10157: https://issues.apache.org/jira/browse/CLOUDSTACK-10157
.. _`#2355`: https://github.com/apache/cloudstack/pull/2355
.. _CLOUDSTACK-10177: https://issues.apache.org/jira/browse/CLOUDSTACK-10177
.. _`#2349`: https://github.com/apache/cloudstack/pull/2349
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2312`: https://github.com/apache/cloudstack/pull/2312
.. _CLOUDSTACK-7793: https://issues.apache.org/jira/browse/CLOUDSTACK-7793
.. _`#2345`: https://github.com/apache/cloudstack/pull/2345
.. _CLOUDSTACK-10164: https://issues.apache.org/jira/browse/CLOUDSTACK-10164
.. _`#2263`: https://github.com/apache/cloudstack/pull/2263
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2342`: https://github.com/apache/cloudstack/pull/2342
.. _CLOUDSTACK-9586: https://issues.apache.org/jira/browse/CLOUDSTACK-9586
.. _`#2124`: https://github.com/apache/cloudstack/pull/2124
.. _CLOUDSTACK-9432: https://issues.apache.org/jira/browse/CLOUDSTACK-9432
.. _`#2322`: https://github.com/apache/cloudstack/pull/2322
.. _CLOUDSTACK-10140: https://issues.apache.org/jira/browse/CLOUDSTACK-10140
.. _`#2335`: https://github.com/apache/cloudstack/pull/2335
.. _CLOUDSTACK-10154: https://issues.apache.org/jira/browse/CLOUDSTACK-10154
.. _`#2341`: https://github.com/apache/cloudstack/pull/2341
.. _CLOUDSTACK-10160: https://issues.apache.org/jira/browse/CLOUDSTACK-10160
.. _`#2321`: https://github.com/apache/cloudstack/pull/2321
.. _CLOUDSTACK-10138: https://issues.apache.org/jira/browse/CLOUDSTACK-10138
.. _`#2334`: https://github.com/apache/cloudstack/pull/2334
.. _CLOUDSTACK-10152: https://issues.apache.org/jira/browse/CLOUDSTACK-10152
.. _`#2332`: https://github.com/apache/cloudstack/pull/2332
.. _CLOUDSTACK-10156: https://issues.apache.org/jira/browse/CLOUDSTACK-10156
.. _`#2028`: https://github.com/apache/cloudstack/pull/2028
.. _CLOUDSTACK-9853: https://issues.apache.org/jira/browse/CLOUDSTACK-9853
.. _`#2310`: https://github.com/apache/cloudstack/pull/2310
.. _CLOUDSTACK-10133: https://issues.apache.org/jira/browse/CLOUDSTACK-10133
.. _`#2219`: https://github.com/apache/cloudstack/pull/2219
.. _CLOUDSTACK-9989: https://issues.apache.org/jira/browse/CLOUDSTACK-9989
.. _`#2303`: https://github.com/apache/cloudstack/pull/2303
.. _CLOUDSTACK-10123: https://issues.apache.org/jira/browse/CLOUDSTACK-10123
.. _`#2329`: https://github.com/apache/cloudstack/pull/2329
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1981`: https://github.com/apache/cloudstack/pull/1981
.. _CLOUDSTACK-9806: https://issues.apache.org/jira/browse/CLOUDSTACK-9806
.. _`#2324`: https://github.com/apache/cloudstack/pull/2324
.. _`#2005`: https://github.com/apache/cloudstack/pull/2005
.. _CLOUDSTACK-9450: https://issues.apache.org/jira/browse/CLOUDSTACK-9450
.. _`#2327`: https://github.com/apache/cloudstack/pull/2327
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2325`: https://github.com/apache/cloudstack/pull/2325
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2316`: https://github.com/apache/cloudstack/pull/2316
.. _CLOUDSTACK-10137: https://issues.apache.org/jira/browse/CLOUDSTACK-10137
.. _`#2157`: https://github.com/apache/cloudstack/pull/2157
.. _CLOUDSTACK-9961: https://issues.apache.org/jira/browse/CLOUDSTACK-9961
.. _`#1723`: https://github.com/apache/cloudstack/pull/1723
.. _`#2306`: https://github.com/apache/cloudstack/pull/2306
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2273`: https://github.com/apache/cloudstack/pull/2273
.. _CLOUDSTACK-10090: https://issues.apache.org/jira/browse/CLOUDSTACK-10090
.. _`#2242`: https://github.com/apache/cloudstack/pull/2242
.. _CLOUDSTACK-9958: https://issues.apache.org/jira/browse/CLOUDSTACK-9958
.. _`#2307`: https://github.com/apache/cloudstack/pull/2307
.. _`#2240`: https://github.com/apache/cloudstack/pull/2240
.. _CLOUDSTACK-10051: https://issues.apache.org/jira/browse/CLOUDSTACK-10051
.. _`#2158`: https://github.com/apache/cloudstack/pull/2158
.. _CLOUDSTACK-9972: https://issues.apache.org/jira/browse/CLOUDSTACK-9972
.. _`#2291`: https://github.com/apache/cloudstack/pull/2291
.. _CLOUDSTACK-10111: https://issues.apache.org/jira/browse/CLOUDSTACK-10111
.. _`#2302`: https://github.com/apache/cloudstack/pull/2302
.. _CLOUDSTACK-10122: https://issues.apache.org/jira/browse/CLOUDSTACK-10122
.. _`#2004`: https://github.com/apache/cloudstack/pull/2004
.. _CLOUDSTACK-9832: https://issues.apache.org/jira/browse/CLOUDSTACK-9832
.. _`#2238`: https://github.com/apache/cloudstack/pull/2238
.. _CLOUDSTACK-10053: https://issues.apache.org/jira/browse/CLOUDSTACK-10053
.. _`#2250`: https://github.com/apache/cloudstack/pull/2250
.. _CLOUDSTACK-10057: https://issues.apache.org/jira/browse/CLOUDSTACK-10057
.. _`#2268`: https://github.com/apache/cloudstack/pull/2268
.. _CLOUDSTACK-10081: https://issues.apache.org/jira/browse/CLOUDSTACK-10081
.. _`#2293`: https://github.com/apache/cloudstack/pull/2293
.. _CLOUDSTACK-10047: https://issues.apache.org/jira/browse/CLOUDSTACK-10047
.. _`#2284`: https://github.com/apache/cloudstack/pull/2284
.. _CLOUDSTACK-10103: https://issues.apache.org/jira/browse/CLOUDSTACK-10103
.. _`#2288`: https://github.com/apache/cloudstack/pull/2288
.. _CLOUDSTACK-10107: https://issues.apache.org/jira/browse/CLOUDSTACK-10107
.. _`#2297`: https://github.com/apache/cloudstack/pull/2297
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2296`: https://github.com/apache/cloudstack/pull/2296
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2181`: https://github.com/apache/cloudstack/pull/2181
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2257`: https://github.com/apache/cloudstack/pull/2257
.. _CLOUDSTACK-10060: https://issues.apache.org/jira/browse/CLOUDSTACK-10060
.. _`#2286`: https://github.com/apache/cloudstack/pull/2286
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2287`: https://github.com/apache/cloudstack/pull/2287
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2246`: https://github.com/apache/cloudstack/pull/2246
.. _CLOUDSTACK-10046: https://issues.apache.org/jira/browse/CLOUDSTACK-10046
.. _`#2074`: https://github.com/apache/cloudstack/pull/2074
.. _CLOUDSTACK-9899: https://issues.apache.org/jira/browse/CLOUDSTACK-9899
.. _`#2280`: https://github.com/apache/cloudstack/pull/2280
.. _CLOUDSTACK-10101: https://issues.apache.org/jira/browse/CLOUDSTACK-10101
.. _`#2285`: https://github.com/apache/cloudstack/pull/2285
.. _CLOUDSTACK-9859: https://issues.apache.org/jira/browse/CLOUDSTACK-9859
.. _`#2278`: https://github.com/apache/cloudstack/pull/2278
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2279`: https://github.com/apache/cloudstack/pull/2279
.. _CLOUDSTACK-9584: https://issues.apache.org/jira/browse/CLOUDSTACK-9584
.. _`#2277`: https://github.com/apache/cloudstack/pull/2277
.. _CLOUDSTACK-10099: https://issues.apache.org/jira/browse/CLOUDSTACK-10099
.. _`#2266`: https://github.com/apache/cloudstack/pull/2266
.. _CLOUDSTACK-10073: https://issues.apache.org/jira/browse/CLOUDSTACK-10073
.. _`#2249`: https://github.com/apache/cloudstack/pull/2249
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#1707`: https://github.com/apache/cloudstack/pull/1707
.. _CLOUDSTACK-9397: https://issues.apache.org/jira/browse/CLOUDSTACK-9397
.. _`#2269`: https://github.com/apache/cloudstack/pull/2269
.. _CLOUDSTACK-10083: https://issues.apache.org/jira/browse/CLOUDSTACK-10083
.. _`#876`: https://github.com/apache/cloudstack/pull/876
.. _CLOUDSTACK-8865: https://issues.apache.org/jira/browse/CLOUDSTACK-8865
.. _`#1252`: https://github.com/apache/cloudstack/pull/1252
.. _CLOUDSTACK-9182: https://issues.apache.org/jira/browse/CLOUDSTACK-9182
.. _`#2153`: https://github.com/apache/cloudstack/pull/2153
.. _CLOUDSTACK-9956: https://issues.apache.org/jira/browse/CLOUDSTACK-9956
.. _`#2078`: https://github.com/apache/cloudstack/pull/2078
.. _CLOUDSTACK-9902: https://issues.apache.org/jira/browse/CLOUDSTACK-9902
.. _`#2252`: https://github.com/apache/cloudstack/pull/2252
.. _CLOUDSTACK-10067: https://issues.apache.org/jira/browse/CLOUDSTACK-10067
.. _`#2143`: https://github.com/apache/cloudstack/pull/2143
.. _CLOUDSTACK-9949: https://issues.apache.org/jira/browse/CLOUDSTACK-9949
.. _`#2248`: https://github.com/apache/cloudstack/pull/2248
.. _CLOUDSTACK-10056: https://issues.apache.org/jira/browse/CLOUDSTACK-10056
.. _`#2243`: https://github.com/apache/cloudstack/pull/2243
.. _CLOUDSTACK-10019: https://issues.apache.org/jira/browse/CLOUDSTACK-10019
.. _`#2261`: https://github.com/apache/cloudstack/pull/2261
.. _CLOUDSTACK-10068: https://issues.apache.org/jira/browse/CLOUDSTACK-10068
.. _`#2054`: https://github.com/apache/cloudstack/pull/2054
.. _CLOUDSTACK-9886: https://issues.apache.org/jira/browse/CLOUDSTACK-9886
.. _`#955`: https://github.com/apache/cloudstack/pull/955
.. _CLOUDSTACK-8969: https://issues.apache.org/jira/browse/CLOUDSTACK-8969
.. _`#2262`: https://github.com/apache/cloudstack/pull/2262
.. _CLOUDSTACK-10069: https://issues.apache.org/jira/browse/CLOUDSTACK-10069
.. _`#2256`: https://github.com/apache/cloudstack/pull/2256
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#2253`: https://github.com/apache/cloudstack/pull/2253
.. _CLOUDSTACK-10061: https://issues.apache.org/jira/browse/CLOUDSTACK-10061
.. _`#2254`: https://github.com/apache/cloudstack/pull/2254
.. _CLOUDSTACK-10058: https://issues.apache.org/jira/browse/CLOUDSTACK-10058
.. _`#1733`: https://github.com/apache/cloudstack/pull/1733
.. _CLOUDSTACK-9563: https://issues.apache.org/jira/browse/CLOUDSTACK-9563
.. _`#2188`: https://github.com/apache/cloudstack/pull/2188
.. _CLOUDSTACK-10004: https://issues.apache.org/jira/browse/CLOUDSTACK-10004
.. _`#914`: https://github.com/apache/cloudstack/pull/914
.. _CLOUDSTACK-8939: https://issues.apache.org/jira/browse/CLOUDSTACK-8939
.. _`#1985`: https://github.com/apache/cloudstack/pull/1985
.. _CLOUDSTACK-9812: https://issues.apache.org/jira/browse/CLOUDSTACK-9812
.. _`#2224`: https://github.com/apache/cloudstack/pull/2224
.. _CLOUDSTACK-10032: https://issues.apache.org/jira/browse/CLOUDSTACK-10032
.. _`#1443`: https://github.com/apache/cloudstack/pull/1443
.. _CLOUDSTACK-9314: https://issues.apache.org/jira/browse/CLOUDSTACK-9314
.. _`#2109`: https://github.com/apache/cloudstack/pull/2109
.. _CLOUDSTACK-9922: https://issues.apache.org/jira/browse/CLOUDSTACK-9922
.. _`#2216`: https://github.com/apache/cloudstack/pull/2216
.. _CLOUDSTACK-10027: https://issues.apache.org/jira/browse/CLOUDSTACK-10027
.. _`#2245`: https://github.com/apache/cloudstack/pull/2245
.. _`#2239`: https://github.com/apache/cloudstack/pull/2239
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2044`: https://github.com/apache/cloudstack/pull/2044
.. _CLOUDSTACK-9877: https://issues.apache.org/jira/browse/CLOUDSTACK-9877
.. _`#2174`: https://github.com/apache/cloudstack/pull/2174
.. _CLOUDSTACK-9996: https://issues.apache.org/jira/browse/CLOUDSTACK-9996
.. _`#2101`: https://github.com/apache/cloudstack/pull/2101
.. _CLOUDSTACK-9915: https://issues.apache.org/jira/browse/CLOUDSTACK-9915
.. _`#2123`: https://github.com/apache/cloudstack/pull/2123
.. _CLOUDSTACK-9914: https://issues.apache.org/jira/browse/CLOUDSTACK-9914
.. _`#2186`: https://github.com/apache/cloudstack/pull/2186
.. _CLOUDSTACK-10002: https://issues.apache.org/jira/browse/CLOUDSTACK-10002
.. _`#1246`: https://github.com/apache/cloudstack/pull/1246
.. _CLOUDSTACK-9165: https://issues.apache.org/jira/browse/CLOUDSTACK-9165
.. _`#2241`: https://github.com/apache/cloudstack/pull/2241
.. _CLOUDSTACK-10052: https://issues.apache.org/jira/browse/CLOUDSTACK-10052
.. _`#2222`: https://github.com/apache/cloudstack/pull/2222
.. _CLOUDSTACK-10022: https://issues.apache.org/jira/browse/CLOUDSTACK-10022
.. _`#2221`: https://github.com/apache/cloudstack/pull/2221
.. _CLOUDSTACK-10030: https://issues.apache.org/jira/browse/CLOUDSTACK-10030
.. _`#2154`: https://github.com/apache/cloudstack/pull/2154
.. _CLOUDSTACK-9967: https://issues.apache.org/jira/browse/CLOUDSTACK-9967
.. _`#1878`: https://github.com/apache/cloudstack/pull/1878
.. _CLOUDSTACK-9717: https://issues.apache.org/jira/browse/CLOUDSTACK-9717
.. _`#2013`: https://github.com/apache/cloudstack/pull/2013
.. _CLOUDSTACK-9734: https://issues.apache.org/jira/browse/CLOUDSTACK-9734
.. _`#2159`: https://github.com/apache/cloudstack/pull/2159
.. _CLOUDSTACK-9964: https://issues.apache.org/jira/browse/CLOUDSTACK-9964
.. _`#2163`: https://github.com/apache/cloudstack/pull/2163
.. _CLOUDSTACK-9939: https://issues.apache.org/jira/browse/CLOUDSTACK-9939
.. _`#1919`: https://github.com/apache/cloudstack/pull/1919
.. _CLOUDSTACK-9763: https://issues.apache.org/jira/browse/CLOUDSTACK-9763
.. _`#1936`: https://github.com/apache/cloudstack/pull/1936
.. _CLOUDSTACK-9773: https://issues.apache.org/jira/browse/CLOUDSTACK-9773
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2215`: https://github.com/apache/cloudstack/pull/2215
.. _CLOUDSTACK-10026: https://issues.apache.org/jira/browse/CLOUDSTACK-10026
.. _`#2180`: https://github.com/apache/cloudstack/pull/2180
.. _CLOUDSTACK-9999: https://issues.apache.org/jira/browse/CLOUDSTACK-9999
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2236`: https://github.com/apache/cloudstack/pull/2236
.. _CLOUDSTACK-10044: https://issues.apache.org/jira/browse/CLOUDSTACK-10044
.. _`#2235`: https://github.com/apache/cloudstack/pull/2235
.. _`#2182`: https://github.com/apache/cloudstack/pull/2182
.. _CLOUDSTACK-10000: https://issues.apache.org/jira/browse/CLOUDSTACK-10000
.. _`#2233`: https://github.com/apache/cloudstack/pull/2233
.. _CLOUDSTACK-10042: https://issues.apache.org/jira/browse/CLOUDSTACK-10042
.. _`#2228`: https://github.com/apache/cloudstack/pull/2228
.. _CLOUDSTACK-10036: https://issues.apache.org/jira/browse/CLOUDSTACK-10036
.. _`#2026`: https://github.com/apache/cloudstack/pull/2026
.. _CLOUDSTACK-9861: https://issues.apache.org/jira/browse/CLOUDSTACK-9861
.. _`#1774`: https://github.com/apache/cloudstack/pull/1774
.. _CLOUDSTACK-9608: https://issues.apache.org/jira/browse/CLOUDSTACK-9608
.. _`#2039`: https://github.com/apache/cloudstack/pull/2039
.. _`#2144`: https://github.com/apache/cloudstack/pull/2144
.. _CLOUDSTACK-9955: https://issues.apache.org/jira/browse/CLOUDSTACK-9955
.. _`#1966`: https://github.com/apache/cloudstack/pull/1966
.. _CLOUDSTACK-9801: https://issues.apache.org/jira/browse/CLOUDSTACK-9801
.. _`#2220`: https://github.com/apache/cloudstack/pull/2220
.. _CLOUDSTACK-9708: https://issues.apache.org/jira/browse/CLOUDSTACK-9708
.. _`#1912`: https://github.com/apache/cloudstack/pull/1912
.. _CLOUDSTACK-9749: https://issues.apache.org/jira/browse/CLOUDSTACK-9749
.. _`#2138`: https://github.com/apache/cloudstack/pull/2138
.. _CLOUDSTACK-9944: https://issues.apache.org/jira/browse/CLOUDSTACK-9944
.. _`#2193`: https://github.com/apache/cloudstack/pull/2193
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2218`: https://github.com/apache/cloudstack/pull/2218
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#883`: https://github.com/apache/cloudstack/pull/883
.. _CLOUDSTACK-8906: https://issues.apache.org/jira/browse/CLOUDSTACK-8906
.. _`#2119`: https://github.com/apache/cloudstack/pull/2119
.. _CLOUDSTACK-9925: https://issues.apache.org/jira/browse/CLOUDSTACK-9925
.. _`#2145`: https://github.com/apache/cloudstack/pull/2145
.. _CLOUDSTACK-9697: https://issues.apache.org/jira/browse/CLOUDSTACK-9697
.. _`#2137`: https://github.com/apache/cloudstack/pull/2137
.. _CLOUDSTACK-9950: https://issues.apache.org/jira/browse/CLOUDSTACK-9950
.. _`#2008`: https://github.com/apache/cloudstack/pull/2008
.. _CLOUDSTACK-9840: https://issues.apache.org/jira/browse/CLOUDSTACK-9840
.. _`#2094`: https://github.com/apache/cloudstack/pull/2094
.. _`#2142`: https://github.com/apache/cloudstack/pull/2142
.. _CLOUDSTACK-9954: https://issues.apache.org/jira/browse/CLOUDSTACK-9954
.. _`#2130`: https://github.com/apache/cloudstack/pull/2130
.. _CLOUDSTACK-8961: https://issues.apache.org/jira/browse/CLOUDSTACK-8961
.. _`#2212`: https://github.com/apache/cloudstack/pull/2212
.. _`#2171`: https://github.com/apache/cloudstack/pull/2171
.. _CLOUDSTACK-9990: https://issues.apache.org/jira/browse/CLOUDSTACK-9990
.. _`#2205`: https://github.com/apache/cloudstack/pull/2205
.. _`#1925`: https://github.com/apache/cloudstack/pull/1925
.. _CLOUDSTACK-9751: https://issues.apache.org/jira/browse/CLOUDSTACK-9751
.. _`#1798`: https://github.com/apache/cloudstack/pull/1798
.. _CLOUDSTACK-9631: https://issues.apache.org/jira/browse/CLOUDSTACK-9631
.. _`#2201`: https://github.com/apache/cloudstack/pull/2201
.. _CLOUDSTACK-10016: https://issues.apache.org/jira/browse/CLOUDSTACK-10016
.. _`#1784`: https://github.com/apache/cloudstack/pull/1784
.. _`#2200`: https://github.com/apache/cloudstack/pull/2200
.. _CLOUDSTACK-10015: https://issues.apache.org/jira/browse/CLOUDSTACK-10015
.. _`#1655`: https://github.com/apache/cloudstack/pull/1655
.. _`#1959`: https://github.com/apache/cloudstack/pull/1959
.. _CLOUDSTACK-9786: https://issues.apache.org/jira/browse/CLOUDSTACK-9786
.. _`#1933`: https://github.com/apache/cloudstack/pull/1933
.. _CLOUDSTACK-9569: https://issues.apache.org/jira/browse/CLOUDSTACK-9569
.. _`#2175`: https://github.com/apache/cloudstack/pull/2175
.. _`#2176`: https://github.com/apache/cloudstack/pull/2176
.. _`#2407`: https://github.com/apache/cloudstack/pull/2407
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2403`: https://github.com/apache/cloudstack/pull/2403
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2298`: https://github.com/apache/cloudstack/pull/2298
.. _CLOUDSTACK-9620: https://issues.apache.org/jira/browse/CLOUDSTACK-9620
.. _`#2396`: https://github.com/apache/cloudstack/pull/2396
.. _CLOUDSTACK-10220: https://issues.apache.org/jira/browse/CLOUDSTACK-10220
.. _`#2152`: https://github.com/apache/cloudstack/pull/2152
.. _CLOUDSTACK-10229: https://issues.apache.org/jira/browse/CLOUDSTACK-10229
.. _`#2097`: https://github.com/apache/cloudstack/pull/2097
.. _CLOUDSTACK-9813: https://issues.apache.org/jira/browse/CLOUDSTACK-9813
.. _`#2362`: https://github.com/apache/cloudstack/pull/2362
.. _CLOUDSTACK-10188: https://issues.apache.org/jira/browse/CLOUDSTACK-10188
.. _`#2146`: https://github.com/apache/cloudstack/pull/2146
.. _CLOUDSTACK-4757: https://issues.apache.org/jira/browse/CLOUDSTACK-4757
.. _`#2394`: https://github.com/apache/cloudstack/pull/2394
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2393`: https://github.com/apache/cloudstack/pull/2393
.. _CLOUDSTACK-10217: https://issues.apache.org/jira/browse/CLOUDSTACK-10217
.. _`#2350`: https://github.com/apache/cloudstack/pull/2350
.. _`#2388`: https://github.com/apache/cloudstack/pull/2388
.. _CLOUDSTACK-10212: https://issues.apache.org/jira/browse/CLOUDSTACK-10212
.. _`#2379`: https://github.com/apache/cloudstack/pull/2379
.. _CLOUDSTACK-10146: https://issues.apache.org/jira/browse/CLOUDSTACK-10146
.. _`#2389`: https://github.com/apache/cloudstack/pull/2389
.. _CLOUDSTACK-10213: https://issues.apache.org/jira/browse/CLOUDSTACK-10213
.. _`#2391`: https://github.com/apache/cloudstack/pull/2391
.. _CLOUDSTACK-10215: https://issues.apache.org/jira/browse/CLOUDSTACK-10215
.. _`#2139`: https://github.com/apache/cloudstack/pull/2139
.. _CLOUDSTACK-9921: https://issues.apache.org/jira/browse/CLOUDSTACK-9921
.. _`#2088`: https://github.com/apache/cloudstack/pull/2088
.. _CLOUDSTACK-9892: https://issues.apache.org/jira/browse/CLOUDSTACK-9892
.. _`#2365`: https://github.com/apache/cloudstack/pull/2365
.. _CLOUDSTACK-10197: https://issues.apache.org/jira/browse/CLOUDSTACK-10197
.. _`#2073`: https://github.com/apache/cloudstack/pull/2073
.. _CLOUDSTACK-9896: https://issues.apache.org/jira/browse/CLOUDSTACK-9896
.. _`#2386`: https://github.com/apache/cloudstack/pull/2386
.. _CLOUDSTACK-9632: https://issues.apache.org/jira/browse/CLOUDSTACK-9632
.. _`#2295`: https://github.com/apache/cloudstack/pull/2295
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2381`: https://github.com/apache/cloudstack/pull/2381
.. _CLOUDSTACK-10117: https://issues.apache.org/jira/browse/CLOUDSTACK-10117
.. _`#2315`: https://github.com/apache/cloudstack/pull/2315
.. _CLOUDSTACK-9025: https://issues.apache.org/jira/browse/CLOUDSTACK-9025
.. _`#2274`: https://github.com/apache/cloudstack/pull/2274
.. _CLOUDSTACK-10096: https://issues.apache.org/jira/browse/CLOUDSTACK-10096
.. _`#2282`: https://github.com/apache/cloudstack/pull/2282
.. _CLOUDSTACK-10104: https://issues.apache.org/jira/browse/CLOUDSTACK-10104
.. _`#2368`: https://github.com/apache/cloudstack/pull/2368
.. _CLOUDSTACK-10126: https://issues.apache.org/jira/browse/CLOUDSTACK-10126
.. _`#2385`: https://github.com/apache/cloudstack/pull/2385
.. _CLOUDSTACK-10211: https://issues.apache.org/jira/browse/CLOUDSTACK-10211
.. _`#2260`: https://github.com/apache/cloudstack/pull/2260
.. _CLOUDSTACK-10065: https://issues.apache.org/jira/browse/CLOUDSTACK-10065
.. _`#2292`: https://github.com/apache/cloudstack/pull/2292
.. _CLOUDSTACK-10108: https://issues.apache.org/jira/browse/CLOUDSTACK-10108
.. _`#1740`: https://github.com/apache/cloudstack/pull/1740
.. _CLOUDSTACK-9572: https://issues.apache.org/jira/browse/CLOUDSTACK-9572
.. _`#2104`: https://github.com/apache/cloudstack/pull/2104
.. _CLOUDSTACK-9908: https://issues.apache.org/jira/browse/CLOUDSTACK-9908
.. _`#2384`: https://github.com/apache/cloudstack/pull/2384
.. _CLOUDSTACK-10210: https://issues.apache.org/jira/browse/CLOUDSTACK-10210
.. _`#2378`: https://github.com/apache/cloudstack/pull/2378
.. _CLOUDSTACK-10205: https://issues.apache.org/jira/browse/CLOUDSTACK-10205
.. _`#2383`: https://github.com/apache/cloudstack/pull/2383
.. _`#1773`: https://github.com/apache/cloudstack/pull/1773
.. _CLOUDSTACK-9607: https://issues.apache.org/jira/browse/CLOUDSTACK-9607
.. _`#2046`: https://github.com/apache/cloudstack/pull/2046
.. _CLOUDSTACK-7958: https://issues.apache.org/jira/browse/CLOUDSTACK-7958
.. _`#2149`: https://github.com/apache/cloudstack/pull/2149
.. _CLOUDSTACK-9932: https://issues.apache.org/jira/browse/CLOUDSTACK-9932
.. _`#2156`: https://github.com/apache/cloudstack/pull/2156
.. _CLOUDSTACK-9971: https://issues.apache.org/jira/browse/CLOUDSTACK-9971
.. _`#2374`: https://github.com/apache/cloudstack/pull/2374
.. _CLOUDSTACK-10024: https://issues.apache.org/jira/browse/CLOUDSTACK-10024
.. _`#2373`: https://github.com/apache/cloudstack/pull/2373
.. _CLOUDSTACK-10202: https://issues.apache.org/jira/browse/CLOUDSTACK-10202
.. _`#2344`: https://github.com/apache/cloudstack/pull/2344
.. _CLOUDSTACK-10163: https://issues.apache.org/jira/browse/CLOUDSTACK-10163
.. _`#2301`: https://github.com/apache/cloudstack/pull/2301
.. _CLOUDSTACK-10121: https://issues.apache.org/jira/browse/CLOUDSTACK-10121
.. _`#1554`: https://github.com/apache/cloudstack/pull/1554
.. _CLOUDSTACK-9602: https://issues.apache.org/jira/browse/CLOUDSTACK-9602
.. _`#1760`: https://github.com/apache/cloudstack/pull/1760
.. _CLOUDSTACK-9593: https://issues.apache.org/jira/browse/CLOUDSTACK-9593
.. _`#2035`: https://github.com/apache/cloudstack/pull/2035
.. _CLOUDSTACK-9867: https://issues.apache.org/jira/browse/CLOUDSTACK-9867
.. _`#2360`: https://github.com/apache/cloudstack/pull/2360
.. _CLOUDSTACK-10189: https://issues.apache.org/jira/browse/CLOUDSTACK-10189
.. _`#2352`: https://github.com/apache/cloudstack/pull/2352
.. _CLOUDSTACK-10175: https://issues.apache.org/jira/browse/CLOUDSTACK-10175
.. _`#2045`: https://github.com/apache/cloudstack/pull/2045
.. _`#1934`: https://github.com/apache/cloudstack/pull/1934
.. _CLOUDSTACK-9772: https://issues.apache.org/jira/browse/CLOUDSTACK-9772
.. _`#2258`: https://github.com/apache/cloudstack/pull/2258
.. _`#2347`: https://github.com/apache/cloudstack/pull/2347
.. _CLOUDSTACK-10166: https://issues.apache.org/jira/browse/CLOUDSTACK-10166
.. _`#2375`: https://github.com/apache/cloudstack/pull/2375
.. _CLOUDSTACK-9456: https://issues.apache.org/jira/browse/CLOUDSTACK-9456
.. _`#2211`: https://github.com/apache/cloudstack/pull/2211
.. _CLOUDSTACK-10013: https://issues.apache.org/jira/browse/CLOUDSTACK-10013
.. _`#1637`: https://github.com/apache/cloudstack/pull/1637
.. _`#2304`: https://github.com/apache/cloudstack/pull/2304
.. _CLOUDSTACK-10127: https://issues.apache.org/jira/browse/CLOUDSTACK-10127
.. _`#2208`: https://github.com/apache/cloudstack/pull/2208
.. _CLOUDSTACK-9542: https://issues.apache.org/jira/browse/CLOUDSTACK-9542
.. _`#2351`: https://github.com/apache/cloudstack/pull/2351
.. _CLOUDSTACK-10173: https://issues.apache.org/jira/browse/CLOUDSTACK-10173
.. _`#2367`: https://github.com/apache/cloudstack/pull/2367
.. _`#2370`: https://github.com/apache/cloudstack/pull/2370
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2366`: https://github.com/apache/cloudstack/pull/2366
.. _CLOUDSTACK-10168: https://issues.apache.org/jira/browse/CLOUDSTACK-10168
.. _`#2371`: https://github.com/apache/cloudstack/pull/2371
.. _`#2042`: https://github.com/apache/cloudstack/pull/2042
.. _CLOUDSTACK-9875: https://issues.apache.org/jira/browse/CLOUDSTACK-9875
.. _`#2281`: https://github.com/apache/cloudstack/pull/2281
.. _CLOUDSTACK-10102: https://issues.apache.org/jira/browse/CLOUDSTACK-10102
.. _`#2048`: https://github.com/apache/cloudstack/pull/2048
.. _CLOUDSTACK-9880: https://issues.apache.org/jira/browse/CLOUDSTACK-9880
.. _`#2364`: https://github.com/apache/cloudstack/pull/2364
.. _CLOUDSTACK-10195: https://issues.apache.org/jira/browse/CLOUDSTACK-10195
.. _`#2361`: https://github.com/apache/cloudstack/pull/2361
.. _CLOUDSTACK-10190: https://issues.apache.org/jira/browse/CLOUDSTACK-10190
.. _`#1437`: https://github.com/apache/cloudstack/pull/1437
.. _`#2247`: https://github.com/apache/cloudstack/pull/2247
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1964`: https://github.com/apache/cloudstack/pull/1964
.. _CLOUDSTACK-9800: https://issues.apache.org/jira/browse/CLOUDSTACK-9800
.. _`#1762`: https://github.com/apache/cloudstack/pull/1762
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2348`: https://github.com/apache/cloudstack/pull/2348
.. _CLOUDSTACK-10196: https://issues.apache.org/jira/browse/CLOUDSTACK-10196
.. _`#2184`: https://github.com/apache/cloudstack/pull/2184
.. _CLOUDSTACK-10003: https://issues.apache.org/jira/browse/CLOUDSTACK-10003
.. _`#2308`: https://github.com/apache/cloudstack/pull/2308
.. _CLOUDSTACK-8908: https://issues.apache.org/jira/browse/CLOUDSTACK-8908
.. _`#2294`: https://github.com/apache/cloudstack/pull/2294
.. _CLOUDSTACK-10039: https://issues.apache.org/jira/browse/CLOUDSTACK-10039
.. _`#2346`: https://github.com/apache/cloudstack/pull/2346
.. _`#2354`: https://github.com/apache/cloudstack/pull/2354
.. _CLOUDSTACK-10176: https://issues.apache.org/jira/browse/CLOUDSTACK-10176
.. _`#2353`: https://github.com/apache/cloudstack/pull/2353
.. _CLOUDSTACK-9986: https://issues.apache.org/jira/browse/CLOUDSTACK-9986
.. _`#2359`: https://github.com/apache/cloudstack/pull/2359
.. _`#2356`: https://github.com/apache/cloudstack/pull/2356
.. _CLOUDSTACK-8313: https://issues.apache.org/jira/browse/CLOUDSTACK-8313
.. _`#2358`: https://github.com/apache/cloudstack/pull/2358
.. _CLOUDSTACK-9736: https://issues.apache.org/jira/browse/CLOUDSTACK-9736
.. _`#2326`: https://github.com/apache/cloudstack/pull/2326
.. _CLOUDSTACK-10184: https://issues.apache.org/jira/browse/CLOUDSTACK-10184
.. _`#2267`: https://github.com/apache/cloudstack/pull/2267
.. _CLOUDSTACK-10077: https://issues.apache.org/jira/browse/CLOUDSTACK-10077
.. _`#2337`: https://github.com/apache/cloudstack/pull/2337
.. _CLOUDSTACK-10157: https://issues.apache.org/jira/browse/CLOUDSTACK-10157
.. _`#2355`: https://github.com/apache/cloudstack/pull/2355
.. _CLOUDSTACK-10177: https://issues.apache.org/jira/browse/CLOUDSTACK-10177
.. _`#2349`: https://github.com/apache/cloudstack/pull/2349
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2312`: https://github.com/apache/cloudstack/pull/2312
.. _CLOUDSTACK-7793: https://issues.apache.org/jira/browse/CLOUDSTACK-7793
.. _`#2345`: https://github.com/apache/cloudstack/pull/2345
.. _CLOUDSTACK-10164: https://issues.apache.org/jira/browse/CLOUDSTACK-10164
.. _`#2263`: https://github.com/apache/cloudstack/pull/2263
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2342`: https://github.com/apache/cloudstack/pull/2342
.. _CLOUDSTACK-9586: https://issues.apache.org/jira/browse/CLOUDSTACK-9586
.. _`#2124`: https://github.com/apache/cloudstack/pull/2124
.. _CLOUDSTACK-9432: https://issues.apache.org/jira/browse/CLOUDSTACK-9432
.. _`#2322`: https://github.com/apache/cloudstack/pull/2322
.. _CLOUDSTACK-10140: https://issues.apache.org/jira/browse/CLOUDSTACK-10140
.. _`#2335`: https://github.com/apache/cloudstack/pull/2335
.. _CLOUDSTACK-10154: https://issues.apache.org/jira/browse/CLOUDSTACK-10154
.. _`#2341`: https://github.com/apache/cloudstack/pull/2341
.. _CLOUDSTACK-10160: https://issues.apache.org/jira/browse/CLOUDSTACK-10160
.. _`#2321`: https://github.com/apache/cloudstack/pull/2321
.. _CLOUDSTACK-10138: https://issues.apache.org/jira/browse/CLOUDSTACK-10138
.. _`#2334`: https://github.com/apache/cloudstack/pull/2334
.. _CLOUDSTACK-10152: https://issues.apache.org/jira/browse/CLOUDSTACK-10152
.. _`#2332`: https://github.com/apache/cloudstack/pull/2332
.. _CLOUDSTACK-10156: https://issues.apache.org/jira/browse/CLOUDSTACK-10156
.. _`#2028`: https://github.com/apache/cloudstack/pull/2028
.. _CLOUDSTACK-9853: https://issues.apache.org/jira/browse/CLOUDSTACK-9853
.. _`#2310`: https://github.com/apache/cloudstack/pull/2310
.. _CLOUDSTACK-10133: https://issues.apache.org/jira/browse/CLOUDSTACK-10133
.. _`#2219`: https://github.com/apache/cloudstack/pull/2219
.. _CLOUDSTACK-9989: https://issues.apache.org/jira/browse/CLOUDSTACK-9989
.. _`#2303`: https://github.com/apache/cloudstack/pull/2303
.. _CLOUDSTACK-10123: https://issues.apache.org/jira/browse/CLOUDSTACK-10123
.. _`#2329`: https://github.com/apache/cloudstack/pull/2329
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1981`: https://github.com/apache/cloudstack/pull/1981
.. _CLOUDSTACK-9806: https://issues.apache.org/jira/browse/CLOUDSTACK-9806
.. _`#2324`: https://github.com/apache/cloudstack/pull/2324
.. _`#2005`: https://github.com/apache/cloudstack/pull/2005
.. _CLOUDSTACK-9450: https://issues.apache.org/jira/browse/CLOUDSTACK-9450
.. _`#2327`: https://github.com/apache/cloudstack/pull/2327
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2325`: https://github.com/apache/cloudstack/pull/2325
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2316`: https://github.com/apache/cloudstack/pull/2316
.. _CLOUDSTACK-10137: https://issues.apache.org/jira/browse/CLOUDSTACK-10137
.. _`#2157`: https://github.com/apache/cloudstack/pull/2157
.. _CLOUDSTACK-9961: https://issues.apache.org/jira/browse/CLOUDSTACK-9961
.. _`#1723`: https://github.com/apache/cloudstack/pull/1723
.. _`#2306`: https://github.com/apache/cloudstack/pull/2306
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2273`: https://github.com/apache/cloudstack/pull/2273
.. _CLOUDSTACK-10090: https://issues.apache.org/jira/browse/CLOUDSTACK-10090
.. _`#2242`: https://github.com/apache/cloudstack/pull/2242
.. _CLOUDSTACK-9958: https://issues.apache.org/jira/browse/CLOUDSTACK-9958
.. _`#2307`: https://github.com/apache/cloudstack/pull/2307
.. _`#2240`: https://github.com/apache/cloudstack/pull/2240
.. _CLOUDSTACK-10051: https://issues.apache.org/jira/browse/CLOUDSTACK-10051
.. _`#2158`: https://github.com/apache/cloudstack/pull/2158
.. _CLOUDSTACK-9972: https://issues.apache.org/jira/browse/CLOUDSTACK-9972
.. _`#2291`: https://github.com/apache/cloudstack/pull/2291
.. _CLOUDSTACK-10111: https://issues.apache.org/jira/browse/CLOUDSTACK-10111
.. _`#2302`: https://github.com/apache/cloudstack/pull/2302
.. _CLOUDSTACK-10122: https://issues.apache.org/jira/browse/CLOUDSTACK-10122
.. _`#2004`: https://github.com/apache/cloudstack/pull/2004
.. _CLOUDSTACK-9832: https://issues.apache.org/jira/browse/CLOUDSTACK-9832
.. _`#2238`: https://github.com/apache/cloudstack/pull/2238
.. _CLOUDSTACK-10053: https://issues.apache.org/jira/browse/CLOUDSTACK-10053
.. _`#2250`: https://github.com/apache/cloudstack/pull/2250
.. _CLOUDSTACK-10057: https://issues.apache.org/jira/browse/CLOUDSTACK-10057
.. _`#2268`: https://github.com/apache/cloudstack/pull/2268
.. _CLOUDSTACK-10081: https://issues.apache.org/jira/browse/CLOUDSTACK-10081
.. _`#2293`: https://github.com/apache/cloudstack/pull/2293
.. _CLOUDSTACK-10047: https://issues.apache.org/jira/browse/CLOUDSTACK-10047
.. _`#2284`: https://github.com/apache/cloudstack/pull/2284
.. _CLOUDSTACK-10103: https://issues.apache.org/jira/browse/CLOUDSTACK-10103
.. _`#2288`: https://github.com/apache/cloudstack/pull/2288
.. _CLOUDSTACK-10107: https://issues.apache.org/jira/browse/CLOUDSTACK-10107
.. _`#2297`: https://github.com/apache/cloudstack/pull/2297
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2296`: https://github.com/apache/cloudstack/pull/2296
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2181`: https://github.com/apache/cloudstack/pull/2181
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2257`: https://github.com/apache/cloudstack/pull/2257
.. _CLOUDSTACK-10060: https://issues.apache.org/jira/browse/CLOUDSTACK-10060
.. _`#2286`: https://github.com/apache/cloudstack/pull/2286
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2287`: https://github.com/apache/cloudstack/pull/2287
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2246`: https://github.com/apache/cloudstack/pull/2246
.. _CLOUDSTACK-10046: https://issues.apache.org/jira/browse/CLOUDSTACK-10046
.. _`#2074`: https://github.com/apache/cloudstack/pull/2074
.. _CLOUDSTACK-9899: https://issues.apache.org/jira/browse/CLOUDSTACK-9899
.. _`#2280`: https://github.com/apache/cloudstack/pull/2280
.. _CLOUDSTACK-10101: https://issues.apache.org/jira/browse/CLOUDSTACK-10101
.. _`#2285`: https://github.com/apache/cloudstack/pull/2285
.. _CLOUDSTACK-9859: https://issues.apache.org/jira/browse/CLOUDSTACK-9859
.. _`#2278`: https://github.com/apache/cloudstack/pull/2278
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2279`: https://github.com/apache/cloudstack/pull/2279
.. _CLOUDSTACK-9584: https://issues.apache.org/jira/browse/CLOUDSTACK-9584
.. _`#2277`: https://github.com/apache/cloudstack/pull/2277
.. _CLOUDSTACK-10099: https://issues.apache.org/jira/browse/CLOUDSTACK-10099
.. _`#2266`: https://github.com/apache/cloudstack/pull/2266
.. _CLOUDSTACK-10073: https://issues.apache.org/jira/browse/CLOUDSTACK-10073
.. _`#2249`: https://github.com/apache/cloudstack/pull/2249
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#1707`: https://github.com/apache/cloudstack/pull/1707
.. _CLOUDSTACK-9397: https://issues.apache.org/jira/browse/CLOUDSTACK-9397
.. _`#2269`: https://github.com/apache/cloudstack/pull/2269
.. _CLOUDSTACK-10083: https://issues.apache.org/jira/browse/CLOUDSTACK-10083
.. _`#876`: https://github.com/apache/cloudstack/pull/876
.. _CLOUDSTACK-8865: https://issues.apache.org/jira/browse/CLOUDSTACK-8865
.. _`#1252`: https://github.com/apache/cloudstack/pull/1252
.. _CLOUDSTACK-9182: https://issues.apache.org/jira/browse/CLOUDSTACK-9182
.. _`#2153`: https://github.com/apache/cloudstack/pull/2153
.. _CLOUDSTACK-9956: https://issues.apache.org/jira/browse/CLOUDSTACK-9956
.. _`#2078`: https://github.com/apache/cloudstack/pull/2078
.. _CLOUDSTACK-9902: https://issues.apache.org/jira/browse/CLOUDSTACK-9902
.. _`#2252`: https://github.com/apache/cloudstack/pull/2252
.. _CLOUDSTACK-10067: https://issues.apache.org/jira/browse/CLOUDSTACK-10067
.. _`#2143`: https://github.com/apache/cloudstack/pull/2143
.. _CLOUDSTACK-9949: https://issues.apache.org/jira/browse/CLOUDSTACK-9949
.. _`#2248`: https://github.com/apache/cloudstack/pull/2248
.. _CLOUDSTACK-10056: https://issues.apache.org/jira/browse/CLOUDSTACK-10056
.. _`#2243`: https://github.com/apache/cloudstack/pull/2243
.. _CLOUDSTACK-10019: https://issues.apache.org/jira/browse/CLOUDSTACK-10019
.. _`#2261`: https://github.com/apache/cloudstack/pull/2261
.. _CLOUDSTACK-10068: https://issues.apache.org/jira/browse/CLOUDSTACK-10068
.. _`#2054`: https://github.com/apache/cloudstack/pull/2054
.. _CLOUDSTACK-9886: https://issues.apache.org/jira/browse/CLOUDSTACK-9886
.. _`#955`: https://github.com/apache/cloudstack/pull/955
.. _CLOUDSTACK-8969: https://issues.apache.org/jira/browse/CLOUDSTACK-8969
.. _`#2262`: https://github.com/apache/cloudstack/pull/2262
.. _CLOUDSTACK-10069: https://issues.apache.org/jira/browse/CLOUDSTACK-10069
.. _`#2256`: https://github.com/apache/cloudstack/pull/2256
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#2253`: https://github.com/apache/cloudstack/pull/2253
.. _CLOUDSTACK-10061: https://issues.apache.org/jira/browse/CLOUDSTACK-10061
.. _`#2254`: https://github.com/apache/cloudstack/pull/2254
.. _CLOUDSTACK-10058: https://issues.apache.org/jira/browse/CLOUDSTACK-10058
.. _`#1733`: https://github.com/apache/cloudstack/pull/1733
.. _CLOUDSTACK-9563: https://issues.apache.org/jira/browse/CLOUDSTACK-9563
.. _`#2188`: https://github.com/apache/cloudstack/pull/2188
.. _CLOUDSTACK-10004: https://issues.apache.org/jira/browse/CLOUDSTACK-10004
.. _`#914`: https://github.com/apache/cloudstack/pull/914
.. _CLOUDSTACK-8939: https://issues.apache.org/jira/browse/CLOUDSTACK-8939
.. _`#1985`: https://github.com/apache/cloudstack/pull/1985
.. _CLOUDSTACK-9812: https://issues.apache.org/jira/browse/CLOUDSTACK-9812
.. _`#2224`: https://github.com/apache/cloudstack/pull/2224
.. _CLOUDSTACK-10032: https://issues.apache.org/jira/browse/CLOUDSTACK-10032
.. _`#1443`: https://github.com/apache/cloudstack/pull/1443
.. _CLOUDSTACK-9314: https://issues.apache.org/jira/browse/CLOUDSTACK-9314
.. _`#2109`: https://github.com/apache/cloudstack/pull/2109
.. _CLOUDSTACK-9922: https://issues.apache.org/jira/browse/CLOUDSTACK-9922
.. _`#2216`: https://github.com/apache/cloudstack/pull/2216
.. _CLOUDSTACK-10027: https://issues.apache.org/jira/browse/CLOUDSTACK-10027
.. _`#2245`: https://github.com/apache/cloudstack/pull/2245
.. _`#2239`: https://github.com/apache/cloudstack/pull/2239
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2044`: https://github.com/apache/cloudstack/pull/2044
.. _CLOUDSTACK-9877: https://issues.apache.org/jira/browse/CLOUDSTACK-9877
.. _`#2174`: https://github.com/apache/cloudstack/pull/2174
.. _CLOUDSTACK-9996: https://issues.apache.org/jira/browse/CLOUDSTACK-9996
.. _`#2101`: https://github.com/apache/cloudstack/pull/2101
.. _CLOUDSTACK-9915: https://issues.apache.org/jira/browse/CLOUDSTACK-9915
.. _`#2123`: https://github.com/apache/cloudstack/pull/2123
.. _CLOUDSTACK-9914: https://issues.apache.org/jira/browse/CLOUDSTACK-9914
.. _`#2186`: https://github.com/apache/cloudstack/pull/2186
.. _CLOUDSTACK-10002: https://issues.apache.org/jira/browse/CLOUDSTACK-10002
.. _`#1246`: https://github.com/apache/cloudstack/pull/1246
.. _CLOUDSTACK-9165: https://issues.apache.org/jira/browse/CLOUDSTACK-9165
.. _`#2241`: https://github.com/apache/cloudstack/pull/2241
.. _CLOUDSTACK-10052: https://issues.apache.org/jira/browse/CLOUDSTACK-10052
.. _`#2222`: https://github.com/apache/cloudstack/pull/2222
.. _CLOUDSTACK-10022: https://issues.apache.org/jira/browse/CLOUDSTACK-10022
.. _`#2221`: https://github.com/apache/cloudstack/pull/2221
.. _CLOUDSTACK-10030: https://issues.apache.org/jira/browse/CLOUDSTACK-10030
.. _`#2154`: https://github.com/apache/cloudstack/pull/2154
.. _CLOUDSTACK-9967: https://issues.apache.org/jira/browse/CLOUDSTACK-9967
.. _`#1878`: https://github.com/apache/cloudstack/pull/1878
.. _CLOUDSTACK-9717: https://issues.apache.org/jira/browse/CLOUDSTACK-9717
.. _`#2013`: https://github.com/apache/cloudstack/pull/2013
.. _CLOUDSTACK-9734: https://issues.apache.org/jira/browse/CLOUDSTACK-9734
.. _`#2159`: https://github.com/apache/cloudstack/pull/2159
.. _CLOUDSTACK-9964: https://issues.apache.org/jira/browse/CLOUDSTACK-9964
.. _`#2163`: https://github.com/apache/cloudstack/pull/2163
.. _CLOUDSTACK-9939: https://issues.apache.org/jira/browse/CLOUDSTACK-9939
.. _`#1919`: https://github.com/apache/cloudstack/pull/1919
.. _CLOUDSTACK-9763: https://issues.apache.org/jira/browse/CLOUDSTACK-9763
.. _`#1936`: https://github.com/apache/cloudstack/pull/1936
.. _CLOUDSTACK-9773: https://issues.apache.org/jira/browse/CLOUDSTACK-9773
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2215`: https://github.com/apache/cloudstack/pull/2215
.. _CLOUDSTACK-10026: https://issues.apache.org/jira/browse/CLOUDSTACK-10026
.. _`#2180`: https://github.com/apache/cloudstack/pull/2180
.. _CLOUDSTACK-9999: https://issues.apache.org/jira/browse/CLOUDSTACK-9999
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2236`: https://github.com/apache/cloudstack/pull/2236
.. _CLOUDSTACK-10044: https://issues.apache.org/jira/browse/CLOUDSTACK-10044
.. _`#2235`: https://github.com/apache/cloudstack/pull/2235
.. _`#2182`: https://github.com/apache/cloudstack/pull/2182
.. _CLOUDSTACK-10000: https://issues.apache.org/jira/browse/CLOUDSTACK-10000
.. _`#2233`: https://github.com/apache/cloudstack/pull/2233
.. _CLOUDSTACK-10042: https://issues.apache.org/jira/browse/CLOUDSTACK-10042
.. _`#2228`: https://github.com/apache/cloudstack/pull/2228
.. _CLOUDSTACK-10036: https://issues.apache.org/jira/browse/CLOUDSTACK-10036
.. _`#2026`: https://github.com/apache/cloudstack/pull/2026
.. _CLOUDSTACK-9861: https://issues.apache.org/jira/browse/CLOUDSTACK-9861
.. _`#1774`: https://github.com/apache/cloudstack/pull/1774
.. _CLOUDSTACK-9608: https://issues.apache.org/jira/browse/CLOUDSTACK-9608
.. _`#2039`: https://github.com/apache/cloudstack/pull/2039
.. _`#2144`: https://github.com/apache/cloudstack/pull/2144
.. _CLOUDSTACK-9955: https://issues.apache.org/jira/browse/CLOUDSTACK-9955
.. _`#1966`: https://github.com/apache/cloudstack/pull/1966
.. _CLOUDSTACK-9801: https://issues.apache.org/jira/browse/CLOUDSTACK-9801
.. _`#2220`: https://github.com/apache/cloudstack/pull/2220
.. _CLOUDSTACK-9708: https://issues.apache.org/jira/browse/CLOUDSTACK-9708
.. _`#1912`: https://github.com/apache/cloudstack/pull/1912
.. _CLOUDSTACK-9749: https://issues.apache.org/jira/browse/CLOUDSTACK-9749
.. _`#2138`: https://github.com/apache/cloudstack/pull/2138
.. _CLOUDSTACK-9944: https://issues.apache.org/jira/browse/CLOUDSTACK-9944
.. _`#2193`: https://github.com/apache/cloudstack/pull/2193
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2218`: https://github.com/apache/cloudstack/pull/2218
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#883`: https://github.com/apache/cloudstack/pull/883
.. _CLOUDSTACK-8906: https://issues.apache.org/jira/browse/CLOUDSTACK-8906
.. _`#2119`: https://github.com/apache/cloudstack/pull/2119
.. _CLOUDSTACK-9925: https://issues.apache.org/jira/browse/CLOUDSTACK-9925
.. _`#2145`: https://github.com/apache/cloudstack/pull/2145
.. _CLOUDSTACK-9697: https://issues.apache.org/jira/browse/CLOUDSTACK-9697
.. _`#2137`: https://github.com/apache/cloudstack/pull/2137
.. _CLOUDSTACK-9950: https://issues.apache.org/jira/browse/CLOUDSTACK-9950
.. _`#2008`: https://github.com/apache/cloudstack/pull/2008
.. _CLOUDSTACK-9840: https://issues.apache.org/jira/browse/CLOUDSTACK-9840
.. _`#2094`: https://github.com/apache/cloudstack/pull/2094
.. _`#2142`: https://github.com/apache/cloudstack/pull/2142
.. _CLOUDSTACK-9954: https://issues.apache.org/jira/browse/CLOUDSTACK-9954
.. _`#2130`: https://github.com/apache/cloudstack/pull/2130
.. _CLOUDSTACK-8961: https://issues.apache.org/jira/browse/CLOUDSTACK-8961
.. _`#2212`: https://github.com/apache/cloudstack/pull/2212
.. _`#2171`: https://github.com/apache/cloudstack/pull/2171
.. _CLOUDSTACK-9990: https://issues.apache.org/jira/browse/CLOUDSTACK-9990
.. _`#2205`: https://github.com/apache/cloudstack/pull/2205
.. _`#1925`: https://github.com/apache/cloudstack/pull/1925
.. _CLOUDSTACK-9751: https://issues.apache.org/jira/browse/CLOUDSTACK-9751
.. _`#1798`: https://github.com/apache/cloudstack/pull/1798
.. _CLOUDSTACK-9631: https://issues.apache.org/jira/browse/CLOUDSTACK-9631
.. _`#2201`: https://github.com/apache/cloudstack/pull/2201
.. _CLOUDSTACK-10016: https://issues.apache.org/jira/browse/CLOUDSTACK-10016
.. _`#1784`: https://github.com/apache/cloudstack/pull/1784
.. _`#2200`: https://github.com/apache/cloudstack/pull/2200
.. _CLOUDSTACK-10015: https://issues.apache.org/jira/browse/CLOUDSTACK-10015
.. _`#1655`: https://github.com/apache/cloudstack/pull/1655
.. _`#1959`: https://github.com/apache/cloudstack/pull/1959
.. _CLOUDSTACK-9786: https://issues.apache.org/jira/browse/CLOUDSTACK-9786
.. _`#1933`: https://github.com/apache/cloudstack/pull/1933
.. _CLOUDSTACK-9569: https://issues.apache.org/jira/browse/CLOUDSTACK-9569
.. _`#2175`: https://github.com/apache/cloudstack/pull/2175
.. _`#2176`: https://github.com/apache/cloudstack/pull/2176
.. _`#2407`: https://github.com/apache/cloudstack/pull/2407
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2403`: https://github.com/apache/cloudstack/pull/2403
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2298`: https://github.com/apache/cloudstack/pull/2298
.. _CLOUDSTACK-9620: https://issues.apache.org/jira/browse/CLOUDSTACK-9620
.. _`#2396`: https://github.com/apache/cloudstack/pull/2396
.. _CLOUDSTACK-10220: https://issues.apache.org/jira/browse/CLOUDSTACK-10220
.. _`#2152`: https://github.com/apache/cloudstack/pull/2152
.. _CLOUDSTACK-10229: https://issues.apache.org/jira/browse/CLOUDSTACK-10229
.. _`#2097`: https://github.com/apache/cloudstack/pull/2097
.. _CLOUDSTACK-9813: https://issues.apache.org/jira/browse/CLOUDSTACK-9813
.. _`#2362`: https://github.com/apache/cloudstack/pull/2362
.. _CLOUDSTACK-10188: https://issues.apache.org/jira/browse/CLOUDSTACK-10188
.. _`#2146`: https://github.com/apache/cloudstack/pull/2146
.. _CLOUDSTACK-4757: https://issues.apache.org/jira/browse/CLOUDSTACK-4757
.. _`#2394`: https://github.com/apache/cloudstack/pull/2394
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2393`: https://github.com/apache/cloudstack/pull/2393
.. _CLOUDSTACK-10217: https://issues.apache.org/jira/browse/CLOUDSTACK-10217
.. _`#2350`: https://github.com/apache/cloudstack/pull/2350
.. _`#2388`: https://github.com/apache/cloudstack/pull/2388
.. _CLOUDSTACK-10212: https://issues.apache.org/jira/browse/CLOUDSTACK-10212
.. _`#2379`: https://github.com/apache/cloudstack/pull/2379
.. _CLOUDSTACK-10146: https://issues.apache.org/jira/browse/CLOUDSTACK-10146
.. _`#2389`: https://github.com/apache/cloudstack/pull/2389
.. _CLOUDSTACK-10213: https://issues.apache.org/jira/browse/CLOUDSTACK-10213
.. _`#2391`: https://github.com/apache/cloudstack/pull/2391
.. _CLOUDSTACK-10215: https://issues.apache.org/jira/browse/CLOUDSTACK-10215
.. _`#2139`: https://github.com/apache/cloudstack/pull/2139
.. _CLOUDSTACK-9921: https://issues.apache.org/jira/browse/CLOUDSTACK-9921
.. _`#2088`: https://github.com/apache/cloudstack/pull/2088
.. _CLOUDSTACK-9892: https://issues.apache.org/jira/browse/CLOUDSTACK-9892
.. _`#2365`: https://github.com/apache/cloudstack/pull/2365
.. _CLOUDSTACK-10197: https://issues.apache.org/jira/browse/CLOUDSTACK-10197
.. _`#2073`: https://github.com/apache/cloudstack/pull/2073
.. _CLOUDSTACK-9896: https://issues.apache.org/jira/browse/CLOUDSTACK-9896
.. _`#2386`: https://github.com/apache/cloudstack/pull/2386
.. _CLOUDSTACK-9632: https://issues.apache.org/jira/browse/CLOUDSTACK-9632
.. _`#2295`: https://github.com/apache/cloudstack/pull/2295
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2381`: https://github.com/apache/cloudstack/pull/2381
.. _CLOUDSTACK-10117: https://issues.apache.org/jira/browse/CLOUDSTACK-10117
.. _`#2315`: https://github.com/apache/cloudstack/pull/2315
.. _CLOUDSTACK-9025: https://issues.apache.org/jira/browse/CLOUDSTACK-9025
.. _`#2274`: https://github.com/apache/cloudstack/pull/2274
.. _CLOUDSTACK-10096: https://issues.apache.org/jira/browse/CLOUDSTACK-10096
.. _`#2282`: https://github.com/apache/cloudstack/pull/2282
.. _CLOUDSTACK-10104: https://issues.apache.org/jira/browse/CLOUDSTACK-10104
.. _`#2368`: https://github.com/apache/cloudstack/pull/2368
.. _CLOUDSTACK-10126: https://issues.apache.org/jira/browse/CLOUDSTACK-10126
.. _`#2385`: https://github.com/apache/cloudstack/pull/2385
.. _CLOUDSTACK-10211: https://issues.apache.org/jira/browse/CLOUDSTACK-10211
.. _`#2260`: https://github.com/apache/cloudstack/pull/2260
.. _CLOUDSTACK-10065: https://issues.apache.org/jira/browse/CLOUDSTACK-10065
.. _`#2292`: https://github.com/apache/cloudstack/pull/2292
.. _CLOUDSTACK-10108: https://issues.apache.org/jira/browse/CLOUDSTACK-10108
.. _`#1740`: https://github.com/apache/cloudstack/pull/1740
.. _CLOUDSTACK-9572: https://issues.apache.org/jira/browse/CLOUDSTACK-9572
.. _`#2104`: https://github.com/apache/cloudstack/pull/2104
.. _CLOUDSTACK-9908: https://issues.apache.org/jira/browse/CLOUDSTACK-9908
.. _`#2384`: https://github.com/apache/cloudstack/pull/2384
.. _CLOUDSTACK-10210: https://issues.apache.org/jira/browse/CLOUDSTACK-10210
.. _`#2378`: https://github.com/apache/cloudstack/pull/2378
.. _CLOUDSTACK-10205: https://issues.apache.org/jira/browse/CLOUDSTACK-10205
.. _`#2383`: https://github.com/apache/cloudstack/pull/2383
.. _`#1773`: https://github.com/apache/cloudstack/pull/1773
.. _CLOUDSTACK-9607: https://issues.apache.org/jira/browse/CLOUDSTACK-9607
.. _`#2046`: https://github.com/apache/cloudstack/pull/2046
.. _CLOUDSTACK-7958: https://issues.apache.org/jira/browse/CLOUDSTACK-7958
.. _`#2149`: https://github.com/apache/cloudstack/pull/2149
.. _CLOUDSTACK-9932: https://issues.apache.org/jira/browse/CLOUDSTACK-9932
.. _`#2156`: https://github.com/apache/cloudstack/pull/2156
.. _CLOUDSTACK-9971: https://issues.apache.org/jira/browse/CLOUDSTACK-9971
.. _`#2374`: https://github.com/apache/cloudstack/pull/2374
.. _CLOUDSTACK-10024: https://issues.apache.org/jira/browse/CLOUDSTACK-10024
.. _`#2373`: https://github.com/apache/cloudstack/pull/2373
.. _CLOUDSTACK-10202: https://issues.apache.org/jira/browse/CLOUDSTACK-10202
.. _`#2344`: https://github.com/apache/cloudstack/pull/2344
.. _CLOUDSTACK-10163: https://issues.apache.org/jira/browse/CLOUDSTACK-10163
.. _`#2301`: https://github.com/apache/cloudstack/pull/2301
.. _CLOUDSTACK-10121: https://issues.apache.org/jira/browse/CLOUDSTACK-10121
.. _`#1554`: https://github.com/apache/cloudstack/pull/1554
.. _CLOUDSTACK-9602: https://issues.apache.org/jira/browse/CLOUDSTACK-9602
.. _`#1760`: https://github.com/apache/cloudstack/pull/1760
.. _CLOUDSTACK-9593: https://issues.apache.org/jira/browse/CLOUDSTACK-9593
.. _`#2035`: https://github.com/apache/cloudstack/pull/2035
.. _CLOUDSTACK-9867: https://issues.apache.org/jira/browse/CLOUDSTACK-9867
.. _`#2360`: https://github.com/apache/cloudstack/pull/2360
.. _CLOUDSTACK-10189: https://issues.apache.org/jira/browse/CLOUDSTACK-10189
.. _`#2352`: https://github.com/apache/cloudstack/pull/2352
.. _CLOUDSTACK-10175: https://issues.apache.org/jira/browse/CLOUDSTACK-10175
.. _`#2045`: https://github.com/apache/cloudstack/pull/2045
.. _`#1934`: https://github.com/apache/cloudstack/pull/1934
.. _CLOUDSTACK-9772: https://issues.apache.org/jira/browse/CLOUDSTACK-9772
.. _`#2258`: https://github.com/apache/cloudstack/pull/2258
.. _`#2347`: https://github.com/apache/cloudstack/pull/2347
.. _CLOUDSTACK-10166: https://issues.apache.org/jira/browse/CLOUDSTACK-10166
.. _`#2375`: https://github.com/apache/cloudstack/pull/2375
.. _CLOUDSTACK-9456: https://issues.apache.org/jira/browse/CLOUDSTACK-9456
.. _`#2211`: https://github.com/apache/cloudstack/pull/2211
.. _CLOUDSTACK-10013: https://issues.apache.org/jira/browse/CLOUDSTACK-10013
.. _`#1637`: https://github.com/apache/cloudstack/pull/1637
.. _`#2304`: https://github.com/apache/cloudstack/pull/2304
.. _CLOUDSTACK-10127: https://issues.apache.org/jira/browse/CLOUDSTACK-10127
.. _`#2208`: https://github.com/apache/cloudstack/pull/2208
.. _CLOUDSTACK-9542: https://issues.apache.org/jira/browse/CLOUDSTACK-9542
.. _`#2351`: https://github.com/apache/cloudstack/pull/2351
.. _CLOUDSTACK-10173: https://issues.apache.org/jira/browse/CLOUDSTACK-10173
.. _`#2367`: https://github.com/apache/cloudstack/pull/2367
.. _`#2370`: https://github.com/apache/cloudstack/pull/2370
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2366`: https://github.com/apache/cloudstack/pull/2366
.. _CLOUDSTACK-10168: https://issues.apache.org/jira/browse/CLOUDSTACK-10168
.. _`#2371`: https://github.com/apache/cloudstack/pull/2371
.. _`#2042`: https://github.com/apache/cloudstack/pull/2042
.. _CLOUDSTACK-9875: https://issues.apache.org/jira/browse/CLOUDSTACK-9875
.. _`#2281`: https://github.com/apache/cloudstack/pull/2281
.. _CLOUDSTACK-10102: https://issues.apache.org/jira/browse/CLOUDSTACK-10102
.. _`#2048`: https://github.com/apache/cloudstack/pull/2048
.. _CLOUDSTACK-9880: https://issues.apache.org/jira/browse/CLOUDSTACK-9880
.. _`#2364`: https://github.com/apache/cloudstack/pull/2364
.. _CLOUDSTACK-10195: https://issues.apache.org/jira/browse/CLOUDSTACK-10195
.. _`#2361`: https://github.com/apache/cloudstack/pull/2361
.. _CLOUDSTACK-10190: https://issues.apache.org/jira/browse/CLOUDSTACK-10190
.. _`#1437`: https://github.com/apache/cloudstack/pull/1437
.. _`#2247`: https://github.com/apache/cloudstack/pull/2247
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1964`: https://github.com/apache/cloudstack/pull/1964
.. _CLOUDSTACK-9800: https://issues.apache.org/jira/browse/CLOUDSTACK-9800
.. _`#1762`: https://github.com/apache/cloudstack/pull/1762
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2348`: https://github.com/apache/cloudstack/pull/2348
.. _CLOUDSTACK-10196: https://issues.apache.org/jira/browse/CLOUDSTACK-10196
.. _`#2184`: https://github.com/apache/cloudstack/pull/2184
.. _CLOUDSTACK-10003: https://issues.apache.org/jira/browse/CLOUDSTACK-10003
.. _`#2308`: https://github.com/apache/cloudstack/pull/2308
.. _CLOUDSTACK-8908: https://issues.apache.org/jira/browse/CLOUDSTACK-8908
.. _`#2294`: https://github.com/apache/cloudstack/pull/2294
.. _CLOUDSTACK-10039: https://issues.apache.org/jira/browse/CLOUDSTACK-10039
.. _`#2346`: https://github.com/apache/cloudstack/pull/2346
.. _`#2354`: https://github.com/apache/cloudstack/pull/2354
.. _CLOUDSTACK-10176: https://issues.apache.org/jira/browse/CLOUDSTACK-10176
.. _`#2353`: https://github.com/apache/cloudstack/pull/2353
.. _CLOUDSTACK-9986: https://issues.apache.org/jira/browse/CLOUDSTACK-9986
.. _`#2359`: https://github.com/apache/cloudstack/pull/2359
.. _`#2356`: https://github.com/apache/cloudstack/pull/2356
.. _CLOUDSTACK-8313: https://issues.apache.org/jira/browse/CLOUDSTACK-8313
.. _`#2358`: https://github.com/apache/cloudstack/pull/2358
.. _CLOUDSTACK-9736: https://issues.apache.org/jira/browse/CLOUDSTACK-9736
.. _`#2326`: https://github.com/apache/cloudstack/pull/2326
.. _CLOUDSTACK-10184: https://issues.apache.org/jira/browse/CLOUDSTACK-10184
.. _`#2267`: https://github.com/apache/cloudstack/pull/2267
.. _CLOUDSTACK-10077: https://issues.apache.org/jira/browse/CLOUDSTACK-10077
.. _`#2337`: https://github.com/apache/cloudstack/pull/2337
.. _CLOUDSTACK-10157: https://issues.apache.org/jira/browse/CLOUDSTACK-10157
.. _`#2355`: https://github.com/apache/cloudstack/pull/2355
.. _CLOUDSTACK-10177: https://issues.apache.org/jira/browse/CLOUDSTACK-10177
.. _`#2349`: https://github.com/apache/cloudstack/pull/2349
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2312`: https://github.com/apache/cloudstack/pull/2312
.. _CLOUDSTACK-7793: https://issues.apache.org/jira/browse/CLOUDSTACK-7793
.. _`#2345`: https://github.com/apache/cloudstack/pull/2345
.. _CLOUDSTACK-10164: https://issues.apache.org/jira/browse/CLOUDSTACK-10164
.. _`#2263`: https://github.com/apache/cloudstack/pull/2263
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2342`: https://github.com/apache/cloudstack/pull/2342
.. _CLOUDSTACK-9586: https://issues.apache.org/jira/browse/CLOUDSTACK-9586
.. _`#2124`: https://github.com/apache/cloudstack/pull/2124
.. _CLOUDSTACK-9432: https://issues.apache.org/jira/browse/CLOUDSTACK-9432
.. _`#2322`: https://github.com/apache/cloudstack/pull/2322
.. _CLOUDSTACK-10140: https://issues.apache.org/jira/browse/CLOUDSTACK-10140
.. _`#2335`: https://github.com/apache/cloudstack/pull/2335
.. _CLOUDSTACK-10154: https://issues.apache.org/jira/browse/CLOUDSTACK-10154
.. _`#2341`: https://github.com/apache/cloudstack/pull/2341
.. _CLOUDSTACK-10160: https://issues.apache.org/jira/browse/CLOUDSTACK-10160
.. _`#2321`: https://github.com/apache/cloudstack/pull/2321
.. _CLOUDSTACK-10138: https://issues.apache.org/jira/browse/CLOUDSTACK-10138
.. _`#2334`: https://github.com/apache/cloudstack/pull/2334
.. _CLOUDSTACK-10152: https://issues.apache.org/jira/browse/CLOUDSTACK-10152
.. _`#2332`: https://github.com/apache/cloudstack/pull/2332
.. _CLOUDSTACK-10156: https://issues.apache.org/jira/browse/CLOUDSTACK-10156
.. _`#2028`: https://github.com/apache/cloudstack/pull/2028
.. _CLOUDSTACK-9853: https://issues.apache.org/jira/browse/CLOUDSTACK-9853
.. _`#2310`: https://github.com/apache/cloudstack/pull/2310
.. _CLOUDSTACK-10133: https://issues.apache.org/jira/browse/CLOUDSTACK-10133
.. _`#2219`: https://github.com/apache/cloudstack/pull/2219
.. _CLOUDSTACK-9989: https://issues.apache.org/jira/browse/CLOUDSTACK-9989
.. _`#2303`: https://github.com/apache/cloudstack/pull/2303
.. _CLOUDSTACK-10123: https://issues.apache.org/jira/browse/CLOUDSTACK-10123
.. _`#2329`: https://github.com/apache/cloudstack/pull/2329
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1981`: https://github.com/apache/cloudstack/pull/1981
.. _CLOUDSTACK-9806: https://issues.apache.org/jira/browse/CLOUDSTACK-9806
.. _`#2324`: https://github.com/apache/cloudstack/pull/2324
.. _`#2005`: https://github.com/apache/cloudstack/pull/2005
.. _CLOUDSTACK-9450: https://issues.apache.org/jira/browse/CLOUDSTACK-9450
.. _`#2327`: https://github.com/apache/cloudstack/pull/2327
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2325`: https://github.com/apache/cloudstack/pull/2325
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2316`: https://github.com/apache/cloudstack/pull/2316
.. _CLOUDSTACK-10137: https://issues.apache.org/jira/browse/CLOUDSTACK-10137
.. _`#2157`: https://github.com/apache/cloudstack/pull/2157
.. _CLOUDSTACK-9961: https://issues.apache.org/jira/browse/CLOUDSTACK-9961
.. _`#1723`: https://github.com/apache/cloudstack/pull/1723
.. _`#2306`: https://github.com/apache/cloudstack/pull/2306
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2273`: https://github.com/apache/cloudstack/pull/2273
.. _CLOUDSTACK-10090: https://issues.apache.org/jira/browse/CLOUDSTACK-10090
.. _`#2242`: https://github.com/apache/cloudstack/pull/2242
.. _CLOUDSTACK-9958: https://issues.apache.org/jira/browse/CLOUDSTACK-9958
.. _`#2307`: https://github.com/apache/cloudstack/pull/2307
.. _`#2240`: https://github.com/apache/cloudstack/pull/2240
.. _CLOUDSTACK-10051: https://issues.apache.org/jira/browse/CLOUDSTACK-10051
.. _`#2158`: https://github.com/apache/cloudstack/pull/2158
.. _CLOUDSTACK-9972: https://issues.apache.org/jira/browse/CLOUDSTACK-9972
.. _`#2291`: https://github.com/apache/cloudstack/pull/2291
.. _CLOUDSTACK-10111: https://issues.apache.org/jira/browse/CLOUDSTACK-10111
.. _`#2302`: https://github.com/apache/cloudstack/pull/2302
.. _CLOUDSTACK-10122: https://issues.apache.org/jira/browse/CLOUDSTACK-10122
.. _`#2004`: https://github.com/apache/cloudstack/pull/2004
.. _CLOUDSTACK-9832: https://issues.apache.org/jira/browse/CLOUDSTACK-9832
.. _`#2238`: https://github.com/apache/cloudstack/pull/2238
.. _CLOUDSTACK-10053: https://issues.apache.org/jira/browse/CLOUDSTACK-10053
.. _`#2250`: https://github.com/apache/cloudstack/pull/2250
.. _CLOUDSTACK-10057: https://issues.apache.org/jira/browse/CLOUDSTACK-10057
.. _`#2268`: https://github.com/apache/cloudstack/pull/2268
.. _CLOUDSTACK-10081: https://issues.apache.org/jira/browse/CLOUDSTACK-10081
.. _`#2293`: https://github.com/apache/cloudstack/pull/2293
.. _CLOUDSTACK-10047: https://issues.apache.org/jira/browse/CLOUDSTACK-10047
.. _`#2284`: https://github.com/apache/cloudstack/pull/2284
.. _CLOUDSTACK-10103: https://issues.apache.org/jira/browse/CLOUDSTACK-10103
.. _`#2288`: https://github.com/apache/cloudstack/pull/2288
.. _CLOUDSTACK-10107: https://issues.apache.org/jira/browse/CLOUDSTACK-10107
.. _`#2297`: https://github.com/apache/cloudstack/pull/2297
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2296`: https://github.com/apache/cloudstack/pull/2296
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2181`: https://github.com/apache/cloudstack/pull/2181
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2257`: https://github.com/apache/cloudstack/pull/2257
.. _CLOUDSTACK-10060: https://issues.apache.org/jira/browse/CLOUDSTACK-10060
.. _`#2286`: https://github.com/apache/cloudstack/pull/2286
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2287`: https://github.com/apache/cloudstack/pull/2287
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2246`: https://github.com/apache/cloudstack/pull/2246
.. _CLOUDSTACK-10046: https://issues.apache.org/jira/browse/CLOUDSTACK-10046
.. _`#2074`: https://github.com/apache/cloudstack/pull/2074
.. _CLOUDSTACK-9899: https://issues.apache.org/jira/browse/CLOUDSTACK-9899
.. _`#2280`: https://github.com/apache/cloudstack/pull/2280
.. _CLOUDSTACK-10101: https://issues.apache.org/jira/browse/CLOUDSTACK-10101
.. _`#2285`: https://github.com/apache/cloudstack/pull/2285
.. _CLOUDSTACK-9859: https://issues.apache.org/jira/browse/CLOUDSTACK-9859
.. _`#2278`: https://github.com/apache/cloudstack/pull/2278
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2279`: https://github.com/apache/cloudstack/pull/2279
.. _CLOUDSTACK-9584: https://issues.apache.org/jira/browse/CLOUDSTACK-9584
.. _`#2277`: https://github.com/apache/cloudstack/pull/2277
.. _CLOUDSTACK-10099: https://issues.apache.org/jira/browse/CLOUDSTACK-10099
.. _`#2266`: https://github.com/apache/cloudstack/pull/2266
.. _CLOUDSTACK-10073: https://issues.apache.org/jira/browse/CLOUDSTACK-10073
.. _`#2249`: https://github.com/apache/cloudstack/pull/2249
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#1707`: https://github.com/apache/cloudstack/pull/1707
.. _CLOUDSTACK-9397: https://issues.apache.org/jira/browse/CLOUDSTACK-9397
.. _`#2269`: https://github.com/apache/cloudstack/pull/2269
.. _CLOUDSTACK-10083: https://issues.apache.org/jira/browse/CLOUDSTACK-10083
.. _`#876`: https://github.com/apache/cloudstack/pull/876
.. _CLOUDSTACK-8865: https://issues.apache.org/jira/browse/CLOUDSTACK-8865
.. _`#1252`: https://github.com/apache/cloudstack/pull/1252
.. _CLOUDSTACK-9182: https://issues.apache.org/jira/browse/CLOUDSTACK-9182
.. _`#2153`: https://github.com/apache/cloudstack/pull/2153
.. _CLOUDSTACK-9956: https://issues.apache.org/jira/browse/CLOUDSTACK-9956
.. _`#2078`: https://github.com/apache/cloudstack/pull/2078
.. _CLOUDSTACK-9902: https://issues.apache.org/jira/browse/CLOUDSTACK-9902
.. _`#2252`: https://github.com/apache/cloudstack/pull/2252
.. _CLOUDSTACK-10067: https://issues.apache.org/jira/browse/CLOUDSTACK-10067
.. _`#2143`: https://github.com/apache/cloudstack/pull/2143
.. _CLOUDSTACK-9949: https://issues.apache.org/jira/browse/CLOUDSTACK-9949
.. _`#2248`: https://github.com/apache/cloudstack/pull/2248
.. _CLOUDSTACK-10056: https://issues.apache.org/jira/browse/CLOUDSTACK-10056
.. _`#2243`: https://github.com/apache/cloudstack/pull/2243
.. _CLOUDSTACK-10019: https://issues.apache.org/jira/browse/CLOUDSTACK-10019
.. _`#2261`: https://github.com/apache/cloudstack/pull/2261
.. _CLOUDSTACK-10068: https://issues.apache.org/jira/browse/CLOUDSTACK-10068
.. _`#2054`: https://github.com/apache/cloudstack/pull/2054
.. _CLOUDSTACK-9886: https://issues.apache.org/jira/browse/CLOUDSTACK-9886
.. _`#955`: https://github.com/apache/cloudstack/pull/955
.. _CLOUDSTACK-8969: https://issues.apache.org/jira/browse/CLOUDSTACK-8969
.. _`#2262`: https://github.com/apache/cloudstack/pull/2262
.. _CLOUDSTACK-10069: https://issues.apache.org/jira/browse/CLOUDSTACK-10069
.. _`#2256`: https://github.com/apache/cloudstack/pull/2256
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#2253`: https://github.com/apache/cloudstack/pull/2253
.. _CLOUDSTACK-10061: https://issues.apache.org/jira/browse/CLOUDSTACK-10061
.. _`#2254`: https://github.com/apache/cloudstack/pull/2254
.. _CLOUDSTACK-10058: https://issues.apache.org/jira/browse/CLOUDSTACK-10058
.. _`#1733`: https://github.com/apache/cloudstack/pull/1733
.. _CLOUDSTACK-9563: https://issues.apache.org/jira/browse/CLOUDSTACK-9563
.. _`#2188`: https://github.com/apache/cloudstack/pull/2188
.. _CLOUDSTACK-10004: https://issues.apache.org/jira/browse/CLOUDSTACK-10004
.. _`#914`: https://github.com/apache/cloudstack/pull/914
.. _CLOUDSTACK-8939: https://issues.apache.org/jira/browse/CLOUDSTACK-8939
.. _`#1985`: https://github.com/apache/cloudstack/pull/1985
.. _CLOUDSTACK-9812: https://issues.apache.org/jira/browse/CLOUDSTACK-9812
.. _`#2224`: https://github.com/apache/cloudstack/pull/2224
.. _CLOUDSTACK-10032: https://issues.apache.org/jira/browse/CLOUDSTACK-10032
.. _`#1443`: https://github.com/apache/cloudstack/pull/1443
.. _CLOUDSTACK-9314: https://issues.apache.org/jira/browse/CLOUDSTACK-9314
.. _`#2109`: https://github.com/apache/cloudstack/pull/2109
.. _CLOUDSTACK-9922: https://issues.apache.org/jira/browse/CLOUDSTACK-9922
.. _`#2216`: https://github.com/apache/cloudstack/pull/2216
.. _CLOUDSTACK-10027: https://issues.apache.org/jira/browse/CLOUDSTACK-10027
.. _`#2245`: https://github.com/apache/cloudstack/pull/2245
.. _`#2239`: https://github.com/apache/cloudstack/pull/2239
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2044`: https://github.com/apache/cloudstack/pull/2044
.. _CLOUDSTACK-9877: https://issues.apache.org/jira/browse/CLOUDSTACK-9877
.. _`#2174`: https://github.com/apache/cloudstack/pull/2174
.. _CLOUDSTACK-9996: https://issues.apache.org/jira/browse/CLOUDSTACK-9996
.. _`#2101`: https://github.com/apache/cloudstack/pull/2101
.. _CLOUDSTACK-9915: https://issues.apache.org/jira/browse/CLOUDSTACK-9915
.. _`#2123`: https://github.com/apache/cloudstack/pull/2123
.. _CLOUDSTACK-9914: https://issues.apache.org/jira/browse/CLOUDSTACK-9914
.. _`#2186`: https://github.com/apache/cloudstack/pull/2186
.. _CLOUDSTACK-10002: https://issues.apache.org/jira/browse/CLOUDSTACK-10002
.. _`#1246`: https://github.com/apache/cloudstack/pull/1246
.. _CLOUDSTACK-9165: https://issues.apache.org/jira/browse/CLOUDSTACK-9165
.. _`#2241`: https://github.com/apache/cloudstack/pull/2241
.. _CLOUDSTACK-10052: https://issues.apache.org/jira/browse/CLOUDSTACK-10052
.. _`#2222`: https://github.com/apache/cloudstack/pull/2222
.. _CLOUDSTACK-10022: https://issues.apache.org/jira/browse/CLOUDSTACK-10022
.. _`#2221`: https://github.com/apache/cloudstack/pull/2221
.. _CLOUDSTACK-10030: https://issues.apache.org/jira/browse/CLOUDSTACK-10030
.. _`#2154`: https://github.com/apache/cloudstack/pull/2154
.. _CLOUDSTACK-9967: https://issues.apache.org/jira/browse/CLOUDSTACK-9967
.. _`#1878`: https://github.com/apache/cloudstack/pull/1878
.. _CLOUDSTACK-9717: https://issues.apache.org/jira/browse/CLOUDSTACK-9717
.. _`#2013`: https://github.com/apache/cloudstack/pull/2013
.. _CLOUDSTACK-9734: https://issues.apache.org/jira/browse/CLOUDSTACK-9734
.. _`#2159`: https://github.com/apache/cloudstack/pull/2159
.. _CLOUDSTACK-9964: https://issues.apache.org/jira/browse/CLOUDSTACK-9964
.. _`#2163`: https://github.com/apache/cloudstack/pull/2163
.. _CLOUDSTACK-9939: https://issues.apache.org/jira/browse/CLOUDSTACK-9939
.. _`#1919`: https://github.com/apache/cloudstack/pull/1919
.. _CLOUDSTACK-9763: https://issues.apache.org/jira/browse/CLOUDSTACK-9763
.. _`#1936`: https://github.com/apache/cloudstack/pull/1936
.. _CLOUDSTACK-9773: https://issues.apache.org/jira/browse/CLOUDSTACK-9773
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2215`: https://github.com/apache/cloudstack/pull/2215
.. _CLOUDSTACK-10026: https://issues.apache.org/jira/browse/CLOUDSTACK-10026
.. _`#2180`: https://github.com/apache/cloudstack/pull/2180
.. _CLOUDSTACK-9999: https://issues.apache.org/jira/browse/CLOUDSTACK-9999
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2236`: https://github.com/apache/cloudstack/pull/2236
.. _CLOUDSTACK-10044: https://issues.apache.org/jira/browse/CLOUDSTACK-10044
.. _`#2235`: https://github.com/apache/cloudstack/pull/2235
.. _`#2182`: https://github.com/apache/cloudstack/pull/2182
.. _CLOUDSTACK-10000: https://issues.apache.org/jira/browse/CLOUDSTACK-10000
.. _`#2233`: https://github.com/apache/cloudstack/pull/2233
.. _CLOUDSTACK-10042: https://issues.apache.org/jira/browse/CLOUDSTACK-10042
.. _`#2228`: https://github.com/apache/cloudstack/pull/2228
.. _CLOUDSTACK-10036: https://issues.apache.org/jira/browse/CLOUDSTACK-10036
.. _`#2026`: https://github.com/apache/cloudstack/pull/2026
.. _CLOUDSTACK-9861: https://issues.apache.org/jira/browse/CLOUDSTACK-9861
.. _`#1774`: https://github.com/apache/cloudstack/pull/1774
.. _CLOUDSTACK-9608: https://issues.apache.org/jira/browse/CLOUDSTACK-9608
.. _`#2039`: https://github.com/apache/cloudstack/pull/2039
.. _`#2144`: https://github.com/apache/cloudstack/pull/2144
.. _CLOUDSTACK-9955: https://issues.apache.org/jira/browse/CLOUDSTACK-9955
.. _`#1966`: https://github.com/apache/cloudstack/pull/1966
.. _CLOUDSTACK-9801: https://issues.apache.org/jira/browse/CLOUDSTACK-9801
.. _`#2220`: https://github.com/apache/cloudstack/pull/2220
.. _CLOUDSTACK-9708: https://issues.apache.org/jira/browse/CLOUDSTACK-9708
.. _`#1912`: https://github.com/apache/cloudstack/pull/1912
.. _CLOUDSTACK-9749: https://issues.apache.org/jira/browse/CLOUDSTACK-9749
.. _`#2138`: https://github.com/apache/cloudstack/pull/2138
.. _CLOUDSTACK-9944: https://issues.apache.org/jira/browse/CLOUDSTACK-9944
.. _`#2193`: https://github.com/apache/cloudstack/pull/2193
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2218`: https://github.com/apache/cloudstack/pull/2218
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#883`: https://github.com/apache/cloudstack/pull/883
.. _CLOUDSTACK-8906: https://issues.apache.org/jira/browse/CLOUDSTACK-8906
.. _`#2119`: https://github.com/apache/cloudstack/pull/2119
.. _CLOUDSTACK-9925: https://issues.apache.org/jira/browse/CLOUDSTACK-9925
.. _`#2145`: https://github.com/apache/cloudstack/pull/2145
.. _CLOUDSTACK-9697: https://issues.apache.org/jira/browse/CLOUDSTACK-9697
.. _`#2137`: https://github.com/apache/cloudstack/pull/2137
.. _CLOUDSTACK-9950: https://issues.apache.org/jira/browse/CLOUDSTACK-9950
.. _`#2008`: https://github.com/apache/cloudstack/pull/2008
.. _CLOUDSTACK-9840: https://issues.apache.org/jira/browse/CLOUDSTACK-9840
.. _`#2094`: https://github.com/apache/cloudstack/pull/2094
.. _`#2142`: https://github.com/apache/cloudstack/pull/2142
.. _CLOUDSTACK-9954: https://issues.apache.org/jira/browse/CLOUDSTACK-9954
.. _`#2130`: https://github.com/apache/cloudstack/pull/2130
.. _CLOUDSTACK-8961: https://issues.apache.org/jira/browse/CLOUDSTACK-8961
.. _`#2212`: https://github.com/apache/cloudstack/pull/2212
.. _`#2171`: https://github.com/apache/cloudstack/pull/2171
.. _CLOUDSTACK-9990: https://issues.apache.org/jira/browse/CLOUDSTACK-9990
.. _`#2205`: https://github.com/apache/cloudstack/pull/2205
.. _`#1925`: https://github.com/apache/cloudstack/pull/1925
.. _CLOUDSTACK-9751: https://issues.apache.org/jira/browse/CLOUDSTACK-9751
.. _`#1798`: https://github.com/apache/cloudstack/pull/1798
.. _CLOUDSTACK-9631: https://issues.apache.org/jira/browse/CLOUDSTACK-9631
.. _`#2201`: https://github.com/apache/cloudstack/pull/2201
.. _CLOUDSTACK-10016: https://issues.apache.org/jira/browse/CLOUDSTACK-10016
.. _`#1784`: https://github.com/apache/cloudstack/pull/1784
.. _`#2200`: https://github.com/apache/cloudstack/pull/2200
.. _CLOUDSTACK-10015: https://issues.apache.org/jira/browse/CLOUDSTACK-10015
.. _`#1655`: https://github.com/apache/cloudstack/pull/1655
.. _`#1959`: https://github.com/apache/cloudstack/pull/1959
.. _CLOUDSTACK-9786: https://issues.apache.org/jira/browse/CLOUDSTACK-9786
.. _`#1933`: https://github.com/apache/cloudstack/pull/1933
.. _CLOUDSTACK-9569: https://issues.apache.org/jira/browse/CLOUDSTACK-9569
.. _`#2175`: https://github.com/apache/cloudstack/pull/2175
.. _`#2176`: https://github.com/apache/cloudstack/pull/2176
.. _`#2407`: https://github.com/apache/cloudstack/pull/2407
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2403`: https://github.com/apache/cloudstack/pull/2403
.. _CLOUDSTACK-10227: https://issues.apache.org/jira/browse/CLOUDSTACK-10227
.. _`#2298`: https://github.com/apache/cloudstack/pull/2298
.. _CLOUDSTACK-9620: https://issues.apache.org/jira/browse/CLOUDSTACK-9620
.. _`#2396`: https://github.com/apache/cloudstack/pull/2396
.. _CLOUDSTACK-10220: https://issues.apache.org/jira/browse/CLOUDSTACK-10220
.. _`#2152`: https://github.com/apache/cloudstack/pull/2152
.. _CLOUDSTACK-10229: https://issues.apache.org/jira/browse/CLOUDSTACK-10229
.. _`#2097`: https://github.com/apache/cloudstack/pull/2097
.. _CLOUDSTACK-9813: https://issues.apache.org/jira/browse/CLOUDSTACK-9813
.. _`#2362`: https://github.com/apache/cloudstack/pull/2362
.. _CLOUDSTACK-10188: https://issues.apache.org/jira/browse/CLOUDSTACK-10188
.. _`#2146`: https://github.com/apache/cloudstack/pull/2146
.. _CLOUDSTACK-4757: https://issues.apache.org/jira/browse/CLOUDSTACK-4757
.. _`#2394`: https://github.com/apache/cloudstack/pull/2394
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2393`: https://github.com/apache/cloudstack/pull/2393
.. _CLOUDSTACK-10217: https://issues.apache.org/jira/browse/CLOUDSTACK-10217
.. _`#2350`: https://github.com/apache/cloudstack/pull/2350
.. _`#2388`: https://github.com/apache/cloudstack/pull/2388
.. _CLOUDSTACK-10212: https://issues.apache.org/jira/browse/CLOUDSTACK-10212
.. _`#2379`: https://github.com/apache/cloudstack/pull/2379
.. _CLOUDSTACK-10146: https://issues.apache.org/jira/browse/CLOUDSTACK-10146
.. _`#2389`: https://github.com/apache/cloudstack/pull/2389
.. _CLOUDSTACK-10213: https://issues.apache.org/jira/browse/CLOUDSTACK-10213
.. _`#2391`: https://github.com/apache/cloudstack/pull/2391
.. _CLOUDSTACK-10215: https://issues.apache.org/jira/browse/CLOUDSTACK-10215
.. _`#2139`: https://github.com/apache/cloudstack/pull/2139
.. _CLOUDSTACK-9921: https://issues.apache.org/jira/browse/CLOUDSTACK-9921
.. _`#2088`: https://github.com/apache/cloudstack/pull/2088
.. _CLOUDSTACK-9892: https://issues.apache.org/jira/browse/CLOUDSTACK-9892
.. _`#2365`: https://github.com/apache/cloudstack/pull/2365
.. _CLOUDSTACK-10197: https://issues.apache.org/jira/browse/CLOUDSTACK-10197
.. _`#2073`: https://github.com/apache/cloudstack/pull/2073
.. _CLOUDSTACK-9896: https://issues.apache.org/jira/browse/CLOUDSTACK-9896
.. _`#2386`: https://github.com/apache/cloudstack/pull/2386
.. _CLOUDSTACK-9632: https://issues.apache.org/jira/browse/CLOUDSTACK-9632
.. _`#2295`: https://github.com/apache/cloudstack/pull/2295
.. _CLOUDSTACK-10109: https://issues.apache.org/jira/browse/CLOUDSTACK-10109
.. _`#2381`: https://github.com/apache/cloudstack/pull/2381
.. _CLOUDSTACK-10117: https://issues.apache.org/jira/browse/CLOUDSTACK-10117
.. _`#2315`: https://github.com/apache/cloudstack/pull/2315
.. _CLOUDSTACK-9025: https://issues.apache.org/jira/browse/CLOUDSTACK-9025
.. _`#2274`: https://github.com/apache/cloudstack/pull/2274
.. _CLOUDSTACK-10096: https://issues.apache.org/jira/browse/CLOUDSTACK-10096
.. _`#2282`: https://github.com/apache/cloudstack/pull/2282
.. _CLOUDSTACK-10104: https://issues.apache.org/jira/browse/CLOUDSTACK-10104
.. _`#2368`: https://github.com/apache/cloudstack/pull/2368
.. _CLOUDSTACK-10126: https://issues.apache.org/jira/browse/CLOUDSTACK-10126
.. _`#2385`: https://github.com/apache/cloudstack/pull/2385
.. _CLOUDSTACK-10211: https://issues.apache.org/jira/browse/CLOUDSTACK-10211
.. _`#2260`: https://github.com/apache/cloudstack/pull/2260
.. _CLOUDSTACK-10065: https://issues.apache.org/jira/browse/CLOUDSTACK-10065
.. _`#2292`: https://github.com/apache/cloudstack/pull/2292
.. _CLOUDSTACK-10108: https://issues.apache.org/jira/browse/CLOUDSTACK-10108
.. _`#1740`: https://github.com/apache/cloudstack/pull/1740
.. _CLOUDSTACK-9572: https://issues.apache.org/jira/browse/CLOUDSTACK-9572
.. _`#2104`: https://github.com/apache/cloudstack/pull/2104
.. _CLOUDSTACK-9908: https://issues.apache.org/jira/browse/CLOUDSTACK-9908
.. _`#2384`: https://github.com/apache/cloudstack/pull/2384
.. _CLOUDSTACK-10210: https://issues.apache.org/jira/browse/CLOUDSTACK-10210
.. _`#2378`: https://github.com/apache/cloudstack/pull/2378
.. _CLOUDSTACK-10205: https://issues.apache.org/jira/browse/CLOUDSTACK-10205
.. _`#2383`: https://github.com/apache/cloudstack/pull/2383
.. _`#1773`: https://github.com/apache/cloudstack/pull/1773
.. _CLOUDSTACK-9607: https://issues.apache.org/jira/browse/CLOUDSTACK-9607
.. _`#2046`: https://github.com/apache/cloudstack/pull/2046
.. _CLOUDSTACK-7958: https://issues.apache.org/jira/browse/CLOUDSTACK-7958
.. _`#2149`: https://github.com/apache/cloudstack/pull/2149
.. _CLOUDSTACK-9932: https://issues.apache.org/jira/browse/CLOUDSTACK-9932
.. _`#2156`: https://github.com/apache/cloudstack/pull/2156
.. _CLOUDSTACK-9971: https://issues.apache.org/jira/browse/CLOUDSTACK-9971
.. _`#2374`: https://github.com/apache/cloudstack/pull/2374
.. _CLOUDSTACK-10024: https://issues.apache.org/jira/browse/CLOUDSTACK-10024
.. _`#2373`: https://github.com/apache/cloudstack/pull/2373
.. _CLOUDSTACK-10202: https://issues.apache.org/jira/browse/CLOUDSTACK-10202
.. _`#2344`: https://github.com/apache/cloudstack/pull/2344
.. _CLOUDSTACK-10163: https://issues.apache.org/jira/browse/CLOUDSTACK-10163
.. _`#2301`: https://github.com/apache/cloudstack/pull/2301
.. _CLOUDSTACK-10121: https://issues.apache.org/jira/browse/CLOUDSTACK-10121
.. _`#1554`: https://github.com/apache/cloudstack/pull/1554
.. _CLOUDSTACK-9602: https://issues.apache.org/jira/browse/CLOUDSTACK-9602
.. _`#1760`: https://github.com/apache/cloudstack/pull/1760
.. _CLOUDSTACK-9593: https://issues.apache.org/jira/browse/CLOUDSTACK-9593
.. _`#2035`: https://github.com/apache/cloudstack/pull/2035
.. _CLOUDSTACK-9867: https://issues.apache.org/jira/browse/CLOUDSTACK-9867
.. _`#2360`: https://github.com/apache/cloudstack/pull/2360
.. _CLOUDSTACK-10189: https://issues.apache.org/jira/browse/CLOUDSTACK-10189
.. _`#2352`: https://github.com/apache/cloudstack/pull/2352
.. _CLOUDSTACK-10175: https://issues.apache.org/jira/browse/CLOUDSTACK-10175
.. _`#2045`: https://github.com/apache/cloudstack/pull/2045
.. _`#1934`: https://github.com/apache/cloudstack/pull/1934
.. _CLOUDSTACK-9772: https://issues.apache.org/jira/browse/CLOUDSTACK-9772
.. _`#2258`: https://github.com/apache/cloudstack/pull/2258
.. _`#2347`: https://github.com/apache/cloudstack/pull/2347
.. _CLOUDSTACK-10166: https://issues.apache.org/jira/browse/CLOUDSTACK-10166
.. _`#2375`: https://github.com/apache/cloudstack/pull/2375
.. _CLOUDSTACK-9456: https://issues.apache.org/jira/browse/CLOUDSTACK-9456
.. _`#2211`: https://github.com/apache/cloudstack/pull/2211
.. _CLOUDSTACK-10013: https://issues.apache.org/jira/browse/CLOUDSTACK-10013
.. _`#1637`: https://github.com/apache/cloudstack/pull/1637
.. _`#2304`: https://github.com/apache/cloudstack/pull/2304
.. _CLOUDSTACK-10127: https://issues.apache.org/jira/browse/CLOUDSTACK-10127
.. _`#2208`: https://github.com/apache/cloudstack/pull/2208
.. _CLOUDSTACK-9542: https://issues.apache.org/jira/browse/CLOUDSTACK-9542
.. _`#2351`: https://github.com/apache/cloudstack/pull/2351
.. _CLOUDSTACK-10173: https://issues.apache.org/jira/browse/CLOUDSTACK-10173
.. _`#2367`: https://github.com/apache/cloudstack/pull/2367
.. _`#2370`: https://github.com/apache/cloudstack/pull/2370
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2366`: https://github.com/apache/cloudstack/pull/2366
.. _CLOUDSTACK-10168: https://issues.apache.org/jira/browse/CLOUDSTACK-10168
.. _`#2371`: https://github.com/apache/cloudstack/pull/2371
.. _`#2042`: https://github.com/apache/cloudstack/pull/2042
.. _CLOUDSTACK-9875: https://issues.apache.org/jira/browse/CLOUDSTACK-9875
.. _`#2281`: https://github.com/apache/cloudstack/pull/2281
.. _CLOUDSTACK-10102: https://issues.apache.org/jira/browse/CLOUDSTACK-10102
.. _`#2048`: https://github.com/apache/cloudstack/pull/2048
.. _CLOUDSTACK-9880: https://issues.apache.org/jira/browse/CLOUDSTACK-9880
.. _`#2364`: https://github.com/apache/cloudstack/pull/2364
.. _CLOUDSTACK-10195: https://issues.apache.org/jira/browse/CLOUDSTACK-10195
.. _`#2361`: https://github.com/apache/cloudstack/pull/2361
.. _CLOUDSTACK-10190: https://issues.apache.org/jira/browse/CLOUDSTACK-10190
.. _`#1437`: https://github.com/apache/cloudstack/pull/1437
.. _`#2247`: https://github.com/apache/cloudstack/pull/2247
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1964`: https://github.com/apache/cloudstack/pull/1964
.. _CLOUDSTACK-9800: https://issues.apache.org/jira/browse/CLOUDSTACK-9800
.. _`#1762`: https://github.com/apache/cloudstack/pull/1762
.. _CLOUDSTACK-9595: https://issues.apache.org/jira/browse/CLOUDSTACK-9595
.. _`#2348`: https://github.com/apache/cloudstack/pull/2348
.. _CLOUDSTACK-10196: https://issues.apache.org/jira/browse/CLOUDSTACK-10196
.. _`#2184`: https://github.com/apache/cloudstack/pull/2184
.. _CLOUDSTACK-10003: https://issues.apache.org/jira/browse/CLOUDSTACK-10003
.. _`#2308`: https://github.com/apache/cloudstack/pull/2308
.. _CLOUDSTACK-8908: https://issues.apache.org/jira/browse/CLOUDSTACK-8908
.. _`#2294`: https://github.com/apache/cloudstack/pull/2294
.. _CLOUDSTACK-10039: https://issues.apache.org/jira/browse/CLOUDSTACK-10039
.. _`#2346`: https://github.com/apache/cloudstack/pull/2346
.. _`#2354`: https://github.com/apache/cloudstack/pull/2354
.. _CLOUDSTACK-10176: https://issues.apache.org/jira/browse/CLOUDSTACK-10176
.. _`#2353`: https://github.com/apache/cloudstack/pull/2353
.. _CLOUDSTACK-9986: https://issues.apache.org/jira/browse/CLOUDSTACK-9986
.. _`#2359`: https://github.com/apache/cloudstack/pull/2359
.. _`#2356`: https://github.com/apache/cloudstack/pull/2356
.. _CLOUDSTACK-8313: https://issues.apache.org/jira/browse/CLOUDSTACK-8313
.. _`#2358`: https://github.com/apache/cloudstack/pull/2358
.. _CLOUDSTACK-9736: https://issues.apache.org/jira/browse/CLOUDSTACK-9736
.. _`#2326`: https://github.com/apache/cloudstack/pull/2326
.. _CLOUDSTACK-10184: https://issues.apache.org/jira/browse/CLOUDSTACK-10184
.. _`#2267`: https://github.com/apache/cloudstack/pull/2267
.. _CLOUDSTACK-10077: https://issues.apache.org/jira/browse/CLOUDSTACK-10077
.. _`#2337`: https://github.com/apache/cloudstack/pull/2337
.. _CLOUDSTACK-10157: https://issues.apache.org/jira/browse/CLOUDSTACK-10157
.. _`#2355`: https://github.com/apache/cloudstack/pull/2355
.. _CLOUDSTACK-10177: https://issues.apache.org/jira/browse/CLOUDSTACK-10177
.. _`#2349`: https://github.com/apache/cloudstack/pull/2349
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2312`: https://github.com/apache/cloudstack/pull/2312
.. _CLOUDSTACK-7793: https://issues.apache.org/jira/browse/CLOUDSTACK-7793
.. _`#2345`: https://github.com/apache/cloudstack/pull/2345
.. _CLOUDSTACK-10164: https://issues.apache.org/jira/browse/CLOUDSTACK-10164
.. _`#2263`: https://github.com/apache/cloudstack/pull/2263
.. _CLOUDSTACK-10070: https://issues.apache.org/jira/browse/CLOUDSTACK-10070
.. _`#2342`: https://github.com/apache/cloudstack/pull/2342
.. _CLOUDSTACK-9586: https://issues.apache.org/jira/browse/CLOUDSTACK-9586
.. _`#2124`: https://github.com/apache/cloudstack/pull/2124
.. _CLOUDSTACK-9432: https://issues.apache.org/jira/browse/CLOUDSTACK-9432
.. _`#2322`: https://github.com/apache/cloudstack/pull/2322
.. _CLOUDSTACK-10140: https://issues.apache.org/jira/browse/CLOUDSTACK-10140
.. _`#2335`: https://github.com/apache/cloudstack/pull/2335
.. _CLOUDSTACK-10154: https://issues.apache.org/jira/browse/CLOUDSTACK-10154
.. _`#2341`: https://github.com/apache/cloudstack/pull/2341
.. _CLOUDSTACK-10160: https://issues.apache.org/jira/browse/CLOUDSTACK-10160
.. _`#2321`: https://github.com/apache/cloudstack/pull/2321
.. _CLOUDSTACK-10138: https://issues.apache.org/jira/browse/CLOUDSTACK-10138
.. _`#2334`: https://github.com/apache/cloudstack/pull/2334
.. _CLOUDSTACK-10152: https://issues.apache.org/jira/browse/CLOUDSTACK-10152
.. _`#2332`: https://github.com/apache/cloudstack/pull/2332
.. _CLOUDSTACK-10156: https://issues.apache.org/jira/browse/CLOUDSTACK-10156
.. _`#2028`: https://github.com/apache/cloudstack/pull/2028
.. _CLOUDSTACK-9853: https://issues.apache.org/jira/browse/CLOUDSTACK-9853
.. _`#2310`: https://github.com/apache/cloudstack/pull/2310
.. _CLOUDSTACK-10133: https://issues.apache.org/jira/browse/CLOUDSTACK-10133
.. _`#2219`: https://github.com/apache/cloudstack/pull/2219
.. _CLOUDSTACK-9989: https://issues.apache.org/jira/browse/CLOUDSTACK-9989
.. _`#2303`: https://github.com/apache/cloudstack/pull/2303
.. _CLOUDSTACK-10123: https://issues.apache.org/jira/browse/CLOUDSTACK-10123
.. _`#2329`: https://github.com/apache/cloudstack/pull/2329
.. _CLOUDSTACK-10012: https://issues.apache.org/jira/browse/CLOUDSTACK-10012
.. _`#1981`: https://github.com/apache/cloudstack/pull/1981
.. _CLOUDSTACK-9806: https://issues.apache.org/jira/browse/CLOUDSTACK-9806
.. _`#2324`: https://github.com/apache/cloudstack/pull/2324
.. _`#2005`: https://github.com/apache/cloudstack/pull/2005
.. _CLOUDSTACK-9450: https://issues.apache.org/jira/browse/CLOUDSTACK-9450
.. _`#2327`: https://github.com/apache/cloudstack/pull/2327
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2325`: https://github.com/apache/cloudstack/pull/2325
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2313`: https://github.com/apache/cloudstack/pull/2313
.. _CLOUDSTACK-10135: https://issues.apache.org/jira/browse/CLOUDSTACK-10135
.. _`#2316`: https://github.com/apache/cloudstack/pull/2316
.. _CLOUDSTACK-10137: https://issues.apache.org/jira/browse/CLOUDSTACK-10137
.. _`#2157`: https://github.com/apache/cloudstack/pull/2157
.. _CLOUDSTACK-9961: https://issues.apache.org/jira/browse/CLOUDSTACK-9961
.. _`#1723`: https://github.com/apache/cloudstack/pull/1723
.. _`#2306`: https://github.com/apache/cloudstack/pull/2306
.. _CLOUDSTACK-10129: https://issues.apache.org/jira/browse/CLOUDSTACK-10129
.. _`#2273`: https://github.com/apache/cloudstack/pull/2273
.. _CLOUDSTACK-10090: https://issues.apache.org/jira/browse/CLOUDSTACK-10090
.. _`#2242`: https://github.com/apache/cloudstack/pull/2242
.. _CLOUDSTACK-9958: https://issues.apache.org/jira/browse/CLOUDSTACK-9958
.. _`#2307`: https://github.com/apache/cloudstack/pull/2307
.. _`#2240`: https://github.com/apache/cloudstack/pull/2240
.. _CLOUDSTACK-10051: https://issues.apache.org/jira/browse/CLOUDSTACK-10051
.. _`#2158`: https://github.com/apache/cloudstack/pull/2158
.. _CLOUDSTACK-9972: https://issues.apache.org/jira/browse/CLOUDSTACK-9972
.. _`#2291`: https://github.com/apache/cloudstack/pull/2291
.. _CLOUDSTACK-10111: https://issues.apache.org/jira/browse/CLOUDSTACK-10111
.. _`#2302`: https://github.com/apache/cloudstack/pull/2302
.. _CLOUDSTACK-10122: https://issues.apache.org/jira/browse/CLOUDSTACK-10122
.. _`#2004`: https://github.com/apache/cloudstack/pull/2004
.. _CLOUDSTACK-9832: https://issues.apache.org/jira/browse/CLOUDSTACK-9832
.. _`#2238`: https://github.com/apache/cloudstack/pull/2238
.. _CLOUDSTACK-10053: https://issues.apache.org/jira/browse/CLOUDSTACK-10053
.. _`#2250`: https://github.com/apache/cloudstack/pull/2250
.. _CLOUDSTACK-10057: https://issues.apache.org/jira/browse/CLOUDSTACK-10057
.. _`#2268`: https://github.com/apache/cloudstack/pull/2268
.. _CLOUDSTACK-10081: https://issues.apache.org/jira/browse/CLOUDSTACK-10081
.. _`#2293`: https://github.com/apache/cloudstack/pull/2293
.. _CLOUDSTACK-10047: https://issues.apache.org/jira/browse/CLOUDSTACK-10047
.. _`#2284`: https://github.com/apache/cloudstack/pull/2284
.. _CLOUDSTACK-10103: https://issues.apache.org/jira/browse/CLOUDSTACK-10103
.. _`#2288`: https://github.com/apache/cloudstack/pull/2288
.. _CLOUDSTACK-10107: https://issues.apache.org/jira/browse/CLOUDSTACK-10107
.. _`#2297`: https://github.com/apache/cloudstack/pull/2297
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2296`: https://github.com/apache/cloudstack/pull/2296
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2181`: https://github.com/apache/cloudstack/pull/2181
.. _CLOUDSTACK-9957: https://issues.apache.org/jira/browse/CLOUDSTACK-9957
.. _`#2257`: https://github.com/apache/cloudstack/pull/2257
.. _CLOUDSTACK-10060: https://issues.apache.org/jira/browse/CLOUDSTACK-10060
.. _`#2286`: https://github.com/apache/cloudstack/pull/2286
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2287`: https://github.com/apache/cloudstack/pull/2287
.. _CLOUDSTACK-9998: https://issues.apache.org/jira/browse/CLOUDSTACK-9998
.. _`#2246`: https://github.com/apache/cloudstack/pull/2246
.. _CLOUDSTACK-10046: https://issues.apache.org/jira/browse/CLOUDSTACK-10046
.. _`#2074`: https://github.com/apache/cloudstack/pull/2074
.. _CLOUDSTACK-9899: https://issues.apache.org/jira/browse/CLOUDSTACK-9899
.. _`#2280`: https://github.com/apache/cloudstack/pull/2280
.. _CLOUDSTACK-10101: https://issues.apache.org/jira/browse/CLOUDSTACK-10101
.. _`#2285`: https://github.com/apache/cloudstack/pull/2285
.. _CLOUDSTACK-9859: https://issues.apache.org/jira/browse/CLOUDSTACK-9859
.. _`#2278`: https://github.com/apache/cloudstack/pull/2278
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2279`: https://github.com/apache/cloudstack/pull/2279
.. _CLOUDSTACK-9584: https://issues.apache.org/jira/browse/CLOUDSTACK-9584
.. _`#2277`: https://github.com/apache/cloudstack/pull/2277
.. _CLOUDSTACK-10099: https://issues.apache.org/jira/browse/CLOUDSTACK-10099
.. _`#2266`: https://github.com/apache/cloudstack/pull/2266
.. _CLOUDSTACK-10073: https://issues.apache.org/jira/browse/CLOUDSTACK-10073
.. _`#2249`: https://github.com/apache/cloudstack/pull/2249
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#1707`: https://github.com/apache/cloudstack/pull/1707
.. _CLOUDSTACK-9397: https://issues.apache.org/jira/browse/CLOUDSTACK-9397
.. _`#2269`: https://github.com/apache/cloudstack/pull/2269
.. _CLOUDSTACK-10083: https://issues.apache.org/jira/browse/CLOUDSTACK-10083
.. _`#876`: https://github.com/apache/cloudstack/pull/876
.. _CLOUDSTACK-8865: https://issues.apache.org/jira/browse/CLOUDSTACK-8865
.. _`#1252`: https://github.com/apache/cloudstack/pull/1252
.. _CLOUDSTACK-9182: https://issues.apache.org/jira/browse/CLOUDSTACK-9182
.. _`#2153`: https://github.com/apache/cloudstack/pull/2153
.. _CLOUDSTACK-9956: https://issues.apache.org/jira/browse/CLOUDSTACK-9956
.. _`#2078`: https://github.com/apache/cloudstack/pull/2078
.. _CLOUDSTACK-9902: https://issues.apache.org/jira/browse/CLOUDSTACK-9902
.. _`#2252`: https://github.com/apache/cloudstack/pull/2252
.. _CLOUDSTACK-10067: https://issues.apache.org/jira/browse/CLOUDSTACK-10067
.. _`#2143`: https://github.com/apache/cloudstack/pull/2143
.. _CLOUDSTACK-9949: https://issues.apache.org/jira/browse/CLOUDSTACK-9949
.. _`#2248`: https://github.com/apache/cloudstack/pull/2248
.. _CLOUDSTACK-10056: https://issues.apache.org/jira/browse/CLOUDSTACK-10056
.. _`#2243`: https://github.com/apache/cloudstack/pull/2243
.. _CLOUDSTACK-10019: https://issues.apache.org/jira/browse/CLOUDSTACK-10019
.. _`#2261`: https://github.com/apache/cloudstack/pull/2261
.. _CLOUDSTACK-10068: https://issues.apache.org/jira/browse/CLOUDSTACK-10068
.. _`#2054`: https://github.com/apache/cloudstack/pull/2054
.. _CLOUDSTACK-9886: https://issues.apache.org/jira/browse/CLOUDSTACK-9886
.. _`#955`: https://github.com/apache/cloudstack/pull/955
.. _CLOUDSTACK-8969: https://issues.apache.org/jira/browse/CLOUDSTACK-8969
.. _`#2262`: https://github.com/apache/cloudstack/pull/2262
.. _CLOUDSTACK-10069: https://issues.apache.org/jira/browse/CLOUDSTACK-10069
.. _`#2256`: https://github.com/apache/cloudstack/pull/2256
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#2253`: https://github.com/apache/cloudstack/pull/2253
.. _CLOUDSTACK-10061: https://issues.apache.org/jira/browse/CLOUDSTACK-10061
.. _`#2254`: https://github.com/apache/cloudstack/pull/2254
.. _CLOUDSTACK-10058: https://issues.apache.org/jira/browse/CLOUDSTACK-10058
.. _`#1733`: https://github.com/apache/cloudstack/pull/1733
.. _CLOUDSTACK-9563: https://issues.apache.org/jira/browse/CLOUDSTACK-9563
.. _`#2188`: https://github.com/apache/cloudstack/pull/2188
.. _CLOUDSTACK-10004: https://issues.apache.org/jira/browse/CLOUDSTACK-10004
.. _`#914`: https://github.com/apache/cloudstack/pull/914
.. _CLOUDSTACK-8939: https://issues.apache.org/jira/browse/CLOUDSTACK-8939
.. _`#1985`: https://github.com/apache/cloudstack/pull/1985
.. _CLOUDSTACK-9812: https://issues.apache.org/jira/browse/CLOUDSTACK-9812
.. _`#2224`: https://github.com/apache/cloudstack/pull/2224
.. _CLOUDSTACK-10032: https://issues.apache.org/jira/browse/CLOUDSTACK-10032
.. _`#1443`: https://github.com/apache/cloudstack/pull/1443
.. _CLOUDSTACK-9314: https://issues.apache.org/jira/browse/CLOUDSTACK-9314
.. _`#2109`: https://github.com/apache/cloudstack/pull/2109
.. _CLOUDSTACK-9922: https://issues.apache.org/jira/browse/CLOUDSTACK-9922
.. _`#2216`: https://github.com/apache/cloudstack/pull/2216
.. _CLOUDSTACK-10027: https://issues.apache.org/jira/browse/CLOUDSTACK-10027
.. _`#2245`: https://github.com/apache/cloudstack/pull/2245
.. _`#2239`: https://github.com/apache/cloudstack/pull/2239
.. _CLOUDSTACK-9993: https://issues.apache.org/jira/browse/CLOUDSTACK-9993
.. _`#2044`: https://github.com/apache/cloudstack/pull/2044
.. _CLOUDSTACK-9877: https://issues.apache.org/jira/browse/CLOUDSTACK-9877
.. _`#2174`: https://github.com/apache/cloudstack/pull/2174
.. _CLOUDSTACK-9996: https://issues.apache.org/jira/browse/CLOUDSTACK-9996
.. _`#2101`: https://github.com/apache/cloudstack/pull/2101
.. _CLOUDSTACK-9915: https://issues.apache.org/jira/browse/CLOUDSTACK-9915
.. _`#2123`: https://github.com/apache/cloudstack/pull/2123
.. _CLOUDSTACK-9914: https://issues.apache.org/jira/browse/CLOUDSTACK-9914
.. _`#2186`: https://github.com/apache/cloudstack/pull/2186
.. _CLOUDSTACK-10002: https://issues.apache.org/jira/browse/CLOUDSTACK-10002
.. _`#1246`: https://github.com/apache/cloudstack/pull/1246
.. _CLOUDSTACK-9165: https://issues.apache.org/jira/browse/CLOUDSTACK-9165
.. _`#2241`: https://github.com/apache/cloudstack/pull/2241
.. _CLOUDSTACK-10052: https://issues.apache.org/jira/browse/CLOUDSTACK-10052
.. _`#2222`: https://github.com/apache/cloudstack/pull/2222
.. _CLOUDSTACK-10022: https://issues.apache.org/jira/browse/CLOUDSTACK-10022
.. _`#2221`: https://github.com/apache/cloudstack/pull/2221
.. _CLOUDSTACK-10030: https://issues.apache.org/jira/browse/CLOUDSTACK-10030
.. _`#2154`: https://github.com/apache/cloudstack/pull/2154
.. _CLOUDSTACK-9967: https://issues.apache.org/jira/browse/CLOUDSTACK-9967
.. _`#1878`: https://github.com/apache/cloudstack/pull/1878
.. _CLOUDSTACK-9717: https://issues.apache.org/jira/browse/CLOUDSTACK-9717
.. _`#2013`: https://github.com/apache/cloudstack/pull/2013
.. _CLOUDSTACK-9734: https://issues.apache.org/jira/browse/CLOUDSTACK-9734
.. _`#2159`: https://github.com/apache/cloudstack/pull/2159
.. _CLOUDSTACK-9964: https://issues.apache.org/jira/browse/CLOUDSTACK-9964
.. _`#2163`: https://github.com/apache/cloudstack/pull/2163
.. _CLOUDSTACK-9939: https://issues.apache.org/jira/browse/CLOUDSTACK-9939
.. _`#1919`: https://github.com/apache/cloudstack/pull/1919
.. _CLOUDSTACK-9763: https://issues.apache.org/jira/browse/CLOUDSTACK-9763
.. _`#1936`: https://github.com/apache/cloudstack/pull/1936
.. _CLOUDSTACK-9773: https://issues.apache.org/jira/browse/CLOUDSTACK-9773
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2215`: https://github.com/apache/cloudstack/pull/2215
.. _CLOUDSTACK-10026: https://issues.apache.org/jira/browse/CLOUDSTACK-10026
.. _`#2180`: https://github.com/apache/cloudstack/pull/2180
.. _CLOUDSTACK-9999: https://issues.apache.org/jira/browse/CLOUDSTACK-9999
.. _`#2223`: https://github.com/apache/cloudstack/pull/2223
.. _CLOUDSTACK-10031: https://issues.apache.org/jira/browse/CLOUDSTACK-10031
.. _`#2236`: https://github.com/apache/cloudstack/pull/2236
.. _CLOUDSTACK-10044: https://issues.apache.org/jira/browse/CLOUDSTACK-10044
.. _`#2235`: https://github.com/apache/cloudstack/pull/2235
.. _`#2182`: https://github.com/apache/cloudstack/pull/2182
.. _CLOUDSTACK-10000: https://issues.apache.org/jira/browse/CLOUDSTACK-10000
.. _`#2233`: https://github.com/apache/cloudstack/pull/2233
.. _CLOUDSTACK-10042: https://issues.apache.org/jira/browse/CLOUDSTACK-10042
.. _`#2228`: https://github.com/apache/cloudstack/pull/2228
.. _CLOUDSTACK-10036: https://issues.apache.org/jira/browse/CLOUDSTACK-10036
.. _`#2026`: https://github.com/apache/cloudstack/pull/2026
.. _CLOUDSTACK-9861: https://issues.apache.org/jira/browse/CLOUDSTACK-9861
.. _`#1774`: https://github.com/apache/cloudstack/pull/1774
.. _CLOUDSTACK-9608: https://issues.apache.org/jira/browse/CLOUDSTACK-9608
.. _`#2039`: https://github.com/apache/cloudstack/pull/2039
.. _`#2144`: https://github.com/apache/cloudstack/pull/2144
.. _CLOUDSTACK-9955: https://issues.apache.org/jira/browse/CLOUDSTACK-9955
.. _`#1966`: https://github.com/apache/cloudstack/pull/1966
.. _CLOUDSTACK-9801: https://issues.apache.org/jira/browse/CLOUDSTACK-9801
.. _`#2220`: https://github.com/apache/cloudstack/pull/2220
.. _CLOUDSTACK-9708: https://issues.apache.org/jira/browse/CLOUDSTACK-9708
.. _`#1912`: https://github.com/apache/cloudstack/pull/1912
.. _CLOUDSTACK-9749: https://issues.apache.org/jira/browse/CLOUDSTACK-9749
.. _`#2138`: https://github.com/apache/cloudstack/pull/2138
.. _CLOUDSTACK-9944: https://issues.apache.org/jira/browse/CLOUDSTACK-9944
.. _`#2193`: https://github.com/apache/cloudstack/pull/2193
.. _CLOUDSTACK-10007: https://issues.apache.org/jira/browse/CLOUDSTACK-10007
.. _`#2218`: https://github.com/apache/cloudstack/pull/2218
.. _CLOUDSTACK-9782: https://issues.apache.org/jira/browse/CLOUDSTACK-9782
.. _`#883`: https://github.com/apache/cloudstack/pull/883
.. _CLOUDSTACK-8906: https://issues.apache.org/jira/browse/CLOUDSTACK-8906
.. _`#2119`: https://github.com/apache/cloudstack/pull/2119
.. _CLOUDSTACK-9925: https://issues.apache.org/jira/browse/CLOUDSTACK-9925
.. _`#2145`: https://github.com/apache/cloudstack/pull/2145
.. _CLOUDSTACK-9697: https://issues.apache.org/jira/browse/CLOUDSTACK-9697
.. _`#2137`: https://github.com/apache/cloudstack/pull/2137
.. _CLOUDSTACK-9950: https://issues.apache.org/jira/browse/CLOUDSTACK-9950
.. _`#2008`: https://github.com/apache/cloudstack/pull/2008
.. _CLOUDSTACK-9840: https://issues.apache.org/jira/browse/CLOUDSTACK-9840
.. _`#2094`: https://github.com/apache/cloudstack/pull/2094
.. _`#2142`: https://github.com/apache/cloudstack/pull/2142
.. _CLOUDSTACK-9954: https://issues.apache.org/jira/browse/CLOUDSTACK-9954
.. _`#2130`: https://github.com/apache/cloudstack/pull/2130
.. _CLOUDSTACK-8961: https://issues.apache.org/jira/browse/CLOUDSTACK-8961
.. _`#2212`: https://github.com/apache/cloudstack/pull/2212
.. _`#2171`: https://github.com/apache/cloudstack/pull/2171
.. _CLOUDSTACK-9990: https://issues.apache.org/jira/browse/CLOUDSTACK-9990
.. _`#2205`: https://github.com/apache/cloudstack/pull/2205
.. _`#1925`: https://github.com/apache/cloudstack/pull/1925
.. _CLOUDSTACK-9751: https://issues.apache.org/jira/browse/CLOUDSTACK-9751
.. _`#1798`: https://github.com/apache/cloudstack/pull/1798
.. _CLOUDSTACK-9631: https://issues.apache.org/jira/browse/CLOUDSTACK-9631
.. _`#2201`: https://github.com/apache/cloudstack/pull/2201
.. _CLOUDSTACK-10016: https://issues.apache.org/jira/browse/CLOUDSTACK-10016
.. _`#1784`: https://github.com/apache/cloudstack/pull/1784
.. _`#2200`: https://github.com/apache/cloudstack/pull/2200
.. _CLOUDSTACK-10015: https://issues.apache.org/jira/browse/CLOUDSTACK-10015
.. _`#1655`: https://github.com/apache/cloudstack/pull/1655
.. _`#1959`: https://github.com/apache/cloudstack/pull/1959
.. _CLOUDSTACK-9786: https://issues.apache.org/jira/browse/CLOUDSTACK-9786
.. _`#1933`: https://github.com/apache/cloudstack/pull/1933
.. _CLOUDSTACK-9569: https://issues.apache.org/jira/browse/CLOUDSTACK-9569
.. _`#2175`: https://github.com/apache/cloudstack/pull/2175
.. _`#2176`: https://github.com/apache/cloudstack/pull/2176

