from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from upload.forms import InvoiceForm



def image_upload(request):
    if request.method == "POST":# and request.FILES["image_file"]:
        #image_file = request.FILES["image_file"]
        #fs = FileSystemStorage()
        #filename = fs.save(image_file.name, image_file)
        #image_url = fs.url(filename)
        #print(image_url)
        form = InvoiceForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
            #return render("upload10.html", RequestContext(request))

    else:
        form = InvoiceForm()
    return render(request, "upload.html", {'form': form})
