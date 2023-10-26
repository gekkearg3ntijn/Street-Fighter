import pygame  
import sys  
  
  
# initializing the constructor  
pygame.init()  
  
# screen resolution  
res = (720,720)  
  
# opens up a window  
screen = pygame.display.set_mode(res)  
  
# white color  
color = (255,255,255)  
  
# light shade of the button  
color_light = (170,170,170)  
  
# dark shade of the button  
color_dark = (100,100,100)  
  
# stores the width of the  
# screen into a variable  
width = screen.get_width()  
  
# stores the height of the  
# screen into a variable  
height = screen.get_height()  
  
# defining a font  
smallfont = pygame.font.SysFont('Corbel',35)  
  
# rendering a text written in  
# this font  
text_1 = smallfont.render('halloween' , True , color)  
text_2 = smallfont.render('boksring' , True , color)  
text_3 = smallfont.render('boksring' , True , color)  
text_4 = smallfont.render('boksring' , True , color)  
text_5 = smallfont.render('boksring' , True , color)  
  
while True:  
      
    for ev in pygame.event.get():  
          
        if ev.type == pygame.QUIT:  
            pygame.quit()  
              
        #checks if a mouse is clicked  
        if ev.type == pygame.MOUSEBUTTONDOWN:  
              
            #if the mouse is clicked on the  
            # button the game is terminated  
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                pygame.quit()  
            if width/2 <= mouse[0] <= width/2+140 and height/2 + 200 <= mouse[1] <= height/2+40:  
                pygame.quit()  
                  
    # fills the screen with a color  
    screen.fill((60,25,60))  
      
    # stores the (x,y) coordinates into  
    # the variable as a tuple  
    mouse = pygame.mouse.get_pos()  
      
    # if mouse is hovered on a button it  
    # changes to lighter shade  
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
        pygame.draw.rect(screen,color_dark,[width/2,height/2+200,140,40])   
    elif width/2 <= mouse[0] <= width/2+140 and height/2 +200<= mouse[1] <= height/2+240:  
        pygame.draw.rect(screen,color_light,[width/2,height/2+200,140,40]) 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])        
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])  
        pygame.draw.rect(screen,color_dark,[width/2,height/2+200,140,40])  

    # if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
    #     pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])  
    # elif width/2 <= mouse[0] <= width/2+140 and height/2 +200<= mouse[1] <= height/2+40:  
    #     pygame.draw.rect(screen,color_light,[width/2,height/2+200,140,40])       
    # else:  
    #     pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])  
    #     pygame.draw.rect(screen,color_dark,[width/2,height/2+200,140,40])  
      
    # superimposing the text onto our button  
    screen.blit(text_1, (width/2+50,100))  
    screen.blit(text_2 , (width/2+50,200))
    screen.blit(text_3 , (width/2+50,300))  
    screen.blit(text_4 , (width/2+50,400))  
    screen.blit(text_5 , (width/2+50,500))  
      
    # updates the frames of the game  
    pygame.display.update()