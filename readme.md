# PostgreSQL Performance Farm

This repository contains the code for the PostgreSQL Performance Farm, aiming to collect Postgres performance data through a Python script, outputting results on a JSON file. Results are then being sent to a Django-REST application and browsed with a Vue.js website on top of it.

----

### Structure

- *pgperffarm-front-end*: directory containing Javascript (Vue) source code.
- *client*: directory containing Python script to collect performance results.
- *rest_api*: directory containing the Django-REST API that forms the basis of the website.

This application is part of the Google Summer of Code project, please consult the license file for necessary grants.


### Requirements

The Performance Farm requires:

- osX or any Linux based distribution (note that the Python script will be unable to collect Linux information on osX);
- Python 3.5 or later (and pip3);
- Node 8.12 or later;
- Django 1.11.17 (later version is also possible, but may involve tuning.);
- Postgres 11 or later (while it should work with 9-10);
- Collectd 5.9 or later.
