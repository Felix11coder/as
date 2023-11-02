from django.shortcuts import render, redirect
from .forms import contactForm

def contact_us(request):
    if request.method == 'POST':
        # Assuming you have a form with fields 'name', 'email', and 'message'
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Do something with the form data, e.g., send an email, save to database, etc.

        return render(request, 'submissions.html', {'name': name, 'email': email, 'message': message})
    else:
        return render(request, 'contact_form.html')


# def contact_us(request):
#     if request.method=='POST':
#         form=contactForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             email=form.cleaned_data['email']
#             message=form.cleaned_data['message']
#             return redirect('submissions',name=name, email=email, message=message)
#

    # else:
    #     form=contactForm()
    # return render(request, 'submissions.html', {'name':name, 'email':email, 'message':message})

def submissions(request):
    # Your view logic goes here
    return render(request, 'submissions.html')

