#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2021-07-02
Purpose: Point cloud down sampling. 
"""

import argparse
import os
from posixpath import basename
import sys
from utilities import load_pcd, down_sample_pcd
from osgeo import gdal
import open3d as o3d

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='PCD downsampling',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pointcloud',
                        metavar='pointcloud',
                        type=str,
                        help='Point cloud to process.')

    parser.add_argument('-o',
                        '--out_path',
                        metavar='out_path',
                        type=str,
                        default='downsample_out',
                        help='Output path for downsampled point cloud.')

    parser.add_argument('-v',
                        '--voxel_size',
                        metavar='voxel_size',
                        type=float,
                        default=0.02,
                        help='Voxel size used for downsampling. Default is 0.02.')

    return parser.parse_args()


# --------------------------------------------------
def create_out_path(out_path):

    if not os.path.isdir(out_path):
        os.makedirs(out_path)


# --------------------------------------------------
def main():
    """Open and downsample point cloud."""

    args = get_args()
    basename = os.path.splitext(os.path.basename(args.pointcloud))[0]
    original_pcd = load_pcd(args.pointcloud)
    downsampled_pcd = down_sample_pcd(pcd=original_pcd, voxel_size=args.voxel_size)
    create_out_path(args.out_path)
    o3d.io.write_point_cloud(os.path.join(args.out_path, ''.join([basename, '_downsampled', '.ply'])), downsampled_pcd)


# --------------------------------------------------
if __name__ == '__main__':
    main()
