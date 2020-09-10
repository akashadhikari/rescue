from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import HelpCenter, Help, SomeoneNeedsHelp
from .forms import HelpCenterForm


# List all help centers and home view
def index(request):
    help_centers = HelpCenter.objects.all()
    context = {
        'help_centers': help_centers,
    }
    return render(request, 'connect/index.html', context)


# Show particular help center
def center(request, pk):
    center = get_object_or_404(HelpCenter, pk=pk)
    help_center = HelpCenter.objects.filter(pk=pk)
    context = {
        'center': center,
        'help_center': help_center,
    }
    return render(request, 'connect/center.html', context)


# Add particular help center
def add_help_center(request):
    form = HelpCenterForm(request.POST or None)
    context = {
        "help_center_form": form,

    }
    if form.is_valid():
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        description = request.POST.get('description')
        needs = request.POST.getlist('needs')

        new_help_center = HelpCenter.objects.create(
            name=name, 
            contact=contact, 
            address=address, 
            description= description,
            )
        new_help_center.needs.add(*needs)


        new_help_center.save()
        if request.method == 'POST':
            return redirect(reverse('connect:index'))
    return render(request, "connect/add_help_center.html", context)


# List all needs
def show_needs(request):
    helps = SomeoneNeedsHelp.objects.all().order_by('id')
    context = {
        'helps': helps
    }
    return render(request, "connect/need_help.html", context)

# add particular need
def add_need(request):
    pass


# add particular help
def add_help(request):
    pass


# list all helps
def show_helps(request):
    pass