'''
Created on Nov 24, 2014

@author: rene
'''
from scipy.constants.constants import sigma, C2K
import math


def calc_horizontal_infrared_radiation_intensity(weatherdata):
    """ TODO TEST"""
    temp_drybulb = C2K(weatherdata._dry_bulb_temperature)
    temp_dew_K = C2K(weatherdata.dew_point_temperature)
    N = weatherdata.opaque_sky_cover_used_if_horizontal_ir_intensity_missing
    sky_emissivity = (0.787 + 0.764 * math.log(temp_dew_K / 273.0) *
                      (1.0 + 0.0224 * N - 0.0035 * N ** 2 + 0.00028 * N ** 3))
    hor_id = sky_emissivity * sigma * temp_drybulb ** 4
    weatherdata.horizontal_infrared_radiation_intensity = hor_id


if __name__ == '__main__':
    pass
