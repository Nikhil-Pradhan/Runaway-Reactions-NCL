import mysql.connector as sql
from openpyxl import load_workbook

data_file = 'Reaction components.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file, data_only=True)

# Load one worksheet.
ws = wb['Master_rxn']
all_rows = list(ws.rows)


mydb = sql.connect(host="localhost", user="root", passwd="", database="RunawayReactions")
my_cursor = mydb.cursor()


def insert_reactions():
    for row in all_rows[1:126]:
        i = 0;
        while i < 18:
            if str(row[i].value) == "None" or str(row[i].value) == "NaN":
                if i == 0 or i == 6:
                    row[i].value = "NULL"
                else:
                    row[i].value = ""
            i += 1
        query = "insert into products_reactions (reaction_id, reaction_desc, reactants, products, yield_percent, additional_products, steps, stages, reagents, catalyst, solvents, conditions, time, temp, pressure, Lit_ref, endo_exo, cas_member_method) values ("
        query += str(row[0].value) + ", '" + str(row[1].value) + "', '" + str(row[2].value) + "', '" + str(row[3].value) + "', '" + str(row[4].value) + "', '" + str(row[5].value) + "', " + str(row[6].value)
        i = 7
        while i < 18:
            query += ", '" + str(row[i].value) + "'"
            i += 1
        query += ");"
        my_cursor.execute(query)
        mydb.commit()


insert_reactions()
