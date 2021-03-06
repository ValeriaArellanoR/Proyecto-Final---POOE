"""
Avance 1 (V): programación de clase persona y Médico especialista
"""

class Persona:
    
    #Atributos
    m_id = 0000
    m_horarioSem = None
    m_depart = None
    _m_nombre = None
    _m_edad = None
    _m_sexo = None
    _m_pronom = None
    _m_horasXsem = None
    
    #Constructor
    def __init__(self, ID, nombre, edad, sexo, pronombre, departamento):
        self.m_id = ID
        self._m_nombre = nombre
        self._m_edad = edad
        self._m_sexo = sexo
        self._m_pronom = pronombre
        self.m_depart = departamento
    
    #Getters
    def getNombre(self):
        return self._m_nombre.title()
    
    def getEdad(self):
        return self._m_edad
    
    def getSexo(self):
        return self._m_sexo.title()
    
    def getPronombre(self):
        return self._m_pronom.title()
    
    def getHorasXsem(self):
        return self._m_horasXsem
    
    def getHorarioSem(self):
        return self.m_horarioSem
    
    def getDepartamento(self):
        return self.m_depart
    
    ##Setters
    def setNombre(self, nombre):
        self._m_nombre = nombre
    
    def setEdad(self, edad):
        self._m_edad = edad
        
    def setSexo(self, sexo):
        self._m_sexo = sexo
    
    def setPronom(self, pronombre):
        self._m_pronom = pronombre
    
    def setHorasXsem(self, HorasSemanales):
        self._m_horasXsem = HorasSemanales
    
    def setDepartamento(self, departamento):
        self.m_depart = departamento  
    #Falta el set para asignar el horario
    
class Medico_Especialista(Persona):
    #Atributos
    m_especialidad = None
    
    #Constructor
    def __init__(self, ID, nombre, edad, sexo, pronombre, departamento, especialidad):
        self.m_id = ID
        self._m_nombre = nombre
        self._m_edad = edad
        self._m_sexo = sexo
        self._m_pronom = pronombre
        self.m_depart = departamento
        self.m_especialidad = especialidad
    
    def getEspecialidad(self):
        return self.m_especialidad.title()
    
    def setEspecialidad(self, especialidad):
        self.m_especialidad = especialidad


class Administrativo(Persona):
    
class Enfermero (Persona):
    
class Limpieza (Persona):
    