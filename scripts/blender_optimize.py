import bpy
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 64
scene.cycles.tile_x = 32
scene.cycles.tile_y = 32
print("✅ Blender оптимізовано для слабкого заліза")
