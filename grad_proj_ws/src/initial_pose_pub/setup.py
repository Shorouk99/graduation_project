from setuptools import setup

package_name = 'initial_pose_pub'

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
    maintainer='Shorouk Magdy',
    maintainer_email='shorouk.magdy.anwar@gmail.com',
    description='Publish initial pose after 15 seconds from launching',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = initial_pose_pub.initial_pose:main',
        ],
    },
)
