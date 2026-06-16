---
attributions:
- entity:
    affiliation: null
    email: null
    name: NDRRMC (National Disaster Risk Reduction and Management Council)
    url: https://data.humdata.org/dataset/philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9
creator:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9
dataset_id: rdls_lss-phl_brc_haimahousedamagepcodedndr_20161025
description: 'This data is about damaged houses in the Philippines after Typhoon Haima
  (Lawin). [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9]'
details: Sporadic Updates - hasn't been an update for over a week as of 2nd November
  2016
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event damage assessment data collected by the Philippines Government
    (NDRRMC) following Typhoon Haima, compiled and geocoded by the British Red Cross
    Maps Team with administrative boundaries (PCODED), and distributed as situation
    report 9.
  sources:
  - id: source_1
    license: null
    name: NDRRMC (National Disaster Risk Reduction and Management Council)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-haima-house-damage-pcoded-ndrrmc-sitrep-9
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Typhoon Haima (strong wind event)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: 'PCODED (Province and Municipality/City level) CSV for house damage
    by Municipality/City from the Philippines NDRRMC Preparedness Measures for Typhoon
    ''Lawin'' (I.N. Haima) Sitrep # 9 (25 October 2016). PCODES as per the Philippine
    Geographic Standard Code (PSGC) dataset. The dataset is also HXLated.'
  download_url: https://data.humdata.org/dataset/3cb60971-0dc7-4743-a7ae-e65744b2dbba/resource/968202f1-856a-4906-ae87-c730e9b1dd27/download/phl_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv
  format: null
  id: resource_968202f1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PHL_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_brc_haimahousedamagepcodedndr_20161025
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-25'
temporal_resolution: null
title: Philippines - Haima House Damage PCODED - NDRRMC Sitrep 9
version: null
vulnerability: null
---
