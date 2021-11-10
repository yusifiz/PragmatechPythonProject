from django import forms
from django.shortcuts import redirect, render
from . forms import ContactForm
from contact.utils.validators import ValidationError



def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'contact.html', {'form': form})