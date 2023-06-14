from django.http import HttpResponse
import pandas as pd
import sqlite3 as sl
import json


def index(request):
    df = pd.read_csv("nutritionapi/scripts/nutrients_csvfile.csv")
    json = df.to_json(orient='records')
    return HttpResponse(json)


def list(request):
    con = sl.connect('nutrition.db')

    cursor = con.execute("SELECT * FROM nutritients")
    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    # Build a list of dictionaries
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))

    # Convert the list to JSON
    json_data = json.dumps(data)

    return HttpResponse(json_data)

def categories(request):
    con = sl.connect('nutrition.db')

    cursor = con.execute("SELECT DISTINCT Category as categories FROM nutritients")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append(row[0])

    json_data = json.dumps(data)

    return HttpResponse(json_data)