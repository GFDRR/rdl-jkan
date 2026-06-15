---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mac
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mac
dataset_id: rdls_exp-mac_worldpop_chinamacaospecialadminist_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mac]'
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
    description: Gridded population estimates for Macao SAR at 100m and 1km resolution
      derived from dasymetric redistribution
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
  description: Population estimates for 2015-2030 were generated using Random Forest-based
    dasymetric redistribution applied to multiple source datasets. The resulting gridded
    population counts were distributed at 100m and 1km spatial resolutions in GeoTIFF
    format with WGS84 projection, providing baseline exposure data for disaster risk
    assessment.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mac
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
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/MAC/v1/100m/constrained/mac_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a0836905
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/MAC/v1/1km_ua/constrained/mac_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_136ed1d5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/MAC/v1/100m/constrained/mac_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_2b8d0822
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/MAC/v1/1km_ua/constrained/mac_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_b1743d94
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/MAC/v1/100m/constrained/mac_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d72203b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/MAC/v1/1km_ua/constrained/mac_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_fadac18a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/MAC/v1/100m/constrained/mac_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d17142e5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/MAC/v1/1km_ua/constrained/mac_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0da6e659
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/MAC/v1/100m/constrained/mac_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_6717e6cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/MAC/v1/1km_ua/constrained/mac_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_bcb02f4c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/MAC/v1/100m/constrained/mac_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_35cbbb76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/MAC/v1/1km_ua/constrained/mac_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_84d97c06
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/MAC/v1/100m/constrained/mac_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d66550c4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/MAC/v1/1km_ua/constrained/mac_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_e38c21ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/MAC/v1/100m/constrained/mac_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_bb537e9f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/MAC/v1/1km_ua/constrained/mac_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_035792ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/MAC/v1/100m/constrained/mac_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_33e62fd5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/MAC/v1/1km_ua/constrained/mac_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0adbbbda
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/MAC/v1/100m/constrained/mac_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_89146c08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/MAC/v1/1km_ua/constrained/mac_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f6ce4ed2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/MAC/v1/100m/constrained/mac_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_b0d3cf90
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/MAC/v1/1km_ua/constrained/mac_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_8f027cfa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/MAC/v1/100m/constrained/mac_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_7301637c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/MAC/v1/1km_ua/constrained/mac_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_754457fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/MAC/v1/100m/constrained/mac_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_66bf9634
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/MAC/v1/1km_ua/constrained/mac_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_482345ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/MAC/v1/100m/constrained/mac_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_c5a1a622
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/MAC/v1/1km_ua/constrained/mac_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d4e77e39
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/MAC/v1/100m/constrained/mac_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_47ecf646
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/MAC/v1/1km_ua/constrained/mac_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f6d06d80
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/MAC/v1/100m/constrained/mac_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_ec6ab5d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: China, Macao Special Administrative Region - Spatial Distribution of
    Population (2015-2030) (Individual population counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/MAC/v1/1km_ua/constrained/mac_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_5b4ce0c8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mac_worldpop_chinamacaospecialadminist_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - MAC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: China, Macao Special Administrative Region - Spatial Distribution of Population
  (2015-2030)
version: null
vulnerability: null
---
