from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

import time
import mcpi.block as Block


time.sleep(3)

dx = 3
dy = 3
dz = 3

distance = 10

playerPos = mc.player.getPos()

blockId = Block.GLOWSTONE_BLOCK.id

x = playerPos.x
y = playerPos.y 
z = playerPos.z 
mc.setBlock(playerPos.x+2,playerPos.y,playerPos.z,7)
