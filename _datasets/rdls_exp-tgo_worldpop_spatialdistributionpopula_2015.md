---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tgo
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tgo
dataset_id: rdls_exp-tgo_worldpop_spatialdistributionpopula_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tgo]'
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
    description: Gridded population estimates at 100m and 1km resolution for Togo
      (2015-2030) derived from dasymetric redistribution
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
    redistribution applied to census and survey data, redistributed to 100m and 1km
    grid cells in WGS84 projection. The dataset provides annual population counts
    per pixel for Togo from 2015 to 2030, serving as baseline exposure data for disaster
    risk assessment.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-tgo
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
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/TGO/v1/100m/constrained/tgo_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_dfd14c46
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/TGO/v1/1km_ua/constrained/tgo_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1b323681
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/TGO/v1/100m/constrained/tgo_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_eec8ddc9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/TGO/v1/1km_ua/constrained/tgo_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_62f29927
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/TGO/v1/100m/constrained/tgo_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0210d176
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/TGO/v1/1km_ua/constrained/tgo_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_7b54cd9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/TGO/v1/100m/constrained/tgo_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_9de87a7e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/TGO/v1/1km_ua/constrained/tgo_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_5e7bdf1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/TGO/v1/100m/constrained/tgo_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6d4c2998
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/TGO/v1/1km_ua/constrained/tgo_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_42eb7a5d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/TGO/v1/100m/constrained/tgo_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_2a709704
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/TGO/v1/1km_ua/constrained/tgo_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_87bb8aee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/TGO/v1/100m/constrained/tgo_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_b7f23957
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/TGO/v1/1km_ua/constrained/tgo_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_7424b0ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/TGO/v1/100m/constrained/tgo_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_3ffae7ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/TGO/v1/1km_ua/constrained/tgo_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_c667353c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/TGO/v1/100m/constrained/tgo_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_4ae28303
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/TGO/v1/1km_ua/constrained/tgo_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_53b7cfd5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/TGO/v1/100m/constrained/tgo_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_4500e01c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/TGO/v1/1km_ua/constrained/tgo_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_9e3d7d97
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/TGO/v1/100m/constrained/tgo_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_318760d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/TGO/v1/1km_ua/constrained/tgo_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_01050634
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/TGO/v1/100m/constrained/tgo_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_01944bc7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/TGO/v1/1km_ua/constrained/tgo_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_037a7f64
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/TGO/v1/100m/constrained/tgo_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d7be804a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/TGO/v1/1km_ua/constrained/tgo_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1bf8f1c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/TGO/v1/100m/constrained/tgo_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0a50f018
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/TGO/v1/1km_ua/constrained/tgo_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_2e860ebe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/TGO/v1/100m/constrained/tgo_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a7658c19
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/TGO/v1/1km_ua/constrained/tgo_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_a4b60934
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/TGO/v1/100m/constrained/tgo_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_e7e834e1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Togo - Spatial Distribution of Population (2015-2030) (Individual population
    counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/TGO/v1/1km_ua/constrained/tgo_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_010f98f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tgo_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tgo_worldpop_spatialdistributionpopula_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - TGO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Togo - Spatial Distribution of Population (2015-2030)
version: null
vulnerability: null
---
