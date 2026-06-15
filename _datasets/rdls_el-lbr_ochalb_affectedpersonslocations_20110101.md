---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations High Commissioner for Refugees (UNHCR) Liberia
    url: https://data.humdata.org/dataset/liberia-affected-persons-locations
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Liberia (inactive)
  url: https://data.humdata.org/dataset/liberia-affected-persons-locations
creator:
  affiliation: null
  email: null
  name: OCHA Liberia (inactive)
  url: https://data.humdata.org/dataset/liberia-affected-persons-locations
dataset_id: rdls_el-lbr_ochalb_affectedpersonslocations_20110101
description: 'Ivorian Refugees location in Liberia in 2011 The file was given to OCHA
  on July 2011 by UNHCR Liberia and represents ivorian refugees location in Liberia
  and host community. The typology (refugees in camp or hosted), geographic coordinates
  and the ratio was indicated.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/liberia-affected-persons-locations]'
details: '**Most Recent Changes:** (2014-11-18) metadata updated **Languages:** EN'
exposure:
- asset_type:
    description: Ivorian refugee and host community populations with geographic locations
      and settlement typology
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNHCR Liberia compiled refugee registration data in July 2011 documenting
    Ivorian refugee locations across Liberia, including camp-based and host community
    settlements with geographic coordinates and population ratios. The dataset represents
    post-displacement population distribution used for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations High Commissioner for Refugees (UNHCR) Liberia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/liberia-affected-persons-locations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Ivorian refugee displacement from conflict in C\xC3\xB4te d'Ivoire,\
      \ located in Liberia"
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
  description: Liberia - Affected Persons Locations (Excel)
  download_url: https://data.humdata.org/dataset/6a57dc3f-e0c2-4cb0-be74-38790375ac06/resource/8201cc03-86dc-40e6-824a-c3fbabf42243/download/refugees_location.xls
  format: null
  id: resource_8201cc03
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: refugees_location.xls
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-lbr_ochalb_affectedpersonslocations_20110101
spatial:
  bbox: null
  centroid: null
  countries:
  - LBR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2011-01-01'
temporal_resolution: null
title: Liberia - Affected Persons Locations
version: null
vulnerability: null
---
