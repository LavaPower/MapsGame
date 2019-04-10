import pygame
import json

from Core.Block import Block
from Core.Block import BlockType


class Map:
    def __init__(self, game, directory):
        self.game = game
        self.directory = directory
        self.blocks = pygame.sprite.Group()

        with open(directory+"/map.json", 'r') as f:
            datas = json.load(f)
        self.name = datas["name"]
        self.description = datas["description"]
        self.author = datas["author"]
        self.scoretowin = int(datas["scoreToWin"])
        self.looseonfall = bool(datas["looseOnFall"])
        for i in datas["blocks"]:
            self.createblock(self.game.blocklist.get(i["id"]), [i["x"], i["y"]])

    def createblock(self, typeblock, pos):
        block = Block(typeblock, pos)
        self.blocks.add(block)

    def deleteblock(self, pos):
        for i in self.blocks.sprites():
            if i.getpos()[0] == pos[0] and i.getpos()[1] == pos[1]:
                self.blocks.remove(i)

    def getblockfrompos(self, pos):
        for i in self.blocks.sprites():
            if i.getpos()[0] == pos[0] and i.getpos()[1] == pos[1]:
                return i.blocktype
        return BlockType(self.game, "", "air", -1, False, [])

