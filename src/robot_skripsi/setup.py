import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'robot_skripsi'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hardson',
    maintainer_email='fx.hardson@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "Str_pico0_server = robot_skripsi.Str_pico0_server:main",
            #"Str_pico1_server = robot_skripsi.Str_pico1_server:main",
            "teleop_key_move = robot_skripsi.teleop_key_move:main",
            "Str_coms_client = robot_skripsi.Str_coms_client:main"
        ],
    },
)