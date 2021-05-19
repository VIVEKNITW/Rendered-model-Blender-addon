import bpy

def add_light1(myvalue):
    bpy.ops.object.light_add(type='SUN', align='WORLD', location=(0, 0, 0))
    bpy.context.object.data.use_shadow = False

        
    bpy.context.scene.transform_orientation_slots[0].type = 'VIEW'
    bpy.ops.object.constraint_add(type='TRACK_TO')

    bpy.context.object.constraints["Track To"].target = bpy.data.objects["lights empty"]
    bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
    bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'
 
    bpy.ops.transform.translate(value=(0, myvalue*2, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, True, False))
        
#    bpy.ops.transform.translate(value=(myvalue*2, 0, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(True, False, False))
    
#    bpy.ops.transform.translate(value=(0, 0, myvalue), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, False, True))
    bpy.context.object.data.energy = 1.5

    

def add_light2(myvalue):
    bpy.ops.object.light_add(type='SUN', align='WORLD', location=(0, 0, 0))
    bpy.context.object.data.use_shadow = False

        
    bpy.context.scene.transform_orientation_slots[0].type = 'VIEW'
    bpy.ops.object.constraint_add(type='TRACK_TO')
        
    bpy.context.object.constraints["Track To"].target = bpy.data.objects["lights empty"]
    bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
    bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'

#    bpy.ops.transform.translate(value=(0, myvalue*2, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, True, False))
        
    bpy.ops.transform.translate(value=(-myvalue*2, 0, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(True, False, False))
    
    bpy.ops.transform.translate(value=(0, 0, myvalue*2), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, False, True))
    bpy.context.object.data.energy = 1.5

    
    
def add_light3(myvalue):
    bpy.ops.object.light_add(type='SUN', align='WORLD', location=(0, 0, 0))
    bpy.context.object.data.use_shadow = False

        
    bpy.context.scene.transform_orientation_slots[0].type = 'VIEW'
    bpy.ops.object.constraint_add(type='TRACK_TO')
    bpy.context.object.constraints["Track To"].target = bpy.data.objects["lights empty"]
    bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
    bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'
        
#    bpy.ops.transform.translate(value=(0, -myvalue*2, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, True, False))
        
    bpy.ops.transform.translate(value=(+myvalue*2, 0, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(True, False, False))
    
    bpy.ops.transform.translate(value=(0, 0, myvalue*2), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, False, True))
    bpy.context.object.data.energy = 1.5



def add_light4(myvalue):
    bpy.ops.object.light_add(type='SUN', align='WORLD', location=(0, 0, 0))
        
    bpy.context.scene.transform_orientation_slots[0].type = 'VIEW'
    bpy.ops.object.constraint_add(type='TRACK_TO')

    bpy.context.object.constraints["Track To"].target = bpy.data.objects["lights empty"]
    bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
    bpy.context.object.constraints["Track To"].up_axis = 'UP_Y'
 
    bpy.ops.transform.translate(value=(0, -myvalue*2, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, True, False))
        
    bpy.ops.transform.translate(value=(-myvalue*2, 0, 0), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(True, False, False))
    
    bpy.ops.transform.translate(value=(0, 0, myvalue), orient_type='VIEW', orient_matrix_type='VIEW', constraint_axis=(False, False, True))
    bpy.context.object.data.energy = 1.5
    
    
    