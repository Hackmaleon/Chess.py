import pygame
import time 
import sys

pygame.init()

#variables principales
size = (600,600)
background0 = pygame.image.load("chess_board.png")
background = pygame.transform.scale(background0,(600,600))
screen = pygame.display.set_mode(size)

#tamaño en pixeles de las piezas
pieze = 70

#diccionario con todas las casillas 
casillas = {'A8': (0, 0), 'A7': (0, 75), 'A6': (0, 150), 'A5': (0, 225), 'A4': (0, 300), 'A3': (0, 375), 'A2': (0, 450), 'A1': (0, 525), 'B8': (75, 0), 'B7': (75, 75), 'B6': (75, 150), 'B5': (75, 225), 'B4': (75, 300), 'B3': (75, 375), 'B2': (75, 450), 'B1': (75, 525), 'C8': (150, 0), 'C7': (150, 75), 'C6': (150, 150), 'C5': (150, 225), 'C4': (150, 300), 'C3': (150, 375), 'C2': (150, 450), 'C1': (150, 525), 'D8': (225, 0), 'D7': (225, 75), 'D6': (225, 150), 'D5': (225, 225), 'D4': (225, 300), 'D3': (225, 375), 'D2': (225, 450), 'D1': (225, 525), 'E8': (300, 0), 'E7': (300, 75), 'E6': (300, 150), 'E5': (300, 225), 'E4': (300, 300), 'E3': (300, 375), 'E2': (300, 450), 'E1': (300, 525), 'F8': (375, 0), 'F7': (375, 75), 'F6': (375, 150), 'F5': (375, 225), 'F4': (375, 300), 'F3': (375, 375), 'F2': (375, 450), 'F1': (375, 525), 'G8': (450, 0), 'G7': (450, 75), 'G6': (450, 150), 'G5': (450, 225), 'G4': (450, 300), 'G3': (450, 375), 'G2': (450, 450), 'G1': (450, 525), 'H8': (525, 0), 'H7': (525, 75), 'H6': (525, 150), 'H5': (525, 225), 'H4': (525, 300), 'H3': (525, 375), 'H2': (525, 450), 'H1': (525, 525)}

casillas_invertido = {v: k for k, v in casillas.items()}

sprites_list = pygame.sprite.Group()

bb = pygame.transform.scale(pygame.image.load("bb.png"),(pieze,pieze))
bk = pygame.transform.scale(pygame.image.load("bk.png"),(pieze,pieze))
bp = pygame.transform.scale(pygame.image.load("bp.png"),(pieze,pieze))
bq = pygame.transform.scale(pygame.image.load("bq.png"),(pieze,pieze))
br = pygame.transform.scale(pygame.image.load("br.png"),(pieze,pieze))
bn = pygame.transform.scale(pygame.image.load("bn.png"),(pieze,pieze))
wb = pygame.transform.scale(pygame.image.load("wb.png"),(pieze,pieze))
wk = pygame.transform.scale(pygame.image.load("wk.png"),(pieze,pieze))
wp = pygame.transform.scale(pygame.image.load("wp.png"),(pieze,pieze))
wq = pygame.transform.scale(pygame.image.load("wq.png"),(pieze,pieze))
wr = pygame.transform.scale(pygame.image.load("wr.png"),(pieze,pieze))
wn = pygame.transform.scale(pygame.image.load("wn.png"),(pieze,pieze))

black = []
white = []

