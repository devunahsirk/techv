from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def home(request):
    return render(request, 'home.html')


def convert(request):
    if request.method == "POST":
        csv_file = request.FILES['csv_file'] 

        df = pd.read_csv(csv_file)

        # Convert 
        xlsx_file = pd.ExcelWriter('converted_file.xlsx', engine='xlsxwriter')
        df.to_excel(xlsx_file, index=False)
        xlsx_file.close()

        # Response 
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="converted_file.xlsx"'

        with open('converted_file.xlsx', 'rb') as file:
            response.write(file.read())

        return response

   
