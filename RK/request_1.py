from source import list_of_display, list_of_pc
import utils

a = [i for i in range(10)]
startLetter = "A"
correct_pc = list(filter(lambda x: x.name.startswith(startLetter), list_of_pc))
id_display = list(map(lambda x: x.disp_id, correct_pc))
correct_display = list(map(lambda x: (x.matrix_type, x.id), filter(lambda x: x.id in id_display, list_of_display)))

display_by_id = {}
for (matrix_type, disp_id) in correct_display:
    display_by_id[disp_id] = matrix_type

results = [["PC name", "price", "matrix type"]]
for pc in correct_pc:
    tmp_arr = []
    tmp_arr.extend(pc.values())
    if pc.disp_id in display_by_id:
        tmp_arr.append(display_by_id[pc.disp_id])
    else:
        tmp_arr.append("---------------------")
    results.append(tmp_arr)

utils.print_pretty_table(results)
