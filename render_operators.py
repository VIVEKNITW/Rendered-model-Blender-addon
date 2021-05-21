import bpy
import math
rad = -1
from .render_helper_functions import deselect, duplicate_items, join_items, origin_to_gem, make_child, emptytocenter, hide, select_activate, white_background, camera_view, hidden_status, add_material, change_to_render, check_obj, unhide, delete_obj, add_empty, unhide_render, hide_in_render, delete_extra_objects, change_to_solid
from .render_lights_functions import add_light1, add_light2, add_light3, add_light4


class Image_OT_objectstocenter(bpy.types.Operator):
    """ """
    bl_label = "Objects to center"
    bl_idname = "object.objectstocenter"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        global joined, empty_name, initial_objects_list, initial_objects_list_name

        initial_objects_list = list(bpy.context.selected_objects)
        initial_objects_list_name = [item.name for item in list(bpy.context.selected_objects)]
        unhide_render(initial_objects_list)

        if len(initial_objects_list) >1:
            joined = " &".join(item for item in initial_objects_list_name)
        else:
            joined = initial_objects_list_name[0] + ' joined'

        status = check_obj(joined)
        if status:
            pass

        else:       
            duplicate_list = duplicate_items(initial_objects_list, joined)      
            join_items(duplicate_list, joined)
        
            origin_to_gem(bpy.data.objects[joined])
        
            bpy.ops.view3d.snap_cursor_to_selected()
        
            empty_name = add_empty(bpy.data.objects[joined], joined)
        
            make_child(initial_objects_list, bpy.data.objects[empty_name])
        
            emptytocenter(bpy.data.objects[empty_name])
        
            hide(bpy.data.objects[joined])
            hide_in_render(bpy.data.objects[joined])
            

        return {'FINISHED'}
    
    
    
class Image_OT_addcamera(bpy.types.Operator):
    """ """
    bl_label = "Add camera"
    bl_idname = "object.addcamera"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        global rad 
        
        dimensions = bpy.data.objects[joined].dimensions
        rad = math.sqrt((dimensions[0]/2)**2 + (dimensions[1]/2)**2 + (dimensions[2]/2)**2)
        print(rad)
        
        status = check_obj('my_cam')
        if status:
            delete_obj(bpy.data.objects['my_cam'])

        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW')
        bpy.context.object.name = 'my_cam'
        bpy.context.object.data.type = 'ORTHO'
        bpy.data.scenes['Scene'].camera = bpy.data.objects['my_cam']

        bpy.ops.transform.translate(value=(0, 0, rad*2), orient_type='LOCAL', orient_matrix_type='LOCAL', constraint_axis=(False, False, True))
        
        white_background()
        camera_view()
        
        return {'FINISHED'}
    

class Image_OT_addlights(bpy.types.Operator):
    """ """
    bl_label = "Add light"
    bl_idname = "object.addlight"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        
        status = check_obj('lights empty')
        if status:
            delete_obj(bpy.data.objects['lights empty'])
        bpy.ops.object.empty_add(type='ARROWS')
        bpy.context.object.name = 'lights empty'
        
        status = check_obj('Light 1')
        if status:
            delete_obj(bpy.data.objects['Light 1'])
        add_light1(rad)
        
        status = check_obj('Light 2')
        if status:
            delete_obj(bpy.data.objects['Light 2'])
        add_light2(rad)

        status = check_obj('Light 3')
        if status:
            delete_obj(bpy.data.objects['Light 3'])
        add_light3(rad)
        
#        add_light4(rad)
        
        hidden_status()
        change_to_render()
        
        return {'FINISHED'}
    
    
class Image_OT_saveimage(bpy.types.Operator):
    """ """
    bl_label = "Save image"
    bl_idname = "object.saveimage"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
    
        hidden_status()
        deselect()
        scene = context.scene
        mytool = scene.my_tool
        filepath = mytool.myfilepath
        filename = mytool.myfilename
        bpy.context.scene.render.filepath = filepath+filename

        scene.render.engine = 'BLENDER_EEVEE'
        scene.render.image_settings.file_format = 'PNG'
        scene.render.filepath = filepath+filename
        bpy.ops.render.render(write_still = 1)

        
        change_to_solid()

        return {'FINISHED'}


class Image_OT_Texture(bpy.types.Operator):
    """ """
    bl_label = "Apply texture"
    bl_idname = "object.applytexture"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        scene = context.scene
        mytool = scene.my_tool
        
        selected_item = bpy.context.selected_objects[0]

        if selected_item.type == "MESH":
            if mytool.mat_enum == 'Al':
                add_material(selected_item.name, 'Aluminium')
            elif mytool.mat_enum == 'B1':
                add_material(selected_item.name, 'Bone 1')
            elif mytool.mat_enum == 'B2':
                add_material(selected_item.name, 'Bone 2')
            elif mytool.mat_enum == 'B3':
                add_material(selected_item.name, 'Bone 3')
            elif mytool.mat_enum == 'B4':
                add_material(selected_item.name, 'Bone 4')
            elif mytool.mat_enum == 'Ti':
                add_material(selected_item.name, 'Titanium')
        else:
            self.report({'ERROR'}, "Select a mesh object")

        return {'FINISHED'}
    

class Image_OT_Energy(bpy.types.Operator):
    """ """
    bl_label = "Change intensity"
    bl_idname = "object.changeenergy"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        scene = context.scene
        mytool = scene.my_tool
        deselect()
        if mytool.light_enum == 'L1':
            select_activate(bpy.data.objects["Light 1"])
        elif mytool.light_enum == 'L2':
            select_activate(bpy.data.objects["Light 2"])
        elif mytool.light_enum == 'L3':
            select_activate(bpy.data.objects["Light 3"])
        

        return {'FINISHED'}


class Image_OT_Clear(bpy.types.Operator):
    """ """
    bl_label = "Clear"
    bl_idname = "object.clear"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
               
        delete_extra_objects(initial_objects_list_name)     

        return {'FINISHED'}