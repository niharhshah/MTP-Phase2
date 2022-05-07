cmake_minimum_required(VERSION 3.1.0)

project(hello)

# Find librealsense2 installed package
find_package(realsense2 REQUIRED)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Add the application sources to the target
# add_executable(${PROJECT_NAME} frameread.cpp ../example.hpp)
include_directories (/home/nihar/Realsense/librealsense/third-party/)
#     include_directories(../ /home/nihar/Realsense/librealsense/third-party/glfw/include/ )


# # Link librealsense2 to the target
# target_link_libraries(${PROJECT_NAME} ${realsense2_LIBRARY} ${DEPENDENCIES} )



# License: Apache 2.0. See LICENSE file in root directory.
# Copyright(c) 2019 Intel Corporation. All Rights Reserved.
#  minimum required cmake version: 3.1.0
# cmake_minimum_required(VERSION 3.1.0)

# project(Nihar)

# if(BUILD_GRAPHICAL_EXAMPLES)
add_executable(rs-nihar-capture frameread.cpp ../example.hpp)
    set_property(TARGET rs-nihar-capture PROPERTY CXX_STANDARD 11)
    target_link_libraries(rs-nihar-capture ${DEPENDENCIES})
    include_directories(../ ../../third-party/tclap/include ../../examples)
    set_target_properties (rs-nihar-capture PROPERTIES FOLDER "Examples")

    install(TARGETS rs-nihar-capture RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
# endif()