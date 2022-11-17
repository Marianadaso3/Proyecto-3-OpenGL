#Proyecto 3
#Graficas por computadora
#Codigo referencia: https://github.com/churly92/RendererOpenGL_2022
#Autor: Mariana David 201055






#Prueba de posiciones
#Taza
# objeto.position.z -= 4
# objeto.position.y -= 0.9
# objeto.position.x -= 0.7
# objeto.scale.x = 0.2
# objeto.scale.y = 0.2
# objeto.scale.z = 0.2
# #HAT/wheel
# objeto.position.z -= 8
# objeto.position.y -= 0.5
# objeto.position.x -= 0
# objeto.scale.x = 4
# objeto.scale.y = 4
# objeto.scale.z = 4


#Importaciones
import pygame
from pygame.locals import *
from shaders import *
from gl import Renderer, Model
from math import cos, sin, radians
import shaders 

#Medidas de ventana
width = 1000
height = 600

#Tiempo
deltaTime = 0.0

#Inicialización
pygame.init()
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader )
rend.target.z = -5

#Inicializar con un objeto predeterminado
objeto = Model('planta.obj', 'textp.jpg')
# #Cono/planta
objeto.position.z -= 9
objeto.position.y -= 2
objeto.position.x -= 0
objeto.scale.x = 10
objeto.scale.y = 10
objeto.scale.z = 10
rend.scene.append( objeto )

#fondo2
fondo = pygame.image.load("fondo.jpg")
screen.blit(fondo, (0,0))

#Sonido de fondo 
pygame.mixer.music.load("slow.mp3")
pygame.mixer.music.play(10)


isRunning = True
while isRunning:
    keys = pygame.key.get_pressed()

    #Cambios de objetos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            if event.key == K_c:
                #Modelo Cono
                pygame.init() 
                #Definir escena con objeto y renderizarla
                screen1 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL)
                rend = Renderer (screen1)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objeto = Model("cono.obj", "textc.png")
                #Posición para que se vea bien
                objeto.position.z -= 9
                objeto.position.y -= 2
                objeto.position.x -= 0
                objeto.scale.x = 10
                objeto.scale.y = 10
                objeto.scale.z = 10
                #Renderizar objeto Cono
                rend.scene.append(objeto)

            
            if event.key == K_h:
                #Modelo Hat (Sombrero)
                pygame.init()
                screen2 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL)
                rend = Renderer (screen2)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objeto = Model("hat.obj", "txth.jpg")
                #Posición para que se vea bien
                objeto.position.z -= 8
                objeto.position.y -= 0.5
                objeto.position.x -= 0
                objeto.scale.x = 4
                objeto.scale.y = 4
                objeto.scale.z = 4 
                #Renderizar objeto Hat (Sombrero)
                rend.scene.append(objeto)


            if event.key == K_l:
                #Modelo Llanta
                pygame.init()
                screen3 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL)
                rend = Renderer (screen3)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objeto = Model("llanta.obj", "textll.jpg")
                #Posición para que se vea bien
                objeto.position.z -= 8
                objeto.position.y -= 0.5
                objeto.position.x -= 0
                objeto.scale.x = 4
                objeto.scale.y = 4
                objeto.scale.z = 4 
                #Renderizar objeto Llanta
                rend.scene.append(objeto)


            if event.key == K_t:
                #Modelo Taza
                pygame.init()
                screen4 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL)
                rend = Renderer (screen4)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objeto = Model("taza.obj", "textt.jpg")
                #Posición para que se vea bien
                objeto.position.z -= 4
                objeto.position.y -= 0.9
                objeto.position.x -= 0.7
                objeto.scale.x = 0.2
                objeto.scale.y = 0.2
                objeto.scale.z = 0.2
                #Renderizar objeto Taza
                rend.scene.append(objeto)

            if event.key == K_p:
                #Modelo Planta
                pygame.init()
                screen5 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL)
                rend = Renderer (screen5)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objeto = Model('planta.obj', 'textp.jpg')
                #Posicion de planta
                objeto.position.z -= 9
                objeto.position.y -= 2
                objeto.position.x -= 0
                objeto.scale.x = 10
                objeto.scale.y = 10
                objeto.scale.z = 10
                 #Renderizar objeto Planta de nuevo
                rend.scene.append( objeto )

            #Asignacion de shaders con keys 
            if event.key == K_1:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
            if event.key == K_2:
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

    #Zoom 
    if keys[K_z]:
        if rend.camDistance > 2:
            rend.camDistance -= 2 * deltaTime
    elif keys[K_x]:
        if rend.camDistance < 10:
            rend.camDistance += 2 * deltaTime
    
    #Movimiento de camara con keys 
    #Lado a Lado 
    if keys[K_a]:
        rend.angle -= 30 * deltaTime
    elif keys[K_d]:
        rend.angle += 30 * deltaTime
    #Arriba y abajo 
    if keys[K_w]:
        if rend.camPosition.y < 2:
            rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        if rend.camPosition.y > -2:
            rend.camPosition.y -= 5 * deltaTime

    #Rotaciones de la camara con respecto al objeto
    if keys[K_y]:
        rend.scene[0].rotation.y += 15 * deltaTime
    if keys[K_u]:
        rend.scene[0].rotation.y -= 15 * deltaTime

    #Manejo de luces 
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    rend.target.y = rend.camPosition.y
    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance

    #Finalizacón 
    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
