from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def registration(request):
    '''View function to register new users'''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, 'Account created successfully!')
            return redirect('homepage')
            
    else:
        form= RegistrationForm()
    title='Create New Account'
    context = {
        'form' : form,
        'title' : title,
    } 
    if request.user.is_authenticated:
        return redirect('homepage')
   
    return render(request, 'registration/registration.html', context)    