#clases
class BB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bb
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

   #calcula los movimientos posibles 
    def Moves(self):
        global sprite_list

    #calcula las longitudes de las diagonales
        pos_casillas = (self.rect.x//75, self.rect.y//75)


        if (7-pos_casillas[0])<(7-pos_casillas[1]):
            casillas_posibles0 = 7-pos_casillas[0] 
        else :
            casillas_posibles0 = 7-pos_casillas[1] 

        if (pos_casillas[0])<(7-pos_casillas[1]):
            casillas_posibles1 = pos_casillas[0] 
        else :
            casillas_posibles1 = 7-pos_casillas[1] 

        if (pos_casillas[0])<(pos_casillas[1]):
            casillas_posibles2 = pos_casillas[0] 
        else :
            casillas_posibles2 = pos_casillas[1] 

        if (7-pos_casillas[0])<(pos_casillas[1]):
            casillas_posibles3 = 7-pos_casillas[0] 
        else :
            casillas_posibles3 = pos_casillas[1] 


        casillas0 = {}
        casillas1 = {}
        casillas2 = {}
        casillas3 = {}

        #n es el numero de casilla en la diagonal (se usa para calcular las coordendas)
        n = 1
        
        #k es la key de las coordenadas generadas (como se suma 1 al principio de cada for k comienza con -1)
        k = -1
        
        #s se usa para la comprobación de piezas (para que el alfil no atraviece piezas)
        s = 0
        
        #para cada diagonal calcula las casillas
        for i in range(casillas_posibles0): 
            s = 0
            k += 1
            casillas0[k] = (self.rect.x + n*75, self.rect.y + n*75)
            
            #revisa si hay una pieza en la casilla
            for a in sprites_list:
                if casillas0.get(k)[0] == a.rect.x and casillas0.get(k)[1] == a.rect.y:
                    
                    #elimina la casilla del diccionario si la pieza pertenece a su mismo bando
                    for b in black:
                        if b == a:
                            del casillas0[k]
                            k -= 1
                            print (k)
                    break
            else:
                s = 1

            if (s == 0):
                break    
            
            n += 1
       
        #k += 1
        n = 1

        for i in range(casillas_posibles1): 
            s = 0
            k += 1
            casillas1[k]=(self.rect.x - n*75, self.rect.y + n*75)
            
            for a in sprites_list:
                if casillas1.get(k)[0] == a.rect.x and casillas1.get(k)[1] == a.rect.y:
                    
                    for b in black:
                        if b == a:
                            del casillas1[k]
                            k -= 1
                            print (k)

                    break

            else:
                s = 1
            
            if (s == 0):
                break 
            
            n += 1

        #k += 1
        n = 1

        for i in range(casillas_posibles2): 
            s = 0
            k += 1
            casillas2[k] = (self.rect.x - n*75, self.rect.y - n*75)
            
            for a in sprites_list:
                if casillas2.get(k)[0] == a.rect.x and casillas2.get(k)[1] == a.rect.y:
                    
                    for b in black:
                        if b == a:
                            del casillas2[k]
                            k -= 1
                            print(k)

                    break
            else:
                s = 1
            
            if (s == 0):
                break 
            
            n += 1

        #k += 1
        n = 1

        for i in range(casillas_posibles3): 
            s = 0
            k += 1
            casillas3[k] = (self.rect.x + n*75, self.rect.y - n*75)
            
            for a in sprites_list:
                if casillas3.get(k)[0] == a.rect.x and casillas3.get(k)[1] == a.rect.y:
                
                    for b in black:
                        if b == a:
                            del casillas3[k]
                            k -= 1
                            print (k)
                    break
            else:
                s = 1
            
            if (s == 0):
                break 
            
            n += 1
        
        x = 0
        
        #print(casillas0)
        for i in casillas0:
            j = casillas0.get(x)
            l = casillas_invertido.get(j)
            print (f"1 {l} \n {j} {x}")
            x += 1
        
        
        #print(casillas1)
        for i in casillas1:
            j = casillas1.get(x)
            l = casillas_invertido.get(j)
            print (f"2 {l} \n {j} {x}")
            x += 1
                
        #print(casillas2)
        for i in casillas2:
            j = casillas2.get(x)
            l = casillas_invertido.get(j)
            print (f"3 {l} \n {j} {x}")
            x += 1

        #print(casillas3)
        for i in casillas3:
            j = casillas3.get(x)
            l = casillas_invertido.get(j)
            print (f"4 {l} \n {j} {x}")
            x += 1




class BK(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= bk
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def Moves (self):
        
        casillas0 = {}
        n = [-1, -1, 0, 1, 1, 1, 0, -1]
        m = [0, 1, 1, 1, 0, -1, -1, -1]
        z = 0
        
        for i in range (8):
            l= n[i]
            j= m[i]
            casillas0[z]= (self.rect.x + j*75, self.rect.y + l*75)
        #revisa que la jugada esté dentro del tablero
            
            g=casillas0[z]
            h= casillas_invertido.get(g)
            if h == None:
                del casillas0[z]
                print ("CHIVATO")
                z-=1
            
            z += 1
        
        for i in casillas0:
            j = casillas0.get(i)
            l= casillas_invertido.get(j)
            print (l)

# Classes of piezes 

class BN(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= bn
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class BP(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= bp
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class BQ(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= bq
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class BR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= br
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class WB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= wb
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class WK(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= wk
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class WN(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= wn
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class WP(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= wp
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class WQ(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= wq
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class WR(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image= wr
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

Bb0 = BB()
Bb1 = BB()
Bk = BK()
Bn0 = BN()
Bn1 = BN()
Bp0 = BP()
Bp1 = BP()
Bp2 = BP()
Bp3 = BP()
Bp4 = BP()
Bp5 = BP()
Bp6 = BP()
Bp7 = BP()
Bq = BQ()
Br0 = BR()
Br1 = BR()

Wb0 = WB()
Wb1= WB()
Wk = WK()
Wn0 = WN()
Wn1 = WN()
Wp0 = WP()
Wp1 = WP()
Wp2 = WP()
Wp3 = WP()
Wp4 = WP()
Wp5 = WP()
Wp6 = WP()
Wp7 = WP()
Wq = WQ()
Wr0 = WR()
Wr1 = WR()

Bb0.rect.x, Bb0.rect.y = casillas["C8"]
Bb1.rect.x, Bb1.rect.y = casillas["F8"]

Br0.rect.x, Br0.rect.y = casillas["D6"]
Br1.rect.x, Br1.rect.y = casillas["H8"]

Bn0.rect.x, Bn0.rect.y = casillas["B8"]
Bn1.rect.x, Bn1.rect.y = casillas["G8"]

Bq.rect.x, Bq.rect.y = casillas["D8"]
Bk.rect.x, Bk.rect.y = casillas["E8"]

Bp0.rect.x, Bp0.rect.y = casillas["A7"]
Bp1.rect.x, Bp1.rect.y = casillas["B7"]
Bp2.rect.x, Bp2.rect.y = casillas["C7"]
Bp3.rect.x, Bp3.rect.y = casillas["D7"]
Bp4.rect.x, Bp4.rect.y = casillas["E7"]
Bp5.rect.x, Bp5.rect.y = casillas["F7"]
Bp6.rect.x, Bp6.rect.y = casillas["G7"]
Bp7.rect.x, Bp7.rect.y = casillas["H7"]


Wr0.rect.x, Wr0.rect.y = casillas["A1"]
Wr1.rect.x, Wr1.rect.y = casillas["H1"]

Wn0.rect.x, Wn0.rect.y = casillas["B1"]
Wn1.rect.x, Wn1.rect.y = casillas["G1"]

Wb0.rect.x, Wb0.rect.y = casillas["C1"]
Wb1.rect.x, Wb1.rect.y = casillas["F1"]

Wq.rect.x, Wq.rect.y = casillas["D1"]
Wk.rect.x, Wk.rect.y = casillas["E1"]

Wp0.rect.x, Wp0.rect.y = casillas["A2"]
Wp1.rect.x, Wp1.rect.y = casillas["B2"]
Wp2.rect.x, Wp2.rect.y = casillas["C2"]
Wp3.rect.x, Wp3.rect.y = casillas["D2"]
Wp4.rect.x, Wp4.rect.y = casillas["E2"]
Wp5.rect.x, Wp5.rect.y = casillas["F2"]
Wp6.rect.x, Wp6.rect.y = casillas["G2"]
Wp7.rect.x, Wp7.rect.y = casillas["H2"]

sprites_list= pygame.sprite.Group()
sprites_list.add(Bb0, Bb1, Bk, Bn0, Bn1, Bp0, Bp1, Bp2,Bp3, Bp4, Bp5, Bp6, Bp7, Bq, Br0, Br1)
sprites_list.add(Wb0, Wb1, Wk, Wn0, Wn1, Wp0, Wp1, Wp2,Wp3, Wp4, Wp5, Wp6, Wp7, Wq, Wr0, Wr1)
black=[Br0, Bn0, Bb0, Bq, Bq, Bb1, Bn1, Br1, Bp0, Bp1, Bp2, Bp3, Bp4, Bp5, Bp6, Bp7]
white=[Wr0, Wn0, Wb0, Wq, Wq, Wb1, Wn1, Wr1, Wp0,Wp1, Wp2,Wp3, Wp4, Wp5, Wp6, Wp7]

#funciones
#cierra el juego
def Exit():
    global event 
    if event.type== pygame.QUIT:
        sys.exit()
        pygame.quit()

#bucle principal

while True:
    #detección de eventos 
    for event in pygame.event.get():
        Exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                for p in sprites_list:    
                    if p.rect.collidepoint(mouse_pos):
                        print(f"click, {p}")
                        p.Moves()

    screen.blit(background, (0,0))
    sprites_list.draw(screen)
    pygame.display.flip()
    
