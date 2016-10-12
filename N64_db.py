# -*- coding: utf-8 -*-
import csv
import sqlite3
import os
import simpletable as st


def build_db():

    conn = sqlite3.connect('N64.db')
    conn.text_factory = str

    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE games
                 (id integer, title text, alt_title text, year integer,
                  developer text, publisher text, regions text, players text,
                  genre text, got integer)''')

    with open('N64_cleaned.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')

        for i, row in enumerate(reader):
            # Insert a row of data, skipping the header
            if 'Title(s)' not in row[0]:
                row = [i] + row[:7] + row[8:]
                c.executemany('insert into games values (?,?,?,?,?,?,?,?,?,?)',
                              (row,))

    conn.commit()
    conn.close()


def update_game(ID):
    conn = sqlite3.connect('N64.db')
    conn.text_factory = str

    c = conn.cursor()

    c.execute('UPDATE games SET got=1 where id=(?)', (ID,))
    conn.commit()
    conn.close()


def execute_query(query):
    conn = sqlite3.connect('N64.db')
    conn.text_factory = str

    c = conn.cursor()
    c.execute(query)

    headers = [desc[0] for desc in c.description]
    rows = c.fetchall()
    conn.close()

    return headers, rows


def MakeTable(headers, data, filename):

    css = """
    table.mytable {
        font-family: times;
        font-size:18px;
        color:#000000;
        border-width: 1px;
        border-color: #eeeeee;
        border-collapse: collapse;
        background-color: #ffffff;
        width=100%;
        max-width:550px;
        table-layout:fixed;
    }
    table.mytable th {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #eeeeee;
        background-color: #e6eed6;
        color:#000000;
    }
    table.mytable td {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #eeeeee;
    }
    """

    table = st.SimpleTable(data, header_row=headers, css_class='mytable')

    page = st.HTMLPage(tables=[])
    page.add_table(table)
    page.css = css
    page.save('{0}.html'.format(filename))


# update_game(23)

queries = {
    'pal': 'select title, year, id, got from games where regions like \"%PAL%\"',
    'got': 'select title, year, id, publisher, genre from games where got==1 and regions like \"%PAL%\"',
    'old': 'select title, alt_title, genre, year from games where regions like \"%PAL%\" and year < 1999'
}


for key in queries:
    headers, rows = execute_query(queries[key])
    MakeTable(headers, rows, key)
