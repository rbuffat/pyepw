'''
Created on Nov 24, 2014

@author: rene
'''
from scipy.constants.constants import sigma, C2K
import math


def calc_horizontal_infrared_radiation_intensity(weatherdata):
    """ Estimates the global horizontal infrared radiation intensity based
    on drybulb, dewpoint and opaque sky cover.
    References:
    Walton, G. N. 1983. Thermal Analysis Research Program Reference Manual. NBSSIR 83-
    2655. National Bureau of Standards, p. 21.
    Clark, G. and C. Allen, "The Estimation of Atmospheric Radiation for Clear and Cloudy
    Skies," Proceedings 2nd National Passive Solar Conference (AS/ISES), 1978, pp. 675-678.
    """
    temp_drybulb_K = C2K(weatherdata._dry_bulb_temperature)
    temp_dew_K = C2K(weatherdata.dew_point_temperature)
    N = weatherdata.opaque_sky_cover
    sky_emissivity = (0.787 + 0.764 * math.log(temp_dew_K / C2K(0.0)) *
                      (1.0 + 0.0224 * N - 0.0035 * N ** 2 + 0.00028 * N ** 3))
    hor_id = sky_emissivity * sigma * temp_drybulb_K ** 4
    weatherdata.horizontal_infrared_radiation_intensity = hor_id


if __name__ == '__main__':
    pass
