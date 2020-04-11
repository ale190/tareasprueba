# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Sector(models.Model):
    id_s = models.AutoField(db_column='Id_s', primary_key=True)  # Field name made lowercase.
    sector = models.CharField(max_length=15, blank=False, null=True)

    def __str__(self):
        return self.sector

    class Meta:
        managed = False
        db_table = 'sector'

class Usuario(models.Model):
    id_us = models.AutoField(db_column='Id_us', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=10, blank=False, null=True)# blank, indica si el campo en el formulario puede estar en blanco, null establece si el valor puede ser nulo en la base de datos.
    contraseña = models.CharField(max_length=8, blank=False, null=True)
    id_s = models.ForeignKey(Sector, models.DO_NOTHING, db_column='Id_s')  # Field name made lowercase.
    def __str__(self):
        #return '%s %s %s %s' % (self.id_us, self.usuario, self.contraseña, self.id_s)
        return self.usuario
    class Meta:
        managed = False
        db_table = 'usuario'

class Estadotarea(models.Model):
    id_e = models.AutoField(db_column='Id_e', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(max_length=14, blank=True, null=True)

    def __str__(self):
        return self.estado

    class Meta:
        managed = False
        db_table = 'estadotarea'

class Estadosolicitud(models.Model):
    id_essol = models.AutoField(db_column='Id_esSol', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.estado

    class Meta:
        managed = False
        db_table = 'estadosolicitud'

class Nivel(models.Model):
    id_n = models.AutoField(db_column='Id_n', primary_key=True)  # Field name made lowercase.
    nivel = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.nivel

    class Meta:
        managed = False
        db_table = 'nivel'

class Prioridad(models.Model):
    id_prioridad = models.AutoField(db_column='Id_prioridad', primary_key=True)  # Field name made lowercase.
    prioridad = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.prioridad

    class Meta:
        managed = False
        db_table = 'prioridad'

class Tarea(models.Model):
    id_ta = models.AutoField(db_column='Id_ta', primary_key=True)  # Field name made lowercase.
    tarea = models.CharField(max_length=30)
    id_e = models.ForeignKey(Estadotarea, models.DO_NOTHING, db_column='Id_e')  # Field name made lowercase.
    id_n = models.ForeignKey(Nivel, models.DO_NOTHING, db_column='Id_n')  # Field name made lowercase.
    id_us = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Id_us')  # Field name made lowercase.
    id_prioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, db_column='Id_prioridad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarea'

class Subtarea(models.Model):
    id_sub = models.AutoField(db_column='Id_sub', primary_key=True)  # Field name made lowercase.
    starea = models.CharField(max_length=30, blank=True, null=True)
    id_ta = models.ForeignKey(Tarea, models.DO_NOTHING, db_column='Id_ta')  # Field name made lowercase.
    id_prioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, db_column='Id_prioridad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subtarea'

class Subtarea2(models.Model):
    id_sub2 = models.AutoField(db_column='Id_sub2', primary_key=True)  # Field name made lowercase.
    starea2 = models.CharField(max_length=30, blank=True, null=True)
    id_sub = models.ForeignKey(Subtarea, models.DO_NOTHING, db_column='Id_sub')  # Field name made lowercase.
    id_prioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, db_column='Id_prioridad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subtarea2'

class Solicitud(models.Model):
    id_sol = models.AutoField(db_column='Id_sol', primary_key=True)  # Field name made lowercase.
    solicitud = models.CharField(max_length=30, blank=True, null=True)
    tiempoi = models.DateTimeField(db_column='tiempoI', blank=True, null=True)  # Field name made lowercase.
    tiempof = models.DateTimeField(db_column='tiempoF', blank=True, null=True)  # Field name made lowercase.
    id_essol = models.ForeignKey(Estadosolicitud, models.DO_NOTHING, db_column='Id_esSol')  # Field name made lowercase.
    id_ta = models.ForeignKey(Tarea, models.DO_NOTHING, db_column='Id_ta', blank=True, null=True)  # Field name made lowercase.
    id_sub = models.ForeignKey(Subtarea, models.DO_NOTHING, db_column='Id_sub', blank=True, null=True)  # Field name made lowercase.
    id_sub2 = models.ForeignKey(Subtarea2, models.DO_NOTHING, db_column='Id_sub2', blank=True, null=True)  # Field name made lowercase.
    id_s = models.ForeignKey(Sector, models.DO_NOTHING, db_column='Id_s', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solicitud'

class Tiempo(models.Model):
    id_tie = models.AutoField(db_column='Id_tie', primary_key=True)  # Field name made lowercase.
    tiempoi = models.DateTimeField(db_column='tiempoI', blank=True, null=True)  # Field name made lowercase.
    tiempof = models.DateTimeField(db_column='tiempoF', blank=True, null=True)  # Field name made lowercase.
    id_ta = models.ForeignKey(Tarea, models.DO_NOTHING, db_column='Id_ta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiempo'
