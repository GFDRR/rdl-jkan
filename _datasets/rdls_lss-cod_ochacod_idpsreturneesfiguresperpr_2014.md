---
attributions:
- entity:
    affiliation: null
    email: null
    name: CMP (Commission Mouvements Population)
    url: https://data.humdata.org/dataset/idps-and-returnees-figures-per-province-per-trimester-as-of-30-septembre-2014
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Democratic Republic of the Congo
    url: https://data.humdata.org/dataset/idps-and-returnees-figures-per-province-per-trimester-as-of-30-septembre-2014
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/idps-and-returnees-figures-per-province-per-trimester-as-of-30-septembre-2014
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/idps-and-returnees-figures-per-province-per-trimester-as-of-30-septembre-2014
dataset_id: rdls_lss-cod_ochacod_idpsreturneesfiguresperpr_2014
description: 'IDP (displaced and returnees) per province for the 3rd quarter 2014..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/idps-and-returnees-figures-per-province-per-trimester-as-of-30-septembre-2014]'
details: Updated every quarter
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IDP and returnee figures were collected by CMP (Commission Mouvements
    Population) across DRC provinces and compiled by OCHA for the third quarter of
    2014. The dataset aggregates displacement movements at provincial level to track
    population displacement trends during this period.
  sources:
  - id: source_1
    license: null
    name: CMP (Commission Mouvements Population)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA Democratic Republic of the Congo
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/idps-and-returnees-figures-per-province-per-trimester-as-of-30-septembre-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees by province for Q3 2014
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DR Congo - IDPs and returnees figures per province per trimester as
    of 30 Septembre 2014 (For more detailed data, please contact dobe@un.org)
  download_url: https://data.humdata.org/dataset/50915aa7-9af3-44c8-a337-9f91cadef501/resource/71096904-8e17-407b-89bd-f21ac19f641a/download/details-deplaces-et-retournes-rdc-trim3-2014.xls
  format: null
  id: resource_71096904
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Details deplaces et retournes RDC_trim3_2014.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_idpsreturneesfiguresperpr_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2014-09-30'
  start: '2014-01-01'
temporal_resolution: null
title: DR Congo - IDPs and returnees figures per province per trimester as of 30 Septembre
  2014
version: null
vulnerability: null
---
