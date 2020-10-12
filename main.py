import pygame

# iniciamos pygame
pygame.init()

'''
***************
***VARIABLES***
***************
'''
tamañoDePantalla = (800, 600)
pantalla = pygame.display.set_mode(tamañoDePantalla)
reloj = pygame.time.Clock()

# colores
negro    = (0  ,   0,   0)
blanco   = (255, 255, 255)
rojo     = (255, 0  ,   0)
amarillo = (255, 255,   0)
naranja  = (255, 165,   0)

permiso1 = False
permiso2 = False
juegocerrado = False
'''
***************
****OBJETOS****
***************
'''

class proyectil(object):
	def __init__(self, _color,_posicionx, _posiciony, _alto, _ancho, _velocidad, _alcanze, _carga):
		self.color = _color
		self.posicionx = _posicionx
		self.posiciony = _posiciony
		self.alto = _alto
		self.ancho = _ancho
		self.velocidad = _velocidad
		self.alcanze = _alcanze
		self.carga = _carga
	def trayectoria(self):
		self.posicionx = self.posicionx - self.velocidad
	def dibujar(self):
		self.contorno = pygame.draw.rect(pantalla, self.color, (self.posicionx, self.posiciony, self.alto, self.ancho))

class personaje(object):
	def __init__(self, _color, _posicionx, _posiciony, _alto, _ancho, _vida, _velocidad1, _velocidad2):
		self.color = _color
		self.posicionx = _posicionx
		self.posiciony = _posiciony
		self.alto = _alto
		self.ancho = _ancho
		self.vida = _vida
		self.velocidad1 = _velocidad1
		self.velocidad2 = _velocidad2
	def dibujar(self):
		self.contorno = pygame.draw.rect(pantalla, self.color, (self.posicionx, self.posiciony, self.alto, self.ancho))

muñecoNieve = personaje(blanco, 50, 300, 20, 20, 4, 0, 0)
proyectilMuñecoNieve = proyectil(blanco, muñecoNieve.posicionx, muñecoNieve.posiciony, 15, 15, -3, 550, 3)

osoPolar = personaje(blanco, 750, 300, 30, 30, 5, 0, 0)
proyectilOsoPolar = proyectil(blanco, osoPolar.posicionx,osoPolar.posiciony, 25, 25, 2, 400, 4)

'''
***************
BUCLE PRINCIPAL
***************
'''

while not juegocerrado:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			juegocerrado = True
		if event.type == pygame.KEYDOWN:
			#jugador1
			if event.key == pygame.K_w:
				muñecoNieve.velocidad1 = -3
			if event.key == pygame.K_s:
				muñecoNieve.velocidad1 = 3
			if event.key == pygame.K_a:
				muñecoNieve.velocidad2 = -3
			if event.key == pygame.K_d:
				muñecoNieve.velocidad2 = 3
			#jugador2
			if event.key == pygame.K_UP:
				osoPolar.velocidad1 = -3
			if event.key == pygame.K_DOWN:
				osoPolar.velocidad1 = 3
			if event.key == pygame.K_LEFT:
				osoPolar.velocidad2 = -3
			if event.key == pygame.K_RIGHT:
				osoPolar.velocidad2 = 3

		if event.type == pygame.KEYUP:
			#jugador1
			if event.key == pygame.K_w:
				muñecoNieve.velocidad1 = 0
			if event.key == pygame.K_s:
				muñecoNieve.velocidad1 = 0
			if event.key == pygame.K_a:
				muñecoNieve.velocidad2 = 0
			if event.key == pygame.K_d:
				muñecoNieve.velocidad2 = 0
			#lanzamiento de bola
			if event.key == pygame.K_q:
				print("lanzar1")
				proyectilMuñecoNieve.posicionx = muñecoNieve.posicionx
				proyectilMuñecoNieve.posiciony = muñecoNieve.posiciony
				permiso1 = True

			#jugador2
			if event.key == pygame.K_UP:
				osoPolar.velocidad1 = 0
			if event.key == pygame.K_DOWN:
				osoPolar.velocidad1 = 0
			if event.key == pygame.K_LEFT:
				osoPolar.velocidad2 = 0
			if event.key == pygame.K_RIGHT:
				osoPolar.velocidad2 = 0
			#lanzamiento de bola
			if event.key == pygame.K_PERIOD:
				print("lanzar2")
				proyectilOsoPolar.posicionx = osoPolar.posicionx
				proyectilOsoPolar.posiciony = osoPolar.posiciony
				permiso2 = True

	# da movimiento a los personajes
	muñecoNieve.posiciony += muñecoNieve.velocidad1
	muñecoNieve.posicionx += muñecoNieve.velocidad2
	osoPolar.posiciony += osoPolar.velocidad1
	osoPolar.posicionx += osoPolar.velocidad2

	pantalla.fill(negro)
	# dibuja a los jugadores 
	if permiso1:
		proyectilMuñecoNieve.dibujar()
		proyectilMuñecoNieve.trayectoria()
		if proyectilMuñecoNieve.posicionx >= proyectilMuñecoNieve.posicionx + proyectilMuñecoNieve.alcanze:
			permiso1 = False
	if permiso2:
		proyectilOsoPolar.dibujar()
		proyectilOsoPolar.trayectoria()
		if proyectilOsoPolar.posicionx >= proyectilOsoPolar.posicionx + proyectilOsoPolar.alcanze:
			permiso2 = False
	muñecoNieve.dibujar()
	osoPolar.dibujar()

	if osoPolar.posicionx == proyectilMuñecoNieve.posicionx:
		print("impacto")
	pygame.display.flip()
	reloj.tick(60)
