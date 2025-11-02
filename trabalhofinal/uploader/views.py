from django.shortcuts import render, redirect
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']

        try:
            df = pd.read_csv(csv_file)
            df_json = df.to_json(orient='split')
            request.session['dataframe'] = df_json
            return redirect('analysis')
        except Exception as e:
            return render(request, 'uploader/upload.html', {'error': str(e)})

    return render(request, 'uploader/upload.html')

def analysis_view(request):
    return render(request, 'uploader/analysis.html')

def prediction_view(request):
    return render(request, 'uploader/prediction.html')