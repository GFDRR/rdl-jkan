---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter-Agency Standing Committee (IASC)
    url: https://data.humdata.org/dataset/informcaucus
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Commission
    url: https://data.humdata.org/dataset/informcaucus
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/informcaucus
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/informcaucus
dataset_id: rdls_el-inform_centralasiacaucasus
description: 'The sub national INFORM model for Caucasus and Central Asia was initiated
  by the Regional Inter-Agency Standing Committee (IASC) Task Force for Caucasus and
  Central Asia and is managed by OCHA. The INFORM model is being used to support coordinated
  preparedness actions. Partners hope to use the model to improve cooperation between
  humanitarian and development actors in managing risk and building resilience across
  the region.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/informcaucus]'
details: null
exposure:
- asset_type:
    description: Population exposed to natural hazards including earthquakes, landslides,
      floods, and droughts
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
- asset_type:
    description: Agricultural areas exposed to drought hazards
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The INFORM model integrates multi-source hazard exposure data (earthquake
    MMI, landslide intensity, flood extent, drought probability), vulnerability indicators
    (human development, poverty, conflict), and coping capacity metrics (aid, governance,
    health) at subnational administrative levels. Data from IASC and European Commission
    are processed through the INFORM risk framework to generate composite risk indices
    for preparedness and resilience planning across Caucasus and Central Asia.
  sources:
  - id: source_1
    license: null
    name: Inter-Agency Standing Committee (IASC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: European Commission
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/informcaucus
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquakes at MMI V and higher intensity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
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
    description: Population affected by medium and high intensity landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
    description: Population affected by floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  - asset_category: agriculture
    asset_dimension: product
    description: People affected by droughts in agricultural regions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://bit.ly/2MB0ZIj
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Central Asia and Caucasus (Excel)
  download_url: https://data.humdata.org/dataset/b5761f1f-a72e-4631-ad40-92d89e8b1922/resource/63ac42e8-302a-46c9-97a3-8fe58652e035/download/inform_cca_2021_30092021.xlsx
  format: null
  id: resource_63ac42e8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_CCA_2021_30092021.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-inform_centralasiacaucasus
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
temporal: null
temporal_resolution: null
title: INFORM Central Asia and Caucasus
version: null
vulnerability: null
---
