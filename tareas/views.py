from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UsuarioForm, UsuarioForm2, SectorForm, TareaForm, EstadoTareaForm, EstadoSolicitudForm, NivelForm, PrioridadForm, SubTareaForm, SubTarea2Form, SolicitudForm, TiempoForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from datetime import datetime
from .models import Usuario, Sector, Tarea, Estadotarea, Estadosolicitud, Nivel, Prioridad, Subtarea, Subtarea2, Solicitud, Tiempo
from django.db.models import Sum
import time

##################SubTarea#####################

def newSubTask(request, idTarea2):
    formSubTarea = SubTareaForm()
    context = {'formSubTarea':formSubTarea}
    if request.method == 'POST':
        formSubTarea = SubTareaForm(request.POST)
        if formSubTarea.is_valid():
            starea = formSubTarea.cleaned_data.get('starea')
            id_ta = int(idTarea2)
            id_prioridad = formSubTarea.cleaned_data.get('id_prioridad')
            new_SubTask = Subtarea.objects.create(starea=starea, id_ta_id=id_ta,id_prioridad=id_prioridad)
            new_SubTask.save()
    return render(request, 'tareas/subTarea/newSubTask.html', context)

def subTasks(request, idTarea3):
    #subTareas = get_list_or_404(Subtarea, id_ta=idTarea3)
    subTareas = Subtarea.objects.filter(id_ta=idTarea3)
    context = {'subTareas':subTareas}
    return render(request, 'tareas/subTarea/subTasks.html', context)

def editSubTask(request, idTarea4):
    instancia = Subtarea.objects.get(id_sub=idTarea4)
    form = SubTareaForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = SubTareaForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/subTarea/editSubTask.html', context)

def deleteSubTask(request, idSubTask):
    instancia = Subtarea.objects.get(id_sub=idSubTask)
    instancia.delete()
    return render(request, 'tareas/subTarea/subTasks.html')

##################SubTarea2########################

def subTasks2(request, idSubTarea):
    subTasks2 = get_list_or_404(Subtarea2, id_sub=idSubTarea)
    context = {'subTasks2':subTasks2}
    return render(request, 'tareas/subTarea2/subTasks2.html', context)

def newSubTask2(request, idSubTarea2):
    form = SubTarea2Form()
    context = {'form':form}
    if request.method == 'POST':
        form = SubTarea2Form(request.POST)
        if form.is_valid():
            starea2 = form.cleaned_data.get('starea2')
            id_sub = int(idSubTarea2)
            id_prioridad = form.cleaned_data.get('id_prioridad')
            new_SubTask2 = Subtarea2.objects.create(starea2=starea2, id_sub_id=id_sub,id_prioridad=id_prioridad)
            new_SubTask2.save()
    return render(request, 'tareas/subTarea2/newSubTask2.html', context)

