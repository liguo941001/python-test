from setuptools import setup

setup(
    name='qzjg_back',
    version='',
    packages=['home', 'home.migrations', 'user', 'user.migrations', 'apps', 'apps.home', 'apps.home.migrations',
              'apps.user', 'apps.user.migrations', 'libs', 'utils', 'settings'],
    package_dir={'': 'qzjg_back/apps'},
    url='',
    license='',
    author='世界尽头与冷酷仙境',
    author_email='',
    description=''
)
