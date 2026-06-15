---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/nws-earthquake-rapid-needs-assessment
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/nws-earthquake-rapid-needs-assessment
dataset_id: rdls_el-syr_reach_northwestearthquakerapidn_20230213
description: 'The dataset contains community-level information from key informants
  (KIs) in 607 assessed communities across Greater Idleb and Northern Aleppo. The
  full survey was carried out in communities reporting direct earthquake impact (damage/service
  disruption) and/or arrival of new IDPs since the initial earthquake, with sections
  covering: 1) Population & Displacement, 2) CCCM, 3) Shelter damage & SNFI emergency
  needs, 4) Nutrition & Protection 5) Key Infrastructure Impacts & Service Access,
  6) Priority Needs and 7) Humanitarian Assistance. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/nws-earthquake-rapid-needs-assessment]'
details: 'Assessment carried out in collaboration with the NWS NGO Forum. Glide: EQ-2023-000015-TUR'
exposure:
- asset_type:
    description: Shelter infrastructure and damage status across 607 assessed communities
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Key infrastructure facilities and service access points in assessed
      communities
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Displaced populations and community demographics in affected areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Community-level data collected through key informant surveys in 607
    communities across Greater Idleb and Northern Aleppo that reported direct earthquake
    damage or new IDP arrivals. Survey sections covered population displacement, shelter
    damage, infrastructure impacts, and humanitarian needs. Data aggregated to provide
    rapid post-earthquake needs assessment for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nws-earthquake-rapid-needs-assessment
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct shelter damage and SNFI emergency needs from earthquake impact
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Service disruption and key infrastructure impacts from earthquake
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement and arrival of new IDPs following earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: North-West Syria - Earthquake Rapid Needs Assessment (Excel)
  download_url: https://data.humdata.org/dataset/fecb8b5c-a587-4b6e-a7cb-ca870e78f74a/resource/ead8a670-1d6f-4820-a770-653c6bede77d/download/reach_nws-ngo-forum_earthquake_rna_dataset_to-share.xlsx
  format: null
  id: resource_ead8a670
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_NWS-NGO-Forum_Earthquake_RNA_Dataset_to-share.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_reach_northwestearthquakerapidn_20230213
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-13'
temporal_resolution: null
title: North-West Syria - Earthquake Rapid Needs Assessment
version: null
vulnerability: null
---
