clase ClaseA:
  def __init__(self):
      . claseA = "Esa es la clase A"
      impresión(auto. claseA)

clase ClaseB(ClaseA):
  def __init__(self):
    súper(). __init__()
    self. claseB = "Esa es la clase B"
    impresión(auto. claseB)

clase ClaseC(ClaseB):
  def init(self):
    súper(). __init__()
    self. claseC = "Esa es la clase C"
    impresión(auto. claseC)

WP = ClaseC()

imprimir(WP)