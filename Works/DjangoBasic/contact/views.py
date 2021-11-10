from django import forms
from django.shortcuts import redirect, render
from . forms import ContactForm
from contact.utils.validators import ValidationError
from django.contrib import messages


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfuly registration!')
            return redirect('/contact')
        else:
            messages.add_message(request, messages.INFO, 'Your mail is not valid!')
        
    return render(request, 'contact.html', {'form': form})