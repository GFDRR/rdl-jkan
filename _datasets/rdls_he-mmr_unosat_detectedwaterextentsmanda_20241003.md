---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-mandalay-kayah-shan-south-nay-pyi-taw-bago-est-mon-and-kayin-states-myanm
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/water-extents-in-mandalay-kayah-shan-south-nay-pyi-taw-bago-est-mon-and-kayin-states-myanm
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-mandalay-kayah-shan-south-nay-pyi-taw-bago-est-mon-and-kayin-states-myanm
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-mandalay-kayah-shan-south-nay-pyi-taw-bago-est-mon-and-kayin-states-myanm
dataset_id: rdls_he-mmr_unosat_detectedwaterextentsmanda_20241003
description: "UNOSAT code: FL20240912MMR This map illustrates aggregated satellite\
  \ detected floods using Sentinel-1 images acquired on 03 to 20 September 2024 using\
  \ an automated analysis with a machine learning method. Within the analysed area\
  \ of about 80,000 km\xB2, a total of about 5,100 km\xB2 of land appears to be affected\
  \ by flood waters and about 4,500 km\xB2 of cropland appears to be inundated. Based\
  \ on Worldpop spatial demographic data, about 760,000 people are exposed or living\
  \ close to flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Flood analysis from radar images may underestimate the\
  \ presence of standing waters in built-up areas and densely vegetated areas due\
  \ to the backscattering properties of the radar signal.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/water-extents-in-mandalay-kayah-shan-south-nay-pyi-taw-bago-est-mon-and-kayin-states-myanm]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposed to or living close to flooded areas based on WorldPop
      spatial demographic data
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
- asset_type:
    description: "Cropland inundated by flood waters, approximately 4,500 km\xB2"
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery from 03-20 September 2024 was processed using\
    \ automated machine learning methods to detect flood water extents across 80,000\
    \ km\xB2 in Myanmar. Population exposure was estimated by overlaying detected\
    \ flood polygons with WorldPop gridded demographic data. The resulting dataset\
    \ provides observed flood extent areas and derived population exposure metrics\
    \ as of the satellite acquisition dates."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop spatial demographic data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-mandalay-kayah-shan-south-nay-pyi-taw-bago-est-mon-and-kayin-states-myanm
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Mandalay, Kayah, Shan (South),
    Nay Pyi Taw, Bago (Est), Mon and Kayin States, Myanmar as of 03 & 23 September
    2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3992/FL20240912MMR_gdb.zip
  format: Geodatabase
  id: resource_7ca41614
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240912MMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Mandalay, Kayah, Shan (South),
    Nay Pyi Taw, Bago (Est), Mon and Kayin States, Myanmar as of 03 & 23 September
    2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3992/FL20240912MMR_SHP.zip
  format: null
  id: resource_62682fd2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240912MMR_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Mandalay, Kayah, Shan (South),
    Nay Pyi Taw, Bago (Est), Mon and Kayin States, Myanmar as of 03 & 23 September
    2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3992/UNOSAT_Population_Exposure_FL20240912MMR_03_23September2024.xlsx
  format: null
  id: resource_ac331ac9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20240912MMR_03_23September2024.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mmr_unosat_detectedwaterextentsmanda_20241003
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-03'
temporal_resolution: null
title: Satellite detected water extents in Mandalay, Kayah, Shan (South), Nay Pyi
  Taw, Bago (Est), Mon and Kayin States, Myanmar as of 03 & 23 September 2024
version: null
vulnerability: null
---
