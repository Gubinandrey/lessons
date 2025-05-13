import pygame
import util
import json
import platform

if platform.system() == 'Darwin':
    BASE_DIR =  '/Users/andrey/python/lessons/game'
else:
    BASE_DIR = 'game'

class Tile_map:
    def __init__(self, scrin, level):
        self.scrin=scrin
        self.camera_x=0
      
        self.now_level=level
        self.camera_y=0
        self.history=[]
        self.grid_stile=True
        self.off_grid_tile=[]
        # self.tile_size=16*6
        # self.tile_map={}
        self.loading()
        self.fon=util.load(f'{BASE_DIR}/images/background.png', 7)
        self.resource={
            'grass':util.load_img(f'{BASE_DIR}/images/tiles/grass', self.k),
            'stone':util.load_img(f'{BASE_DIR}/images/tiles/stone', self.k),
            'large_decor':util.load_img(f'{BASE_DIR}/images/tiles/large_decor', self.k),
            'decor':util.load_img(f'{BASE_DIR}/images/tiles/decor', self.k),
            'nps':util.load_img(f'{BASE_DIR}/images/tiles/spawners', self.k+2),
            'Порталоткройся':util.load_img(f'{BASE_DIR}/images/tiles/Порталоткройся', self.k+2),
            'coins':util.load_img(f'{BASE_DIR}/images/tiles/coins', self.k+2), 
            'зелья':util.load_img(f'{BASE_DIR}/images/tiles/зелья', 0.4)
        }
        self.resource_names=['grass', 'stone', 'large_decor', 'decor','nps', 'Порталоткройся', 'coins', "зелья"]
        self.curent_resourse_index=0
        self.curent_index=0
        
    def render(self):
        self.scrin.blit(self.fon, (0, 0))
        for asd in self.off_grid_tile:
            x=asd['position'][0]*self.k-self.camera_x
            y=asd['position'][1]*self.k-self.camera_y
            desk=asd
            image=self.resource[desk['type']][desk['index']]
            self.scrin.blit(image, (x, y))
        for asd in self.tile_map:
            
            desk=self.tile_map[asd]
            asd=[asd[1:].split(',')[0], asd[:-1].split(',')[1]]
            x=int(asd[0])*self.tile_size
            y=int(asd[1])*self.tile_size
            image=self.resource[desk['type']][desk['index']]
            self.scrin.blit(image, (x-self.camera_x, y-self.camera_y))
        
    def update(self):
        pass
    def loading(self):
        try:
            f=open(f'{BASE_DIR}/map'+str(self.now_level)+'.json', 'r')
            settings=json.load(f)
            self.tile_map=settings['tile_map']
            self.tile_size=settings['tile_size']
            self.camera_x=settings['camera_x']
            self.camera_y=settings['camera_y']
            self.off_grid_tile=settings['off_grid']
            self.k = self.tile_size // 16
            self.portal_load=util.load(f'{BASE_DIR}/images/tiles/Порталоткройся/314251053108211 (4).png', self.k+2)

            for tile in self.tile_map.values():
                if tile['type'] == 'spawners':
                    tile['type'] = 'nps'
            for tile in self.off_grid_tile:
                if tile['type'] == 'spawners':
                    tile['type'] = 'nps'
            for asd in self.tile_map:
                self.tile=self.tile_map[asd]
                if self.tile['type']=='Порталоткройся':
                    self.portal_bbx=self.portal_load.get_rect()
                    
                    asd=[asd[1:].split(',')[0], asd[:-1].split(',')[1]]
                    x=int(asd[0])*self.tile_size
                    y=int(asd[1])*self.tile_size
                    self.portal_bbx.x=x
                    self.portal_bbx.y=y

            f.close()
        except:
            print('error has occured')
            pass
    def issolid(self, x, y):
        self.tx=x//self.tile_size
        self.ty=y//self.tile_size
        self.key=str((self.tx, self.ty))
        if self.key not in self.tile_map or not self.tile_map[self.key].get('solid', True):
            return False
        else:
            self.tile=self.tile_map[self.key]
            if self.tile['type']=='grass' or self.tile['type']=='stone':
                return True
            else:
                return False
    def get_coins(self):
        self.coins=[]
        
        for p in self.tile_map.copy():
            asd=self.tile_map[p]
            if asd ['type']=='coins':
                c=tuple(map(int, p[1:-1].split(',')))
                c=(c[0]*self.tile_size, c[1]*self.tile_size)
                del self.tile_map[p]
                self.coins.append(c)
        return self.coins



    # it will be more optimized for Andrew's laptop
    def get_intersections(self, player_bbx):
        self.tiles_intersections=[]
        i_start = player_bbx.left // self.tile_size - 1
        i_end = player_bbx.right // self.tile_size + 1
        j_start = player_bbx.top // self.tile_size - 1
        j_end = player_bbx.bottom // self.tile_size + 1
        for i in range(i_start, i_end + 1):
            for j in range(j_start, j_end + 1):
                rect = pygame.Rect(i * self.tile_size, j * self.tile_size, self.tile_size, self.tile_size)
                if str((i, j)) in self.tile_map:
                    tile = self.tile_map[str((i, j))]
                    if tile.get('solid', True) and tile['type'] in ['grass', 'stone'] and rect.colliderect(player_bbx):
                        self.tiles_intersections.append(rect)
        return self.tiles_intersections
        # for asd in self.tile_map:
            
        #     self.tx=int(asd[1:-1].split(',')[0])
        #     self.ty=int(asd[1:-1].split(',')[1])
        #     self.tile_bbx=pygame.Rect(self.tx*self.tile_size, self.ty*self.tile_size, self.tile_size, self.tile_size)
        #     if self.tile_map[asd]['type']=='grass' or self.tile_map[asd]['type']=='stone':
        #         if player_bbx.colliderect(self.tile_bbx):
        #             self.tiles_intersections.append(self.tile_bbx)
        # return self.tiles_intersections


    def get_nps(self):
        self.npsss=[]
        
        for p in self.tile_map.copy():
            asd=self.tile_map[p]
            if asd ['type']=='nps':
                c=tuple(map(int, p[1:-1].split(',')))
                c=(c[0]*self.tile_size, c[1]*self.tile_size)
                del self.tile_map[p]
                self.npsss.append(c)
        return self.npsss
    def get_zelia(self):
        self.coins=[]
        
        for p in self.tile_map.copy():
            asd=self.tile_map[p]
            if asd ['type']=='зелья':
                c=tuple(map(int, p[1:-1].split(',')))
                c=(c[0]*self.tile_size, c[1]*self.tile_size)
                del self.tile_map[p]
                self.coins.append(c)
        return self.coins