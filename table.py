import simpletable as st

css = """
table.mytable {
    font-family: times;
    font-size:12px;
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
#code {
    display:inline;
    font-family: courier;
    color: #3d9400;
}
#string {
    display:inline;
    font-weight: bold;
}
"""

data = [('Aidyn Chronicles: The First Mage', 8, 0), ('Animal Crossing', 14, 0), ('Bomberman 64', 39, 0), ("Conker's Bad Fur Day", 63, 0), ('Dr. Mario 64', 85, 0), ('Hamster Monogatari 64', 125, 0), ('Jikkyo Powerful Pro Yakyu Basic-ban 2001', 157, 0), ('Madden NFL 2002', 176, 0), ('NFL Blitz Special Edition', 230, 0), ('PowerpThe Powerpuff Girls: Chemical X-traction', 265, 0), ('Razor Freestyle Scooter', 281, 0), ("Tony Hawk's Pro Skater 2", 339, 0), ("Tony Hawk's Pro Skater 3", 340, 0)]

table1 = st.SimpleTable(data,
                        header_row=['Name', 'ID', 'Got'],
                        css_class='mytable')

page = st.HTMLPage()
page.add_table(table1)
page.css = css
page.save("test.html")
