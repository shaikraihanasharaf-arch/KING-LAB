import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Dragon Movement")

# Dragon position
x = 350
y = 200

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Mouse scroll
        if event.type == pygame.MOUSEWHEEL:
            y -= event.y * 20

    screen.fill((200, 230, 255))

    # Simple dragon representation
    pygame.draw.circle(screen, (0, 150, 0), (x, y), 40)  # head
    pygame.draw.polygon(
        screen,
        (0, 120, 0),
        [(x - 30, y - 20), (x - 80, y - 60), (x - 60, y + 10)]
    )

    pygame.draw.circle(screen, (255, 255, 255), (x - 15, y - 10), 8)
    pygame.draw.circle(screen, (0, 0, 0), (x - 15, y - 10), 4)

    pygame.display.update()

pygame.quit()