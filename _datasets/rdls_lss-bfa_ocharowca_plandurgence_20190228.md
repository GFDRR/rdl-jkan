---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/burkina-faso-plan-d-urgence
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/burkina-faso-plan-d-urgence
dataset_id: rdls_lss-bfa_ocharowca_plandurgence_20190228
description: 'Burkina Faso people in need figures by province (admin 2) from the 2019
  Emergency Plan. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burkina-faso-plan-d-urgence]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The 2019 Emergency Plan aggregated people in need figures from multiple
    sources and compiled them into a provincial-level registry to support humanitarian
    response planning in Burkina Faso.
  sources:
  - id: source_1
    license: null
    name: OCHA West and Central Africa (ROWCA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burkina-faso-plan-d-urgence
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need figures from 2019 Emergency Plan, aggregated by province
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Plan d''Urgence (Burkina Faso 2019 people in need figures)'
  download_url: https://data.humdata.org/dataset/8ebbe48b-ba17-4521-abdc-9972abb63794/resource/8b0feea6-20e4-45dc-aaae-c8b6fbd5a9f4/download/bfa_pin_2019.xlsx
  format: null
  id: resource_8b0feea6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bfa_pin_2019.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_ocharowca_plandurgence_20190228
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-02-28'
temporal_resolution: null
title: 'Burkina Faso: Plan d''Urgence'
version: null
vulnerability: null
---
