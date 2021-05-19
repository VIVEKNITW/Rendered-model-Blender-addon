import bpy
import os, sys

def deselect():
    bpy.ops.object.select_all(action='DESELECT')
    
    
def hide(object):
    bpy.context.view_layer.objects.active = object
    bpy.context.object.hide_set(True)
    
def unhide(object):
    bpy.context.view_layer.objects.active = object
    bpy.context.object.hide_set(False)
        
        
def select_activate(object):
    object.select_set(True)
    bpy.context.view_layer.objects.active = object


def origin_to_gem(item):
    deselect()
    select_activate(item)
    bpy.ops.object.origin_set(type = 'ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')    
    

def duplicate_items(my_list):
    duplicate_list = []
    for item in my_list:
        select_activate(item)
        bpy.ops.object.duplicate_move()
        duplicate_list.append(bpy.context.object)
        deselect()
    return duplicate_list


def join_items(duplicate_list):
    for item in duplicate_list:
        select_activate(item)
                        
    bpy.ops.object.join()
    bpy.context.object.name = 'joined'
    

def obj_to_org(obj):
    
    bpy.ops.object.empty_add(type='ARROWS')
    bpy.context.object.name = 'empty_parent'


def make_child(my_list, empty):
    for item in my_list:
        select_activate(item)
        
    select_activate(empty)
    
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

    
def emptytocenter(obj):
    deselect()
    select_activate(obj)
    bpy.ops.view3d.snap_cursor_to_center()
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    
    
def makeparent():
    deselect()
    bpy.data.objects['empty_parent'].select_set(True)
    bpy.data.objects['360_empty'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['360_empty']
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    

def hidden_status():
    for obj in list(bpy.data.objects):
        if (obj.visible_get()):
            pass
        else:
            obj.hide_render = True    


def camera_view():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
            break


def white_background():
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
        
    for node in tree.nodes:
        tree.nodes.remove(node)
        
    my_node1 = tree.nodes.new(type = 'CompositorNodeRLayers')
    my_node1.location = 0,0
        
    my_node2 = tree.nodes.new(type = 'CompositorNodeAlphaOver')
    my_node2.location = 300,0
        
    my_node3 = tree.nodes.new(type = 'CompositorNodeComposite')
    my_node3.location = 500,0
        
    bpy.data.scenes["Scene"].node_tree.nodes["Alpha Over"].premul = 1

    links = tree.links
    link1 = links.new(my_node1.outputs[0], my_node2.inputs[2])
    link2 = links.new(my_node2.outputs[0], my_node3.inputs[0])
        
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.view_settings.view_transform = 'Standard'


def add_image(name):
    addon_path = os.path.dirname(os.path.abspath(__file__))
    if not addon_path in sys.path:
        sys.path.append(addon_path)
    data_folder = os.path.join(addon_path, "render_texture_images\\")
    if name == 'Aluminium':
        path = os.path.join(data_folder, "Aluminium.PNG")
        return path

    elif name == 'Bone 1':
        path = os.path.join(data_folder, "Tan 1.PNG")
        return path

    elif name == 'Bone 2':
        path = os.path.join(data_folder, "Tan 2.PNG")
        return path

    elif name == 'Bone 3':
        path = os.path.join(data_folder, "Tan 3.PNG")
        return path

    elif name == 'Bone 4':
        path = os.path.join(data_folder, "Tan 4.PNG")
        return path

    elif name == 'Titanium':
        path = os.path.join(data_folder, "Titanium.PNG")
        return path


def add_material(obj, name):

    mat_name = name + " " + obj + " Material"
    obj_mat_name = name + " " + obj
    mat_name = bpy.data.materials.new(name = obj_mat_name)
    mat_name.use_nodes = True

    nodes = bpy.data.materials[obj_mat_name].node_tree.nodes
    for node in nodes:
        nodes.remove(node)
    
    bsdf_node = mat_name.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
    bsdf_node.location = (0, 0)
    img_texture = mat_name.node_tree.nodes.new('ShaderNodeTexImage')
    img_texture.location = (-350, 0)
    output_node = mat_name.node_tree.nodes.new('ShaderNodeOutputMaterial')
    output_node.location = (350, 0)

    mat_name.node_tree.links.new(img_texture.outputs[0], bsdf_node.inputs[0])
    mat_name.node_tree.links.new(bsdf_node.outputs[0], output_node.inputs[0])
    
    path = add_image(name)
    img = bpy.data.images.load(path)
    img_texture.image = img

    ob = bpy.context.view_layer.objects.active
    if ob.data.materials:
        ob.data.materials[0] = mat_name
    else:
        ob.data.materials.append(mat_name)


def change_to_render():
    my_areas = bpy.context.workspace.screens[0].areas
    my_shading = 'RENDERED'
    for area in my_areas:
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.type = my_shading