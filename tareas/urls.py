from django.urls import path,include
from . import views

app_name = 'tareas'

urlpatterns = [
########################SubTarea################################################

    path('subTarea/newSubTask/<int:idTarea2>/', views.newSubTask, name='newSubTask'),
    path('subTarea/subTasks/<int:idTarea3>/', views.subTasks, name='subTasks'),
    path('subTarea/editSubTask/<int:idTarea4>/', views.editSubTask),
    path('subTarea/deleteSubTask/<int:idSubTask>/', views.deleteSubTask),

########################SubTarea2###############################################

    path('subTarea2/subTasks2/<int:idSubTarea>', views.subTasks2, name='subTasks2'),
    path('subTarea2/newSubTask2/<int:idSubTarea2>/', views.newSubTask2, name='newSubTask2'),
    path('subTarea2/editSubTask2/<int:idSubTarea3>/', views.editSubTask2),
    path('subTarea2/deleteSubTask2/<int:idSubTarea4>/', views.deleteSubTask2),

########################Solicitud###############################################

    path('solicitud/newRequest/<int:idTarea>', views.newRequestTarea, name='newRequestTarea'),
    path('solicitud/requests/<int:idTarea>', views.requestsTarea, name='requestsTarea'),
    path('solicitud/editRequest/<int:idRequestTarea>', views.editRequestTarea, name='editRequestTarea'),
    path('solicitud/deleteRequest/<int:idRequestTarea>', views.deleteRequestTarea, name='deleteRequestTarea'),
    path('solicitud/finalizarRequestTarea/<int:idRequestTarea>', views.finalizarRequestTarea, name='finalizarRequestTarea'),

########################Tiempo##################################################

    path('tiempo/newTime/<int:idTarea>', views.newTime, name='newTime'),
    path('tiempo/layOffTime/<int:idTarea>', views.layOffTime, name='layOffTime'),
    path('tiempo/finalizeTime/<int:idTarea>', views.finalizeTime, name='finalizeTime'),
    path('tiempo/myTimes/<int:idTarea>', views.myTimes, name='myTimes'),

################################################################################

    path('login',views.login, name='login'),
    #path('auditoria', views.auditoria, name='auditoria'),
    path('contabilidad', views.contabilidad, name='contabilidad'),
    #path('tarea/myTasks/<int:idUsuario>/', views.myTasks, name='myTasks'),
    path('tarea/editTask/<int:idTarea>/', views.editTask),
    path('tarea/deleteTask/<int:idTarea>/', views.deleteTask),
    path('tarea/newTask/<int:idUsuario>', views.newTask, name='newTask'),
    path('sector/sectors', views.sectors, name='sectors'),
    path('sector/editSector/<int:idSector>/', views.editSector),
    path('sector/deleteSector/<int:idSector>/', views.deleteSector),
    path('newSector', views.newSector, name='newSector'),
    path('usuario/users', views.users, name='users'),
    path('usuario/editUser/<int:idUser>/', views.editUser),
    path('usuario/deleteUser/<int:idUser>/', views.deleteUser),
    path('usuario/newUser', views.newUser, name='newUser'),
    path('estadoTarea/taskStates', views.taskStates, name='taskStates'),
    path('estadoTarea/editTaskState/<int:idEstado>/', views.editTaskState),
    path('estadoTarea/deleteTaskState/<int:idEstado>/', views.deleteTaskState),
    path('estadoTarea/newTaskState', views.newTaskState, name='newTaskState'),
    path('estadoSolicitud/requestStatus', views.requestStatus, name='requestStatus'),
    path('estadoSolicitud/editRequestStatus/<int:idEstado>/', views.editRequestStatus),
    path('estadoSolicitud/deleteRequestStatus/<int:idEstado>/', views.deleteRequestStatus),
    path('estadoSolicitud/newRequestStatus', views.newRequestStatus, name='newRequestStatus'),
    path('nivel/levels', views.levels, name='levels'),
    path('nivel/editLevel/<int:idLevel>/', views.editLevel),
    path('nivel/deleteLevel/<int:idLevel>/', views.deleteLevel),
    path('nivel/newLevel', views.newLevel, name='newLevel'),
    path('prioridad/prioritys', views.prioritys, name='prioritys'),
    path('prioridad/editPriority/<int:idPriority>/', views.editPriority),
    path('prioridad/deletePriority/<int:idPriority>/', views.deletePriority),
    path('prioridad/newPriority', views.newPriority, name='newPriority'),
    #path('subTarea/sub*Tasks', views.subTasks, name='subTasks'),
    #path('subTarea/editSubTask/<int:idSubTask>/', views.editSubTask),
    #path('subTarea/newSubTask', views.newSubTask, name='newSubTask'),
    #path('solicitud/requests', views.requests, name='requests'),
    path('solicitud/editRequest/<int:idRequest>/', views.editRequest),
    path('solicitud/deleteRequest/<int:idRequest>/', views.deleteRequest),
    #path('solicitud/newRequest', views.newRequest, name='newRequest'),
    #path('subTarea2/editSubTask2/<int:idSubTask2>/', views.editSubTask2),
    #path('subTarea2/deleteSubTask2/<int:idSubTask2>/', views.deleteSubTask2),
    #path('subTarea2/newSubTask2', views.newSubTask2, name='newSubTask2'),
    #path('solicitud/requests', views.requests, name='requests'),
    path('solicitud/editRequest/<int:idRequest>/', views.editRequest),
    path('solicitud/deleteRequest/<int:idRequest>/', views.deleteRequest),
    #path('solicitud/newRequest', views.newRequest, name='newRequest'),
    #path('tiempo/times', views.times, name='times'),
    #path('tiempo/editTime/<int:idTime>/', views.editTime),
    #path('tiempo/deleteTime/<int:idTime>/', views.deleteTime),
]
