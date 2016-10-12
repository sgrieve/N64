N64
---

A python and sqlite database of every released N64 game. Data scraped from [this](https://en.wikipedia.org/wiki/List_of_Nintendo_64_games) wikipedia article. This repo contains code to generate simple html pages from the database to display different subsets of the data.

`N64.py` cleans the data using some horrible hacks to create the N64_cleaned.csv, ready to be loaded into the database.

`N64_db.py` contains all of the database code to build the db and perform operations with it.

The html output is generated using the simpletable library, grabbed from [here](https://github.com/matheusportela/simpletable).
