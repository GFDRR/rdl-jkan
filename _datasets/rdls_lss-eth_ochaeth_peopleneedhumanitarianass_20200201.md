---
attributions:
- entity:
    affiliation: null
    email: null
    name: DTM (Round 19)
    url: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: VAS
    url: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HEA
    url: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IPC
    url: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NDRMC
    url: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
creator:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
dataset_id: rdls_lss-eth_ochaeth_peopleneedhumanitarianass_20200201
description: 'This file contains the number of people in need of humanitarian assistance
  based on the 2020 HNO. The breakdown is by population group as IDPs, IDP returnees
  and non-displaced general population at admin 3 level including the coordinates
  of the admin 3 centroids.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The 2020 Humanitarian Needs Overview (HNO) aggregated data from multiple
    sources (DTM, VAS, HEA, IPC, NDRMC) using sample survey methodology to estimate
    people in need of humanitarian assistance. Population counts were disaggregated
    by vulnerability group (IDPs, IDP returnees, non-displaced) and spatially referenced
    to admin level 3 boundaries with centroid coordinates.
  sources:
  - id: source_1
    license: null
    name: DTM (Round 19)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: VAS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: HEA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: IPC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: NDRMC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/people-in-need-of-humanitarian-assistance-in-2020-by-population-group
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need of humanitarian assistance by population group (IDPs,
      IDP returnees, non-displaced) derived from 2020 HNO
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file contains the number of people in need of humanitarian assistance
    based on the 2020 HNO. The breakdown is by population group as IDPs, IDP returnees
    and non-displaced general population at admin 3 level including the coordinates
    of the admin 3 centroids.
  download_url: https://data.humdata.org/dataset/2aac4607-054f-4443-961d-e51e29df7f51/resource/acdcd5f5-641a-488a-a636-7801f39b044c/download/ethiopia-people-in-need-by-population-group.xlsx
  format: null
  id: resource_acdcd5f5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia people in need by population group.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ochaeth_peopleneedhumanitarianass_20200201
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-02-01'
temporal_resolution: null
title: Ethiopia - People in Need of humanitarian assistance in 2020 by population
  group
version: null
vulnerability: null
---
