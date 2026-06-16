---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM Model (OCHA)
    url: https://data.humdata.org/dataset/subnational-inform-caucasus-and-central-asia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Regional Inter-Agency Standing Committee (IASC) Task Force for Caucasus
      and Central Asia
    url: https://data.humdata.org/dataset/subnational-inform-caucasus-and-central-asia
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA ROCCA (inactive)
  url: https://data.humdata.org/dataset/subnational-inform-caucasus-and-central-asia
creator:
  affiliation: null
  email: null
  name: OCHA ROCCA (inactive)
  url: https://data.humdata.org/dataset/subnational-inform-caucasus-and-central-asia
dataset_id: rdls_el-ocharocca_subnationalinformcaucasus_20161231
description: 'The subnational INFORM model for Caucasus and Central Asia was initiated
  by the Regional Inter-Agency Standing Committee (IASC) Task Force for Caucasus and
  Central Asia and is managed by OCHA. The INFORM model is being used to support coordinated
  preparedness actions. Partners hope to use the model to improve cooperation between
  humanitarian and development actors in managing risk and building resilience across
  the region. INFORM identifies areas at a high risk of humanitarian crisis that are
  more likely to require international assistance. The INFORM model is based on risk
  concepts published in scientific literature and envisages three dimensions of risk:
  Hazards & Exposure, Vulnerability and Lack of Coping Capacity. The INFORM model
  is split into different levels to provide a quick overview of the underlying factors
  leading to humanitarian risk. The regional subnational INFORM model for Caucasus
  and Central Asia is developed at the first administrative level (corresponding to
  the provinces/oblasts/regions and few independent cities) of the eight countries
  in South Caucasus and Central Asia. The INFORM index supports a proactive crisis
  management framework. It will be helpful for an objective allocation of resources
  for disaster management as well as for coordinated actions focused on anticipating,
  mitigating, and preparing for humanitarian emergencies.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/subnational-inform-caucasus-and-central-asia]'
details: null
exposure:
- asset_type:
    description: Subnational population distribution across Caucasus and Central Asia
      administrative units
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
  description: The INFORM model integrates multiple hazard, exposure, and vulnerability
    datasets from various sources (as documented in the Excel metadata sheet) to produce
    a composite humanitarian crisis risk index at administrative level 1. The model
    applies risk theory combining hazard and exposure dimensions with vulnerability
    and coping capacity assessments to generate subnational risk scores indicating
    likelihood of requiring international humanitarian assistance.
  sources:
  - id: source_1
    license: null
    name: INFORM Model (OCHA)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Regional Inter-Agency Standing Committee (IASC) Task Force for Caucasus
      and Central Asia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/subnational-inform-caucasus-and-central-asia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Humanitarian crisis risk and need for international assistance derived
      from multi-hazard INFORM model
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Humanitarian crisis risk and need for international assistance derived
      from multi-hazard INFORM model
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
  - asset_category: population
    asset_dimension: population
    description: Humanitarian crisis risk and need for international assistance derived
      from multi-hazard INFORM model
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Subnational INFORM - Caucasus and Central Asia (Subnational INFORM
    results for 2017, Caucasus and Central Asia)
  download_url: https://data.humdata.org/dataset/a1875850-ebb6-485c-aa03-37a0ff36f66c/resource/387bbc01-ea4d-4c74-acc0-8be755688a56/download/inform_cca_2017_v1.1.xlsx
  format: null
  id: resource_387bbc01
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_CCA_2017_v1.1.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'FOR VISUALIZATION PURPOSES OF INFORM RESULTS ONLY: geographical boundaries
    of first administrative units, Caucasus and Central Asia'
  download_url: https://data.humdata.org/dataset/a1875850-ebb6-485c-aa03-37a0ff36f66c/resource/b3183686-c7cc-4d9c-a323-b239a5f94ea0/download/cca-admin1-shapefile.zip
  format: null
  id: resource_b3183686
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CCA admin1 shapefile.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ocharocca_subnationalinformcaucasus_20161231
spatial:
  bbox: null
  centroid: null
  countries:
  - AZE
  - ARM
  - GEO
  - KAZ
  - KGZ
  - TJK
  - TKM
  - UZB
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-12-31'
temporal_resolution: null
title: Subnational INFORM - Caucasus and Central Asia
version: null
vulnerability: null
---
