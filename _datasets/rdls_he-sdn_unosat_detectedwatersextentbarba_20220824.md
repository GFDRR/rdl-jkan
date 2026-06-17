---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/waters-extent-in-barbar-district-river-nile-state-sudan-as-of-20-august-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/waters-extent-in-barbar-district-river-nile-state-sudan-as-of-20-august-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extent-in-barbar-district-river-nile-state-sudan-as-of-20-august-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-extent-in-barbar-district-river-nile-state-sudan-as-of-20-august-2022
dataset_id: rdls_he-sdn_unosat_detectedwatersextentbarba_20220824
description: 'UNOSAT code: FL20220816SDN This map illustrates satellite-detected surface
  waters in Barbar district, River Nile State as observed from a Sentinel-2 image
  acquired on 20 August 2022 at 10:25 local time. Within the analyzed area of about
  780 km2, about 43 km2 of lands appear to be flooded. Based on Worldpop population
  data and the detected surface waters in the analyzed area, about 7,800 people are
  potentially exposed or living close to flooded areas. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/waters-extent-in-barbar-district-river-nile-state-sudan-as-of-20-august-2022]'
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
    description: Population potentially exposed or living close to flooded areas derived
      from WorldPop data
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
  description: "Satellite imagery from Sentinel-2 acquired on 20 August 2022 was analyzed\
    \ by UNOSAT to detect surface water extent through visual interpretation and change\
    \ detection methods. Detected flooded areas (43 km\xB2) were intersected with\
    \ WorldPop gridded population data to estimate approximately 7,800 people potentially\
    \ exposed to flooding in the 780 km\xB2 study area of Barbar District."
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
    name: Sentinel-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/waters-extent-in-barbar-district-river-nile-state-sudan-as-of-20-august-2022
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
  description: Satellite detected waters extent in Barbar District, River Nile State,
    Sudan as of 20 August 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/SD/FL20220816SDN/FL20220816SDN_gdb.zip
  format: Geodatabase
  id: resource_2d9779de
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220816SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters extent in Barbar District, River Nile State,
    Sudan as of 20 August 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/SD/FL20220816SDN/FL20220816SDN_SHP.zip
  format: null
  id: resource_e2c0ce53
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220816SDN_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-sdn_unosat_detectedwatersextentbarba_20220824
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-24'
temporal_resolution: null
title: Satellite detected waters extent in Barbar District, River Nile State, Sudan
  as of 20 August 2022
version: null
vulnerability: null
---
