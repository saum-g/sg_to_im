# sg_to_im

Steps to generate images from scene graphs using our ensemble model:-

1. Clone the repo and go inside folder
```
git clone https://github.com/saum-g/sg_to_im.git
cd sg_to_im
```
2. Generating layouts from Scene graphs using sg2im model
```
bash scripts/download_models.sh
cd scripts
python run_model.py
```
3. Creating images from layouts using SPADE
**Copy/Overwrite the folders val_img, val_inst, val_label inside sg_to_im/scripts/outputs to SPADE/my_datasets**
```
cd ../SPADE
python test.py --name coco_pretrained --dataset_mode coco --dataroot my_datasets --gpu_ids -1
```
