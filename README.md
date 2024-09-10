# gopro_ros

This is assuming that you are using a GoPro connected to an Elgato HD60 X capture card.

## Installation Instructions

1. **Install Requirements**:
     ```sh
     pip install linuxpy
     ```

2. **Clone this repository into your catkin workspace**:
     ```sh
     cd /path/to/catkin_ws/src
     git clone https://github.com/iamlab-cmu/gopro_ros.git
     ```

3. **Build the package using catkin_make or catkin build**:
     ```sh
     cd /path/to/catkin_ws
     catkin_make
     catkin build
     source devel/setup.bash
     ```

## Running Instructions
1. **Start the GoPro Server**:
     ```sh
     rosrun gopro_ros gopro_server.py
     ```