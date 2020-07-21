from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_view,name="pages-home"),
    path("slides",views.SlidesCreateView.as_view(success_url='/'),name="pages-slides-create"),
    path("category/<str:short>",views.category_view,name="pages-category"),
    path("search/",views.search_view,name="pages-search"),
]
