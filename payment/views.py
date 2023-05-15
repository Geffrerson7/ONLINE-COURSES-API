from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import mercadopago
import json
from rest_framework.permissions import IsAuthenticated
import traceback
from django.db import transaction
from course.models import Course

@transaction.atomic
def create_courses(items, user):
    courses = []
    for item in items:
        course = Course(
            product_code=item["product_code"],
            type=item["type"],
            name=item["name"],
            image=item["image"],
            description=item["description"],
            price=item["price"],
            user=user
        )
        courses.append(course)
    Course.objects.bulk_create(courses)

class ProcessPaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            request_values = json.loads(request.body)
            
            payment_data = {
                "transaction_amount": float(request_values["transaction_amount"]),
                "token": request_values["token"],
                "installments": int(request_values["installments"]),
                "payment_method_id": request_values["payment_method_id"],
                "issuer_id": request_values["issuer_id"],
                "payer": {
                    "email": request_values["payer"]["email"],
                    "identification": {
                        "type": request_values["payer"]["identification"]["type"],
                        "number": request_values["payer"]["identification"]["number"],
                    },
                },
            }

            sdk = mercadopago.SDK(str(settings.YOUR_ACCESS_TOKEN))

            payment_response = sdk.payment().create(payment_data)

            payment = payment_response["response"]
            status = {
                "id": payment["id"],
                "status": payment["status"],
                "status_detail": payment["status_detail"],
                "captured": payment["captured"],
            }
            
            #Guardar curso comprado
            additional_info = request_values.get("additional_info")
            items = additional_info.get("items") if additional_info else []
            create_courses(items, request.user)

            return Response(data={"body": status, "statusCode": payment_response["status"]}, status=201)
        except Exception as e:
            print("Ocurrió un error:", e)
            print("Traceback completo:")
            traceback.print_exc()
            return Response(data={"body": payment_response}, status=400)
