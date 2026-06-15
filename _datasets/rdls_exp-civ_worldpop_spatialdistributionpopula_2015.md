---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-civ
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-civ
dataset_id: rdls_exp-civ_worldpop_spatialdistributionpopula_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-civ]'
details: Disclaimer:The dataset currently represents an alpha version (R2025A) product
  and may change over the coming year as improvements are made. Data for earlier dates
  is available directly from WorldPop Bondarenko M., Priyatikanto R., Tejedor-Garavito
  N., Zhang W., McKeen T., Cunningham A., Woods T., Hilton J., Cihan D., Nosatiuk
  B., Brinkhoff T., Tatem A., Sorichetta A.. 2025 Constrained estimates of 2015-2030
  total number of people per grid square at a resolution of 3 arc (approximately 100m
  at the equator) R2025A version v1. Global Demographic Data Project - Funded by The
  Bill and Melinda Gates Foundation (INV-045237). WorldPop - School of Geography and
  Environmental Science, University of Southampton. DOI:10.5258/SOTON/WP00839
exposure:
- asset_type:
    description: Gridded population estimates at 100m and 1km resolution for 2015-2030
      using dasymetric redistribution
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "WorldPop Global 2015-2030 Release (R2025A) provides spatially disaggregated\
    \ population estimates for C\xF4te d'Ivoire derived from multiple census and administrative\
    \ sources using Random Forest-based dasymetric redistribution. Data are provided\
    \ at 100m and 1km grid resolutions in GeoTIFF format with WGS84 projection, covering\
    \ annual estimates from 2015 to 2030."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-civ
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.worldpop.org/repo/prj/Global_2015_2030/R2025A/doc/Global2_Release_Statement_R2025A_v1.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2015)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/CIV/v1/100m/constrained/civ_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_877ebe3c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2015)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/CIV/v1/1km_ua/constrained/civ_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_08648273
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2016)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/CIV/v1/100m/constrained/civ_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6ddefa29
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2016)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/CIV/v1/1km_ua/constrained/civ_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f97e5920
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2017)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/CIV/v1/100m/constrained/civ_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_50cf5ec0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2017)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/CIV/v1/1km_ua/constrained/civ_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_75915dbf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2018)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/CIV/v1/100m/constrained/civ_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a18eb454
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2018)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/CIV/v1/1km_ua/constrained/civ_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_52b0ad38
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2019)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/CIV/v1/100m/constrained/civ_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_4fb66cd5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2019)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/CIV/v1/1km_ua/constrained/civ_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_54696777
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2020)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/CIV/v1/100m/constrained/civ_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_5487c1e9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2020)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/CIV/v1/1km_ua/constrained/civ_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cd12c247
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2021)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/CIV/v1/100m/constrained/civ_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_4ae4e279
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2021)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/CIV/v1/1km_ua/constrained/civ_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_84295b22
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2022)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/CIV/v1/100m/constrained/civ_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_fb29561b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2022)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/CIV/v1/1km_ua/constrained/civ_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_7dddfe7f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2023)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/CIV/v1/100m/constrained/civ_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a47918bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2023)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/CIV/v1/1km_ua/constrained/civ_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0191ac7d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2024)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/CIV/v1/100m/constrained/civ_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_7e9e5388
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2024)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/CIV/v1/1km_ua/constrained/civ_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_c695f9fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2025)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/CIV/v1/100m/constrained/civ_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_f11c2031
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2025)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/CIV/v1/1km_ua/constrained/civ_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_5cdf971c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2026)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/CIV/v1/100m/constrained/civ_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d8b5d1b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2026)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/CIV/v1/1km_ua/constrained/civ_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_2c73da61
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2027)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/CIV/v1/100m/constrained/civ_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_3c45c382
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2027)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/CIV/v1/1km_ua/constrained/civ_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_fa75accb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2028)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/CIV/v1/100m/constrained/civ_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_65129979
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2028)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/CIV/v1/1km_ua/constrained/civ_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f90233df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2029)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/CIV/v1/100m/constrained/civ_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_5f6cd090
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2029)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/CIV/v1/1km_ua/constrained/civ_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f505d11f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2030)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/CIV/v1/100m/constrained/civ_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_b294d9e0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2030)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/CIV/v1/1km_ua/constrained/civ_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1310d17c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-civ_worldpop_spatialdistributionpopula_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - CIV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: "C\xF4te d'Ivoire - Spatial Distribution of Population (2015-2030)"
version: null
vulnerability: null
---
