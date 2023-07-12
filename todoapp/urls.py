
from django.urls import path

from todoapp import views

urlpatterns=[
    path('', views.home, name='home'),
    path('forms/', views.forms, name='forms'),
    path('usingModelForm/', views.usingModelForm, name='usingModelForm'),
    path('mark_as_done/int:<pk>', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/int:<pk>', views.mark_as_undone, name='mark_as_undone'),
    path('editTask/int:<pk>', views.editTask, name='editTask'),
    path('editTaskUsingModelForm/int:<pk>', views.editTaskUsingModelForm, name='editTaskUsingModelForm'),
    path('moveToTrash/int:<pk>', views.moveToTrash, name="moveToTrash"),
    path('confirmMoveToTrash/int:<pk>', views.confirmMoveToTrash, name="confirmMoveToTrash"),
    path('trash/', views.trash, name='trash'),
    path('confirmPermanentDelete/int:<pk>', views.confirmPermanentDelete, name='confirmPermanentDelete'),
    path('permanentDelete/int:<pk>', views.permanentDelete, name='permanentDelete'),
    path('restore/int:<pk>', views.restore, name='restore'),
    path('restoreConfirm/int:<pk>', views.restoreConfirm, name='restoreConfirm'),
    path('restoreAll/', views.restoreAll, name='restoreAll'),
    path('restoreAlConfirm/', views.restoreAllConfirm, name='restoreAllConfirm'),
    path('deleteAllInTrash/', views.deleteAllInTrash, name='deleteAllInTrash'),
    path('deleteAllInTrashConfirm', views.deleteAllInTrashConfirm, name='deleteAllInTrashConfirm'),


]
