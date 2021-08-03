from imposm.parser import OSMParser
# simple class that handles the parsed OSM data.


class NodePrinter(object):
    buildings_num = 0
    node_lst = []
    building_list = []

    def print_node(self, coords):
        for osm_id, lon, lat in coords:
            self.node_lst.append([osm_id, lon, lat])

    def print_building(self, ways):
        for osm_id, tag_dict, ref_list in ways:
            t_entry = [osm_id]
            for val in ref_list:
                t_entry.append(val)
            self.building_list.append(t_entry)


osm_file_add = "/media/shengjie/other/OSM_2012_Sep/buildings_in_ROI_110928.osm"
counter = NodePrinter()
p = OSMParser(concurrency=4, coords_callback=counter.print_node)
p.parse(osm_file_add)
q = OSMParser(concurrency=4, ways_callback=counter.print_building)
q.parse(osm_file_add)


# print len(counter.node_lst)
f = open('/media/shengjie/other/OSM_2012_Sep/nodes.txt', 'w')
for entry in counter.node_lst:
    t_str = ""
    for x in entry:
        t_str += (str(x))
        t_str += '\t'
    t_str += '\n'
    f.write(t_str)
f.close()

f = open('buildings.txt', 'w')
for entry in counter.building_list:
    t_str = ""
    for x in entry:
        t_str += str(x)
        t_str += '\t'
    t_str += '\n'
    f.write(t_str)
f.close()