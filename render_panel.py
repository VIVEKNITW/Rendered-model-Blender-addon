import bpy

class Image(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Image rendering"
    bl_idname = "Imagerendering_initialsetup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Image rendering"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()
        row.operator("object.objectstocenter")
        row = layout.row()
        row.operator("object.addcamera")
        
        row = layout.row()
        row.prop(context.scene.camera.data, 'ortho_scale')
        row = layout.row()
        row.prop(context.scene.camera.data, 'shift_x')
        row = layout.row()
        row.prop(context.scene.camera.data, 'shift_y')
        
        row = layout.row()
        row.operator("object.addlight")
        
        row = layout.row()
        layout.prop(mytool, 'mat_enum')
        row = layout.row()
        row.operator("object.applytexture")

        row = layout.row()
        row.prop(mytool, "myfilename")
        row = layout.row()
        row.prop(mytool, "myfilepath")
        
        row = layout.row()
        row.operator("object.saveimage")