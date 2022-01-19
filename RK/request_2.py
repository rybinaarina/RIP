from source import list_of_display, list_of_pc
import utils


id_display = list(map(lambda x: x.id, list_of_display))
prices = list(map(lambda x: (x.price, x.disp_id), filter(lambda x: x.disp_id in id_display, list_of_pc)))

correct_price_by_id = {}
for (price, disp_id) in prices:
    if disp_id not in correct_price_by_id or correct_price_by_id[disp_id] > price:
        correct_price_by_id[disp_id] = price

results = []
for display in list_of_display:
    tmp_arr = []
    tmp_arr.extend(display.values())
    if display.id in correct_price_by_id:
        tmp_arr.append(correct_price_by_id[display.id])
    else:
        tmp_arr.append(utils.max_int)
    results.append(tmp_arr)

results = [["matrix type", "diagonal", "price"]] + list(map(lambda x: utils.change_elem(x, "-----------------", 2) if x[2] == utils.max_int else x,
                                                                     sorted(results, key=lambda x: x[2])))

utils.print_pretty_table(results)