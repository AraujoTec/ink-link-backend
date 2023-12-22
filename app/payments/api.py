from ninja import Router
from app.payments.service import PaymentService
from app.payments.schemas import PaymentSchema, PaymentSchemaOut
from app.authenticate.service import JWTAuth
from app.utils.jwt_manager import authenticate

payments_router = Router(auth=JWTAuth(), tags=['Formas de Pagamento'])
service = PaymentService ()

#GETS
@payments_router.get("", response=list[PaymentSchemaOut])
def get_payment(request):
    token = authenticate(request)
    response = service.get_payment(empresa_id=token.get("empresa_id"))    
    return response

#POST
@payments_router.post("cargo")
def create_payment(request, payload: PaymentSchema):
    response = service.create_payment(request, payload)
    return response

#DELETE
@payments_router.delete("{payment_id}")
def delete_payment(request, payment_id: str):
    response = service.delete_payment(request, payment_id)
    return response

