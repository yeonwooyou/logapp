from django.urls import path
from log import views

app_name = "log"

urlpatterns = [
    path("", views.index, name="index"), #http://127.0.0.1:8000/ -> log:index
    path("geni/",views.gen_i, name="geni"), #http:/127.0.0.1:8000/log/geni/ -> log:geni
    path("btn_geni_click/<int:product_id>", views.btn_geni_click),
    path("genii/",views.gen_ii, name="genii"),
    path("geniii/",views.gen_iii, name="geniii"),
]