---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) DTM
    url: https://data.humdata.org/dataset/honduras-displacement-idps-hurricane-eta-and-iota-response-site-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/honduras-displacement-idps-hurricane-eta-and-iota-response-site-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/honduras-displacement-idps-hurricane-eta-and-iota-response-site-assessment-iom-dtm
dataset_id: rdls_lss-hnd_iom_displacementidpshurricane_202011
description: 'The dataset contains IDPs and it''s needs.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/honduras-displacement-idps-hurricane-eta-and-iota-response-site-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted site assessments in Honduras following Hurricanes
    ETA and IOTA using the DTM Standard Methodology to enumerate internally displaced
    persons (IDPs) and assess their humanitarian needs. Data was collected at displacement
    sites and compiled into a structured dataset capturing displacement figures and
    needs indicators at the sub-national level.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) DTM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-displacement-idps-hurricane-eta-and-iota-response-site-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) and their needs assessed following
      Hurricanes ETA and IOTA in Honduras
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) and their needs assessed following
      Hurricanes ETA and IOTA in Honduras
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
  description: Honduras Displacement - [IDPs] - Hurricane ETA and IOTA - Site Assessment
    [IOM DTM] (DTM Honduras Site Assessment Hurricane ETA And IOTA Response R 1)
  download_url: https://data.humdata.org/dataset/0700918a-1719-430b-8950-2feb5b76bd44/resource/4f44557e-e5e8-4892-9984-247d0fbd1ea8/download/dtm-honduras-site-assessment-hurricane-eta-and-iota-response-r-1-.xlsx
  format: null
  id: resource_4f44557e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Honduras Site Assessment Hurricane ETA And IOTA Response R 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_iom_displacementidpshurricane_202011
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-11-22'
  start: '2020-11-16'
temporal_resolution: null
title: Honduras Displacement - [IDPs] - Hurricane ETA and IOTA - Site Assessment [IOM
  DTM]
version: null
vulnerability: null
---
