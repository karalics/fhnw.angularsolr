from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='fhnw.angularsolr',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Davide Moro',
      author_email='davide.moro@gmail.com',
      url='https://github.com/karalics/fhnw.angularsolr',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fhnw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone

      [console_scripts]
      fhnw.angularsolr_clone = fhnw.angularsolr.scripts:fhnw.angularsolr_clone
      """,
      )
