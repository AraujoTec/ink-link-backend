from django.http import JsonResponse
from app.detalhe_servico.models import Detalhes
from app.detalhe_servico.schemas import DetalheBase
from app.materiais.models import Materiais
from app.servicos.models import Servicos



class DetalheService:
    def get_servico(self):
        return Detalhes.objects.all() 

    def get_servico_by_id(self, detalhe_id: str):
        return Detalhes.objects.filter(id=detalhe_id) 

    def create_servico(self, payload: DetalheBase):
        material = Materiais.objects.filter(id=payload.materiais_id)
        busca_servico = Servicos.objects.filter(id=payload.servico_id).first()
        valor_total=material.first().preco_revenda*payload.quantidade
        
        payload_dict = payload.dict()
        payload_dict["valor_total"] = valor_total + busca_servico.valor
        payload_dict["lucro_estudio"] = (material.first().custo*payload.quantidade) + (busca_servico.valor/2)
        payload_dict["lucro_colaborador"] = busca_servico.valor/2
        
        servico = Detalhes.objects.create(**payload_dict)
        
        estoque_atual = material.first().estoque-payload.quantidade
        if estoque_atual < 0:
            return JsonResponse(data={"erro":"estoque insuficiente"}, status=400)
            
        estoque = {"estoque": estoque_atual}
        for attr, value in estoque.items():
            setattr(material, attr, value)
        material.save()
        
        return JsonResponse(data={"message": "CREATE", "sucess": f'{"Serviço criado com sucesso"} - {servico.id}'}, status=200)
    
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
