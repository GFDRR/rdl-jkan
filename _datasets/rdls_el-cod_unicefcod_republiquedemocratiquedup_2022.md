---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF RDC
    url: https://data.humdata.org/dataset/priorisation-s1-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Cluster Nutrition RDC
    url: https://data.humdata.org/dataset/priorisation-s1-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Democratic Republic of Congo
  url: https://data.humdata.org/dataset/priorisation-s1-2021
creator:
  affiliation: null
  email: null
  name: UNICEF Democratic Republic of Congo
  url: https://data.humdata.org/dataset/priorisation-s1-2021
dataset_id: rdls_el-cod_unicefcod_republiquedemocratiquedup_2022
description: "Priorisation du cluster nutrition qui se base sur plusieurs facteurs\
  \ aggravants pour permettre de mettre en avant les zones de sant\xE9 les plus sensibles\
  \ \xE0 la malnutrition alors que les donn\xE9es provenant des enqu\xEAtes nutritionnelles\
  \ sont vieillissantes pour certaine Zone de sant\xE9.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/priorisation-s1-2021]"
details: null
exposure:
- asset_type:
    description: Population by age/sex groups (total, men, women, children 6-59 months,
      children 6-23 months, pregnant and lactating women) at health zone level
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Nutritional survey data (GAM, SAM, MAM, stunting prevalence) and food
    security classifications (IPC) from multiple years are aggregated at health zone
    level. A multi-factor prioritization algorithm applies scoring weights to prevalence
    indicators, aggravating factors (chronic malnutrition, epidemics, population displacement),
    and coverage of nutrition interventions to generate priority rankings for humanitarian
    response targeting.
  sources:
  - id: source_1
    license: null
    name: UNICEF RDC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Cluster Nutrition RDC
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/priorisation-s1-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition prevalence (GAM, SAM, MAM) in children and pregnant/lactating
      women derived from nutritional surveys
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Chronic malnutrition (stunting) prevalence in children as aggravating
      factor
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/report/democratic-republic-congo/republique-democratique-du-congo-lignes-directrices-du-cluster-nutrition-2022
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Priorisation du cluster nutrition January 2024 - June 2024. Source\
    \ des donn\xE9es: DRC Cluster Nutrition."
  download_url: https://data.humdata.org/dataset/0e58c4cc-9dc8-4f82-bec4-e808be8bd064/resource/5d8779e7-8d97-4ae9-bc24-894f59300bd6/download/rdc_priorisation-s1-2024-cluster-nutrition.xlsx
  format: null
  id: resource_5d8779e7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_Priorisation S1 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Priorisation du cluster nutrition January 2024 - June 2023. Source\
    \ des donn\xE9es: DRC Cluster Nutrition."
  download_url: https://data.humdata.org/dataset/0e58c4cc-9dc8-4f82-bec4-e808be8bd064/resource/84b2072f-56fc-485c-862a-88886371f95e/download/priorisartion-s1-2023-vf.xlsx
  format: null
  id: resource_84b2072f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Priorisartion S1 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Priorisation du cluster nutrition pour les 6 prochains mois Juin 2022\
    \ - Novembre 2022. Source des donn\xE9es: enqu\xEAtes SMART, MICS 2018, Cluster\
    \ Sant\xE9, IPC AFI 20\xE8me cycle, OCHA, PRONANUT."
  download_url: https://data.humdata.org/dataset/0e58c4cc-9dc8-4f82-bec4-e808be8bd064/resource/b7eab54e-1a8b-4fe1-acfd-6445d1465a1e/download/priorisation-s2-2022.xlsx
  format: null
  id: resource_b7eab54e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: priorisation-s2 2022
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-cod_unicefcod_republiquedemocratiquedup_2022
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
  end: '2024-06-30'
  start: '2022-06-21'
temporal_resolution: null
title: "R\xE9publique D\xE9mocratique du Congo: Priorisation Juin 2024"
version: null
vulnerability: null
---
