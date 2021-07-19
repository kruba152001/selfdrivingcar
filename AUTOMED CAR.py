import pygame
pygame.init()
window = pygame.display.set_caption("TESLA BY KRUBA")
window=pygame.display.set_mode((1200,400))
track=pygame.image.load("track6.png")
car=pygame.image.load("tesla.png")
car=pygame.transform.scale(car,(30,60))
carx=150
cary=300
focusdis=25
direction='up'
camxoffset=0
camyoffset=0
drive = True
#create clock to reduse speed
clock= pygame.time.Clock()
while drive: 
    for event in pygame.event.get(): #to stop the while loop
        if event.type==pygame.QUIT:
            drive==False

    clock.tick(60)
    camx=carx + camxoffset+15 #move camera position
    camy=cary+camyoffset+15
    #detect road
    up_px= window.get_at((camx, camy - focusdis ))[0]
    down_px= window.get_at((camx, camy + focusdis ))[0]
    right_px= window.get_at((camx+focusdis, camy))[0]
    print(up_px,down_px,right_px)
    #change direction
    #change right direction
    if direction=='up' and up_px!=255 and right_px==255:
        direction= 'right'
        camxoffset=30
        car=pygame.transform.rotate(car, -90)
    elif direction=='right' and right_px!=255 and down_px==255: #change down
        direction='down'
        carx=carx+30
        camxoffset=0
        camyoffset=30
        car=pygame.transform.rotate(car , -90)
    elif direction =='down' and down_px!=255 and right_px==255:
        direction='right'
        cary=cary+30
        camxoffset=30
        camyoffset=0
        car=pygame.transform.rotate(car , 90)
    elif direction=='right' and right_px!=255 and up_px==255: #again up
        direction='up'
        carx=carx+30
        camxoffset=0
        car=pygame.transform.rotate(car ,90)




    #move car
    if direction=='up' and up_px==255:
     cary=cary-2  #move car
    elif direction== 'right' and right_px==255: #move right
        carx=carx+2
    elif direction=='down' and down_px==255:
        cary=cary+2

    window.blit(track, (0,0))
    window.blit(car,(carx,cary))  #image transfer
    pygame.draw.circle(window,(0,255,0),(camx,camy),5,5) #draw camera
    pygame.display.update()


