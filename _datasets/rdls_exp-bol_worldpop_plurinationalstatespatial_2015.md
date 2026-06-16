---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-bol
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-bol
dataset_id: rdls_exp-bol_worldpop_plurinationalstatespatial_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-bol]'
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
    description: Gridded population estimates at 100m and 1km resolution for Bolivia,
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
  description: Population estimates derived from multiple census and administrative
    sources processed through Random Forest-based dasymetric redistribution to generate
    gridded population counts at 100m and 1km resolution for Bolivia across 2015-2030.
    The dataset provides baseline spatial population distribution for disaster risk
    assessment and humanitarian planning.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-bol
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
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/BOL/v1/100m/constrained/bol_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_1dee90f8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/BOL/v1/1km_ua/constrained/bol_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d4bbac74
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/BOL/v1/100m/constrained/bol_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_b78cf4f2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/BOL/v1/1km_ua/constrained/bol_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d45c3294
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/BOL/v1/100m/constrained/bol_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_bd49ad15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/BOL/v1/1km_ua/constrained/bol_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_66e104ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/BOL/v1/100m/constrained/bol_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_86c56a37
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/BOL/v1/1km_ua/constrained/bol_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d7d4e4b1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/BOL/v1/100m/constrained/bol_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0deecf65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/BOL/v1/1km_ua/constrained/bol_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_2ecab4b0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/BOL/v1/100m/constrained/bol_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0ccfa8fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/BOL/v1/1km_ua/constrained/bol_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f594793d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/BOL/v1/100m/constrained/bol_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_f96165fd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/BOL/v1/1km_ua/constrained/bol_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_045da24b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/BOL/v1/100m/constrained/bol_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_ef3c8a9f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/BOL/v1/1km_ua/constrained/bol_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_751e08e1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/BOL/v1/100m/constrained/bol_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_bc46186b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/BOL/v1/1km_ua/constrained/bol_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f95a2161
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/BOL/v1/100m/constrained/bol_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_b8147e55
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/BOL/v1/1km_ua/constrained/bol_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_29880a44
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/BOL/v1/100m/constrained/bol_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_81f8af29
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/BOL/v1/1km_ua/constrained/bol_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1ba34dfa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/BOL/v1/100m/constrained/bol_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_2c1cde42
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/BOL/v1/1km_ua/constrained/bol_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_8b7fa4d9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/BOL/v1/100m/constrained/bol_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_8fb04492
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/BOL/v1/1km_ua/constrained/bol_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f77fee7a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/BOL/v1/100m/constrained/bol_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d385425d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/BOL/v1/1km_ua/constrained/bol_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_594932c2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/BOL/v1/100m/constrained/bol_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_bd870988
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/BOL/v1/1km_ua/constrained/bol_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_a60525d3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/BOL/v1/100m/constrained/bol_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_1d13cd6b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Spatial Distribution of Population
    (2015-2030) (Individual population counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/BOL/v1/1km_ua/constrained/bol_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cae233fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bol_worldpop_plurinationalstatespatial_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Bolivia (Plurinational State of) - Spatial Distribution of Population (2015-2030)
version: null
vulnerability: null
---
