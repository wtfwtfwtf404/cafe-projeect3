from django.http import JsonResponse
from .models import Order
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            name = data.get("name")
            phone = data.get("phone")
            raw_date = data.get("date")
            raw_time = data.get("time")
            guests = data.get("guests")
            zone = data.get("zone")

#Проверка на пустые поля
            if not all([name, phone, raw_date, raw_time, guests, zone]):
                return JsonResponse({"error": "Все поля обязательны"}, status=400)

#преобразование даты
            date = datetime.strptime(raw_date, "%d.%m.%Y").date() #%d

#преобразование времени
            time = datetime.strptime(raw_time, "%H:%M").time()


            Order.objects.create(
                name=name,
                phone=phone,
                date=date,
                time=time,
                guests=guests,
                zone=zone
            )
            print(
                f"\n НОВЫЙ ЗАКАЗ!\n"
                f"Имя: {name}\n"
                f"Телефон: {phone}\n"
                f"Дата: {raw_date}\n"
                f"Время: {raw_time}\n"
                f"Гости: {guests}\n"
                f"Зона: {zone}\n"
                f"----------------------"
            )

            return JsonResponse({"message": "Бронь создана"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Только POST запрос"}, status=405)



def get_orders(request):
    if request.method == "GET":
        orders = Order.objects.all()

        data = []
        for o in orders:
            data.append({
                "id": o.id,
                "name": o.name,
                "phone": o.phone,
                "date": str(o.date),
                "time": str(o.time),
                "guests": o.guests,
                "zone": o.zone
            })

        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "Только GET запрос"}, status=405)




# from django.http import JsonResponse

# def create_order(request):
#     return JsonResponse({"ok": True})

# def get_orders(request):
#     return JsonResponse([])