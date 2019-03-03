import numpy as np
from util.noob import *

# dictionary of original columns to extract from data mapped to:
# - how to rename them
# - their dtype
columns_dic = {
    'Date': {'dtype': np.unicode_, 'name': 'date'},

    'AVG DAILY TEMP. (all hours) °F': {'dtype': np.float64, 'name': 'avg_temp'},
    'AVG DAILY TEMP. (X/N)°F': {'dtype': np.float64, 'name': 'avg_temp_2'},
    'DAILY AVG FEELS LIKE TEMP. (all hours) °F': {'dtype': np.float64, 'name': 'avg_feels_like'},

    'AVG HEAT INDEX TEMP. (all hours) °F': {'dtype': np.float64, 'name': 'avg_heat_index'},
    'AVG HEAT INDEX TEMP. (X/N)°F': {'dtype': np.float64, 'name': 'avg_heat_index_2'},
    'AVG DAILY WINDCHILL TEMP. (all hours) °F': {'dtype': np.float64, 'name': 'avg_wind_chill_temp'},
    'DAILY AVG WIND CHILL ENERGY W/M^2 (all hours)': {'dtype': np.float64, 'name': 'avg_wind_chill_energy'},

    'AVG DAILY DEW POINT TEMP. (all hours) °F': {'dtype': np.float64, 'name': 'avg_dew_point'},
    'AVG DAILY DEW POINT TEMP. (X/N) °F': {'dtype': np.float64, 'name': 'avg_dew_point_2'},

    'AVG DAILY RELATIVE HUMIDITY (all hours) %': {'dtype': np.float64, 'name': 'observed_avg_humidity'},

    'HIGHEST SUSTAIN SPEED MPH': {'dtype': np.float64, 'name': 'highest_sustained_wind_speed'},
    'AVG DAILY WIND SPEED (all hours) MPH': {'dtype': np.float64, 'name': 'observed_avg_wind_speed'},
    'PREDOMINATE WIND DIR DEG': {'dtype': np.float64, 'name': 'wind_direction'},
    'HIGHEST WIND GUST MPH': {'dtype': np.float64, 'name': 'max_wind_gust'},

    'AVG DAILY CLOUD COVER (all hours) %': {'dtype': np.float64, 'name': 'avg_cloud_cover'},
    'AVG VISIBILITY (all hours) MILES': {'dtype': np.float64, 'name': 'avg_visibility'},

    'AVG SOLAR RADIANCE W/M^2': {'dtype': np.float64, 'name': 'avg_solar_radiance_2'},
    'AVG SOLAR RADIANCE FT-CANDLES': {'dtype': np.float64, 'name': 'avg_solar_radiance'},
    'TOTAL MINUTES of SUNSHINE (calculated)': {'dtype': np.float64, 'name': 'sunshine_calculated'},
    'TOTAL MINUTES of SUNSHINE (if observed)': {'dtype': np.float64, 'name': 'sunshine_observed'},
    'TOT MIN of SUNSHINE POSSIBLE (on cloud-free day)': {'dtype': np.float64, 'name': 'sunshine_possible'},
    'PERCENT of SUNSHINE POSSIBLE (calc/total possible)': {'dtype': np.float64, 'name': 'sunshine_percent'},
    'SUNRISE (local AM)': {'dtype': np.unicode_, 'name': 'sunrise'},
    'SUNSET (local PM)': {'dtype': np.unicode_, 'name': 'sunset'},

    'SNOWFALL (DAILY): METAR': {'dtype': np.float64, 'name': 'snowfall_metar'},
    'SNOWFALL (DAILY): SUM of DAY': {'dtype': np.float64, 'name': 'snowfall_day'},
    'SNOWFALL (DAILY): RTP': {'dtype': np.float64, 'name': 'snowfall_rtp'},
    'SNOWFALL (DAILY): NWS CF6 REPORT': {'dtype': np.float64, 'name': 'snowfall_nws'},
    'SNOWFALL WBI (calculated; sum of all hours)': {'dtype': np.float64, 'name': 'snowfall_wbi'},

    'CALENDAR DAY TOTAL HOURS of PRECIP.': {'dtype': np.float64, 'name': 'precip_hours'},
    'OBSERVED DAILY WATER EQUIVALENT (inches)': {'dtype': np.float64, 'name': 'observed_water'},

    'HIGHEST PRESSURE (all hours inches)': {'dtype': np.float64, 'name': 'highest_pressure_in'},
    'LOWEST PRESSURE (all hours inches)': {'dtype': np.float64, 'name': 'lowest_pressure_in'},
    'AVG DAILY PRESSURE (all hours inches)': {'dtype': np.float64, 'name': 'avg_pressure_in'},
    'HIGHEST PRESSURE (all hours millibars if reported)': {'dtype': np.float64, 'name': 'highest_pressure_mb'},
    'LOWEST PRESSURE (all hours millibars if reported)': {'dtype': np.float64, 'name': 'lowest_pressure_mb'},
    'AVG DAILY PRESSURE (all hours millibars if reported)': {'dtype': np.float64, 'name': 'avg_daily_pressure_mb'},

    'PREDOMINATE WEATHER TEXT (all hours)': {'dtype': np.unicode_, 'name': 'predominate_weather'}
}

rename_columns_dic = map_dic( columns_dic, lambda k,v: v['name'] )
type_columns_dic = map_dic( columns_dic, lambda k,v: v['dtype'] )
