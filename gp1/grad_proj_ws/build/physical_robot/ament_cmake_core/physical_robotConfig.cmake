# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_physical_robot_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED physical_robot_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(physical_robot_FOUND FALSE)
  elseif(NOT physical_robot_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(physical_robot_FOUND FALSE)
  endif()
  return()
endif()
set(_physical_robot_CONFIG_INCLUDED TRUE)

# output package information
if(NOT physical_robot_FIND_QUIETLY)
  message(STATUS "Found physical_robot: 0.0.0 (${physical_robot_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'physical_robot' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${physical_robot_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(physical_robot_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${physical_robot_DIR}/${_extra}")
endforeach()
