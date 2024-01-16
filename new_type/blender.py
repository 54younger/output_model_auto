import bpy
import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent_dir", type = str)
    parser.add_argument("--pic_name", type = str)
    argv = sys.argv[sys.argv.index("--") + 1 :]
    return parser.parse_args(argv)

if __name__ == "__main__":

    args=parse_args()
    parent_dir = args.parent_dir
    blender_file = os.path.join(parent_dir, "model.blend")
    temp_file = os.path.join(parent_dir, "temp.blend")
    temp_file1= os.path.join(parent_dir, "temp.blend1")
    pic_path = os.path.join(parent_dir, "img", "resize", args.pic_name + "_resize.jpg")
    model_file = os.path.join(parent_dir, "model.glb")

    bpy.ops.wm.open_mainfile(filepath=blender_file)
    bpy.ops.wm.save_as_mainfile(filepath=temp_file)

    obj = bpy.data.objects["pointer"]
    obj.select_set(True)
    obj.rotation_mode = 'QUATERNION'
    bpy.ops.object.select_all(action='DESELECT')

    obj = bpy.data.objects["plain"]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # 添加材质
    mat = bpy.data.materials.new(name="Material")
    obj.data.materials.append(mat)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # 添加原理化BSDF节点
    bsdf_node = None
    for node in nodes:
        if node.type == 'BSDF_PRINCIPLED':
            bsdf_node = node
            break
    bsdf_node.location = (0, 0)
    # 添加图像纹理节点
    tex_node = nodes.new(type='ShaderNodeTexImage')
    tex_node.location = (-400, 0)
    tex_node.image = bpy.data.images.load(filepath=pic_path)
    # 连接图像纹理节点和原理化BSDF节点
    links.new(tex_node.outputs[0], bsdf_node.inputs["Base Color"])
    bpy.ops.wm.save_as_mainfile(filepath=temp_file)

    # 导出模型为.glb文件
    bpy.ops.export_scene.gltf(filepath=model_file, export_animations=True, export_animation_mode='ACTIVE_ACTIONS')

    bpy.ops.wm.quit_blender()

    os.remove(temp_file)
    os.remove(temp_file1)
