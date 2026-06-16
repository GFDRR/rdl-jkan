---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA DR Congo
    url: https://data.humdata.org/dataset/mouvement-de-population
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/mouvement-de-population
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/mouvement-de-population
dataset_id: rdls_lss-cod_ochacod_mouvementdepopulation
description: "la valeur pour les personnes d\xE9plac\xE9es est calcul\xE9 pour une\
  \ p\xE9riode de 24 mois sur la date d'\xE9valuation. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/mouvement-de-population]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Displacement figures were compiled by OCHA DR Congo from field assessments
    and administrative records, with values calculated as cumulative population movements
    over rolling 24-month periods relative to the assessment date.
  sources:
  - id: source_1
    license: null
    name: OCHA DR Congo
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mouvement-de-population
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement counts over a 24-month assessment period
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
  description: DR Congo - Mouvement de population (Excel)
  download_url: https://data.humdata.org/dataset/99c44e7b-cee4-46dd-bca9-107c1616b53d/resource/0fee2f84-061d-4d02-8185-2e05702d7265/download/rdc_mouvement_de_population_deplace_juin_2021.xlsx
  format: null
  id: resource_0fee2f84
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplac\xE9_Juin_2021.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_mouvementdepopulation
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: DR Congo - Mouvement de population
version: null
vulnerability: null
---
