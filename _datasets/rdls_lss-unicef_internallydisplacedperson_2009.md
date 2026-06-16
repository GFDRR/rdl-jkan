---
attributions:
- entity:
    affiliation: null
    email: null
    name: Multiple Indicator Cluster Surveys (MICS)
    url: https://data.humdata.org/dataset/unicef-mg-internal-disp-pers
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Demographic and Health Surveys (DHS)
    url: https://data.humdata.org/dataset/unicef-mg-internal-disp-pers
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations organizations administrative sources
    url: https://data.humdata.org/dataset/unicef-mg-internal-disp-pers
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Data and Analytics (HQ)
  url: https://data.humdata.org/dataset/unicef-mg-internal-disp-pers
creator:
  affiliation: null
  email: null
  name: UNICEF Data and Analytics (HQ)
  url: https://data.humdata.org/dataset/unicef-mg-internal-disp-pers
dataset_id: rdls_lss-unicef_internallydisplacedperson_2009
description: 'Internally displaced persons are persons or groups of persons who have
  been forced or obliged to flee or to leave their homes or places of habitual residence,
  in particular as a result of or in order to avoid the effects of armed conflict,
  situations of generalized violence, violations of human rights or natural or human-made
  disasters, and who have not crossed an internationally recognized State border.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unicef-mg-internal-disp-pers]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The dataset aggregates internally displaced persons estimates from
    inter-agency sources, nationally representative household surveys (MICS and DHS),
    and UN administrative records. Data are compiled and standardized by UNICEF Data
    and Analytics to provide global indicators of displacement resulting from armed
    conflict, violence, human rights violations, and natural disasters.
  sources:
  - id: source_1
    license: null
    name: Multiple Indicator Cluster Surveys (MICS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Demographic and Health Surveys (DHS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: United Nations organizations administrative sources
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unicef-mg-internal-disp-pers
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from natural disasters including floods
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from natural disasters including earthquakes
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
purpose: Please consult (see referenced_by) or email data@unicef.org
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.unicef.org
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Internally displaced persons (.MG_INTERNAL_DISP_PERS..?format=csv)
  download_url: https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,MG,1.0/.MG_INTERNAL_DISP_PERS..?format=csv
  format: null
  id: resource_358b9605
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Internally displaced persons (CSV)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Internally displaced persons
  download_url: https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/UNICEF,MG,1.0/.MG_INTERNAL_DISP_PERS..
  format: null
  id: resource_0b5b1d53
  media_type: application/xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Internally displaced persons (XML)
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-unicef_internallydisplacedperson_2009
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2009-01-01'
temporal_resolution: null
title: Internally displaced persons
version: null
vulnerability: null
---
