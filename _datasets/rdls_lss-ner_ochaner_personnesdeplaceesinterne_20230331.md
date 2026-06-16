---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Comit\xE9 National de collecte de Donn\xE9es Personnes D\xE9plac\xE9es\
      \ Internes"
    url: https://data.humdata.org/dataset/niger-personnes-deplacees-internes
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Niger
  url: https://data.humdata.org/dataset/niger-personnes-deplacees-internes
creator:
  affiliation: null
  email: null
  name: OCHA Niger
  url: https://data.humdata.org/dataset/niger-personnes-deplacees-internes
dataset_id: rdls_lss-ner_ochaner_personnesdeplaceesinterne_20230331
description: 'This data is about the internally displaced persons (IDPs). [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/niger-personnes-deplacees-internes]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Registry data collected by the National Committee for IDP Data Collection
    in Niger, documenting population movements and displacement counts aggregated
    by administrative department for May 2024.
  sources:
  - id: source_1
    license: null
    name: "Comit\xE9 National de collecte de Donn\xE9es Personnes D\xE9plac\xE9es\
      \ Internes"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/niger-personnes-deplacees-internes
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Count of internally displaced persons registered by movement events
      in May 2024
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger: Personnes d\xE9plac\xE9es internes (Personnes d\xE9plac\xE9\
    es internes mai 2024)"
  download_url: https://data.humdata.org/dataset/ff3e190e-3991-4ee2-b009-807d8a31c4c4/resource/fa91d147-873c-44d3-b890-554f4eb407e7/download/bd_mouvements-populations_ope_06052024.xlsx
  format: null
  id: resource_fa91d147
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BD_mouvements populations_ope_06052024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_ochaner_personnesdeplaceesinterne_20230331
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-31'
temporal_resolution: null
title: "Niger: Personnes d\xE9plac\xE9es internes"
version: null
vulnerability: null
---
