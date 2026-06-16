---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR Protection and Return Monitoring Network (PRMN)
    url: https://data.humdata.org/dataset/somalia-internally-displaced-persons-idps
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/somalia-internally-displaced-persons-idps
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/somalia-internally-displaced-persons-idps
dataset_id: rdls_lss-som_unhcr_internallydisplacedperson_2016
description: 'Data collated by UNHCR - Protection and Return Monitoring Network (PRMN),
  contains internally displaced persons. The data includes regions (departure and
  arrival), districts (departure and arrival), reasons of displacements and the IDPs
  from January 2016 - October 2022.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-internally-displaced-persons-idps]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNHCR PRMN collects displacement monitoring data through field surveys
    and administrative records across Somalia, tracking IDP movements between regions
    and districts with associated reasons and humanitarian needs from January 2016
    onwards. Data is aggregated by month and week to produce displacement flow statistics.
  sources:
  - id: source_1
    license: null
    name: UNHCR Protection and Return Monitoring Network (PRMN)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-internally-displaced-persons-idps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from January 2016 to October 2022 with
      origin and destination regions
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.unhcr.org/en/documents/download/53888
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Internally Displaced Persons (IDPs) (Internal displacements
    from January 2016 - August 2023 at district level)'
  download_url: https://data.humdata.org/dataset/475e2e3c-3cec-4961-b73c-d8e68791ce60/resource/981e0a25-8a83-48a2-a46c-0be81a881856/download/unhcr-prmn-displacement-dataset-1.xlsx
  format: null
  id: resource_981e0a25
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SOM_UNHCR-PRMN-Displacement-Dataset-August-2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Internally Displaced Persons (IDPs) (Internal displacements
    as at 30th November 2022 district level)'
  download_url: https://data.humdata.org/dataset/475e2e3c-3cec-4961-b73c-d8e68791ce60/resource/fca8af92-f589-4604-be97-f55bd57f228f/download/som_prmn_map_data.csv
  format: null
  id: resource_fca8af92
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SOM_UNHCR-PRMN_Displacement-Dataset.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_unhcr_internallydisplacedperson_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-08-31'
  start: '2016-01-01'
temporal_resolution: null
title: 'Somalia: Internally Displaced Persons (IDPs)'
version: null
vulnerability: null
---
