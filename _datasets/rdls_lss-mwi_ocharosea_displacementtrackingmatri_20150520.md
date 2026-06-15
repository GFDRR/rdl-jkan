---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/malawi-affected-persons-locations
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/malawi-affected-persons-locations
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/malawi-affected-persons-locations
dataset_id: rdls_lss-mwi_ocharosea_displacementtrackingmatri_20150520
description: 'IOM DTM (Displacement Tracking Matrix) Displacement Sites as of 20 May
  2015 (Google Earth kmz file).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-affected-persons-locations]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM collected displacement site data across Malawi as of May 2015,
    recording locations and populations of internally displaced persons. The dataset
    represents post-event impact assessment of displacement, with sites georeferenced
    as point locations in KMZ format.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-affected-persons-locations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons recorded at displacement sites, likely
      triggered by flooding or other hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: Malawi - Displacement Tracking Matrix (Rar file of kmz files)
  download_url: https://data.humdata.org/dataset/e2eba921-1709-4c9b-9bf4-ddeafba27f32/resource/e08fc5bf-518f-4b4c-8f70-d1b3c16527b0/download/05_iom_dtm_malawi_displacement_site_round_iii_report_20150513.rar
  format: null
  id: resource_e08fc5bf
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 05_iom_dtm_malawi_displacement_site_round_iii_report_20150513.rar
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mwi_ocharosea_displacementtrackingmatri_20150520
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-05-20'
temporal_resolution: null
title: Malawi - Displacement Tracking Matrix
version: null
vulnerability: null
---
