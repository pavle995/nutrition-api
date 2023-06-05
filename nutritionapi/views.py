from django.http import HttpResponse
import pandas as pd


def index(request):
    df = pd.read_csv("nutritionapi/scripts/nutrients_csvfile.csv")
    json = df.to_json(orient='records')
    return HttpResponse(json)