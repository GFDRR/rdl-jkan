---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-twn
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-twn
dataset_id: rdls_exp-twn_worldpop_provincechinaspatialdistr_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-twn]'
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
    description: Gridded population estimates at 100m and 1km resolution for Taiwan,
      2015-2030
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
  description: Gridded population estimates derived from Random Forest-based dasymetric
    redistribution of census data and ancillary geospatial variables. Data provided
    at 100m and 1km spatial resolutions in GeoTIFF format for annual snapshots from
    2015-2030, representing baseline population distribution for disaster risk assessment.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-twn
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
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/TWN/v1/100m/constrained/twn_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a3f8869f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/TWN/v1/1km_ua/constrained/twn_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_b77ec1a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/TWN/v1/100m/constrained/twn_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_7b407cbf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/TWN/v1/1km_ua/constrained/twn_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_b1141104
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/TWN/v1/100m/constrained/twn_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_fcf9519d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/TWN/v1/1km_ua/constrained/twn_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_e4844be2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/TWN/v1/100m/constrained/twn_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_4a4cba72
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/TWN/v1/1km_ua/constrained/twn_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d1e204ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/TWN/v1/100m/constrained/twn_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_cb6b7163
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/TWN/v1/1km_ua/constrained/twn_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_78db86c2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/TWN/v1/100m/constrained/twn_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d7cfb8fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/TWN/v1/1km_ua/constrained/twn_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_c2e605e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/TWN/v1/100m/constrained/twn_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_8317f75f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/TWN/v1/1km_ua/constrained/twn_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1b5441f7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/TWN/v1/100m/constrained/twn_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_74de3ad5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/TWN/v1/1km_ua/constrained/twn_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_7f39f809
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/TWN/v1/100m/constrained/twn_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a6a5181f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/TWN/v1/1km_ua/constrained/twn_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_e5d77fd2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/TWN/v1/100m/constrained/twn_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d166da9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/TWN/v1/1km_ua/constrained/twn_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_459a4a0c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/TWN/v1/100m/constrained/twn_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_949bb9bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/TWN/v1/1km_ua/constrained/twn_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_e08cb3f6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/TWN/v1/100m/constrained/twn_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0969e548
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/TWN/v1/1km_ua/constrained/twn_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_23db2c5f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/TWN/v1/100m/constrained/twn_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_5581b25e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/TWN/v1/1km_ua/constrained/twn_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_4fe81877
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/TWN/v1/100m/constrained/twn_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0f24b87f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/TWN/v1/1km_ua/constrained/twn_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_b13de452
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/TWN/v1/100m/constrained/twn_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_745aa47b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/TWN/v1/1km_ua/constrained/twn_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0249b8b7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/TWN/v1/100m/constrained/twn_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_1798afad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/TWN/v1/1km_ua/constrained/twn_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d168104a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-twn_worldpop_provincechinaspatialdistr_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - TWN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Taiwan (Province of China) - Spatial Distribution of Population (2015-2030)
version: null
vulnerability: null
---
