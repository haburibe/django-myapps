from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from photos.forms import EntryForm
from photos.models import Entry


def upload_file(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('photos:upload_file'))
    else:
        form = EntryForm()
    entries = Entry.objects.all().order_by('-pk')
    return render(request, 'photos/upload_file.html',
            {'form': form, 'entries': entries})
