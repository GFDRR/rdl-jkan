---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-ala
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-ala
dataset_id: rdls_exp-ala_worldpop_alandislandsspatialdistri_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-ala]'
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
    description: "Gridded population estimates (people per pixel) for \xC5land Islands\
      \ at 100m and 1km resolution for years 2015-2030"
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
  description: "Population estimates were generated using Random Forest-based dasymetric\
    \ redistribution applied to census and administrative data sources, producing\
    \ gridded population counts at 100m and 1km spatial resolution for the \xC5land\
    \ Islands across the 2015-2030 period. The dataset represents baseline population\
    \ distribution without disaster-specific context."
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-ala
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
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2015)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/ALA/v1/100m/constrained/ala_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_9a166cb6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2015)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/ALA/v1/1km_ua/constrained/ala_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_879bd43d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2016)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/ALA/v1/100m/constrained/ala_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_2492eb26
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2016)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/ALA/v1/1km_ua/constrained/ala_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_da7306fe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2017)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/ALA/v1/100m/constrained/ala_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_fd5ad74b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2017)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/ALA/v1/1km_ua/constrained/ala_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_e35a7489
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2018)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/ALA/v1/100m/constrained/ala_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_26336093
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2018)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/ALA/v1/1km_ua/constrained/ala_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_3f245100
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2019)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/ALA/v1/100m/constrained/ala_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_1b0eda14
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2019)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/ALA/v1/1km_ua/constrained/ala_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_9861e703
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2020)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/ALA/v1/100m/constrained/ala_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_e6f419bf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2020)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/ALA/v1/1km_ua/constrained/ala_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cd5659ed
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2021)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/ALA/v1/100m/constrained/ala_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_935c5d8f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2021)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/ALA/v1/1km_ua/constrained/ala_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_64bd1556
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2022)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/ALA/v1/100m/constrained/ala_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_e257b285
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2022)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/ALA/v1/1km_ua/constrained/ala_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_531f94c8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2023)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/ALA/v1/100m/constrained/ala_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_beb02525
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2023)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/ALA/v1/1km_ua/constrained/ala_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1df0a022
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2024)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/ALA/v1/100m/constrained/ala_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a9193fd9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2024)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/ALA/v1/1km_ua/constrained/ala_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f02cc028
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2025)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/ALA/v1/100m/constrained/ala_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_e0425a08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2025)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/ALA/v1/1km_ua/constrained/ala_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_5561f01e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2026)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/ALA/v1/100m/constrained/ala_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6942b06d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2026)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/ALA/v1/1km_ua/constrained/ala_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_fe83dd71
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2027)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/ALA/v1/100m/constrained/ala_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_bc6d5232
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2027)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/ALA/v1/1km_ua/constrained/ala_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_922152f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2028)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/ALA/v1/100m/constrained/ala_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_b646551b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2028)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/ALA/v1/1km_ua/constrained/ala_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_37825a70
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2029)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/ALA/v1/100m/constrained/ala_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_e03f2f48
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2029)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/ALA/v1/1km_ua/constrained/ala_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_42337890
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (100m resolution) for 2030)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/ALA/v1/100m/constrained/ala_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_bcbe5d16
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Spatial Distribution of Population (2015-2030)\
    \ (Individual population counts (1km resolution) for 2030)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/ALA/v1/1km_ua/constrained/ala_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cfd01dd9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ala_worldpop_alandislandsspatialdistri_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - ALA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: "\xC5land Islands - Spatial Distribution of Population (2015-2030)"
version: null
vulnerability: null
---
