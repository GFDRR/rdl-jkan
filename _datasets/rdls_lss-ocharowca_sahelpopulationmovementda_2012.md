---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/sahel-population-movement
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/sahel-population-movement
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/sahel-population-movement
dataset_id: rdls_lss-ocharowca_sahelpopulationmovementda_2012
description: 'This data is about the refugees, IDPs, and returnees in the Sahel from
  2012 till March 2021.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sahel-population-movement]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Population movement data compiled from multiple humanitarian partners
    through registry methodology, documenting displacement flows (refugees, IDPs,
    returnees) across the Sahel from 2012 to March 2021. Data aggregated by OCHA ROWCA
    to track humanitarian impacts of regional crises.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sahel-population-movement
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displacement of refugees, IDPs, and returnees in the Sahel region
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
        metric: displaced
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
  description: Sahel population movement HNRO 2021.xlsx
  download_url: https://data.humdata.org/dataset/370b28e6-5c76-4c69-992e-8d2bb126a598/resource/f53abb96-3814-482b-9eed-9ab5cec48e2f/download/sahel-population-mvt-hnro-2021.xlsx
  format: null
  id: resource_f53abb96
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sahel population movement HNRO 2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ocharowca_sahelpopulationmovementda_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - MRT
  - SEN
  - MLI
  - BFA
  - NER
  - TCD
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-03-29'
  start: '2012-01-01'
temporal_resolution: null
title: Sahel Population Movement Data
version: null
vulnerability: null
---
