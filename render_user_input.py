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
    intensity_enum : bpy.props.EnumProperty(name = "Light intensity",
                items = [('I1', '0', ''),
                        ('I2', '0.25', ''),
                        ('I3', '0.5', ''),
                        ('I4', '0.75', ''),
                        ('I5', '1.0', ''),
                        ('I6', '1.25', ''),
                        ('I7', '1.5', ''),
                        ('I8', '1.75', ''),
                        ('I9', '2.0', ''),
                        ('I10', '2.25', ''),
                        ('I11', '2.5', ''),
                        ('I12', '2.75', ''),
                        ('I13', '3.0', ''),
                        ('I14', '3.25', ''),
                        ('I15', '3.5', ''),
                        ('I16', '3.75', ''),
                        ('I17', '4.0', ''),
                        ('I18', '4.25', ''),
                        ('I19', '4.5', ''),
                        ('I20', '4.75', ''),
                        ('I21', '5.0', ''),
                        ('I22', '5.25', ''),
                        ('I23', '5.5', ''),
                        ('I24', '5.75', ''),
                        ('I25', '6.0', '')
    ])
    
    light_enum : bpy.props.EnumProperty(name = "Light",
                items = [('L1', 'Light 1', ''),
                        ('L2', 'Light 2', ''),
                        ('L3', 'Light 3', '')
    ])