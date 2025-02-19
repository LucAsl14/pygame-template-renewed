from __future__ import annotations

from pygame import Surface
from src.core import *
from .area_spell import AreaSpell

class Mud(AreaSpell):
    def __init__(self, scene: MainScene) -> None:
        super().__init__(scene, 1, "earth", 20, 125, Layer.GROUND)

    def draw_charge(self, screen: Surface) -> None:
        trans_surf = pygame.surface.Surface(Vec(2 * self.rad), pygame.SRCALPHA)
        pygame.draw.circle(trans_surf, EARTH, Vec(self.rad), self.rad)
        trans_surf.set_alpha(int(255 * self.charging_time.progress))
        self.set_screen_pos(screen)
        screen.blit(trans_surf, self.screen_pos - Vec(self.rad))

    def draw_spell(self, screen: Surface) -> None:
        self.set_screen_pos(screen)
        pygame.draw.circle(screen, EARTH, self.screen_pos, self.rad)

    def update_spell(self, dt: float) -> None:
        if self.scene.player.pos.distance_to(self.pos) < self.rad:
            self.scene.player.vel *= 0.0000004 ** dt
        super().update_spell(dt)
