import bpy

class RenderMyProperties(bpy.types.PropertyGroup):
    myfilepath : bpy.props.StringProperty(name= "Filepath", maxlen = 1000, subtype='DIR_PATH')
    myfilename : bpy.props.StringProperty(name= "Filename", maxlen = 1000, subtype='FILE_NAME')
    mat_enum : bpy.props.EnumProperty(name = "Material texture",
                items = [('Al', 'Aluminium', ''),
                        ('B1', 'Bone 1', ''),
                        ('B2', 'Bone 2', ''),
                        ('B3', 'Bone 3', ''),
                        ('B4', 'Bone 4', ''),
                        ('Ti', 'Titanium', '')
    ])