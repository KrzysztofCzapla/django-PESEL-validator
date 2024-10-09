from django.shortcuts import render
from .forms import PeselNumberForm

from .utils import get_info_from_pesel


def pesel_view(request):
    if request.method == 'POST':
        form = PeselNumberForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            birth_date, gender = get_info_from_pesel(pesel)
            return render(request, 'peselvalidator/result.html', {
                'valid': True,
                'pesel': pesel,
                'birth_date': birth_date,
                'gender': gender,
            })
    else:
        form = PeselNumberForm()

    return render(request, 'peselvalidator/base.html', {'form': form})
