# Generating Photorealistic Images from Scene Graphs

This code has been developed as part of a course project for "CS726: Advanced Machine Learning" under the supervision of Prof Sunita Sarawagi. The aim of our project is to develop a model for creation of photorealistic images from scene graph descriptions of images. We utilise the [sg2im](https://github.com/google/sg2im) architecture to generate semantically rich intermediate image layouts from scene graphs. We then exploit the power of [SPADE](https://github.com/NVlabs/SPADE) to generate photorealistic images.

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

```
cp -r scripts/outputs ../SPADE/my_datasets/
cd ../SPADE
python test.py --name coco_pretrained --dataset_mode coco --dataroot my_datasets --gpu_ids -1
```

Outputs are generated under sg_to_im/SPADE/results/coco_pretrained/test_latest
You could either open the index.html file or go inside images/syntesized_images under the aforementioned directory
