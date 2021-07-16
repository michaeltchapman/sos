# Copyright (C) 2021 Red Hat, Inc., Michael Chapman <michapma@redhat.com>

# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import Plugin, RedHatPlugin
#from sos.report.plugins import Plugin, IndependentPlugin


class Unbound(Plugin, RedHatPlugin):

    short_desc = 'Unbound'

    plugin_name = 'unbound'
    profiles = ('openstack', 'openstack_controller', 'services', 'network')

    container_conf = "/var/lib/config-data/ansible-generated/unbound/tripleo-base-unbound.conf"
    unbound_conf = '/etc/unbound.conf'

    packages = ('unbound')

    def setup(self):
        if (self.container_exists('unbound')):
            cmd = self.fmt_container_copy('unbound', '/etc/unbound/', self.get_cmd_output_path())
            self.add_cmd_output(cmd)

# vim: set et ts=4 sw=4 :
