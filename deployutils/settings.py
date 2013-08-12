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

"""
Convenience module for access of deployutils app settings, which enforces
default settings when the main settings module does not contain
the appropriate settings.
"""
from django.conf import settings


DRY_RUN = getattr(settings, 'DEPLOYUTILS_DRY_RUN', False)

DEPLOYED_WEBAPP_ROOT = getattr(settings, 'DEPLOYUTILS_DEPLOYED_WEBAPP_ROOT',
                               '/var/www/%s' % settings.ALLOWED_HOSTS[0])

DEPLOYED_SERVERS = getattr(settings, 'DEPLOYUTILS_DEPLOYED_SERVERS',
                           (settings.ALLOWED_HOSTS[0], ))

RESOURCES_MACHINE = getattr(settings, 'DEPLOYUTILS_RESOURCES_SERVER',
                           'git@' + settings.ALLOWED_HOSTS[0])
