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


Depreciation of realhostip.com 
------------------------------
   
The realhostip.com dynamic DNS resolution service is being retired on
September 30th, 2014. In advance of that, CloudStack 4.4 and later no longer uses 
realhostip.com DNS domains or SSL certificates to encrypt Console Proxy or 
file copy communications.

For latest update about realhostip.com follow `Apache CloudStack Blog <https://blogs.apache.org/cloudstack/>`_.



Settings Changes
----------------

Console Proxy URL
^^^^^^^^^^^^^^^^^

Please use ***.realhostip.com** (note the asterisk) as
``consoleproxy.url.domain`` value in global configs if you are using HTTPS for
console proxy. Please note that you need to restart the management server when you change
the global config value.

If you started with 4.3, you are likely running the console in HTTP mode
and the value of the above global config should be blank.

If switching between HTTP / HTTPS, the console proxy VM has to be
destroyed and recreated (available via UI)


Cluster Settings
^^^^^^^^^^^^^^^^

After upgrading to 4.2 and later, Settings ``mem.overporvisioning.factor`` and 
``cpu.overporvisioning.factor`` are now at the cluster level and be set to 1 
which is the default.

If Global Settings ``mem.overporvisioning.factor`` and 
``cpu.overporvisioning.factor`` have been changed prior the upgrade to 4.2 and 
later, the upgrade process will be reset them to 1. Values can be changed by 
editing clusters settings.

All clusters created after the upgrade will get created with the Global Settings 
values for ``mem.overporvisioning.factor`` and ``cpu.overporvisioning.factor``.


Active-Directory Authentication (LDAP)
--------------------------------------

If using Active-Directory (LDAP/LDAPs) as user authentication; Upgrading to 
4.3 and later require changes in Global Settings. After upgrading CloudStack
to 4.3 or latest, following Global Settings must be change:

======================= ============== ==============
Global Settings         Default        New
======================= ============== ==============
ldap.user.object        inetOrgPerson  user
ldap.username.attribute uid            sAMAccountName
======================= ============== ==============


SystemVM 32bit deprecated
-------------------------

32bit version of systemvm templates are in the process of behing deprecated. Upgrade instructions from this Release Notes use 64bit templates. 32bit systemvm-templates are available for this version on `http://cloudstack.apt-get.eu/systemvm/4.4/ <http://cloudstack.apt-get.eu/systemvm/4.4/>`_. Follow the dev mailing list for further updates.


.. not confirmed 
   Build From Sources
   ------------------
   
   Since CloudStack 4.2.1 build packages from source using non opensource 
   modules param ``-nonoss`` changed to ``-   noredist``.


