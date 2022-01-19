from source import list_of_display, list_of_pc, list_of_pc_display
import utils

id_display = list(map(lambda x: x.id, list_of_display))
pcs = list(filter(lambda x: x.disp_id in id_display, list_of_pc))

pcs_by_id = {}
for pc in pcs:
    if pc.disp_id in pcs_by_id:
        pcs_by_id[pc.disp_id].append(pc)
    else:
        pcs_by_id[pc.disp_id] = [pc]

for key in pcs_by_id.keys():
    pcs_by_id[key] = sorted(pcs_by_id[key], key=lambda x: x.name)

results = [["matrix type", "diagonal", "PC"]]
for processor in list_of_display:
    tmp_arr = []
    tmp_arr.extend(processor.values())
    if processor.id in pcs_by_id:
        tmp_arr.append(pcs_by_id[processor.id])
    else:
        tmp_arr.append("-------------")
    results.append(tmp_arr)

utils.print_pretty_table(results)