---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM Sudan
    url: https://data.humdata.org/dataset/idp-population-dtm-iom-sudan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/idp-population-dtm-iom-sudan
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/idp-population-dtm-iom-sudan
dataset_id: rdls_lss-sdn_ochasdn_idppopulationdtmiom_20200229
description: 'IDP population in Sudan through Displacement Tracking Matrix by IOM.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/idp-population-dtm-iom-sudan]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IDP population data collected through IOM's Displacement Tracking Matrix
    (DTM) registration methodology, which systematically tracks internally displaced
    persons across Sudan to document displacement counts and population movements
    resulting from various hazards.
  sources:
  - id: source_1
    license: null
    name: IOM Sudan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/idp-population-dtm-iom-sudan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from various hazards including flooding
      tracked through DTM registration
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
  description: IDP Population DTM IOM - Sudan (Internally Displaced Population)
  download_url: https://data.humdata.org/dataset/7e86e642-d1e0-4c03-8943-075936e46bce/resource/1eae3776-bc50-4105-a32b-1fec5bf10cda/download/sudan-dtm-idps-dataset-29feb20-003.xlsx
  format: null
  id: resource_1eae3776
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sudan DTM IDPs DATASET 29Feb20 (003).xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_idppopulationdtmiom_20200229
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
  start: '2020-02-29'
temporal_resolution: null
title: IDP Population DTM IOM - Sudan
version: null
vulnerability: null
---
