import os

from setuptools import setup

ROOT = os.path.dirname(os.path.realpath(__file__))

setup(
    # Meta data
    name='grab',
    version='0.6.41',
    author='Gregory Petukhov',
    author_email='lorien@lorien.name',
    maintainer='Gregory Petukhov',
    maintainer_email='lorien@lorien.name',
    url='http://grablib.org',
    description='Web Scraping Framework',
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    download_url='https://pypi.python.org/pypi/grab',
    keywords='pycurl multicurl curl network parsing grabbing scraping'
             ' lxml xpath data mining',
    license='MIT License',
    # Package files
    packages=[
        'grab',
        'grab.script',
        'grab.spider',
        'grab.spider.cache_backend',
        'grab.spider.queue_backend',
        'grab.spider.network_service',
        'grab.transport',
        'grab.util',
    ],
    include_package_data=True,
    # Dependencies
    install_requires=[
        'weblib>=0.1.28',
        'six',
        'user_agent',
        'selection',
        'lxml;platform_system!="Windows"',
        'pycurl==7.44.1;platform_system!="Windows"',
        'defusedxml',
    ],
    extras_require={
        'full': ['urllib3', 'certifi'],
    },
    # Topics
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
