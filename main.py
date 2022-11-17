#Proyecto 3
#Graficas por computadora
#Codigo referencia: https://github.com/churly92/RendererOpenGL_2022
#Autor: Mariana David 201055

#Importaciones
from pickle import TRUE
import pygame
from pygame.locals import *
from shaders import *
from gl import Renderer, Model
from math import cos, sin, radians

#Medidas de ventana
width = 1000
height = 600

#Tiempo
deltaTime = 0.0

#Inicialización
pygame.init()
screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(vertex_shader, fragment_shader)
rend.target.z = -5

objeto = Model("planta.obj", "model_normal.bmp")

# #Cono/planta
objeto.position.z -= 9
objeto.position.y -= 2
objeto.position.x -= 0
objeto.scale.x = 10
objeto.scale.y = 10
objeto.scale.z = 10
#Prueba de posiciones
# #Taza
# objeto.position.z -= 4
# objeto.position.y -= 0.9
# objeto.position.x -= 0.7
# objeto.scale.x = 0.2
# objeto.scale.y = 0.2
# objeto.scale.z = 0.2i
# # #HAT/wheel
# objeto.position.z -= 8
# objeto.position.y -= 0.5
# objeto.position.x -= 0
# objeto.scale.x = 4
# objeto.scale.y = 4
# objeto.scale.z = 4

rend.scene.append( objeto )
#Sonido de fondo 
pygame.mixer.music.load("slow.mp3")
pygame.mixer.music.play(10)

isRunning = True
while isRunning:

    keys = pygame.key.get_pressed()
    #Movimiento del objeto
    rend.scene[0].rotation.y += 25 * deltaTime
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
                #rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objecto = Model("planta.obj", "model_normal.bmp")
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
                #rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objecto = Model("hat.obj", "model_normal.bmp")
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
                #rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objecto = Model("llanta.obj", "model_normal.bmp")
                #Posición para que se vea bien
                objeto.position.z -= 8
                objeto.position.y -= 0.5
                objeto.position.x -= 0
                objeto.scale.x = 4
                objeto.scale.y = 4
                objeto.scale.z = 4 
                #Renderizar objeto Llanta
                rend.scene.append(objeto)
            
            # if event.key == K_p:
            #     #Modelo Planta
            #     pygame.init()
            #     screen4 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL)
            #     rend = Renderer (screen4)
            #     #rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
            #     objecto = Model("planta.obj", "model_normal.bmp")
            #     #Posición para que se vea bien
            #     objeto.position.z -= 9
            #     objeto.position.y -= 2
            #     objeto.position.x -= 0
            #     objeto.scale.x = 10
            #     objeto.scale.y = 10
            #     objeto.scale.z = 10
            #     #Renderizar objeto Planta
            #     rend.scene.append(objeto)

            if event.key == K_t:
                #Modelo Taza
                pygame.init()
                screen5 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL)
                rend = Renderer (screen5)
                #rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                objecto = Model("taza.obj", "model_normal.bmp")
                #Posición para que se vea bien
                objeto.position.z -= 4
                objeto.position.y -= 0.9
                objeto.position.x -= 0.7
                objeto.scale.x = 0.2
                objeto.scale.y = 0.2
                objeto.scale.z = 0.2
                #Renderizar objeto Taza
                rend.scene.append(objeto)

            #Asignacion de shaders con keys 
            if event.key == K_1:
                rend.filledMode()
            if event.key == K_2:
                rend.wireframeMode()
            if event.key == K_3:
                rend.setShaders(vertex_shader, fragment_shader)
            if event.key == K_4:
                rend.setShaders(vertex_shader, fragment_shader)

    #DisCamara
    distance = ((rend.camPosition.x)**2 + (rend.camPosition.y)**2 + (rend.camPosition.z)**2)**0.5
    
    #Zoom 
    if keys[K_z]:
        rend.camPosition += 0.01
    if keys[K_x]:
        rend.camPosition -= 0.01
    
    #Traslaciones de camara con keys 
    if keys[K_w]:
            rend.camPosition.z += 1 * deltaTime
    if keys[K_s]:
        rend.camPosition.z -= 1 * deltaTime
    if keys[K_d]:
            rend.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= 1 * deltaTime
    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime

    #Roraciones de la camara con respecto al objeto
    if keys[K_y]:
        rend.camRotation.y += 15 * deltaTime
    if keys[K_u]:
        rend.camRotation.y -= 15 * deltaTime
    if keys[K_i]:
        rend.camRotation, 25 * deltaTime
    if keys[K_o]:
        rend.camPosition, 25 * deltaTime

    rend.target.y = rend.camPosition.y
    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance
    
    #Manejo de luces 
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime


    #Finalizacón 
    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
