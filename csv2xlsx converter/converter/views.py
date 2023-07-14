from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from openpyxl import Workbook
from io import BytesIO

def home(request):
    return render(request, 'converter/home.html')

def convert(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)

        # Create a new workbook
        workbook = Workbook()
        sheet = workbook.active

        # Write the CSV data to the workbook
        for row_data in df.itertuples(index=False):
            sheet.append(row_data)

        # Save the workbook in memory
        output = BytesIO()
        workbook.save(output)
        output.seek(0)

        # Create the HTTP response with the XLSX file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=converted.xlsx'
        response.write(output.getvalue())

        return response

    return render(request, 'converter/home.html')
