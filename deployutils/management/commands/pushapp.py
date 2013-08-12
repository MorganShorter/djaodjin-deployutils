# Copyright (c) 2013, The DjaoDjin Team
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of DjaoDjin nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY The DjaoDjin Team ''AS IS'' AND ANY
#   EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL The DjaoDjin Team LLC BE LIABLE FOR ANY
#   DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import logging, subprocess

import fabric.api as fab

from deployutils.management.commands import (
    DeployCommand, upload, shell_command)


LOGGER = logging.getLogger(__name__)


class Command(DeployCommand):
    help = "[Hotfix] Push local code and resources to deployed servers."

    def handle(self, *args, **options):
        DeployCommand.handle(self, *args, **options)
        status = subprocess.check_output(['git', 'status', '--porcelain'])
        if len(status) == 0:
            sha1 = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        else:
            sha1 = "??"
        with open('.timestamp', 'w') as timestamp_file:
            timestamp_file.write(sha1)
        for host in fab.env.hosts:
            fab.env.host_string = host
            pushapp(self.webapp, self.path, sha1)


@fab.task
def pushapp(webapp, webapp_path, sha1):
    shell_command([
            '/usr/bin/rsync',
            '--copy-links', '--exclude', '.git', '--exclude', '.DS_Store',
            '--exclude', '*~', '--exclude', 'htdocs/', '-pthrRvz',
            '--rsync-path', '/usr/bin/rsync', '--delete',
            # css and js directories are under source control
            '.', './htdocs/static/css', './htdocs/static/js',
            '%s:%s' % (fab.env.host_string, webapp_path) ])
    upload(fab.env.host_string, webapp_path)
    LOGGER.info("pushapp %s %s %s", webapp, fab.env.host_string, sha1)