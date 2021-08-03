# Download Raw Data
You can download Raw openstreet data from [here](https://www.openstreetmap.org/export#map=13/49.0526/8.3570). 
I recommend to download by manually select a rectangle bounding box.

For sample data used in this instruction, you can download from [Google Drive](https://drive.google.com/drive/folders/1hiyMIDPMz_oiL8mcYQEIVSVoGHookff9?usp=sharing)

# Extract Region of interest
I extract Region of interest via computing kitti odometry bounding box in gps coodinate system. 
To extract your interested region, you can use the following command.

```
osmium extract -b 8.3295,48.9359,8.5007,49.0738 planet-120912.osm.bz2 -o kitti_range_120912.osm.pbf
osmium tags-filter kitti_range_120912.osm.pbf w/building -o buildings_in_ROI.osm
```
For the above two line of codes, I first extract a small regeion according to odometry sequence. Then I extract all labels with buildings. I think the dataset only provides labels inlcuding buildings, street, highway, juncture, traffic poles.

# Parse OSM Data with Python
I parse all nodes belonging to Buildings using this python script to txt file.

# Convert GPS Coordinates to Camera Coordinates
Kitti provide tools to map GPS data to camera [here](http://www.cvlibs.net/datasets/kitti/user_login.php).

Within the folder, you can find sample usage in 'run_demoVehiclePath.m'. In my experience, IMU Rotataion is very noisy. GPS is accurate. 