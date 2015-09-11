# download the ez_setup file from [https://bootstrap.pypa.io/ez_setup.py]
# and add it to the directory of your package.
# It will install setuptools if it is not already installed
# or update it to the correct version if it is.
# Then add the two next lines at the head of your setup script.
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages


setup(
	# name of your package 
    name = "NANOGravData",
    
    
    # add versionning for your package
    version = "0.1",
       
       
    # requirements: list here all the dependancies for the package 
    install_requires = [
        "Flask==0.10.1",
        "Flask-Script==2.0.5",
        "marshmallow==2.0.0b3",
    ],
    
    
    # this allows you to add optional requirements for your project
    # that are used in certain conditions. 
    # For example, a project might offer optional reStructuredText
    # support if docutils is installed.
    extra_requires={'reST': ["docutils>=0.3"],},
    
    
    # specify dependencies that need to be present in order
    # for the setup.py script to run
    setup_requires=['some_package','another_package'],
    
    
    # find_packages will include all the packages
    # that are in the same directory as the setup.py script
    # if a source is not define.
    # find_packages() walks the target directory,
    # filtering by inclusion patterns,
    # and finds Python packages (any directory).  
    # On Python 3.2 and earlier, packages are only recognized
    # if they include an __init__.py file.  
    # Organising your packages in a single package simplifies
    # the use of the find_packages function  
    packages = find_packages(),
    
    
    # You can specify the source for the directory to look packages in.
    # You need this if you use find_packages('scr')
    package_dir = {'':'scr'},
    
    
    # if you haven't used the Manifest.in file, this allows you
    # to list manually all the files to include
    package_data = {'templates': ['*.html']},
    
    
    # You can include other files that are not in any of the packages.
    # To use if you haven't followed the package tree structure
    # suggested above and/or have files that you would like to include 
    # but that are not in any of the other packages.
    # You can specify the directory name where the data files will
    # be installed
    data_files = [('name_of_new_dir', ['file.py', 'other_files.txt',])],
     
                                 
    # tell setuptools to install any data files it finds in your packages
    # and in the Manifest.in                              
    include_package_data = True,
    
    
    # specifies files to exclude when a package is installed, 
    # even if they would otherwise have been included 
    # by include_package_data or package_data.
    exclude_package_data = {'':['*.7z', '*.dmg', '*.gz','*.iso'
                                , '*.jar', '*.rar', '*.tar', '*.zip', '*.',
                            'data': ['settings.cfg'],
                            },
     
                            
    # Scripts are files containing Python source code,
    # intended to be started from the command line.
    # This allows you to list files to run as scripts
    scripts = ['manage.py'],
    
    
    # A preferred script tool is the 'console_scripts' entry point.
    # Syntax: "command_to_create = package.module:fonction".
    entry_points = {'consolee_scripts':
                        ['routes = auth_files.manage:list_routes()']},


    # metadata for your project.
    # Will be included in the PKG-INFO
    author = "Me",
    author_email = "me@nanogra.org",
    license = "",
    keywords = "NANOGravData",
    url = "http://data.nanograv.org",
    long_description = open('README.md').read(),
    download_url = "",
    
    
    # metadata
    classifiers=[    
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'License :: OSI Approved :: Academic Free License (AFL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.4',
    ],
    
    
    # if zip_safe is set to True: it will install the packages as egg files
    # if set to false : the project will be installed as a directory 
    zip_safe = False, 
     
     
    # to add dependancies that are not registered in PyPI
    # You can list the urls to download the needed packages from.
    dependency_links = ["http://www.site.com/downlaods/"],
    
    
    # specify the test suite to run
    test_suite = "my_package.tests.test_all",
    
    
    # list additional packages needed for the package's tests to run
    tests_require = ['pytest'],
    
    
    # specify other ways to find tests to run
    test_loader = "",
    
       
    # to convert your Python 2 source code to Python 3      
    use_2to3 = {''},    
    convert_2to3_doctests ={''},
    
    
    # modules to search for additional fixers to be used 
    # during the 2to3 conversion    
    use_2to3_fixers = {''},    
)

