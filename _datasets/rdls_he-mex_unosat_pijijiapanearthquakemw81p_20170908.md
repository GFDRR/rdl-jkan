---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS
    url: https://data.humdata.org/dataset/mexico-pijijiapan-earthquake-mw-8-1-population-exposure-analysis
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/mexico-pijijiapan-earthquake-mw-8-1-population-exposure-analysis
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mexico-pijijiapan-earthquake-mw-8-1-population-exposure-analysis
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mexico-pijijiapan-earthquake-mw-8-1-population-exposure-analysis
dataset_id: rdls_he-mex_unosat_pijijiapanearthquakemw81p_20170908
description: 'Population Exposure Analysis Based on Ground Shake Data (USGS) and Population
  data (WorldPop).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mexico-pijijiapan-earthquake-mw-8-1-population-exposure-analysis]'
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
    description: Population distribution from WorldPop exposed to earthquake ground
      shaking
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
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT integrated USGS ground shake data from the Mw 8.1 Pijijiapan
    earthquake with WorldPop gridded population data to produce a population exposure
    analysis, identifying the spatial distribution of people exposed to earthquake
    ground motion hazard.
  sources:
  - id: source_1
    license: null
    name: USGS
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
- href: https://data.humdata.org/dataset/mexico-pijijiapan-earthquake-mw-8-1-population-exposure-analysis
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
  description: Mexico-Pijijiapan earthquake Mw 8.1 - Population Exposure Analysis
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170908MEX/UNOSAT_PoP_Exposure_EQ_M8.1_Mexico.xlsx
  format: null
  id: resource_e9e44ba2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PoP_Exposure_EQ_M8.1_Mexico.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mex_unosat_pijijiapanearthquakemw81p_20170908
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-08'
temporal_resolution: null
title: Mexico-Pijijiapan earthquake Mw 8.1 - Population Exposure Analysis
version: null
vulnerability: null
---
