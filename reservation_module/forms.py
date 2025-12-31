from django import forms
from api_module.models import Reservation


class ReservationForm(forms.ModelForm):
    # ⏰ ساعت از طریق دکمه‌ها ست میشه
    time = forms.CharField(
        required=False,   # خیلی مهم
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Reservation
        fields = ['full_name', 'phone', 'date', 'time']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره تماس'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control jalali-datepicker',
                'autocomplete': 'off',
                'placeholder': 'انتخاب تاریخ'
            }),
        }

    def validate_unique(self):
        """
        ⛔ جلوگیری از validate خودکار unique_together (date + time)
        چون تداخل رو دستی توی View مدیریت می‌کنیم
        """
        pass




