Install new MySQL connector
---------------------------

Apache CloudStack |version| require an upgrade of the MySQL connector. To install
the connector via 'apt-get' following steps must be taken:


MySQL connector APT repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the following package provided by MySQL to enable official repositories:

.. sourcecode:: bash

   wget http://dev.mysql.com/get/mysql-apt-config_0.7.3-1_all.deb
   sudo dpkg -i mysql-apt-config_0.7.3-1_all.deb

Make sure to activate the repository for MySQL connectors.

.. sourcecode:: bash

   sudo apt-get update
   sudo apt-get install mysql-connector-python   


MySQL connector RPM repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a new yum repo ``/etc/yum.repos.d/mysql.repo``:

.. sourcecode:: bash

   [mysql-community]
   name=MySQL Community connectors
   baseurl=http://repo.mysql.com/yum/mysql-connectors-community/el/$releasever/$basearch/
   enabled=1
   gpgcheck=1

Import GPG public key from MySQL:

.. sourcecode:: bash

   rpm --import http://repo.mysql.com/RPM-GPG-KEY-mysql

Install mysql-connector

.. sourcecode:: bash

   yum install mysql-connector-python

