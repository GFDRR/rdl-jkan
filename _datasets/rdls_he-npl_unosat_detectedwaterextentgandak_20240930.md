---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-in-gandaki-lumbini-bagmati-and-madhesh-provinces-as-of-29-september-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop spatial demographic data
    url: https://data.humdata.org/dataset/water-extent-in-gandaki-lumbini-bagmati-and-madhesh-provinces-as-of-29-september-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-gandaki-lumbini-bagmati-and-madhesh-provinces-as-of-29-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-gandaki-lumbini-bagmati-and-madhesh-provinces-as-of-29-september-2024
dataset_id: rdls_he-npl_unosat_detectedwaterextentgandak_20240930
description: "UNOSAT code: FL20240928NPL This map illustrates the floods using Sentinel-1\
  \ images acquired on 29 September 2024 at 18:15 local time (12:30 UTC). Within the\
  \ analysed area of about 20,000 km\xB2, a total of about 110 km\xB2 of land appears\
  \ to be affected by flood waters. Based on Worldpop spatial demographic data, about\
  \ 58,000 people are exposed or living close to flooded areas. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT). Important note: Flood analysis\
  \ from radar images may underestimate the presence of standing waters in built-up\
  \ areas and densely vegetated areas due to the backscattering properties of the\
  \ radar signal.. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-gandaki-lumbini-bagmati-and-madhesh-provinces-as-of-29-september-2024]"
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
    description: Population exposed or living close to flooded areas, estimated at
      approximately 58,000 people based on WorldPop spatial demographic data
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
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 29 September\
    \ 2024 by comparing pre- and post-flood satellite images to detect notable changes\
    \ in water extent. The detected flood water polygons (approximately 110 km\xB2\
    ) were then intersected with WorldPop gridded population data to estimate exposure\
    \ of approximately 58,000 people across Gandaki, Lumbini, Bagmati, and Madhesh\
    \ Provinces. This is a preliminary rapid assessment product not yet validated\
    \ in the field."
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
- href: https://data.humdata.org/dataset/water-extent-in-gandaki-lumbini-bagmati-and-madhesh-provinces-as-of-29-september-2024
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Satellite detected water extent in Gandaki, Lumbini, Bagmati
    and Madhesh Provinces as of 29 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3986/FL20240928NPL_gdb.zip
  format: Geodatabase
  id: resource_d0565d48
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240928NPL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Satellite detected water extent in Gandaki, Lumbini, Bagmati
    and Madhesh Provinces as of 29 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3986/FL20240928NPL_SHP.zip
  format: null
  id: resource_c7c49288
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240928NPL_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-npl_unosat_detectedwaterextentgandak_20240930
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-30'
temporal_resolution: null
title: Nepal - Satellite detected water extent in Gandaki, Lumbini, Bagmati and Madhesh
  Provinces as of 29 September 2024
version: null
vulnerability: null
---
