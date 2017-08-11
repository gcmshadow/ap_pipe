#!/usr/bin/env python

from documenteer.sphinxconfig.stackconf import build_package_configs

import lsst.ap.pipe

_g = globals()
_g.update(build_package_configs(
    project_name="ap_pipe",
    copyright="2017 Association of Univerities for "
              "Research in Astronomy, Inc.",
    version=lsst.ap.pipe.version.__version__,
    doxygen_xml_dirname=None))

intersphinx_mapping['astropy'] = ('http://docs.astropy.org/en/stable', None)

# DEBUG only
automodsumm_writereprocessed = False
