## Data science demo for conferences

This repo contains the code for building the data science demos for DataSpell and PyCharm using the feature trainer. The full instructions for building these demos is [here](https://docs.google.com/document/d/1oDulMihLGZ4iJQ0XeZ6-DdVLqlAwMH8O0NyfxOC0C1Y/edit?usp=sharing).

## Set up

### Dependencies
The dependencies for this project are contained in the `requirements.txt` file. These can be automatically imported into a virtualenv using the IDEs. Instructions are [here](https://www.jetbrains.com/help/pycharm/managing-dependencies.html).

### Setting up and connecting to the database
Part of the demo shows off the _Database_ tool window. This part of the demo depends on a PostgreSQL database running locally in a Docker container. The instructions to set this up are below:
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and make sure it is running by opening the application.
2. In a terminal window, navigate to the directory containing this repo.
3. Run `docker-compose up`. This will execute `docker-compose.yml` and create the container with the PostgreSQL database.
4. Run `insert_airlines_into_postgres.py`. This will insert the airlines dataset into the database.
5. Connect to the database using the _Database_ tool window in PyCharm/DataSpell. Go to _Database | New | Data Source | PostgreSQL_.   
6. Under the _General_ tab, leave _Host_ as “localhost”, enter “jetbrains” as the User, “jetbrains” as the Password, and under _Database_ enter “demo”. If you are asked to install the drivers, go ahead and do so. Click _Test Connection_ to check it worked (it should), and then click “OK”.
7. You should now see a new Database connection called `demo@localhost`. Expand `demo`, `public`, `tables` and finally `airlines` so you can show how the database introspection shows database contents down to the table level for the demo. If the airlines table is not there immediately, click _Refresh_ and it will turn up eventually.

## Other instructions

All other instructions for the demos are in the Google docs document. Ping @jodie.burchell on Slack if you have any other questions.