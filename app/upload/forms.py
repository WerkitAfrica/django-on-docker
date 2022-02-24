from django.forms import ModelForm
from upload.models import Invoice

# Create the form class.
class InvoiceForm(ModelForm):
     class Meta:
         model = Invoice
         fields = ['invoice_id', 'company', 'csv']