
def cam_expos (neutral, photographer):
    aperture_list = ['f/1.4', 'f/2', 'f/2.8', 'f/4', 'f/5.6', 'f/8', 'f/11', 'f/16', 'f/22']
    shutter_list = ['1/4', '1/8', '1/15', '1/30', '1/60', '1/125', '1/250', '1/500', '1/1000', '1/2000', '1/4000']
    iso_list = ['100', '200', '400', '800', '1600', '3200']
    
    diff_aperture = aperture_list.index(neutral[0]) - aperture_list.index(photographer[0])
    diff_shutter = shutter_list.index(neutral[1]) - shutter_list.index(photographer[1])
    diff_iso = iso_list.index(photographer[2]) - iso_list.index(neutral[2])
    
    total_diff = diff_aperture + diff_shutter + diff_iso
    
    return (diff_aperture, diff_shutter, diff_iso, total_diff)


