# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Rendered images",
    "author" : "Vivekanand Shanbhag",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from .render_user_input import RenderMyProperties
from .render_panel import Image_PT_Panel
from .render_operators import Image_OT_objectstocenter, Image_OT_addcamera, Image_OT_addlights, Image_OT_saveimage, Image_OT_Texture, Image_OT_Energy


classes = (RenderMyProperties, Image_PT_Panel, Image_OT_objectstocenter, Image_OT_addcamera, Image_OT_addlights, Image_OT_saveimage, Image_OT_Texture, Image_OT_Energy)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=RenderMyProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()