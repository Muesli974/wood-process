import pygame, time, math, sys

pygame.init()
screen = pygame.display.set_mode((100, 100), 0, 32)
print("Number of joysticks: ")
jsNb = pygame.joystick.get_count() 
print(jsNb)

if jsNb <= 0:
    sys.exit("No joystick found!")

js = pygame.joystick.Joystick(0)
js.init()

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    axisX = js.get_axis(0)
    axisY = js.get_axis(1)

    screen.fill((35, 35, 35))
    pygame.draw.circle(screen, (50, 50, 175), (int((axisX + 1) * 40) + 10, int((axisY + 1) * 40) + 10), 10)
    pygame.display.flip()

js.quit()
pygame.quit()

