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


Upgrade Instructions for |version|
==================================

This section contains upgrade instructions from prior versions of
CloudStack to Apache CloudStack |version|. We include instructions on
upgrading to Apache CloudStack from pre-Apache versions of Citrix
CloudStack (last version prior to Apache is 3.0.2) and from the releases
made while CloudStack was in the Apache Incubator.

If you run into any issues during upgrades, please feel free to ask
questions on users@cloudstack.apache.org or dev@cloudstack.apache.org.

.. warning::
   :name: Depreciation of realhostip.com DNS and SSL certificate
   
   The realhostip.com dynamic DNS resolution service is being retired this
   summer. In advance of that, CloudStack 4.3 and later no longer uses realhostip.com
   DNS domains or SSL certificates to encrypt Console Proxy or file copy
   communications.



.. include:: upgrade/valid_source.rst


.. include:: global.rst