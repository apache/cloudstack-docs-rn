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


General Upgrade Notes
=====================

Settings Changes
----------------

After upgrading to 4.2 and later, Settings ``mem.overporvisioning.factor`` and 
``cpu.overporvisioning.factor`` are now at the cluster level and be set to 1 
which is the default.

If Global Settings ``mem.overporvisioning.factor`` and 
``cpu.overporvisioning.factor`` have been changed prior the upgrade to 4.2 and 
later, the upgrade process will be reset them to 1. Values can be changed by 
editing clusters settings.

All clusters created after the upgrade will get created with the Global Settings 
values for ``mem.overporvisioning.factor`` and ``cpu.overporvisioning.factor``.

.. not confirmed 
   Build From Sources
   ------------------
   
   Since CloudStack 4.2.1 build packages from source using non opensource 
   modules param ``-nonoss`` changed to ``-   noredist``.
   