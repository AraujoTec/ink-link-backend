from django.http import JsonResponse, FileResponse
from datetime import datetime
from app.settings import MEDIA_ROOT
from app.detalhe_servico.models import Detalhes
from app.detalhe_servico.schemas import DetalheBase
from app.materiais.models import Materiais
from app.servicos.models import Servicos
from app.utils.jwt_manager import authenticate
from app.utils.csv import format_csv, generate_csv

class DetalheService:
    
    def __init__(self, request):
        self.token = authenticate(request)
        self.empresa = self.token.get("empresa_id")
        self.servico = Detalhes.objects.filter(empresa_id=self.empresa)
    
    def _calculos(self, material, servico, payload):
        preco_revenda = material.preco_revenda
        preco_custo = material.custo
        preco_servico = servico.valor
        quantidade = payload.quantidade
        valor_revenda = preco_revenda * quantidade
        valor_custo = preco_custo * quantidade
        
        dados = payload.dict()
        dados["valor_total"] = valor_revenda + preco_servico
        dados["lucro_estudio"] = valor_custo + (preco_servico/2)
        dados["lucro_colaborador"] = preco_servico/2
        
        return dados
    
    def get_servico(self):
        return self.empresa 

    def get_servico_by_id(self, detalhe_id: str):
        return Detalhes.objects.filter(id=detalhe_id, empresa_id=self.empresa) 

    def create_servico(self, payload: DetalheBase):
        material = Materiais.objects.filter(id=payload.materiais_id).first()
        servico = Servicos.objects.filter(id=payload.servico_id).first()
               
        if material.estoque < 0 or payload.quantidade>material.estoque:
            return JsonResponse(data={"erro":"estoque insuficiente"}, status=400)
        
        dados = self._calculos(material, servico, payload)       
               
        detalhes_servico = Detalhes.objects.create(**dados)
        
        material.estoque -= payload.quantidade
                    
        estoque = {"estoque": material.estoque}
        for attr, value in estoque.items():
            setattr(material, attr, value)
        material.save()
        
        if material.estoque <= 10:
            return JsonResponse(data={"sucess": f'{"Serviço criado com sucesso"} - {detalhes_servico.id}', "aviso": "Estoque baixo, verificar!!"}, status=200)  
          
        return JsonResponse(data={"sucess": f'{"Serviço criado com sucesso"} - {detalhes_servico.id}'}, status=200)
    
    def create_csv(self, filters):
        datetime_now = datetime.now()  
        path = f'{MEDIA_ROOT}/{self.empresa}'
        servicos = filters.filter(self.servico)
        dados = format_csv(Servicos)
    
        for itens in servicos:
            valores = [            
                        str(itens.id),  
                        str(itens.servico),
                        str(itens.materiais),
                        str(itens.quantidade),
                        str(itens.valor_total),
                        str(itens.lucro_estudio),
                        str(itens.lucro_colaborador),
                    ]
            dados.append(valores)
        
        generate_csv(path, datetime_now, dados)
        
        return FileResponse(open(f'{path}/reports_{datetime_now}.csv', 'rb'), as_attachment=True)

    def update_servico(self, detalhe_id: str, empresa_id: str, payload: DetalheBase):
        detalhes_servico = self.get_servico_by_id(detalhe_id=detalhe_id, empresa_id=empresa_id)
        for attr, value in payload.dict.items():
            setattr(detalhes_servico, attr, value)
        detalhes_servico.save()
        return JsonResponse(data={"sucess": "Agenda alterada com sucesso"}, status=200)
    
    def delete_servico(self, detalhe_id: str, empresa_id: str):
        detalhes_servico = self.get_servico_by_id(detalhe_id=detalhe_id, empresa_id=empresa_id)
        detalhes_servico.delete()
        return JsonResponse(data={"sucess": "Serviço excluído com sucesso"}, status=200)
