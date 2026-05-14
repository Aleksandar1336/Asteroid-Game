
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame

class Player(CircleShape):
      def __init__(self, x, y):
          super().__init__(x, y, PLAYER_RADIUS)
          self.x = x
          self.y = y
          self.PLAYER_RADIUS = PLAYER_RADIUS
          self.rotation = 0
      def draw(self, screen):
        pygame.draw.polygon(
        screen,
        "white",
        self.triangle(),
        LINE_WIDTH
    )
      def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
      def move(self, dt):
         unit_vector = pygame.Vector2(0, 1)
         rotated_vector = unit_vector.rotate(self.rotation)
         rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
         self.position += rotated_with_speed_vector
      def rotate(self, dt):
         self.rotation += PLAYER_TURN_SPEED * dt
      def update(self, dt):
         keys = pygame.key.get_pressed()

         if keys[pygame.K_d]:   # rotate right
             self.rotate(dt)

         if keys[pygame.K_a]:   # rotate left
            self.rotate(-dt)

         if keys[pygame.K_w]:   # move forward
             self.move(dt)

         if keys[pygame.K_s]:   # move backwards
            self.move(-dt)