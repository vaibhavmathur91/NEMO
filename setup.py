from setuptools import setup, find_packages

setup(
	name='NEMO',
	version='1.2.0',
	python_requires='>=3.6',
	packages=find_packages(exclude=['NEMO.tests']),
	include_package_data=True,
	url='https://github.com/usnistgov/NEMO',
	license='Public domain',
	author='Dylan Klomparens',
	author_email='dylan.klomparens@nist.gov',
	description='NEMO is a laboratory logistics web application. Use it to schedule reservations, control tool access, track maintenance issues, and more.',
	long_description='Find out more about NEMO on the GitHub project page https://github.com/usnistgov/NEMO',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Science/Research',
		'Intended Audience :: System Administrators',
		'License :: Public Domain',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.6',
	],
	install_requires=[
		'cryptography==2.2.2',
		'Django==1.11.13',
		'django-filter==1.1.0',
		'djangorestframework==3.8.2',
		'ldap3==2.5',
		'python-dateutil==2.7.2',
		'requests==2.18.4',
		'Pillow==5.1.0',
	],
	entry_points={
		'console_scripts': ['nemo=NEMO.provisioning:entry_point'],
	},
)
