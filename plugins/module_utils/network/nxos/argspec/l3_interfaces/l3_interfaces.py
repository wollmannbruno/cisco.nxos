#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the nxos_l3_interfaces module
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type


class L3_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_l3_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "elements": "dict",
            "options": {
                "dot1q": {"type": "int"},
                "ipv4": {
                    "elements": "dict",
                    "options": {
                        "address": {"type": "str"},
                        "secondary": {"type": "bool"},
                        "tag": {"type": "int"},
                    },
                    "type": "list",
                },
                "ipv6": {
                    "elements": "dict",
                    "options": {
                        "address": {"type": "str"},
                        "tag": {"type": "int"},
                    },
                    "type": "list",
                },
                "name": {"required": True, "type": "str"},
                "redirects": {"type": "bool"},
                "unreachables": {"type": "bool"},
            },
            "type": "list",
        },
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
