---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/number-of-tdps
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: National Database & Registration Authority (NADRA)
    url: https://data.humdata.org/dataset/number-of-tdps
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/number-of-tdps
creator:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/number-of-tdps
dataset_id: rdls_lss-pak_ochapak_numbertdps_20150131
description: 'Number of Temporarily Displaced People (TDPs) from FATA region registered
  by UNHCR verified through National Database & Registration Authority (NADRA). [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/number-of-tdps]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Displaced population data collected through UNHCR registration processes
    and verified against Pakistan's national identity database (NADRA) to ensure accuracy
    of displacement counts from the FATA region.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: National Database & Registration Authority (NADRA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/number-of-tdps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Temporarily displaced population from FATA region due to conflict/crisis
      events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pakistan - Number of TDPs (TDPs_31 Jan 2015.xlsx)
  download_url: https://data.humdata.org/dataset/9d9d120a-f995-4d89-8058-a2a9557eb0f2/resource/b4d67a5c-2d99-4c94-87e9-ed43caa3106c/download/tdps-31-jan-2015.xlsx
  format: null
  id: resource_b4d67a5c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TDPs_31 Jan 2015.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pak_ochapak_numbertdps_20150131
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-31'
temporal_resolution: null
title: Pakistan - Number of TDPs
version: null
vulnerability: null
---
