# .. cmake_module::
#
# This module's content is executed whenever a Dune module requires or
# suggests opm-grid!
#

# make sure that we get the FindZOLTAN.cmake module from opm-common,
# not that of a random dune module (the version of dune-alugrid seems
# to be buggy)
list(INSERT 0 CMAKE_MODULE_PATH "${opm-grid_MODULE_PATH}")

find_package(ZOLTAN)
if(ZOLTAN_FOUND)
  dune_register_package_flags(
    LIBRARIES "${ZOLTAN_LIBRARIES}"
    INCLUDE_DIRS "${ZOLTAN_INCLUDE_DIRS}")
endif()

find_package(Boost
  COMPONENTS filesystem system date_time
  REQUIRED)
