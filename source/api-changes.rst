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


API Changes Introduced in |version|
===================================

updateSnapshotPolicy (Updates the snapshot policy.)

+-----------------------------------+-------------------------------------------------------------------------------------------+
| API                               | Description                                                                               |
+===================================+===========================================================================================+
|  updateSnapshotPolicy             |                                                                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listSnapshotPolicies             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional), id (optional)                                    |
|                                   |                                                                                           |
|                                   |   Changed parameters: volumeid (old version - required, new version - optional)           |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  getUser                          | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: userapikey (required)                                                   |
|                                   |                                                                                           |
|                                   |   Removed parameters: apikey                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  listResourceDetails              | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: value (optional)                                                        |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  createSnapshotPolicy             | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay (optional)                                                   |
|                                   |                                                                                           |
|                                   | Response:                                                                                 |
|                                   |                                                                                           |
|                                   |   New parameters: fordisplay                                                              |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
|  uploadVolume                     | Request:                                                                                  |
|                                   |                                                                                           |
|                                   |   New parameters: diskofferingid (optional)                                               |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+

