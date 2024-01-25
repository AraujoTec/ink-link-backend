from ninja import NinjaAPI
from app.authenticate.api import auth_router
from app.agendamento.api import agendamento_router
from app.cargos.api import cargos_router
from app.clientes.api import clientes_router
from app.usuarios.api import colaborador_router
from app.detalhe_servico.api import detalhes_router
from app.empresas.api import empresas_router
from app.payments.api import payments_router
from app.materiais.api import materiais_router
from app.servicos.api import servicos_router


api = NinjaAPI(csrf=False, title="INK-LINK")

api.add_router("/authenticate/", auth_router)
api.add_router("/agendamento/", agendamento_router)
api.add_router("/cargos/", cargos_router)
api.add_router("/clientes/", clientes_router)
api.add_router("/users/", colaborador_router)
api.add_router("/detalhamento/", detalhes_router)
api.add_router("/empresas/", empresas_router)
api.add_router("/payments/", payments_router)
api.add_router("/materiais/", materiais_router)
api.add_router("/servicos/", servicos_router)

