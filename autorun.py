import os
import sys
import setup_lib

setup_lib.install_prereqs()
setup_lib.copy_configs()
setup_lib.update_main_config_file("RFID Attendance System AP", "n", "300", "y", "8181")