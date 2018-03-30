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

Version |release| includes more than 190 commits and 100 issue fixes since the
4.9.2.0 release.

The 4.9.3.1 is part of the LTS 4.9.x releases. The 4.9 LTS branch is supported
for 20 months, and will receives updates for first 14 months and only
security updates in its last 6 months. The 4.9 LTS branch is supported till 1
June 2018.

A LOT changed_ in this release, so this is not a complete list, but here is a quick summary of
some of the changes.


Changes
-------

* Robot attack security fix
* Several VR fixes
* Snapshot improvements
* Fixes router aggregation timeout
* Packaging and upgrade improvements
* Password server speedups
* DB optimizations and improvements
* Support for VMware 6.5
* Improved metrics view performance
* Added list of router(s) in network details tab
* Power off VM when force stop is used to stop VMs
* Hides credentials in ``listCluster`` response
* Higher quality releases due to better QA automation, testing and code reviewing

Build dependency
----------------

When building Apache CloudStack with ``noredist``, it now require the file
``deps/vim25_60.jar`` available from vSphere SDK 6.0,
VMware-vSphere-SDK-6.0.0-3634981.zip.

.. _changed: https://github.com/apache/cloudstack/compare/4.9.2.0...4.9.3.0
