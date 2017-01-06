#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information#
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# FIXME: Tidy up the script

from jira import JIRA

options = {'server': 'https://issues.apache.org/jira/'}
jira = JIRA(options)

def findPR(issue):
    for comment in issue.fields.comment.comments:
        if 'asfgit closed the pull request' in comment.body:
            return comment.body.split("cloudstack/pull/")[1].split("\n")[0].strip()
    return ""

def printTable(issue, ticket, pr):
    if pr:
        pr = "`#%s`_" % pr
    print "| %-19s| %-8s | %-18s | %-13s | %-8s | %-58s |" % ("4.9", pr, ticket+"_", issue.fields.issuetype, issue.fields.priority, issue.fields.summary[:58])
    print "+--------------------+----------+--------------------+---------------+----------+------------------------------------------------------------+"

prs = []
tickets = open('jira.txt', 'r').read().split('\n')[:-1]
for ticket in tickets:
    issue = jira.issue(ticket)
    pr = findPR(issue)
    printTable(issue, ticket, pr)
    prs.append(pr)

print

for ticket in tickets:
    print ".. _%s: https://issues.apache.org/jira/browse/%s" % (ticket, ticket)

for pr in prs:
    print ".. _`#%s`: https://github.com/apache/cloudstack/pull/%s" % (pr, pr)
