import time
import plyfile
import glob
import logging
import numpy as np
import os
import random
import torch
import torch.utils.data
import trimesh
import skimage.measure
import argparse
import mrcfile
from tqdm import tqdm

def write_obj(verts, faces, obj_path):
    """_summary_

    Args:
        verts (_type_): _description_
        faces (_type_): _description_
        obj_path (_type_): _description_
    """
    assert obj_path[-4:] == '.obj'
    
    with open(obj_path, 'w') as fp:
        for v in verts:
            fp.write('v %f %f %f\n' % (v[0], v[1], v[2]))
        for f in faces +1:
            fp.write('f %d %d %d\n' % (f[0], f[1], f[2]))
        
def convert_ply_to_obj(ply_f, obj):
    '''
    Convert given ply data
    '''
    from plyfile import PlyData
    ply = PlyData.read(ply_f)
    
    pc = ply['vertex'].data
    faces = ply['face'].data
    
    try:
        pc_array = np.array([[x,y,z] for x,y,z,_,_,_ in pc])
    except:
        pc_array = np.array([[x,y,z] for x, y, z in pc])
    
    face_array = np.array([face[0] for face in faces], dtype=np.int)
    write_obj(pc_array, face_array, obj)
        