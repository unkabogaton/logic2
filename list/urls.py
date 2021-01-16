from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('delete/<int:item_id>/',  views.delete, name='delete'),
    path('cross_off/<int:item_id>/',  views.cross_off, name='cross_off'),
    path('uncross/<int:item_id>/',  views.uncross, name='uncross'),
    path('edit/<int:item_id>/',  views.edit, name='edit'),
    path('search/',  views.search, name='search'),
    path('completed_task/',  views.completed_task, name='completed_task'),
    path('ongoing_task/',  views.ongoing_task, name='ongoing_task'),
    path('all_completed/',  views.all_completed, name='all_completed'),
    path('all_ongoing/',  views.all_ongoing, name='all_ongoing'),
    path('hominem/',  views.hominem, name='hominem'),
    path('baculum/',  views.baculum, name='baculum'),
    path('misericordiam/',  views.misericordiam, name='misericordiam'),
    path('populum/',  views.populum, name='populum'),
    path('false_dichotomy/',  views.dichotomy, name='dichotomy'),
    path('false_cause/',  views.false_cause, name='false_cause'),
    path('equivocation/',  views.equivocation, name='equivocation'),
    path('slippery_slope/',  views.slippery_slope, name='slippery_slope'),
    path('false_analogy/',  views.false_analogy, name='false_analogy'),
    path('generalization/',  views.generalization, name='generalization'),
]
