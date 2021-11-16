from graphics import *
import time

def fundo(win): 
    win.setBackground("Gray")
    # imagem = Image(Point(425, 190), "fundo.png")
    # imagem.draw(win)
    
class Personagem:
    def __init__(self, janela):
        self.janela = janela
        self.imagem = Image(Point(100,340), "adventurer-idle-2-00.png")
        self.centro = self.imagem.getAnchor()
        self.cont_parado = 0
        self.cont_correndo = 0
        self.cont_pulando = 0
        self.cont_descendo = 0
        self.cont_attack = 0
        
        
    def movimento(self, para, corre,pula,desce,ataque):
        while True:
            self.verifica = self.janela.checkKey()
            if self.verifica == "Right":
                self.imagem.move(15, 0)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 6:
                    self.cont_correndo = 0

            elif self.verifica == "Left":
                self.imagem.move(-15, 0)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, corre[self.cont_correndo])
                self.imagem.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.cont_correndo+=1
                time.sleep(.001)
                if self.cont_correndo >= 6:
                    self.cont_correndo = 0

            elif self.verifica == "Up":
                self.imagem.move(0,-35)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, pula[self.cont_pulando])
                self.imagem.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.cont_pulando+=1
                time.sleep(.001)
                self.imagem.move(0,35)
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, desce[self.cont_descendo])
                self.imagem.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.cont_pulando+=1
                time.sleep(.001)
                if self.cont_pulando >= 4:
                    self.cont_pulando = 0
                elif self.cont_descendo >= 2:
                    self.cont_descendo = 0

            elif self.verifica == "k":
                self.centro = self.imagem.getAnchor()
                self.imagem = Image(self.centro, ataque[3])
                self.imagem.draw(self.janela)
                time.sleep(.08)
                self.imagem.undraw()
                self.cont_attack+=1
                time.sleep(0.3)
                if self.cont_attack >= 6:
                    self.cont_attack = 0
     
            else: 
                if self.cont_parado >= 4:
                    self.cont_parado = 0
                self.imagem = Image(self.centro, para[self.cont_parado])
                self.imagem.draw(self.janela)
                time.sleep(.09)
                self.imagem.undraw()
                self.cont_parado+=1


def main (Titulo: str, largura: int, altura:int):

    win = GraphWin(Titulo, largura, altura)
    fundo(win)
    player = Personagem(win)
    parado = ["adventurer-idle-2-00.png","adventurer-idle-2-01.png","adventurer-idle-2-02.png","adventurer-idle-2-03.png"]
    correndo = ["adventurer-run-00.png","adventurer-run-01.png", "adventurer-run-02.png", "adventurer-run-03.png", "adventurer-run-04.png","adventurer-run-05.png"]
    pulando = ["adventurer-jump-00.png","adventurer-jump-01.png", "adventurer-jump-02.png", "adventurer-jump-03.png"]
    descendo = ["adventurer-fall-00.png","adventurer-fall-01.png"]
    attack = ["adventurer-attack2-00.png","adventurer-attack2-01.png", "adventurer-attack2-02.png", "adventurer-attack2-03.png", "adventurer-attack2-04.png", "adventurer-attack2-05.png"]
    player.movimento(parado, correndo,pulando,descendo,attack)
    
    win.getMouse()
    win.close()

if __name__ == "__main__":    
    main("Animação", 850, 478)
