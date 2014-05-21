System-VMs and Virtual-Routers
------------------------------

Once you've upgraded the packages on your management servers, you'll
need to restart the system VMs. Ensure that the admin port is set to
8096 by using the "integration.api.port" global parameter. This port
is used by the cloud-sysvmadm script at the end of the upgrade
procedure. For information about how to set this parameter, see
`Setting Global Configuration Parameters <http://docs.cloudstack.apache.org/projects/cloudstack-installation/en/latest/configuration.html#setting-global-configuration-parameters>`_ in the Installation Guide.
Changing this parameter will require management server restart. Also
make sure port 8096 is open in your local host firewall to do this.

There is a script that will do this for you, all you need to do is
run the script and supply the IP address for your MySQL instance and
your MySQL credentials:

.. sourcecode:: bash

    # nohup cloudstack-sysvmadm -d IP address -u cloud -p -a > sysvm.log 2>&1 &

You can monitor the log for progress. The process of restarting the
system VMs can take an hour or more.

.. sourcecode:: bash

    # tail -f sysvm.log

The output to ``sysvm.log`` will look something like this:

.. sourcecode:: bash

    Stopping and starting 1 secondary storage vm(s)...
    Done stopping and starting secondary storage vm(s)
    Stopping and starting 1 console proxy vm(s)...
    Done stopping and starting console proxy vm(s).
    Stopping and starting 4 running routing vm(s)...
    Done restarting router(s).

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

.. sub-section included in upgrade notes.
