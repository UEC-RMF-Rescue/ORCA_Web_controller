from setuptools import setup
import os
from glob import glob

package_name = 'orca_web_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shunsuke',
    maintainer_email='shunsuke@todo.todo',
    description='ORCA Web Controller',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'orca_web_controller = orca_web_controller.orca_web_controller:main',
            'websocket_server = orca_web_controller.websocket_server:main',
        ],
    },
)
