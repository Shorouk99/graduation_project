# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/shorouk/graduation_project/no_map_2021/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/shorouk/graduation_project/no_map_2021/build

# Include any dependencies generated for this target.
include amcl/CMakeFiles/amcl_sensors.dir/depend.make

# Include the progress variables for this target.
include amcl/CMakeFiles/amcl_sensors.dir/progress.make

# Include the compile flags for this target's objects.
include amcl/CMakeFiles/amcl_sensors.dir/flags.make

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.o: amcl/CMakeFiles/amcl_sensors.dir/flags.make
amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.o: /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_sensor.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/shorouk/graduation_project/no_map_2021/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.o"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.o -c /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_sensor.cpp

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.i"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_sensor.cpp > CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.i

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.s"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_sensor.cpp -o CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.s

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.o: amcl/CMakeFiles/amcl_sensors.dir/flags.make
amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.o: /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_odom.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/shorouk/graduation_project/no_map_2021/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.o"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.o -c /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_odom.cpp

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.i"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_odom.cpp > CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.i

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.s"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_odom.cpp -o CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.s

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.o: amcl/CMakeFiles/amcl_sensors.dir/flags.make
amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.o: /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_laser.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/shorouk/graduation_project/no_map_2021/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.o"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.o -c /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_laser.cpp

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.i"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_laser.cpp > CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.i

amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.s"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/shorouk/graduation_project/no_map_2021/src/amcl/src/amcl/sensors/amcl_laser.cpp -o CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.s

# Object files for target amcl_sensors
amcl_sensors_OBJECTS = \
"CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.o" \
"CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.o" \
"CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.o"

# External object files for target amcl_sensors
amcl_sensors_EXTERNAL_OBJECTS =

/home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so: amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_sensor.cpp.o
/home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so: amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_odom.cpp.o
/home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so: amcl/CMakeFiles/amcl_sensors.dir/src/amcl/sensors/amcl_laser.cpp.o
/home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so: amcl/CMakeFiles/amcl_sensors.dir/build.make
/home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so: /home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_map.so
/home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so: /home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_pf.so
/home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so: amcl/CMakeFiles/amcl_sensors.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/shorouk/graduation_project/no_map_2021/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared library /home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so"
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/amcl_sensors.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
amcl/CMakeFiles/amcl_sensors.dir/build: /home/shorouk/graduation_project/no_map_2021/devel/lib/libamcl_sensors.so

.PHONY : amcl/CMakeFiles/amcl_sensors.dir/build

amcl/CMakeFiles/amcl_sensors.dir/clean:
	cd /home/shorouk/graduation_project/no_map_2021/build/amcl && $(CMAKE_COMMAND) -P CMakeFiles/amcl_sensors.dir/cmake_clean.cmake
.PHONY : amcl/CMakeFiles/amcl_sensors.dir/clean

amcl/CMakeFiles/amcl_sensors.dir/depend:
	cd /home/shorouk/graduation_project/no_map_2021/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/shorouk/graduation_project/no_map_2021/src /home/shorouk/graduation_project/no_map_2021/src/amcl /home/shorouk/graduation_project/no_map_2021/build /home/shorouk/graduation_project/no_map_2021/build/amcl /home/shorouk/graduation_project/no_map_2021/build/amcl/CMakeFiles/amcl_sensors.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : amcl/CMakeFiles/amcl_sensors.dir/depend

