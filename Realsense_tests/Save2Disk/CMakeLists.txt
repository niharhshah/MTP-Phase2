cmake_minimum_required(VERSION 3.1.0)

project(Save2Disk)

# Find librealsense2 installed package
find_package(realsense2 REQUIRED)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
# Add the application sources to the target
add_executable(${PROJECT_NAME} Savetodisk.cpp)
set_property(TARGET Save2Disk PROPERTY CXX_STANDARD 11)
target_link_libraries(Save2Disk ${DEPENDENCIES})
include_directories(/home/slam/librealsense/common /home/slam/librealsense/third-party)
include_directories(/home/slam/librealsense/third-party/tcap/include) 
# Link librealsense2 to the target
target_link_libraries(${PROJECT_NAME} ${realsense2_LIBRARY})

