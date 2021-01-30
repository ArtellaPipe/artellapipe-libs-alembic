#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions to work with Alembics
"""

from __future__ import print_function, division, absolute_import

import os
import logging

from tpDcc import dcc

from artellapipe.utils import exceptions

from artellapipe.managers import files
from artellapipe.libs.alembic.core import consts

logger = logging.getLogger(consts.LIB_ID)


def import_alembic(alembic_file, mode='import', nodes=None, parent=None, fix_path=False, reference=False):
    """
    Imports Alembic into current DCC scene

    :param str alembic_file: file we want to load
    :param str mode: mode we want to use to import the Alembic File
    :param list(str) nodes: optional list of nodes to import
    :param parent:
    :param fix_path: bool, whether to fix path or not
    :param reference: bool,
    :return:
    """

    if not os.path.exists(alembic_file):
        logger.error('Given Alembic File: {} does not exists!'.format(alembic_file))
        dcc.client().confirm_dialog(
            title='Error',
            message='Alembic File does not exists:\n{}'.format(alembic_file)
        )
        return None

    logger.debug(
        'Import Alembic File (%s) with job arguments:\n\t(alembic_file) %s\n\t(nodes) %s', mode,
        alembic_file, nodes)

    res = None
    try:
        if fix_path:
            abc_file = files.fix_path(alembic_file)
        else:
            abc_file = alembic_file

        if not parent:
            logger.warning('Impossible to import Alembic File because not Alembic parent given!')
            return False
        parent.parm('fileName').set(abc_file)
        build_hierarch_param = parent.parm('buildHierarchy')
        if build_hierarch_param:
            build_hierarch_param.pressButton()

    except RuntimeError as exc:
        exceptions.capture_sentry_exception(exc)
        return res

    logger.debug('Alembic File %s imported successfully!', os.path.basename(alembic_file))
    return res