def editSubTask2(request, idSubTarea3):
    instancia = Subtarea2.objects.get(id_sub2=idSubTarea3)
    form = SubTarea2Form(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = SubTarea2Form(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/subTarea2/editSubTask2.html', context)

def deleteSubTask2(request, idSubTarea4):
    instancia = Subtarea2.objects.get(id_sub2=idSubTarea4)
    instancia.delete()
    return render(request, 'tareas/subTarea2/subTasks2.html')

##################Solicitud########################

def newRequestTarea(request, idTarea):##Cada cierto periodo, mostrar una alerta. agregar un campo sector.
    form = SolicitudForm()
    context = {'form':form}
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.cleaned_data.get('solicitud')
            tiempoi = time.strftime("%Y-%m-%d %H:%M:%S")
            #tiempof = time.strftime("%Y-%m-%d %H:%M:%S"
            id_essol = int(1)
            id_ta = int(idTarea)
            id_s = form.cleaned_data.get('id_s')###MODIFICAR
            new_requestTarea = Solicitud.objects.create(solicitud=solicitud, tiempoi=tiempoi, tiempof=None, id_essol_id=id_essol, id_ta_id=id_ta, id_sub=None, id_sub2=None, id_s=id_s)
            print(id_s)
            new_requestTarea.save()
    return render(request, 'tareas/solicitud/newRequest.html', context)

def requestsTarea(request, idTarea):
    #requests = get_list_or_404(Solicitud, id_ta=idTarea, id_essol=1)
    requests = Solicitud.objects.filter(id_ta=idTarea, id_essol=1)
    context = {'requests':requests}
    return render(request, 'tareas/solicitud/requests.html', context)

def editRequestTarea(request, idRequestTarea):
    instancia = Solicitud.objects.get(id_sol=idRequestTarea)
    form = SolicitudForm(instance=instancia)
    context = {'form':form}
    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation = "La solicitud se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/solicitud/editRequest.html', context)

def deleteRequestTarea(request, idRequestTarea):
    instancia = Solicitud.objects.get(id_sol=idRequestTarea)
    instancia.delete()
    return render(request, 'tareas/solicitud/requests.html')

def finalizarRequestTarea(request, idRequestTarea):
    tiempof = time.strftime("%Y-%m-%d %H:%M:%S")
    instancia = Solicitud.objects.filter(id_sol=idRequestTarea).update(id_essol=4,tiempof=tiempof)
    return render(request, 'tareas/solicitud/requests.html')

##################Tiempo########################

def newTime(request, idTarea):#RELEER ESTA FUNCIÓN.
    tiempoi = time.strftime("%Y-%m-%d %H:%M:%S")
    id_ta = idTarea
    new_time = Tiempo.objects.create(tiempoi=tiempoi, tiempof=None, id_ta_id=id_ta)
    new_time.save()
    instancia = Tarea.objects.filter(id_ta=idTarea).update(id_e=1)
    resultUser = Tarea.objects.get(id_ta=id_ta)#No deberían poder crearse tareas con el mismo nombre.
    idUsuario = resultUser.id_us_id#Cuando no se trata de una clave primaria, sino de una foránea, deben tenerse en cuenta estas relaciones.
    tareas = Tarea.objects.filter(id_us=idUsuario).order_by('id_e')
    user = Usuario.objects.get(id_us=idUsuario)
    username = user.usuario
    context = {'tareas':tareas,
            'username':username,
            'idUsuario':idUsuario,
            }
    print(idUsuario)
    return render(request, 'tareas/tarea/myTasks.html', context)

def layOffTime(request, idTarea):
    tiempof = time.strftime("%Y-%m-%d %H:%M:%S")
    instanciaTiempo = Tiempo.objects.filter(id_ta=idTarea).last()
    instanciaTiempo.tiempof = tiempof
    instanciaTiempo.save()
    instanciaTarea = Tarea.objects.filter(id_ta=idTarea).update(id_e=2)
    resultUser = Tarea.objects.get(id_ta=idTarea)#No deberían poder crearse tareas con el mismo nombre.
    idUsuario = resultUser.id_us_id#Cuando no se trata de una clave primaria, sino de una foránea, deben tenerse en cuenta estas relaciones al momento de instanciar campos de una tabla.
    tareas = Tarea.objects.filter(id_us=idUsuario).order_by('id_e')
    user = Usuario.objects.get(id_us=idUsuario)
    username = user.usuario
    context = {'tareas':tareas,
            'username':username,
            'idUsuario':idUsuario,
            }
    return render(request, 'tareas/tarea/myTasks.html', context)

def finalizeTime(request, idTarea):
    instancia = Tarea.objects.filter(id_ta=idTarea).update(id_e=3)
    resultUser = Tarea.objects.get(id_ta=idTarea)
    idUsuario = resultUser.id_us_id
    tareas = Tarea.objects.filter(id_us=idUsuario).order_by('id_e')
    user = Usuario.objects.get(id_us=idUsuario)
    username = user.usuario
    context = {'tareas':tareas,
                'username':username,
                'idUsuario':idUsuario
                }
    return render(request, 'tareas/tarea/myTasks.html', context)

def myTimes(request, idTarea):
    times = Tiempo.objects.filter(id_ta=idTarea)
    suma = datetime(2000,1,1)
    for t in times:
        if t.tiempof!=None and t.tiempoi!=None:
            f = t.tiempof-t.tiempoi
            print(f)
            suma += f
        #i = i+f
    print(suma)
    #sumaTotal = str('Horas: '+str(suma.hour)+' - Minutos: '+str(suma.minute)+' - Segundos: '+str(suma.second))
    hh = suma.hour
    mm = suma.minute
    ss = suma.second
    context = {'times':times,'hh':hh,'mm':mm,'ss':ss}
    return render(request, 'tareas/tiempo/myTimes.html', context)

################################################

def deleteTask(request, idTarea):
    instancia = Tarea.objects.get(id_ta=idTarea)
    instancia.delete()
    return render(request, 'tareas/tarea/myTasks.html')

def editTask(request, idTarea):#Modificar método. No crear tareas con un nombre ya existente.
    instancia = Tarea.objects.get(id_ta=idTarea)
    form = TareaForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = TareaForm(request.POST, instance=instancia)
        if form.is_valid():
            nombreTarea = form.cleaned_data.get('tarea')
            nameT = Tarea.objects.filter(tarea=nombreTarea).exists()
            if nameT == False:
                instancia = form.save(commit=False)
                instancia.save()
                message= "Modificado!"
                context = {'form':form, 'message':message}
            else:
                message= "El nombre de la tarea ya existe!"
                context = {'form':form, 'message':message}
    return render(request, 'tareas/tarea/editTask.html', context)

def newTask(request, idUsuario):
    formTarea = TareaForm()
    #tareas = Tarea.objects.all()
    #context = {'formTarea':formTarea, 'tareas':tareas}
    context = {'formTarea':formTarea}
    if request.method == 'POST':
        formTarea = TareaForm(request.POST)
        if formTarea.is_valid():
            tareaF = formTarea.cleaned_data.get('tarea')
            t = Tarea.objects.filter(tarea=tareaF).exists()
            if t == False:
                tarea = tareaF
                id_e = int(2)
                id_n = formTarea.cleaned_data.get('id_n')
                id_prioridad = formTarea.cleaned_data.get('id_prioridad')
                id_us = int(idUsuario)
                #id_us = int(1) Se envía un valor al campo id_us de la tabla Tarea.
                new_Task = Tarea.objects.create(tarea=tarea, id_e_id=id_e,id_n=id_n,id_us_id=id_us,id_prioridad=id_prioridad)
                new_Task.save()
                formTarea = TareaForm()
                message = 'Registro creado!'
                context = {'formTarea':formTarea, 'message':message}
            else:
                message = "El nombre de la tarea ya existe."
                context = {'formTarea':formTarea, 'message':message}
                #print(id_n)
    return render(request, 'tareas/tarea/newTask.html', context)

#def myTasks(request, idUsuario):
#    #ahora = datetime.now()
#    #tareas = get_list_or_404(Tarea, id_us=idUsuario)
#    tareas = Tarea.objects.filter(id_us=idUsuario).order_by('id_e')
#    #idUsuario = get_object_or_404(Usuario, id_us=idUsuario)
#    resultUsuario = Usuario.objects.get(id_us=idUsuario)
#    idUsuario = resultUsuario.id_us
#    valoresTareas = Tarea.objects.values()
#    usuarios2 = Usuario.objects.all()
    #diaActual = ahora.day
    #mesActual = ahora.month
    #añoActual = ahora.year
#    context = {'tareas':tareas,
#                'idUsuario':idUsuario,
#                'diaActual':diaActual,
#                'mesActual':mesActual,
#                'añoActual':añoActual,
#                #'usuarios2':usuarios2,
#                #'valoresTareas':valoresTareas,
#                }
#    return render(request, 'tareas/tarea/myTasks.html', context)

def sectors(request):
    sectores = Sector.objects.all()
    context = {'sectores':sectores}
    return render(request, 'tareas/sector/sectors.html', context)

def editSector(request, idSector):
    instancia = Sector.objects.get(id_s=idSector)
    form = SectorForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = SectorForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/sector/editSector.html', context)

def deleteSector(request, idSector):
    instancia = Sector.objects.get(id_s=idSector)
    instancia.delete()
    return render(request, 'tareas/sector/sectors.html')

def newSector(request):
    form = SectorForm()
    context = {'form':form}
    if request.method == 'POST':
        form = SectorForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tareas/sector/newSector.html', context)

def users(request):
    users = Usuario.objects.all()
    context = {'users':users}
    return render(request, 'tareas/usuario/users.html', context)

def editUser(request, idUser):
    instancia = Usuario.objects.get(id_us=idUser)
    form = UsuarioForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/usuario/editUser.html', context)

def deleteUser(request, idUser):
    instancia = Usuario.objects.get(id_us=idUser)
    instancia.delete()
    return render(request, 'tareas/usuario/users.html')

def newUser(request):
    form = UsuarioForm2()
    context = {'form':form}
    if request.method == 'POST':
         form = UsuarioForm2(request.POST)
         if form.is_valid():
             username = form.cleaned_data['usuario']
             user = Usuario.objects.filter(usuario=username).exists()
             if user == False:
                 form.save()
                 form = UsuarioForm2()
                 message = "Registro creado!"
                 context = {'form':form, 'message':message}
             else:
                 message = "El nombre de usuario ya existe."
                 context = {'form':form, 'message':message}
    return render(request, 'tareas/usuario/newUser.html', context)

def taskStates(request):
    estadosTareas = Estadotarea.objects.all()
    context = {'estadosTareas':estadosTareas}
    return render(request, 'tareas/estadoTarea/taskStates.html', context)

def editTaskState(request, idEstado):
    instancia = Estadotarea.objects.get(id_e=idEstado)
    form = EstadoTareaForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = EstadoTareaForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/estadoTarea/editTaskState.html', context)

def deleteTaskState(request, idEstado):
    instancia = Estadotarea.objects.get(id_e=idEstado)
    instancia.delete()
    return render(request, 'tareas/estadoTarea/taskStates.html')

def newTaskState(request):
    form = EstadoTareaForm()
    if request.method == 'POST':
         form = EstadoTareaForm(request.POST)
         if form.is_valid():
             form.save()
    return render(request, 'tareas/estadoTarea/newTaskStates.html', {'form':form})

def requestStatus(request):
    estados = Estadosolicitud.objects.all()
    context = {'estados':estados}
    return render(request, 'tareas/estadoSolicitud/requestStatus.html', context)

def editRequestStatus(request, idEstado):
    instancia = Estadosolicitud.objects.get(id_essol=idEstado)
    form = EstadoSolicitudForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = EstadoSolicitudForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/estadoSolicitud/editRequestStatus.html', context)

def deleteRequestStatus(request, idEstado):
    instancia = Estadosolicitud.objects.get(id_essol=idEstado)
    instancia.delete()
    return render(request, 'tareas/estadoSolicitud/requestStatus.html')

def newRequestStatus(request):
    form = EstadoSolicitudForm()
    context = {'form':form}
    if request.method == 'POST':
        form = EstadoSolicitudForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tareas/estadoSolicitud/newRequestStatus.html', context)

def levels(request):
    levels = Nivel.objects.all()
    context = {'levels':levels}
    return render(request, 'tareas/nivel/levels.html', context)

def editLevel(request, idLevel):
    instancia = Nivel.objects.get(id_n=idLevel)
    form = NivelForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = NivelForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/nivel/editLevel.html', context)

def deleteLevel(request, idLevel):
    instancia = Nivel.objects.get(id_n=idLevel)
    instancia.delete()
    return render(request, 'tareas/nivel/levels.html')

def newLevel(request):
    form = NivelForm()
    context = {'form':form}
    if request.method == 'POST':
        form = NivelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tareas/nivel/newLevel.html', context)

def prioritys(request):
    prioritys = Prioridad.objects.all()
    context = {'prioritys':prioritys}
    return render(request, 'tareas/prioridad/prioritys.html', context)

def editPriority(request, idPriority):
    instancia = Prioridad.objects.get(id_prioridad=idPriority)
    form = PrioridadForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = PrioridadForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/prioridad/editPriority.html', context)

def deletePriority(request, idPriority):
    instancia = Prioridad.objects.get(id_prioridad=idPriority)
    instancia.delete()
    return render(request, 'tareas/prioridad/prioritys.html')

def newPriority(request):
    form = PrioridadForm()
    context = {'form':form}
    if request.method == 'POST':
        form = PrioridadForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tareas/prioridad/newPriority.html', context)

#def editSubTask(request, idSubTask):
#    instancia = Subtarea.objects.get(id_sub=idSubTask)
#    form = SubTareaForm(instance=instancia)
#    if request.method == "POST":
#        form = SubTareaForm(request.POST, instance=instancia)
#        if form.is_valid():
#            instancia = form.save(commit=False)
#            instancia.save()
#            confirmation= "La tarea se modificó correctamente!"
#            context = {'form':form, 'confirmation':confirmation}
#    return render(request, 'tareas/subTarea/editSubTask.html', context)

#def newSubTask(request):
#    form = SubTareaForm()
#    context = {'form':form}
#    if request.method == 'POST':
#        form = SubTareaForm(request.POST)
#        if form.is_valid():
#            form.save()
#    return render(request, 'tareas/subTarea/newSubTask.html', context)

#def subTasks(request):
#    subTasks = Subtarea.objects.all()
#    context = {'subTasks':subTasks}
#    return render(request, 'tareas/subTarea/subTasks.html', context)
#def deleteSubTask2(request, idSubTask2):
#    instancia = Subtarea2.objects.get(id_sub=idSubTask2)
#    instancia.delete()
#    return render(request, 'tareas/subTarea2/subTasks2.html')

#def editSubTask2(request, idSubTask2):
#    instancia = Subtarea2.objects.get(id_sub2=idSubTask2)
#    form = SubTarea2Form(instance=instancia)
#    context = {'form':form}
#    if request.method == "POST":
#        form = SubTarea2Form(request.POST, instance=instancia)
#            instancia.save()
#            confirmation= "La tarea se modificó correctamente!"
#            context = {'form':form, 'confirmation':confirmation}
#    return render(request, 'tareas/subTarea2/editSubTask2.html', context)

#def newSubTask2(request):
#    form = SubTarea2Form()
#    context = {'form':form}
#    if request.method == 'POST':
#        form = SubTarea2Form(request.POST)
#        if form.is_valid():
#            form.save()
#    return render(request, 'tareas/subTarea2/newSubTask2.html', context)

#def subTasks2(request):
#    subTasks2 = Subtarea2.objects.all()
#    context = {'subTasks2':subTasks2}
#    return render(request, 'tareas/subTarea2/subTasks2.html', context)

def deleteRequest(request, idRequest):
    instancia = Solicitud.objects.get(id_sol=idRequest)
    instancia.delete()
    return render(request, 'tareas/solicitud/requests.html')

def editRequest(request, idRequest):
    instancia = Solicitud.objects.get(id_sol=idRequest)
    form = SolicitudForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = SolicitudForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/solicitud/editRequest.html', context)

#def requests(request):
#    requests = Solicitud.objects.all()
#    context = {'requests':requests}
#    return render(request, 'tareas/solicitud/requests.html', context)

def deleteTime(request, idTime):
    instancia = Tiempo.objects.get(id_tie=idTime)
    instancia.delete()
    return render(request, 'tareas/tiempo/requests.html')

def editTime(request, idTime):
    instancia = Tiempo.objects.get(id_tie=idTime)
    form = TiempoForm(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = TiempoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            confirmation= "La tarea se modificó correctamente!"
            context = {'form':form, 'confirmation':confirmation}
    return render(request, 'tareas/tiempo/editTime.html', context)

#def newTime(request):
#    form = TiempoForm()
#    context = {'form':form}
#    if request.method == 'POST':
#        form = TiempoForm(request.POST)
#        if form.is_valid():
#            form.save()
#    return render(request, 'tareas/tiempo/newTime.html', context)

#def times(request):
#    times = Tiempo.objects.all()
#    context = {'times':times}
#    return render(request, 'tareas/tiempo/times.html', context)

def login(request):
    form = UsuarioForm()
    context = {'form':form}
    if request.method == "POST":
        form = UsuarioForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['contraseña']
            try:
                if Usuario.objects.get(usuario=username, contraseña=password):
                    usuarioResult = Usuario.objects.get(usuario=username, contraseña=password)
                    idSector = usuarioResult.id_s_id
                    idUsuario = usuarioResult.id_us
                    if idSector==1:
                        #context = {'username':username, 'idUsuario':idUsuario}
                        ahora = datetime.now()
                        #tareas = get_list_or_404(Tarea, id_us=idUsuario)
                        tareas = Tarea.objects.filter(id_us=idUsuario).order_by('id_e')
                        #subTarea = SubTarea.object.all()
                        #idUsuario = get_object_or_404(Usuario, id_us=idUsuario)
                        resultUsuario = Usuario.objects.get(id_us=idUsuario)
                        idUsuario = resultUsuario.id_us
                        #valoresTareas = Tarea.objects.values()
                        #usuarios2 = Usuario.objects.all()
                        diaActual = ahora.day
                        mesActual = ahora.month
                        añoActual = ahora.year
                        context = {'tareas':tareas,
                                    'username':username,
                                    'idUsuario':idUsuario,
                                    'diaActual':diaActual,
                                    'mesActual':mesActual,
                                    'añoActual':añoActual,
                                    #'subTarea':subTarea,
                                    #'usuarios2':usuarios2,
                                    #'valoresTareas':valoresTareas,
                                    }
                                    #print(idUsuario)
                                    #form = UsuarioForm()
                        return render(request, "tareas/tarea/myTasks.html", context)
                    elif idSector==3:
                        #form = UsuarioForm()
                        return render(request, "tareas/newSector.html")
            except:
                    print("Registrarse")
                    errorIngreso = 'Usuario o contraseña no válidos'
                    context = {'form':form, 'errorIngreso':errorIngreso}
                    return render(request, 'tareas/login.html', context)
    return render(request, 'tareas/login.html', context)

def auditoria(request):
    return render(request, 'tareas/auditoria.html')

def contabilidad(request):
    return render(request, 'tareas/contabilidad.html')
