import csv, os

def format_csv(model):
    return [[field.name for field in model._meta.fields],]

def generate_csv(path, datetime_now, dados):
    
    if not os.path.exists(path):  
            os.makedirs(path)
                           
    with open(f'{path}/reports_{datetime_now}.csv','w') as arquivo:
        material_reports = csv.writer(arquivo)
        material_reports.writerows(dados)
        
        
        
        
    