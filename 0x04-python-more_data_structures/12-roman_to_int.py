#!/usr/bin/python3    
def roman_to_int(roman_string):
    lt = roman_string
    roms_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = roms_num[lt[0]]
    last = roms_num[lt[-1]]
    sec_last = roms_num[lt[-2]] if len(lt) > 2 else 0
    if len(lt) == 1:
        return count
    elif len(lt) == 2:
        if roms_num[lt[-1]] > count:
            count = roms_num[lt[1]] - count
        else:
            count += roms_num[lt[1]]
        return count
    else:
        for i in lt:
            if last > sec_last:
                diff = last - sec_last
                for j in lt[1:-2]:
                    if roms_num[i] >= roms_num[j]:
                        count += roms_num[j]
                    else:
                        count = roms_num[j] - count
                count = count + diff
                break
            else:
                for j in lt[1:]:
                    if roms_num[i] >= roms_num[j]:
                        count += roms_num[j]
                    else:
                        count = roms_num[j] - count
            break
        return count
