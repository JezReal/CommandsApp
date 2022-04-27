from django.shortcuts import render


# Create your views here.
def commands_index(request):
    return render(request, 'command_index.html')


def commands_list(request):
    # Load your template html that shows the commands list from the database here
    pass
