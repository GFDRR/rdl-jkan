---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tur
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tur
dataset_id: rdls_exp-tur_worldpop_spatialdistributionpopula_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tur]'
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
    description: "Gridded population estimates (people per pixel) for T\xFCrkiye at\
      \ 100m and 1km resolution for years 2015-2030"
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
  description: Population estimates were generated using Random Forest-based dasymetric
    redistribution applied to census and administrative data sources. The methodology
    redistributes population counts from administrative units to grid cells at 100m
    resolution using spatial covariates. Annual estimates span 2015-2030 and are provided
    in both 100m and 1km resolution GeoTIFF formats in WGS84 projection.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tur
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
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2015)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/TUR/v1/100m/constrained/tur_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_efd48310
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2015)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/TUR/v1/1km_ua/constrained/tur_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_20d5804e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2016)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/TUR/v1/100m/constrained/tur_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_fd52012f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2016)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/TUR/v1/1km_ua/constrained/tur_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d8039720
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2017)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/TUR/v1/100m/constrained/tur_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_ab2714f8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2017)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/TUR/v1/1km_ua/constrained/tur_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_b2497200
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2018)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/TUR/v1/100m/constrained/tur_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6360b997
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2018)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/TUR/v1/1km_ua/constrained/tur_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_2c016825
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2019)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/TUR/v1/100m/constrained/tur_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_720f9105
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2019)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/TUR/v1/1km_ua/constrained/tur_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_05262131
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2020)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/TUR/v1/100m/constrained/tur_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_3d8473d3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2020)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/TUR/v1/1km_ua/constrained/tur_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_050f7652
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2021)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/TUR/v1/100m/constrained/tur_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_1295a28d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2021)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/TUR/v1/1km_ua/constrained/tur_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_92a2fcd4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2022)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/TUR/v1/100m/constrained/tur_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_db526598
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2022)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/TUR/v1/1km_ua/constrained/tur_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_174a950f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2023)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/TUR/v1/100m/constrained/tur_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_432b0f17
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2023)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/TUR/v1/1km_ua/constrained/tur_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_37634f1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2024)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/TUR/v1/100m/constrained/tur_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_644c77c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2024)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/TUR/v1/1km_ua/constrained/tur_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_97be6f8a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2025)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/TUR/v1/100m/constrained/tur_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_296df07f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2025)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/TUR/v1/1km_ua/constrained/tur_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_82374dda
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2026)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/TUR/v1/100m/constrained/tur_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_9df3067f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2026)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/TUR/v1/1km_ua/constrained/tur_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_6c13304d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2027)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/TUR/v1/100m/constrained/tur_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_78b09577
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2027)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/TUR/v1/1km_ua/constrained/tur_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_06255134
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2028)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/TUR/v1/100m/constrained/tur_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_7d88e97f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2028)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/TUR/v1/1km_ua/constrained/tur_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0507c62a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2029)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/TUR/v1/100m/constrained/tur_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_51b7f698
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2029)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/TUR/v1/1km_ua/constrained/tur_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_bd5e6904
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (100m resolution) for 2030)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/TUR/v1/100m/constrained/tur_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_78fdc6f2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye - Spatial Distribution of Population (2015-2030) (Individual\
    \ population counts (1km resolution) for 2030)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/TUR/v1/1km_ua/constrained/tur_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1657d675
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tur_worldpop_spatialdistributionpopula_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: "T\xFCrkiye - Spatial Distribution of Population (2015-2030)"
version: null
vulnerability: null
---
