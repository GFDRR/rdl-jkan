---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-nzl
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-nzl
dataset_id: rdls_exp-nzl_worldpop_spatialdistributionpopula_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-nzl]'
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
    description: Gridded population estimates for New Zealand at 100m and 1km resolution
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
license: CC-BY-4.0
lineage:
  description: Population estimates derived from multiple census and administrative
    sources processed through Random Forest-based dasymetric redistribution to generate
    gridded population counts at 100m and 1km resolution for New Zealand across 2015-2030,
    providing baseline exposure data for disaster risk assessment.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-nzl
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
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/NZL/v1/100m/constrained/nzl_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_e47abd21
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/NZL/v1/1km_ua/constrained/nzl_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_c9490eb8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/NZL/v1/100m/constrained/nzl_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_17d21252
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/NZL/v1/1km_ua/constrained/nzl_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_9d5d6b54
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/NZL/v1/100m/constrained/nzl_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_9e5f65df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/NZL/v1/1km_ua/constrained/nzl_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_6c4daae9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/NZL/v1/100m/constrained/nzl_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_62221845
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/NZL/v1/1km_ua/constrained/nzl_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_bda4ab1e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/NZL/v1/100m/constrained/nzl_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_edaf211a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/NZL/v1/1km_ua/constrained/nzl_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_2b822f76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/NZL/v1/100m/constrained/nzl_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d9106a2c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/NZL/v1/1km_ua/constrained/nzl_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_a4ea7b1f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/NZL/v1/100m/constrained/nzl_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0f1bd4bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/NZL/v1/1km_ua/constrained/nzl_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_24ea7b16
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/NZL/v1/100m/constrained/nzl_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_100545d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/NZL/v1/1km_ua/constrained/nzl_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_682dc171
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/NZL/v1/100m/constrained/nzl_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_ab26feeb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/NZL/v1/1km_ua/constrained/nzl_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_5d54ae1e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/NZL/v1/100m/constrained/nzl_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_8b8a4d5e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/NZL/v1/1km_ua/constrained/nzl_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cb29b306
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/NZL/v1/100m/constrained/nzl_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_de11db62
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/NZL/v1/1km_ua/constrained/nzl_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_07d9216a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/NZL/v1/100m/constrained/nzl_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_123016fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/NZL/v1/1km_ua/constrained/nzl_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_a441b2c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/NZL/v1/100m/constrained/nzl_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_5d0650f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/NZL/v1/1km_ua/constrained/nzl_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_433e5d25
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/NZL/v1/100m/constrained/nzl_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a0aa62b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/NZL/v1/1km_ua/constrained/nzl_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_b640f7d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/NZL/v1/100m/constrained/nzl_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_909db774
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/NZL/v1/1km_ua/constrained/nzl_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f2c43558
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/NZL/v1/100m/constrained/nzl_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_835ad3b7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New Zealand - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/NZL/v1/1km_ua/constrained/nzl_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f93d2db1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nzl_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nzl_worldpop_spatialdistributionpopula_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - NZL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: New Zealand - Spatial Distribution of Population (2015-2030)
version: null
vulnerability: null
---
