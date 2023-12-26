from django.http import JsonResponse
from app.detalhe_servico.models import Detalhes
from app.detalhe_servico.schemas import DetalheBase
from app.materiais.models import Materiais
from app.servicos.models import Servicos



class DetalheService:
    
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
        return Detalhes.objects.all() 

    def get_servico_by_id(self, detalhe_id: str):
        return Detalhes.objects.filter(id=detalhe_id) 

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
        
        return JsonResponse(data={"message": "CREATE", "sucess": f'{"Serviço criado com sucesso"} - {detalhes_servico.id}'}, status=200)
    
    def update_servico(self, detalhe_id: str, payload: DetalheBase):
        servico = self.get_servico_by_id(id=detalhe_id)
        for attr, value in payload.dict.items():
            setattr(servico, attr, value)
        servico.save()
        return JsonResponse(data={"message": "UPDATE", "sucess": "Agenda alterada com sucesso"}, status=200)
    
    def delete_servico(self, detalhe_id: str):
        detalhe = Detalhes.objects.filter(id=detalhe_id)
        detalhe.delete()
        return JsonResponse(data={"message": "DELETE", "sucess": "Serviço excluído com sucesso"}, status=200)
