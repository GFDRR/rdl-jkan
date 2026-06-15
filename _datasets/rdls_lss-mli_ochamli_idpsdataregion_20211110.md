---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM Displacement Tracking Matrix (DTM)
    url: https://data.humdata.org/dataset/idps-data-by-region-in-mali
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Commission on Population Movements
    url: https://data.humdata.org/dataset/idps-data-by-region-in-mali
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/idps-data-by-region-in-mali
creator:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/idps-data-by-region-in-mali
dataset_id: rdls_lss-mli_ochamli_idpsdataregion_20211110
description: 'The dataset highlights the number of IDPs in Mali by region from Sep
  ''12 - juillet 21.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/idps-data-by-region-in-mali]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDP displacement data compiled by IOM through their Displacement Tracking
    Matrix (DTM) exercise combined with field evaluations from the Commission on Population
    Movements partners. Data aggregated by administrative region covering the period
    September 2012 to July 2021, tracking conflict-induced internal displacement in
    Mali.
  sources:
  - id: source_1
    license: null
    name: IOM Displacement Tracking Matrix (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Commission on Population Movements
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/idps-data-by-region-in-mali
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict and violence in Mali by
      region
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
  description: Mali - IDPs Data by region (IDP figures from 2012 to 2021 by region)
  download_url: https://data.humdata.org/dataset/1d309b64-970f-4f28-818e-33869d13b04e/resource/9affe23f-3ce2-40d1-ae6a-1d7060b548a5/download/pdi_mali_2012_2021.xlsx
  format: null
  id: resource_9affe23f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PDI_Mali_2012_2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_ochamli_idpsdataregion_20211110
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-11-10'
temporal_resolution: null
title: Mali - IDPs Data by region
version: null
vulnerability: null
---
