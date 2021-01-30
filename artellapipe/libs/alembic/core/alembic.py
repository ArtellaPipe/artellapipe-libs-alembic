#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions to work with Alembics
"""

from __future__ import print_function, division, absolute_import

import logging

from tpDcc.core import dcc as core_dcc
from tpDcc.core import library, reroute

from artellapipe.libs.alembic.core import consts

LOGGER = logging.getLogger(consts.LIB_ID)


class AlembicLib(library.DccLibrary, object):

    ID = consts.LIB_ID

    def __init__(self, *args, **kwargs):
        super(AlembicLib, self).__init__(*args, **kwargs)

    @classmethod
    def config_dict(cls):
        base_tool_config = library.DccLibrary.config_dict()
        tool_config = {
            'name': 'Alembic Library',
            'id': AlembicLib.ID,
            'supported_dccs': {
                core_dcc.Dccs.Maya: ['2017', '2018', '2019', '2020'],
                core_dcc.Dccs.Houdini: ['18.0.391']
            },
            'tooltip': 'Library to handle Alembics',
            'root': cls.ROOT if hasattr(cls, 'ROOT') else '',
            'file': cls.PATH if hasattr(cls, 'PATH') else '',
        }
        base_tool_config.update(tool_config)

        return base_tool_config


@reroute.reroute_factory(AlembicLib.ID, 'alembic')
def load_alembic_plugin():
    """
    Forces the loading of the Alembic plugin if it is not already loaded
    """

    raise NotImplementedError('load_alembic_plugin function for is not implemented!')


@reroute.reroute_factory(AlembicLib.ID, 'alembic')
def export_alembic(*args, **kwargs):
    """
    Exports Alembic file with given attributes
    """

    raise NotImplementedError('export_alembic function is not implemented!')


@reroute.reroute_factory(AlembicLib.ID, 'alembic')
def import_alembic(
        alembic_file, mode='import', nodes=None, parent=None, fix_path=False, namespace=None, reference=False):
    """
    Imports Alembic into current DCC scene

    :param str alembic_file: file we want to load
    :param str mode: mode we want to use to import the Alembic File
    :param list(str) nodes: optional list of nodes to import
    :param parent:
    :param fix_path: bool, whether to fix path or not
    :param namespace: str
    :param reference: bool, whether to fix path or not
    :return:
    """

    raise NotImplementedError('import_alembic function is not implemented!')
