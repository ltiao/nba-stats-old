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
