class DetalleVenta:

    def __init__(self, id, idventa,idproducto, cantidad,subtotal):
        self.__id = id
        self.__cantidad = cantidad
        self.__idproducto = idproducto
        self.__idventa = idventa
        self.__subtotal = subtotal
    
    @property
    def Id(self):
        return self.__id
    
    @Id.setter
    def Id(self, id):
        self.__id = id
    
    @property
    def idventa(self):
        return self.__idventa
    
    @idventa.setter
    def idventa(self, idventa):
        self.__idventa = idventa
    
    @property
    def idproducto(self):
        return self.__idproducto
    
    @idproducto.setter
    def idproducto(self, idproducto):
        self.__idproducto = idproducto
    
    @property
    def Cantidad(self):
        return self.__cantidad
    
    @Cantidad.setter
    def Cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    @property
    def Subtotal(self):
        return self.__subtotal
    
    @Subtotal.setter
    def Subtotal(self, subtotal):
        self.__subtotal = subtotal
    
    def __str__(self):
        return self.__cantidad + " - " + self.__producto

   
        
