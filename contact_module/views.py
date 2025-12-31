from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


class ContactView(View):
    template_name = "contact_module/contact_page.html"

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'لطفاً همه فیلدها را به درستی پر کنید')
            return render(request, self.template_name, {'form': form})

        form.save()
        messages.success(
            request,
            'پیام شما با موفقیت ارسال شد. در صورت نیاز با شما تماس گرفته می‌شود 🌸'
        )
        return redirect('contact_page')
