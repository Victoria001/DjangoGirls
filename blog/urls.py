from django.conf.urls import include, url
from . import views
# crear los urls y decir que url corresponde a que pagina
urlpatterns = [
    url(r'^$', views.post_list),
]
