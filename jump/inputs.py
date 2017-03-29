import pygame
import numbers

def onKeyEscape(c, pushed):
    if pushed:
        c['quit'] = True
    else:
        c['quit'] = False

def onKeyLeft(c, pushed):
    if pushed:
        if c['axisX'] <= 0.0:
            c['axisX'] = -1.0 + abs(1 * c['axisY'])
        else:
            c['axisX'] = 0.0
    else:
        c['axisX'] = 0.0

def onKeyUp(c, pushed):
    if pushed:
        if c['axisY'] <= 0.0:
            c['axisY'] = -1.0 + abs(1 * c['axisX'])
        else:
            c['axisY'] = 0.0
    else:
        c['axisY'] = 0.0

def onKeyRight(c, pushed):
    if pushed:
        if c['axisX'] >= 0.0:
            c['axisX'] = 1.0 - abs(1 * c['axisY'])
        else:
            c['axisX'] = 0.0
    else:
        c['axisX'] = 0.0

def onKeyDown(c, pushed):
    if pushed:
        if c['axisY'] >= 0.0:
            c['axisY'] = 1.0 - abs(1 * c['axisX'])
        else:
            c['axisY'] = 0.0
    else:
        c['axisY'] = 0.0

def onKeyDash(c, pushed):
    if pushed:
        c['dash'] = True
    else:
        c['dash'] = False

class EventHandler:
    MAX_PLAYER_NUMBER = 4
    BIND_TABLE = [{
        pygame.K_ESCAPE: onKeyEscape
    }, {
        pygame.K_LEFT: onKeyLeft,
        pygame.K_UP: onKeyUp,
        pygame.K_RIGHT: onKeyRight,
        pygame.K_DOWN: onKeyDown,
        pygame.K_KP_PERIOD: onKeyDash
    }]

    def __init__(self, pNb = 1):
<<<<<<< HEAD
        print("New class EventHandler")
=======
>>>>>>> origin/master
        #Attributes
        self.controllers = [{
            'quit': False
        }];
        self.playerNumber = 0

        #Initialize the controllers
        self.setPlayerNumber(pNb)

    def getInputs(self):
        #Listen events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                onKeyEscape(self.controllers[0], True)
            elif event.type == pygame.KEYDOWN:
                for i in range(0, self.playerNumber + 1):
                    if self.BIND_TABLE[i].has_key(event.key):
                        self.BIND_TABLE[i][event.key](self.controllers[i], True)
            elif event.type == pygame.KEYUP:
                for i in range(0, self.playerNumber + 1):
                    if self.BIND_TABLE[i].has_key(event.key):
                        self.BIND_TABLE[i][event.key](self.controllers[i], False)

        return self.controllers

    def setPlayerNumber(self, nb):
        if nb >= 0 and nb <= self.MAX_PLAYER_NUMBER:
            while self.playerNumber > nb:
                self.controllers.pop()
                self.playerNumber -= 1

            while self.playerNumber < nb:
                self.controllers.append({
                    'axisX': 0.0,
                    'axisY': 0.0,
                    'dash': False
                })
                self.playerNumber += 1
