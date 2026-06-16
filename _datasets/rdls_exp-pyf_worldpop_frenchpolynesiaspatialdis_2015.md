---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Global 2015-2030 R2025A
    url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-pyf
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-pyf
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-pyf
dataset_id: rdls_exp-pyf_worldpop_frenchpolynesiaspatialdis_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-pyf]'
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
    description: "Gridded population estimates for French Polynesia at 100m and 1km\
      \ resolution for years 2015\u20132030, derived using Random Forest-based dasymetric\
      \ redistribution"
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
  description: "Census and administrative population data for French Polynesia were\
    \ disaggregated to a 3 arc-second (~100m) grid using a Random Forest-based dasymetric\
    \ mapping approach, incorporating ancillary geospatial covariates. Annual estimates\
    \ from 2015 to 2030 were produced as part of the WorldPop Global 2015\u20132030\
    \ R2025A release, providing spatially explicit population counts per pixel for\
    \ use in exposure assessment and disaster risk analysis."
  sources:
  - id: source_1
    license: null
    name: "WorldPop Global 2015\u20132030 R2025A"
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-pyf
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
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/PYF/v1/100m/constrained/pyf_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_9d0da7aa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/PYF/v1/1km_ua/constrained/pyf_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_bb8ab9af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/PYF/v1/100m/constrained/pyf_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_139718de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/PYF/v1/1km_ua/constrained/pyf_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_750941ef
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/PYF/v1/100m/constrained/pyf_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_82c1a2e9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/PYF/v1/1km_ua/constrained/pyf_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1a7e349e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/PYF/v1/100m/constrained/pyf_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6b9d3be3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/PYF/v1/1km_ua/constrained/pyf_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_a2c83511
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/PYF/v1/100m/constrained/pyf_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_e47bb4b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/PYF/v1/1km_ua/constrained/pyf_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_899c0c6f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/PYF/v1/100m/constrained/pyf_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_853fa91f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/PYF/v1/1km_ua/constrained/pyf_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_6a2ef6b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/PYF/v1/100m/constrained/pyf_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d48e391f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/PYF/v1/1km_ua/constrained/pyf_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d00e97d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/PYF/v1/100m/constrained/pyf_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_18273f41
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/PYF/v1/1km_ua/constrained/pyf_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_56005582
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/PYF/v1/100m/constrained/pyf_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_fb6ed876
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/PYF/v1/1km_ua/constrained/pyf_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0ddc2bd9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/PYF/v1/100m/constrained/pyf_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a91605f3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/PYF/v1/1km_ua/constrained/pyf_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_35c426ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/PYF/v1/100m/constrained/pyf_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_c2de071a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/PYF/v1/1km_ua/constrained/pyf_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_357e6de7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/PYF/v1/100m/constrained/pyf_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_61d87e50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/PYF/v1/1km_ua/constrained/pyf_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cbfdbbfb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/PYF/v1/100m/constrained/pyf_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_feb3b898
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/PYF/v1/1km_ua/constrained/pyf_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_93399913
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/PYF/v1/100m/constrained/pyf_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_cde1cfef
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/PYF/v1/1km_ua/constrained/pyf_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_937f6d76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/PYF/v1/100m/constrained/pyf_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_ea1a37ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/PYF/v1/1km_ua/constrained/pyf_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_b67e78fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/PYF/v1/100m/constrained/pyf_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6aefa226
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Polynesia - Spatial Distribution of Population (2015-2030) (Individual
    population counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/PYF/v1/1km_ua/constrained/pyf_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_05921f5c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pyf_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-pyf_worldpop_frenchpolynesiaspatialdis_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - PYF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: French Polynesia - Spatial Distribution of Population (2015-2030)
version: null
vulnerability: null
---
