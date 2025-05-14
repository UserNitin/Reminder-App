from django.shortcuts import render, redirect
from .forms import ReminderForm
from .models import Reminder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer

def reminder_list(request):
    reminders = Reminder.objects.all().order_by('-date', '-time')
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})

def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminder_success')
    else:
        form = ReminderForm()
    return render(request, 'reminders/create_reminder.html', {'form': form})

@api_view(['POST'])
def api_create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        reminder = serializer.save()
        return Response(ReminderSerializer(reminder).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def reminder_success(request):
    return render(request, 'reminders/success.html')
