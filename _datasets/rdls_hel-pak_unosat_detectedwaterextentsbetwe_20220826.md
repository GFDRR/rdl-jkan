---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-03-and-23-august-2022-over-pakistan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: VIIRS
    url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-03-and-23-august-2022-over-pakistan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-03-and-23-august-2022-over-pakistan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extents-between-03-and-23-august-2022-over-pakistan
dataset_id: rdls_hel-pak_unosat_detectedwaterextentsbetwe_20220826
description: 'UNOSAT code: FL20220808PAK This map illustrates cumulative satellite-detected
  water using VIIRS in Pakistan between 03 to 23 August 2022. Within the cloud free
  analyzed areas of about 780,000 km2, a total of about 55,000 km2 of lands appear
  to be affected with flood waters. Based on Worldpop population data and the maximum
  flood water coverage, ~19,368,000 people are potentially exposed or living close
  to flooded areas. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to the United Nations Satellite Centre
  (UNOSAT).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extents-between-03-and-23-august-2022-over-pakistan]'
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
      on WorldPop data
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery acquired between
    3-23 August 2022 over Pakistan, comparing multiple images to detect cumulative
    water extents across cloud-free areas of approximately 780,000 km2. Detected flood
    water coverage (55,000 km2) was intersected with WorldPop gridded population data
    to estimate population exposure. This is a preliminary post-event satellite-based
    damage assessment not yet validated in the field.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: VIIRS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extents-between-03-and-23-august-2022-over-pakistan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by or exposed to satellite-detected flood waters
      during August 2022 Pakistan floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Satellite detected water extents between 03 and 23 August 2022 over
    Pakistan (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PK/FL20220808PAK/FL20220808PAK_gdb.zip
  format: Geodatabase
  id: resource_dc392bed
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 03 and 23 August 2022 over
    Pakistan (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PK/FL20220808PAK/FL20220808PAK_SHP.zip
  format: null
  id: resource_fe9be194
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_detectedwaterextentsbetwe_20220826
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-26'
temporal_resolution: null
title: Satellite detected water extents between 03 and 23 August 2022 over Pakistan
version: null
vulnerability: null
---
