---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2025-ven
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2025-ven
dataset_id: rdls_exp-ven_worldpop_bolivarianrepublicspatial_2015
description: 'Constrained estimates, total number of people per grid-cell. The dataset
  is available to download in Geotiff format at a resolution of 3 arc (approximately
  100m at the equator). The projection is Geographic Coordinate System, WGS84. The
  units are number of people per pixel. The mapping approach is Random Forest-based
  dasymetric redistribution. More information can be found in the Release Statement
  The difference between constrained and unconstrained is explained on this page:
  https://www.worldpop.org/methods/top_down_constrained_vs_unconstrained. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2025-ven]'
details: Disclaimer:The dataset currently represents a beta version (R2024B) product
  and may change over the coming year as improvements are made. Data for earlier dates
  is available directly from WorldPop Bondarenko M., Priyatikanto R., Tejedor-Garavito
  N., Zhang W., McKeen T., Cunningham A., Woods T., Hilton J., Cihan D., Nosatiuk
  B., Brinkhoff T., Tatem A., Sorichetta A.. Constrained estimates of 2015-2030 total
  number of people per grid square at a resolution of 3 arc (approximately 100m at
  the equator) R2024B version v1. Global Demographic Data Project - Funded by The
  Bill and Melinda Gates Foundation (INV-045237). WorldPop - School of Geography and
  Environmental Science, University of Southampton. DOI:10.5258/SOTON/WP00803
exposure:
- asset_type:
    description: Gridded population distribution constrained by dasymetric redistribution
      using Random Forest methodology at 100m and 1km resolution
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
  description: Gridded population data generated through Random Forest-based dasymetric
    redistribution of census-derived population counts, constrained by satellite-derived
    settlement and land use layers, producing annual estimates at 100m and 1km resolution
    for Venezuela 2015-2025.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2025-ven
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
  url: https://www.worldpop.org/methods/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2015/VEN/v1/100m/constrained/ven_pop_2015_CN_100m_R2024B_v1.tif
  format: null
  id: resource_8ac503ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2015/VEN/v1/1km_ua/constrained/ven_pop_2015_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_9a8a09b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2016/VEN/v1/100m/constrained/ven_pop_2016_CN_100m_R2024B_v1.tif
  format: null
  id: resource_651d8b0c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2016/VEN/v1/1km_ua/constrained/ven_pop_2016_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_d842b676
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2017/VEN/v1/100m/constrained/ven_pop_2017_CN_100m_R2024B_v1.tif
  format: null
  id: resource_30ccf2d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2017/VEN/v1/1km_ua/constrained/ven_pop_2017_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_2d363de2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2018/VEN/v1/100m/constrained/ven_pop_2018_CN_100m_R2024B_v1.tif
  format: null
  id: resource_084c7185
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2018/VEN/v1/1km_ua/constrained/ven_pop_2018_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_a38544a3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2019/VEN/v1/100m/constrained/ven_pop_2019_CN_100m_R2024B_v1.tif
  format: null
  id: resource_161324dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2019/VEN/v1/1km_ua/constrained/ven_pop_2019_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_551fe756
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2020/VEN/v1/100m/constrained/ven_pop_2020_CN_100m_R2024B_v1.tif
  format: null
  id: resource_9913290b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2020/VEN/v1/1km_ua/constrained/ven_pop_2020_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_2fcf6ac1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2021/VEN/v1/100m/constrained/ven_pop_2021_CN_100m_R2024B_v1.tif
  format: null
  id: resource_25a769c1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2021/VEN/v1/1km_ua/constrained/ven_pop_2021_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_3262d231
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2022/VEN/v1/100m/constrained/ven_pop_2022_CN_100m_R2024B_v1.tif
  format: null
  id: resource_87ac6862
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2022/VEN/v1/1km_ua/constrained/ven_pop_2022_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_506d9c67
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2023/VEN/v1/100m/constrained/ven_pop_2023_CN_100m_R2024B_v1.tif
  format: null
  id: resource_f0b7f45d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2023/VEN/v1/1km_ua/constrained/ven_pop_2023_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_447574ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2024/VEN/v1/100m/constrained/ven_pop_2024_CN_100m_R2024B_v1.tif
  format: null
  id: resource_5879b11d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2024/VEN/v1/1km_ua/constrained/ven_pop_2024_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_d5c3bf8b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2025/VEN/v1/100m/constrained/ven_pop_2025_CN_100m_R2024B_v1.tif
  format: null
  id: resource_30c08256
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population
    (2015-2025) (Constrained population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2024B/2025/VEN/v1/1km_ua/constrained/ven_pop_2025_CN_1km_R2024B_UA_v1.tif
  format: null
  id: resource_c32581b3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ven_pop_2025_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ven_worldpop_bolivarianrepublicspatial_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - VEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: Venezuela (Bolivarian Republic of) - Spatial Distribution of Population (2015-2025)
version: null
vulnerability: null
---
