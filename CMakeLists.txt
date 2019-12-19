# -*- mode: cmake; tab-width: 2; indent-tabs-mode: t; truncate-lines: t
# vim: set filetype=cmake autoindent tabstop=2 shiftwidth=2 noexpandtab softtabstop=2 nowrap:

cmake_minimum_required(VERSION 3.0.1)

# set up project and specify the minimum cmake version
project("opm-grid" C CXX)

# find the build system (i.e., dune-common) and set cmake's module path
find_package(dune-common REQUIRED)
list(APPEND CMAKE_MODULE_PATH ${dune-common_MODULE_PATH})

# include the dune macros
include(DuneMacros)

# start a dune project with information from dune.module
dune_project()

# include the OPM cmake macros
include(OpmMacros)

# find the packages needed to compile the module
find_package(Boost COMPONENTS unit_test_framework REQUIRED)

# make sure that the HAVE_CONFIG_H C macro evaluates to one instead of
# being only defined
get_property(CD_LIST DIRECTORY "." PROPERTY COMPILE_DEFINITIONS)
list(REMOVE_ITEM CD_LIST "HAVE_CONFIG_H")
list(APPEND CD_LIST "HAVE_CONFIG_H=1")
set_property(DIRECTORY "." PROPERTY COMPILE_DEFINITIONS "${CD_LIST}")

# add source files from CMakeLists_files.cmake to
# library libopmgrid.a and create executables
opm_add_headers_library_and_executables("opmgrid")

opm_recusive_copy_testdata_to_builddir("tests/*.data" "tests/*.DATA")

if(dune-python_FOUND)
  add_subdirectory(python)
  dune_python_install_package(PATH "python")
elseif(dune-corepy_FOUND)
  add_subdirectory(python)
  dune_python_install_package(PATH "python")
endif()

# finalize the dune project, e.g. generating config.h etc.
finalize_dune_project(GENERATE_CONFIG_H_CMAKE)
