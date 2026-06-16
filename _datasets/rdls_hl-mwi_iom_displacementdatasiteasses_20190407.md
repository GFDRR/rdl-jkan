---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-idai-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-idai-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-idai-iom-dtm
dataset_id: rdls_hl-mwi_iom_displacementdatasiteasses_20190407
description: 'Malawi has experienced floods and sustained heavy rains caused by the
  tropical cyclone Idai weather system. IOM, in close coordination with the Government
  of Malawi through the Department of Disaster Management Affairs (DoDMA), conducted
  multi-sectoral location assessments in Chikwawa, Nsanje, Phalombe, Zomba districts.
  The dataset contains number of IDPs, households and their needs at sub-national
  level.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-idai-iom-dtm]'
details: "Copyright \xC2\xA9 International Organization for Migration 2018 IOM reserves\
  \ the right to assert ownership of the Materials collected on the https://data.humdata.org/\
  \ website. The Materials may be viewed, downloaded, and printed for non-commercial\
  \ use only, without, inter alia, any right to sell, resell, redistribute or create\
  \ derivative works therefrom. At all times the User shall credit the DTM as the\
  \ source, unless otherwise stated. The user must include the URL of the Materials\
  \ from the HDX Website, as well as the following credit line: Source: 'International\
  \ Organization for Migration (IOM), Displacement Tracking Matrix (DTM)'."
exposure: []
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted multi-round site assessments (3 rounds) in four Malawi
    districts (Chikwawa, Nsanje, Phalombe, Zomba) following tropical cyclone Idai,
    documenting displacement populations and household-level needs through sample
    survey methodology at sub-national assessment sites.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-idai-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from tropical cyclone Idai in Malawi
      districts
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
        metric: displaced
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi Displacement Data - Site Assessment - Idai - [IOM DTM] (53,237
    individuals and 12,470 families recorded.)
  download_url: https://data.humdata.org/dataset/8dfed11c-838f-41d3-8162-3e0cc2f5311b/resource/d21f0711-2722-42ee-aa1c-6dda74287ff4/download/dtm-malawi-site-assessment-round-3.xlsx
  format: null
  id: resource_d21f0711
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Malawi Site Assessment Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 110,110 individuals (24,887 households) were recorded across 103 displacement
    sites. An additional 40 sites in the 4 districts were assessed and verified in
    this data collection round.
  download_url: https://data.humdata.org/dataset/8dfed11c-838f-41d3-8162-3e0cc2f5311b/resource/8b8d307d-b65d-4c6b-b9bf-56374d05ade1/download/dtm-malawi-site-assessment-round-2.xlsx
  format: null
  id: resource_8b8d307d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Malawi Site Assessment Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 76,471 individuals (17,254 households) were reported across the 63
    assessed displacement sites. The IDPs population is composed of 58% of females
    and 42% of males. In terms of nationality, 330 Mozambicans were identified in
    two sites in Nsanje district.
  download_url: https://data.humdata.org/dataset/8dfed11c-838f-41d3-8162-3e0cc2f5311b/resource/c7daff9a-8bbe-4e65-ac80-9aeda985ce5d/download/dtm-malawi-site-assessment-round-1.xlsx
  format: null
  id: resource_c7daff9a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Malawi Site Assessment Round 1
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mwi_iom_displacementdatasiteasses_20190407
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
  start: '2019-04-07'
temporal_resolution: null
title: Malawi Displacement Data - Site Assessment - Idai - [IOM DTM]
version: null
vulnerability: null
---
