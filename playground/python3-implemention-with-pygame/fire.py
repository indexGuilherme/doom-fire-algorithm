from random import randint
import pygame

pygame.init()

screenWidth = 720
screenHeight = 480

fireWidth = 72
fireHeight = 48

pixelWidth = screenWidth // fireWidth
pixelHeight =  screenHeight // fireHeight

fireColorsPalette = [{"r":7,"g":7,"b":7},{"r":31,"g":7,"b":7},{"r":47,"g":15,"b":7},{"r":71,"g":15,"b":7},{"r":87,"g":23,"b":7},{"r":103,"g":31,"b":7},{"r":119,"g":31,"b":7},{"r":143,"g":39,"b":7},{"r":159,"g":47,"b":7},{"r":175,"g":63,"b":7},{"r":191,"g":71,"b":7},{"r":199,"g":71,"b":7},{"r":223,"g":79,"b":7},{"r":223,"g":87,"b":7},{"r":223,"g":87,"b":7},{"r":215,"g":95,"b":7},{"r":215,"g":95,"b":7},{"r":215,"g":103,"b":15},{"r":207,"g":111,"b":15},{"r":207,"g":119,"b":15},{"r":207,"g":127,"b":15},{"r":207,"g":135,"b":23},{"r":199,"g":135,"b":23},{"r":199,"g":143,"b":23},{"r":199,"g":151,"b":31},{"r":191,"g":159,"b":31},{"r":191,"g":159,"b":31},{"r":191,"g":167,"b":39},{"r":191,"g":167,"b":39},{"r":191,"g":175,"b":47},{"r":183,"g":175,"b":47},{"r":183,"g":183,"b":47},{"r":183,"g":183,"b":55},{"r":207,"g":207,"b":111},{"r":223,"g":223,"b":159},{"r":239,"g":239,"b":199},{"r":255,"g":255,"b":255}]

def createScreen():
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    return screen, clock

def createFireDataStructure():
    pixelsFire = [0 for x in range(fireWidth * fireHeight)]
    createFireSource(pixelsFire)
    return pixelsFire

def createFireSource(pixelsFire):
    lastCol = fireHeight - 1
    for rows in range(fireWidth):
        pixelIndex = rows + (fireWidth * lastCol)
        pixelsFire[pixelIndex] = 36

def calculateFirePropagation(pixelsFire):
    for rows in range(fireWidth):
        for cols in range(fireHeight):
            pixelIndexCurrent = rows + (fireWidth * cols)
            updateFireIntensityPerPixel(pixelsFire, pixelIndexCurrent)

def updateFireIntensityPerPixel(pixelsFire, pixelIndexCurrent):
    pixelIndexNeighbor = pixelIndexCurrent + fireWidth   

    decay = randint(0, 3)

    if pixelIndexNeighbor >= fireHeight * fireWidth - decay:
        return                

    belowPixelFireIntensity = pixelsFire[pixelIndexNeighbor] 

    fireIntensity = belowPixelFireIntensity - decay    
    newFireIntensity = fireIntensity if fireIntensity > 0 else 0   

    pixelsFire[pixelIndexCurrent + decay] = newFireIntensity 

def calculateFireColor(pixelsFire, pixelIndex):     
    colorIndex = pixelsFire[pixelIndex]
    color = fireColorsPalette[colorIndex]
    return (color["r"], color["g"], color["b"])

def renderFire(screen, pixelsFire):
    calculateNewPosition = lambda x, y: x * y 

    for rows in range(fireWidth):
        for cols in range(fireHeight):
            pixelIndex = rows + (fireWidth * cols)            
            fireColor = calculateFireColor(pixelsFire, pixelIndex)

            x = calculateNewPosition(rows, pixelWidth)
            y = calculateNewPosition(cols, pixelHeight)

            pygame.draw.rect(screen, fireColor, (x, y, pixelWidth, pixelHeight))           


screen, clock = createScreen()
pixelsFire = createFireDataStructure()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))   

    calculateFirePropagation(pixelsFire)
    renderFire(screen, pixelsFire)

    pygame.display.flip()
    clock.tick(30)          
