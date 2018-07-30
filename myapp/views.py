from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            category = form.cleaned_data['category']
            subject = form.cleaned_data['subject']
            body =  form.cleaned_data['body']

            print(name, email, category, subject, body)

    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form})

def snipper_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()

    form = SnippetForm()
    return render(request, 'form.html', {'form': form})
