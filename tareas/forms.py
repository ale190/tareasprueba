from django import forms
from .models import Usuario, Sector, Tarea, Estadotarea, Nivel, Prioridad, Estadosolicitud, Subtarea, Subtarea2, Solicitud, Tiempo
from betterforms.multiform import MultiModelForm

class UsuarioForm(forms.ModelForm):
    usuario = forms.CharField(max_length=10, required=True, help_text='*')
    contraseña = forms.CharField(max_length=8, widget=forms.PasswordInput,required=True, help_text='*')

    class Meta:
        model = Usuario
        fields = ['usuario','contraseña']
        #labels = {'usuario':'Usuario','contraseña':'Contraseña'}

class UsuarioForm2(forms.ModelForm):
    contraseña = forms.CharField(max_length=8, widget=forms.PasswordInput, required=True, help_text="*")
    class Meta:
        model = Usuario
        fields = ['usuario','contraseña','id_s']
        labels = {'usuario':'Usuario','contraseña':'Contraseña','id_s':'Sector'}

class SectorForm(forms.ModelForm):

    class Meta:
        model = Sector
        fields = ['sector']

class TareaForm(forms.ModelForm): # Field# Field name made lowercase.
    #class Meta:#No son campos (IntegerField, CharField, DateTimeField). Son metadatos específicos a la clase (Orden de muestra, nombres).
    #id_n = forms.ModelChoiceField(queryset=Nivel.objects.values())
    #tarea = forms.CharField(max_length=30, required=True)
    #id_e = forms.ModelChoiceField(queryset=Estadotarea.objects.values_list('id_e', flat=True), empty_label=None)
    #id_n = forms.ModelChoiceField(queryset=Nivel.objects.values_list('nivel', flat=True), empty_label=None)
    #id_us = forms.ModelChoiceField(queryset=Usuario.objects.values_list('usuario', flat=True), empty_label=None)
    #id_prioridad = forms.ModelChoiceField(queryset=Prioridad.objects.values_list('prioridad', flat=True), empty_label=None)
    class Meta:
        model = Tarea
        fields = ['tarea', 'id_n','id_prioridad']
        labels = {'tarea':'Nombre', 'id_n':'Nivel','id_prioridad':'Prioridad'}
    #objects.values()Retorna diccionarios.
    #objects.values_list()Retorna tuplas.
    #objects.values_list('', flat(texto plano)=True)Retorna listas.
#        fields = ['tarea', 'id_e', 'id_n', 'id_us', 'id_prioridad']#[] Los corchetes indican la creación de una nueva lista.
        #labels = {'tarea':'Nombre', 'id_e':'Estado', 'id_n':'Nivel', 'id_us':'Usuario', 'id_prioridad':'Prioridad'}

class EstadoTareaForm(forms.ModelForm):

     class Meta:
         model = Estadotarea
         fields = ['id_e','estado']

class EstadoSolicitudForm(forms.ModelForm):

     class Meta:
         model = Estadosolicitud
         fields = ['id_essol','estado']

class NivelForm(forms.ModelForm):

     class Meta:
         model = Nivel
         fields = ['id_n','nivel']

class PrioridadForm(forms.ModelForm):

     class Meta:
         model = Prioridad
         fields = ['id_prioridad','prioridad']

class SubTareaForm(forms.ModelForm):

     class Meta:
         model = Subtarea
         fields = ['id_sub','starea','id_prioridad']

class SubTarea2Form(forms.ModelForm):

     class Meta:
         model = Subtarea2
         fields = ['id_sub2','starea2','id_prioridad']

class SolicitudForm(forms.ModelForm):

     class Meta:
         model = Solicitud
         fields = ['id_sol','solicitud','id_s']
         labels = {'id_s':'Sector'}

class TiempoForm(forms.ModelForm):

     class Meta:
         model = Tiempo
         fields = ['id_tie','tiempoi','tiempof','id_ta']
