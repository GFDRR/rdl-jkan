---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/potential-population-exposure-around-lewotobi-laki-laki-volcano
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-population-exposure-around-lewotobi-laki-laki-volcano
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potential-population-exposure-around-lewotobi-laki-laki-volcano
dataset_id: rdls_he-idn_unosat_potentialpopulationexposu_20241106
description: 'UNOSAT code: VO20241105IDN, GDACS ID: 1000099 This map illustrates the
  population potentially exposed following the Lewotobi Laki-Laki volcanic eruption.
  Based on Worldpop spatial demographic data, ~11,400; ~26,000 and 37,000 people live
  within a 5km; 7.5km and 10km radius zone from the volcano crater. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/potential-population-exposure-around-lewotobi-laki-laki-volcano]'
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
    description: Population potentially exposed within concentric distance zones from
      the volcano crater based on WorldPop spatial demographic data
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
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: h_vaf:mm
      process: ashfall
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed satellite imagery of the Lewotobi Laki-Laki
    volcanic eruption and delineated hazard exposure zones at 5km, 7.5km, and 10km
    radial distances from the crater. WorldPop spatial demographic data was intersected
    with these zones to estimate the population potentially exposed to volcanic hazards
    in each buffer area.
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
- href: https://data.humdata.org/dataset/potential-population-exposure-around-lewotobi-laki-laki-volcano
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
  description: Indonesia - Potential population exposure around Lewotobi Laki-Laki
    volcano (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4019/VO20241105IDN_gdb.zip
  format: Geodatabase
  id: resource_564e58c2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20241105IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Potential population exposure around Lewotobi Laki-Laki
    volcano (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4019/VO20241105IDN_SHP.zip
  format: null
  id: resource_0299edef
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20241105IDN_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-idn_unosat_potentialpopulationexposu_20241106
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-06'
temporal_resolution: null
title: Indonesia - Potential population exposure around Lewotobi Laki-Laki volcano
version: null
vulnerability: null
---
