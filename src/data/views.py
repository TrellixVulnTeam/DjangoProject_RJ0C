from django.shortcuts import render

# Create your views here.
def table_view(request, *args, **kwargs):
	return render(request, "data/show_table.html", {})