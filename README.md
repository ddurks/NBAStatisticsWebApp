We have organized our code as follows.
    finalproject - 4 django files
        init.py - application initialization
        settings.py - definition of global project settings (db config, port config, etc.)
        urls.py - definition of routes in application
        wsgi.py - application helper file
    manage.py - wrapper file for all django functionalities
    myprojectenv - folder of virtualenv files
    nbastats - django files
        migrations - db migration utilities
        admin.py - django admin functions
        apps.py - app name definition
        models.py - defines models for postgres
        views.py - defines views for django app
    runserver.sh - custom server running script
    static - folder of static files
    templates - folder of view templates
        home.html - home screen
        player.html - individual player page
        players.html - player list page
        team.html - individual team page
        teams.html - team list page
    web_scraping - folder containing image scraping scripts for player and team images

The algorithm used to determine the best season for each player is as follows:
BESTSEASON = (PER * 0.3) + (PPG * 0.3) + (winshares * 0.3) + effectiveFieldGoal% + (RBD/game * 0.2) + (AST/game * 0.2) + (STL/game * 0.1) + (BLK/game * 0.1) - (TOV/game * 0.1)