import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw an Irregular Figure and Calculate Area")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Variables
drawing = False
points = []
calculation_done = False
estimated_area = 0
iterations = 0

# Function to check if a point is inside the drawn figure
def is_inside_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    px, py = polygon[0]
    for i in range(1, n + 1):
        sx, sy = polygon[i % n]
        if y > min(py, sy):
            if y <= max(py, sy):
                if x <= max(px, sx):
                    if py != sy:
                        xinters = (y - py) * (sx - px) / (sy - py) + px
                    if px == sx or x <= xinters:
                        inside = not inside
        px, py = sx, sy

    return inside

# Function to calculate area using Monte Carlo method
def calculate_area(polygon, bounding_box, num_points=10000):
    global estimated_area, iterations
    x_min, y_min, x_max, y_max = bounding_box
    total_points = 0
    inside_points = 0

    for _ in range(num_points):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        total_points += 1

        # Check if the point is inside the polygon
        if is_inside_polygon((x, y), polygon):
            # Draw green dot if inside the polygon
            pygame.draw.circle(screen, GREEN, (int(x), int(y)), 1)
            inside_points += 1
        else:
            # Draw red dot if outside the polygon
            pygame.draw.circle(screen, RED, (int(x), int(y)), 1)

        # Show the number of iterations
        iterations = total_points
        pygame.display.flip()

    # Calculate area
    bounding_area = (x_max - x_min) * (y_max - y_min)
    estimated_area = (inside_points / total_points) * bounding_area
    return estimated_area

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                points = []
                calculation_done = False  # Reset calculation on new drawing

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
                # Stop drawing and calculate the area
                if len(points) > 2:  # Only calculate if polygon has more than 2 points
                    points.append(points[0])  # Close the polygon

                    # Determine bounding box
                    x_coords = [p[0] for p in points]
                    y_coords = [p[1] for p in points]
                    bounding_box = (min(x_coords), min(y_coords), max(x_coords), max(y_coords))

                    # Calculate the area
                    estimated_area = calculate_area(points, bounding_box)
                    calculation_done = True

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                points.append(event.pos)

    # Drawing the figure while drawing
    if drawing and len(points) > 1:
        pygame.draw.lines(screen, BLACK, False, points, 2)

    # If drawing is complete and calculation is done, draw the polygon and the estimated area
    if calculation_done:
        pygame.draw.polygon(screen, BLACK, points, 2)
        area_text = f"Estimated Area: {estimated_area:.2f} square pixels"
        font = pygame.font.SysFont(None, 30)
        area_label = font.render(area_text, True, BLACK)
        screen.blit(area_label, (10, 10))  # Display area on screen

        # Display the number of iterations on the screen
        iteration_text = f"Iterations: {iterations}"
        iteration_label = font.render(iteration_text, True, BLACK)
        screen.blit(iteration_label, (10, 40))  # Display iterations below area

    pygame.display.flip()

# Quit pygame
pygame.quit()
