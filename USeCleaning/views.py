from django.shortcuts import render, redirect
from django.contrib import messages
def USeCleaning(request):
    return render(request, 'USeCleaning.html')

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')


from .models import Booking
from .utils.google_calendar import create_calendar_event
from datetime import datetime, timedelta

def booking_page(request):
    if request.method == "POST":
        service_type = request.POST['service_type']
        rooms = request.POST['rooms']
        bathrooms = request.POST['bathrooms']
        date = request.POST['date']
        time = request.POST['time']
        address = request.POST['address']

        start_dt = datetime.strptime(
            f"{date} {time}", "%Y-%m-%d %H:%M"
        )
        end_dt = start_dt + timedelta(hours=3)

        # 1️⃣ Create Google Calendar event
        event = create_calendar_event(
            summary=f"Cleaning Service – {service_type}",
            description=f"""
Service: {service_type}
Rooms: {rooms}
Bathrooms: {bathrooms}
Address: {address}
""",
            start_datetime=start_dt.isoformat(),
            end_datetime=end_dt.isoformat()
        )

        # 2️⃣ Save to database
        Booking.objects.create(
            service_type=service_type,
            rooms=rooms,
            bathrooms=bathrooms,
            date=date,
            time=time,
            address=address,
            calendar_event_id=event.get('id')
        )

        return redirect('booking')

    return render(request, 'booking.html')
