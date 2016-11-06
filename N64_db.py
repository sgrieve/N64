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


def HowMany():
    conn = sqlite3.connect('N64.db')
    conn.text_factory = str

    c = conn.cursor()
    c.execute('SELECT id from games where got=1')

    rows = c.fetchall()
    conn.close()

    return len(rows)


def execute_query(query):
    conn = sqlite3.connect('N64.db')
    conn.text_factory = str

    c = conn.cursor()
    c.execute(query)

    headers = [desc[0] for desc in c.description]
    rows = c.fetchall()
    conn.close()

    return CapitalizeHeader(headers), BinaryConvert(headers, rows)


def CapitalizeHeader(headers):
    headers = [h.title() for h in headers]
    headers = ['ID' if h == 'Id' else h for h in headers]

    return ['Alternate Title(s)' if h == 'Alt_Title' else h for h in headers]


def BinaryConvert(headers, rows):

    if 'got' in headers:
        index = headers.index('got')

        FinalRows = []

        for row in rows:
            tmp = list(row)
            if row[index] == 0:
                tmp[index] = 'No'
            else:
                tmp[index] = 'Yes'
            FinalRows.append(tmp)

        return FinalRows
    else:
        return rows


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


print HowMany()

'''
update_game(game)

queries = {
    'pal': 'select title, year, id, got from games where regions like \"%PAL%\"',
    'all': 'select title, year, id, got from games',
    'got': 'select title, year, id, publisher, genre, got from games where got==1 and regions like \"%PAL%\"',
    'old': 'select title, alt_title, genre, year from games where regions like \"%PAL%\" and year < 1999'
}


for key in queries:
    headers, rows = execute_query(queries[key])
    MakeTable(headers, rows, key)
'''
