#!/bin/bash
osmium extract -b 8.3295,48.9359,8.5007,49.0738 /media/shengjie/other/OSM_2012_Sep/planet-120912.osm.bz2 -o /media/shengjie/other/OSM_2012_Sep/kitti_range_120912.osm.pbf
osmium extract -b 8.3295,48.9359,8.5007,49.0738 /media/shengjie/other/OSM_2012_Sep/planet-110928.osm.bz2 -o /media/shengjie/other/OSM_2012_Sep/kitti_range_110928.osm.pbf
osmium tags-filter /media/shengjie/other/OSM_2012_Sep/kitti_range_120912.osm.pbf w/building -o buildings_in_ROI.osm
