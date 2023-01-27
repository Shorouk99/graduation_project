from setuptools import setup

package_name = 'sensors_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shorouk',
    maintainer_email='shorouk.magdy1999@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensors_talker = sensors_sim.sensors_pub:main',
            'cmd_vel_talker = sensors_sim.cmd_vel_pub:main',
            'odom_pub = sensors_sim.odom:main',
            'ypr_pub = sensors_sim.quat_to_euler:main',
            'scan_pub = sensors_sim.scan_sub:main',
        ],
    },
)
