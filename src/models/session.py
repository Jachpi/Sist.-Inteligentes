class Sesion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Sesion, cls).__new__(cls)
            cls._instancia.usuario_id = None
            cls._instancia.nombre = None
            cls._instancia.correo = None
        return cls._instancia

    def iniciar_sesion(self, usuario_id, nombre, correo):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.correo = correo

    def cerrar_sesion(self):
        self.usuario_id = None
        self.nombre = None
        self.correo = None

    def esta_logueado(self):
        return self.usuario_id is not None
