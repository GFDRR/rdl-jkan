---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-25-and-29-may-2022-over-guyana
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-25-and-29-may-2022-over-guyana
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-25-and-29-may-2022-over-guyana
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-between-25-and-29-may-2022-over-guyana
dataset_id: rdls_he-guy_unosat_detectedwaterextentbetwee_20220530
description: 'UNOSAT code: FL20220526GUY This map illustrates cumulative satellite-detected
  water using VIIRS in Guyana between 25 to 29 May 2022 compared with the period from
  20 to 24 May 2022. Within the cloud free analyzed areas of about 205,000 km2, a
  total of about 3,900 km2 of lands appear to be affected with flood waters. Water
  extent appears to have increased of about 1,200 km2 since the period between 20
  to 24 may 2022. Based on Worldpop population data and the maximal flood water coverage,
  ~22,000 people are potentially exposed or living close to flooded areas. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-between-25-and-29-may-2022-over-guyana]'
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data and maximal flood water coverage
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery from 25-29 May 2022
    and compared it with imagery from 20-24 May 2022 to detect cumulative water extent
    changes across cloud-free areas of Guyana. The resulting water extent polygons
    (3,900 km2) were intersected with WorldPop population grids to estimate exposure
    of approximately 22,000 people to flood hazard.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-between-25-and-29-may-2022-over-guyana
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
  description: Satellite detected water extent between 25 and 29 May 2022 over Guyana
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20220526GUY/FL20220526GUY_gdb.zip
  format: Geodatabase
  id: resource_4bfe006c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220526GUY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent between 25 and 29 May 2022 over Guyana
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/GY/FL20220526GUY/FL20220526GUY_SHP.zip
  format: null
  id: resource_42202afb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220526GUY_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-guy_unosat_detectedwaterextentbetwee_20220530
spatial:
  bbox: null
  centroid: null
  countries:
  - GUY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-05-30'
temporal_resolution: null
title: Satellite detected water extent between 25 and 29 May 2022 over Guyana
version: null
vulnerability: null
---
