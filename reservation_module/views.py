from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from .forms import ReservationForm
from api_module.models import Reservation
import jdatetime
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin



class ReserveView(LoginRequiredMixin, View):
    template_name = 'reservation_module/reserve_page.html'
    login_url = "login_page"

    def get(self, request):
        form = ReservationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ReservationForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'لطفاً نام، شماره تماس و تاریخ را وارد کنید')
            return render(request, self.template_name, {'form': form})

        date_str = form.cleaned_data.get('date')
        time = form.cleaned_data.get('time')

        if not time:
            messages.error(request, 'لطفاً ساعت رزرو را انتخاب کنید')
            return redirect('reserve_page')

        # تبدیل تاریخ جلالی
        try:
            y, m, d = map(int, date_str.split('/'))
            selected_date = jdatetime.date(y, m, d).togregorian()
        except Exception:
            messages.error(request, 'فرمت تاریخ نامعتبر است')
            return redirect('reserve_page')

        if selected_date < datetime.today().date():
            messages.error(request, 'امکان رزرو برای تاریخ گذشته وجود ندارد')
            return redirect('reserve_page')

        if Reservation.objects.filter(date=date_str, time=time).exists():
            messages.error(request, 'این روز و ساعت قبلاً رزرو شده است')
            return redirect('reserve_page')

        Reservation.objects.create(
            full_name=form.cleaned_data['full_name'],
            phone=form.cleaned_data['phone'],
            date=date_str,
            time=time
        )

        return redirect(
            reverse('reserve_success') + f'?date={date_str}&time={time}'
        )

class ReservedTimesView(View):
    def get(self, request):
        date = request.GET.get('date')
        times = list(
            Reservation.objects.filter(date=date)
                .values_list('time', flat=True)
        )
        return JsonResponse(times, safe=False)


class ReserveSuccessView(View):
    template_name = 'reservation_module/reserve_success.html'

    def get(self, request):
        date = request.GET.get('date')
        time = request.GET.get('time')

        context = {
            'date': date,
            'time': time
        }
        return render(request, self.template_name, context)


