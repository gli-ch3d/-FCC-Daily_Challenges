## Plant the Crop
# 2026-01-12

def get_number_of_plants(field_size, unit, crop):
    
    uni = {
        "acre"      :   4046.86,
        "hectare"   :   10000
    }
    crops = {
        "corn"      :   1,
        "wheat"     :   0.1,
        "soybeans"  :   0.5,
        "tomatoes"  :   0.25,
        "lettuce"   :   0.2
    }

    s_o_f = field_size * uni[unit]

    crop_no = s_o_f / crops[crop]

    crop_no = int(crop_no)

    return crop_no