---
attributions:
- entity:
    affiliation: null
    email: null
    name: Spot-6 satellite imagery
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-the-capital-city-of-kathmandu-bagmati-province-nepal-as-of-30-s
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/flood-impact-assessment-of-the-capital-city-of-kathmandu-bagmati-province-nepal-as-of-30-s
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-the-capital-city-of-kathmandu-bagmati-province-nepal-as-of-30-s
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-of-the-capital-city-of-kathmandu-bagmati-province-nepal-as-of-30-s
dataset_id: rdls_hel-npl_unosat_floodimpactassessmentcapi_20241003
description: "UNOSAT code: FL20240928NPL This map illustrates the floods using the\
  \ Spot-6 image acquired on 30 September 2024 at 14:20 local time (08:35 UTC). Within\
  \ the analysed area of about 450 km\xB2, a total of about 8 km\xB2 of land appears\
  \ to be affected by flood waters. and about 4 km\xB2 of cropland seems to be inundated.\
  \ Based on Worldpop spatial demographic data, about 46,000 people are exposed or\
  \ living close to flooded areas. UNITAR-UNOSAT identified about 5,000 potentially\
  \ affected structures within the analysed area. This is a preliminary analysis and\
  \ has not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-of-the-capital-city-of-kathmandu-bagmati-province-nepal-as-of-30-s]"
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
    description: Approximately 5,000 potentially affected structures identified within
      the analysed area
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Approximately 46,000 people exposed or living close to flooded areas
      based on WorldPop spatial demographic data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: "Approximately 4 km\xB2 of cropland inundated by flood waters"
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_3
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed Spot-6 satellite imagery acquired on 30 September
    2024 and compared it with reference imagery to identify flood extent and inundated
    areas. Flood polygons were delineated and intersected with WorldPop population
    grids and building footprint data to estimate exposure and direct impacts. This
    preliminary post-event damage assessment has not yet been validated.
  sources:
  - id: source_1
    license: null
    name: Spot-6 satellite imagery
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
- href: https://data.humdata.org/dataset/flood-impact-assessment-of-the-capital-city-of-kathmandu-bagmati-province-nepal-as-of-30-s
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct impact on approximately 5,000 structures from flood inundation
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
  - asset_category: population
    asset_dimension: population
    description: Direct exposure of approximately 46,000 people to flooded areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: agriculture
    asset_dimension: product
    description: "Direct inundation of approximately 4 km\xB2 of cropland"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Flood Impact assessment of the Capital city of Kathmandu, Bagmati Province,
    Nepal as of 30 September 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3993/FL20240928NPL_gdb.zip
  format: Geodatabase
  id: resource_ba79356b
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
  description: Flood Impact assessment of the Capital city of Kathmandu, Bagmati Province,
    Nepal as of 30 September 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3993/FL20240928NPL_SHP.zip
  format: null
  id: resource_8bb80bc7
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
- loss
schema: rdls-10
slug: rdls_hel-npl_unosat_floodimpactassessmentcapi_20241003
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
  start: '2024-10-03'
temporal_resolution: null
title: Flood Impact assessment of the Capital city of Kathmandu, Bagmati Province,
  Nepal as of 30 September 2024
version: null
vulnerability: null
---
