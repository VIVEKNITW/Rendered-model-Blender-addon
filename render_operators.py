import bpy
import math
rad = -1
from .render_helper_functions import deselect, duplicate_items, join_items, origin_to_gem, make_child, emptytocenter, obj_to_org, hide, white_background, camera_view, hidden_status, add_material, change_to_render
from .render_lights_functions import add_light1, add_light2, add_light3, add_light4

class Image_objectstocenter(bpy.types.Operator):
    """ """
    bl_label = "Objects to center"
    bl_idname = "object.objectstocenter"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):

        my_list = bpy.context.selected_objects
        
        deselect()
        
        duplicate_list = duplicate_items(my_list)
          
        deselect()
        
        join_items(duplicate_list)
        
        origin_to_gem(bpy.data.objects["joined"])
        
        bpy.ops.view3d.snap_cursor_to_selected()
        
        obj_to_org(bpy.data.objects["joined"])
        
        make_child(my_list, bpy.data.objects['empty_parent'])
        
        emptytocenter(bpy.data.objects['empty_parent'])
        
        hide(bpy.data.objects['joined'])
        
        change_to_render()

        return {'FINISHED'}
    
    
    
class Image_addcamera(bpy.types.Operator):
    """ """
    bl_label = "Add camera"
    bl_idname = "object.addcamera"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        global rad 
        
        dimensions = bpy.data.objects['joined'].dimensions
        rad = math.sqrt((dimensions[0]/2)**2 + (dimensions[1]/2)**2 + (dimensions[2]/2)**2)
        print(rad)
        
        
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW')
        bpy.context.object.name = 'my_cam'
        bpy.context.object.data.type = 'ORTHO'
        bpy.data.scenes['Scene'].camera = bpy.data.objects['my_cam']


        bpy.ops.transform.translate(value=(0, 0, rad*2), orient_type='LOCAL', orient_matrix_type='LOCAL', constraint_axis=(False, False, True))
        
        white_background()
        camera_view()
        
        return {'FINISHED'}
    

class Image_addlights(bpy.types.Operator):
    """ """
    bl_label = "Add light"
    bl_idname = "object.addlight"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        
        bpy.ops.object.empty_add(type='ARROWS')
        bpy.context.object.name = 'lights empty'
        
        add_light1(rad)
        
        add_light2(rad)
        
        add_light3(rad)
        
#        add_light4(rad)
        
        hidden_status()

        return {'FINISHED'}
    
    
class Image_saveimage(bpy.types.Operator):
    """ """
    bl_label = "Save image"
    bl_idname = "object.saveimage"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
    
        hidden_status()
        bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
        bpy.context.scene.render.image_settings.file_format = 'PNG'

        
        scene = context.scene
        mytool = scene.my_tool
        filepath = mytool.myfilepath
        filename = mytool.myfilename
        bpy.context.scene.render.filepath = filepath+filename
        
#        del_objects = ['joined', 'my_path', 'my_cam', "360_empty", 'empty_parent']
#        for obj in del_objects:
#            unhide(bpy.data.objects[obj])
#            select_activate(bpy.data.objects[obj])
#            bpy.ops.object.delete()
        
        return {'FINISHED'}


class Image_Texture(bpy.types.Operator):
    """ """
    bl_label = "Apply texture"
    bl_idname = "object.applytexture"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        scene = context.scene
        mytool = scene.my_tool
        
        selected_item = bpy.context.selected_objects[0].name
        if mytool.mat_enum == 'Al':
            add_material(selected_item, 'Aluminium')
        elif mytool.mat_enum == 'B1':
            add_material(selected_item, 'Bone 1')
        elif mytool.mat_enum == 'B2':
            add_material(selected_item, 'Bone 2')
        elif mytool.mat_enum == 'B3':
            add_material(selected_item, 'Bone 3')
        elif mytool.mat_enum == 'B4':
            add_material(selected_item, 'Bone 4')
        elif mytool.mat_enum == 'Ti':
            add_material(selected_item, 'Titanium')


        return {'FINISHED'}
    
