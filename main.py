import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default='coco_pretrained')
parser.add_argument('--dataset_mode', type=str, default='coco')
parser.add_argument('--dataroot', type=str, default='my_datasets')
parser.add_argument('--scene_graphs_json', type=str, default='../scene_graphs/figure_5_coco.json')
args = parser.parse_args()

# Run this main.py from the parent sg_to_im directory
os.chdir('scripts/')

for dirs in ['val_img', 'val_inst', 'val_label']:
    os.system(f'rm -rf outputs/{dirs}')
    os.mkdir(f'outputs/{dirs}')

# Generate the corresponding layouts from the given scene graphs json
command = f'python run_model.py --scene_graphs_json {args.scene_graphs_json}'
os.system(command)

for dirs in ['val_img', 'val_inst', 'val_label']:
    command = f'cp -r outputs/{dirs}/ ../SPADE/{args.dataroot}'
    os.system(command)

os.chdir('../SPADE/')

command = f'python test.py --name {args.name} --dataset_mode {args.dataset_mode} --dataroot {args.dataroot} --gpu_ids -1'
os.system(command)


