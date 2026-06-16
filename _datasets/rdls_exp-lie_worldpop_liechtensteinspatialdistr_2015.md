---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-lie
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-lie
dataset_id: rdls_exp-lie_worldpop_liechtensteinspatialdistr_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-lie]'
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
    description: Gridded population estimates (people per pixel) at 100m and 1km resolution
      for 2015-2030
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
license: CC-BY-4.0
lineage:
  description: WorldPop population estimates were generated using Random Forest-based
    dasymetric redistribution applied to multiple source data (census, administrative
    records) to create gridded population counts at 100m and 1km resolution for Liechtenstein
    across 2015-2030. The dataset provides annual snapshots of spatial population
    distribution in GeoTIFF format with WGS84 projection.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-lie
  rel: source
loss: null
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
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/LIE/v1/100m/constrained/lie_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_ffb6316e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/LIE/v1/1km_ua/constrained/lie_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1a68d733
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/LIE/v1/100m/constrained/lie_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_7ec169f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/LIE/v1/1km_ua/constrained/lie_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_16a0c00f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/LIE/v1/100m/constrained/lie_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_de2da77f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/LIE/v1/1km_ua/constrained/lie_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cbbb18a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/LIE/v1/100m/constrained/lie_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_8716a25b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/LIE/v1/1km_ua/constrained/lie_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_ae36691b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/LIE/v1/100m/constrained/lie_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_12bf7edf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/LIE/v1/1km_ua/constrained/lie_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_7f0b2940
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/LIE/v1/100m/constrained/lie_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6b28b9ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/LIE/v1/1km_ua/constrained/lie_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_533627a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/LIE/v1/100m/constrained/lie_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_96a75ad5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/LIE/v1/1km_ua/constrained/lie_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_e3084193
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/LIE/v1/100m/constrained/lie_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_ba845a5c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/LIE/v1/1km_ua/constrained/lie_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_fbee9788
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/LIE/v1/100m/constrained/lie_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_dcdeeba5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/LIE/v1/1km_ua/constrained/lie_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_61d3da3a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/LIE/v1/100m/constrained/lie_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_dea1a6d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/LIE/v1/1km_ua/constrained/lie_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_dd9ba8f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/LIE/v1/100m/constrained/lie_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_94ce5714
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/LIE/v1/1km_ua/constrained/lie_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_7095adf0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/LIE/v1/100m/constrained/lie_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_96095f43
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/LIE/v1/1km_ua/constrained/lie_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_23886472
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/LIE/v1/100m/constrained/lie_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_16640a45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/LIE/v1/1km_ua/constrained/lie_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_7edda00a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/LIE/v1/100m/constrained/lie_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d487db2f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/LIE/v1/1km_ua/constrained/lie_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_2ea54ace
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/LIE/v1/100m/constrained/lie_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_c854371b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/LIE/v1/1km_ua/constrained/lie_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f632b1e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/LIE/v1/100m/constrained/lie_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_cdb0f129
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liechtenstein - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/LIE/v1/1km_ua/constrained/lie_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_fc80db7b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lie_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-lie_worldpop_liechtensteinspatialdistr_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - LIE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Liechtenstein - Spatial Distribution of Population (2015-2030)
version: null
vulnerability: null
---
