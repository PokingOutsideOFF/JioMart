from django.shortcuts import render
from django.shortcuts import render
from .forms import brandsForm
# Create your views here.

def create_brand_name(request):
    brand_form = brandsForm()
    data = {
        'brand_form': brand_form
    } 
    return render(request,"sample_page.html", data)

def view_brand_name(request, brand_id):
    print(brand_id)
    data_dict = {"brand_id": brand_id, "brand_name": "Sipon", }
    return render(request,"brand/view_brand_name.html", data_dict)

def homepage_fn(request, brand_id):
    print(brand_id)
    data_dict = {"brand_id": brand_id,
                  "brand_name": "Sipon",
                   "to_do_list": ["to_do_1", "to_do_2", "to_do_3", "to_do_4", "to_do_5"], }
    return render(request,"index.html",data_dict)