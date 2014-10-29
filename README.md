nba-stats
=========

Refer to https://gist.github.com/ltiao/9810719feecccb432b4a for specifics on the structure of this project.

## Setup ##

To get setup for development,

-   Create a `virtualenv`: `mkvirtualenv <env_name>`
-   `workon <env_name>`
-   `git clone https://github.com/ltiao/nba-stats.git <project_root>`
-   `pip install -r requirements.txt`
-   Modify `nba-stats.sublime-project` to set this up as a Sublime Text project
-   Now you can easily access the `postactivate`/`predeactivate` triggers for your `virtualenv`
-   Modify the `postactivate` script:
    
    ```bash
    export PROJECT_ROOT=<project_root>

    # So that Scrapy can use Django models
    export PYTHONPATH="$PROJECT_ROOT/nba_stats/:$PYTHONPATH"

    export DJANGO_SETTINGS_MODULE=nba_stats.settings.local
    export DATABASE_URL=postgres://<username>:<password>@localhost:5432/<db_name>

    echo "Changing current working directory to [$PROJECT_ROOT]..."
    cd $PROJECT_ROOT

    # Start up sublime text project
    echo "Starting up Sublime Text project..."
    subl --project nba-stats.sublime-project
    ```
-   Modify the `predeactivate` script:
    
    ```bash
    unset DJANGO_SETTINGS_MODULE
    unset DATABASE_URL
    ```
-   `deactivate` and then `workon <env_name>` and you should be good to go!

## Tips ##

When running `pip install -r requirements.txt` on a fresh install of Mac OS X 10.9+ 
(Mavericks or Yosemite), you may (probably will) run into the the following issues. 
Here's how to overcome them.

-   When installing `psycopg`, it is not common to get 

    ```
    Error: pg_config executable not found.



    Please add the directory containing pg_config to the PATH

    or specify the full executable path with the option:



        python setup.py build_ext --pg-config /path/to/pg_config build ...



    or with the pg_config option in 'setup.cfg'.
    ```

    Just make sure `postgresql` is installed: `brew install postgresql`

-   Installing `cffi` can be a pain in the neck.
    
    ```
    Package libffi was not found in the pkg-config search path.

    Perhaps you should add the directory containing `libffi.pc'

    to the PKG_CONFIG_PATH environment variable

    No package 'libffi' found

    compiling '_configtest.c':

    __thread int some_threadlocal_variable_42;



    clang -fno-strict-aliasing -fno-common -dynamic -I/usr/local/include -I/usr/local/opt/sqlite/include -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk -I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -c _configtest.c -o _configtest.o

    success!

    removing: _configtest.c _configtest.o

    c/_cffi_backend.c:13:10: fatal error: 'ffi.h' file not found

    #include <ffi.h>

             ^

    1 error generated.
    ```

    First make sure `libffi` is installed: `brew install libffi`.

    Now set the compiler flags 

    ```
    $ export CFLAGS=-Qunused-arguments
    $ export CPPFLAGS=-Qunused-arguments
    $ export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/
    ```

    And try installing again. See [a](http://stackoverflow.com/questions/22875270/error-installing-bcrypt-with-pip-on-os-x-cant-find-ffi-h-libffi-is-installed), [b](http://stackoverflow.com/questions/22703393/clang-error-unknown-argument-mno-fused-madd-wunused-command-line-argumen#comment34658415_22704271).

    Intestingly enough, this is only a workaround to "[...] a change in clang defaults in Xcode 5.1 and Apple not noticing that it would break extension module builds using the system Python." However, this is still a problem with Xcode 6.1 from late October 2014.

-   If your command line tools for XCode are already up to date and installing `lxml` gives you an error like this

    ```
      Running setup.py install for lxml
    /usr/local/Cellar/python/2.7.8_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'bugtrack_url'
      warnings.warn(msg)
    Building lxml version 3.3.5.
    Building without Cython.
    Using build configuration of libxslt 1.1.28
    building 'lxml.etree' extension
    clang -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Qunused-arguments -Qunused-arguments -I/usr/include/libxml2 -I/Users/tiao/.virtualenvs/nba/build/lxml/src/lxml/includes -I/usr/local/Cellar/python/2.7.8_2/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c src/lxml/lxml.etree.c -o build/temp.macosx-10.10-x86_64-2.7/src/lxml/lxml.etree.o -w -flat_namespace
    In file included from src/lxml/lxml.etree.c:346:
    /Users/tiao/.virtualenvs/nba/build/lxml/src/lxml/includes/etree_defs.h:9:10: fatal error: 'libxml/xmlversion.h' file not found
    #include "libxml/xmlversion.h"
             ^
    1 error generated.
    error: command 'clang' failed with exit status 1
    Complete output from command /Users/tiao/.virtualenvs/nba/bin/python2.7 -c "import setuptools, tokenize;__file__='/Users/tiao/.virtualenvs/nba/build/lxml/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /var/folders/6m/np01qkkx5g58_kw6bwpssbjr0000gn/T/pip-utBV4q-record/install-record.txt --single-version-externally-managed --compile --install-headers /Users/tiao/.virtualenvs/nba/bin/../include/site/python2.7:
    /usr/local/Cellar/python/2.7.8_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/distutils/dist.py:267: UserWarning: Unknown distribution option: 'bugtrack_url'
    ```

    Simply install it with `STATIC_DEPS=true pip install lxml`. Refer to [this](http://stackoverflow.com/questions/19548011/cannot-install-lxml-on-mac-os-x-10-9) and an [explanation](http://lxml.de/installation.html#using-lxml-with-python-libxml2).
