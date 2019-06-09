from mininet.topo import Topo
import math
class Example( Topo ):
  def __init__( self, half_ports = 2, **opts ):
    Topo.__init__(self, **opts)


    # Primero creamos el switch raiz
    sw0 = self.addSwitch('sw0')

    #Agregamos los tres hosts
    h1 = self.addHost('h1')
    h2 = self.addHost('h2')
    h3 = self.addHost('h3')

    #Cremos los links
    self.addLink(sw0, h1) # Conectando el sw0 con h1
    self.addLink(sw0, h2) # Conectando el sw0 con h2
    self.addLink(sw0, h3) # Conectando el sw0 con h3

    nivelAnterior = []
    nivelAnterior.append(sw0)

    nivelActual = []

    print("ingrese niveles")
    #n es la cantidad de niveles, que es el input del usuario
    n = input() 
     
    currentLevel = 2
    for x in range(1,(int)(math.pow(2,n) - 1)):
      switch = self.addSwitch('sw' + str(x))
      if x == (math.pow(2,currentLevel) - 1):
        nivelAnterior = nivelActual
        nivelActual = []
        currentLevel = currentLevel + 1
      nivelActual.append(switch)
      for switchNivelAnterior in nivelAnterior:
        self.addLink(switchNivelAnterior, switch) # Conectando nuevo switch con switch de nivel anterior

    j = 4
    for switchHoja in nivelActual:
      h = self.addHost('h'+str(j)) # Creamos los hosts hojas
      self.addLink(switchHoja, h) # Conectando el switchHoja con host
      j = j + 1

topos = { 'example': Example }
