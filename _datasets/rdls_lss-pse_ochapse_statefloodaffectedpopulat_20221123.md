---
attributions:
- entity:
    affiliation: null
    email: null
    name: WASH Cluster
    url: https://data.humdata.org/dataset/west-bank-and-gaza-wash-vulnerability-and-flood-events
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA occupied Palestinian territory (oPt)
  url: https://data.humdata.org/dataset/west-bank-and-gaza-wash-vulnerability-and-flood-events
creator:
  affiliation: null
  email: null
  name: OCHA occupied Palestinian territory (oPt)
  url: https://data.humdata.org/dataset/west-bank-and-gaza-wash-vulnerability-and-flood-events
dataset_id: rdls_lss-pse_ochapse_statefloodaffectedpopulat_20221123
description: 'The dataset captures HHs flooded by community in the WB and GZ in the
  last three years. 8,196 HH affected by floods events in the last three years in
  Gaza Strip 10,173 affected by flood events in the last three years in the West Bank.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/west-bank-and-gaza-wash-vulnerability-and-flood-events]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event flood impact data collected by the WASH Cluster through
    direct observation and community reporting in Gaza Strip and West Bank over a
    three-year period, aggregated by community to quantify affected households.
  sources:
  - id: source_1
    license: null
    name: WASH Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/west-bank-and-gaza-wash-vulnerability-and-flood-events
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Households affected by flood events over a three-year period in Gaza
      Strip and West Bank
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
        metric: exposure
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: State of Palestine - Flood Affected Population (WASH Vulnerability
    Map 2022 (Flood))
  download_url: https://data.humdata.org/dataset/fe024e7c-85fa-4a2d-8e83-b828f9d07583/resource/92855698-a9ae-4d2b-95a6-6c1b07c1b575/download/wash-vulnerability-map-2022-flood.xlsx
  format: null
  id: resource_92855698
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WASH Vulnerability Map 2022 (Flood)
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_ochapse_statefloodaffectedpopulat_20221123
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-23'
temporal_resolution: null
title: State of Palestine - Flood Affected Population
version: null
vulnerability: null
---
