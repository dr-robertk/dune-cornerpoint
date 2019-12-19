from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import logging
logger = logging.getLogger(__name__)

from dune.common.checkconfiguration import assertHave, ConfigurationError

try:
    assertHave("HAVE_OPM_GRID")

    def polyhedralGrid(domain, dimgrid=None, ctype="double"):
        from ..grid.grid_generator import module, getDimgrid

        if dimgrid is None:
            dimgrid = getDimgrid(domain)

        typeName = "Dune::PolyhedralGrid< " + str(dimgrid) + ", " + str(dimgrid) + ", " + ctype + " >"
        includes = ["opm/grid/polyhedralgrid.hh", "opm/grid/polyhedralgrid/dgfparser.hh"]
        gridModule = module(includes, typeName)

        return gridModule.LeafGrid(gridModule.reader(domain))

    grid_registry = {
        "Polyhedral" : polyhedralGrid
    }

except ConfigurationError:
    grid_registry = {}
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

