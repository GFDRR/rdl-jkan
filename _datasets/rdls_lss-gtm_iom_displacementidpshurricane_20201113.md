---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/guatemala-displacement-idps-hurricane-eta-and-iota-site-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/guatemala-displacement-idps-hurricane-eta-and-iota-site-assessment-iom-dtm
dataset_id: rdls_lss-gtm_iom_displacementidpshurricane_20201113
description: 'The dataset contains number of IDPs, their location and needs in assessed
  sites.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/guatemala-displacement-idps-hurricane-eta-and-iota-site-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM standard methodology applied to assess internally displaced
    persons from Hurricanes ETA and IOTA in Guatemala, collecting site-level data
    on displacement numbers, geographic locations, and humanitarian needs through
    direct assessment.
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
- href: https://data.humdata.org/dataset/guatemala-displacement-idps-hurricane-eta-and-iota-site-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from Hurricanes ETA and IOTA assessed
      at displacement sites
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
  description: Guatemala Displacement - [IDPs] - Hurricane ETA and IOTA - Site Assessment
    [IOM DTM] (DTM Guatemala Site Assessment ETA_IOTA R1)
  download_url: https://data.humdata.org/dataset/a9e6c001-fda1-47d9-bfce-31ed91187099/resource/be59bc8b-11a2-4430-bbc2-dd7584d9cf06/download/dtm-guatemala-site-assessment-eta_iota-r1.xlsx
  format: null
  id: resource_be59bc8b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Guatemala Site Assessment ETA_IOTA R1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_iom_displacementidpshurricane_20201113
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-13'
temporal_resolution: null
title: Guatemala Displacement - [IDPs] - Hurricane ETA and IOTA - Site Assessment
  [IOM DTM]
version: null
vulnerability: null
---
