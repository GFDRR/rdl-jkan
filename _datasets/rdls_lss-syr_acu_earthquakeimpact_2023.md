---
attributions:
- entity:
    affiliation: null
    email: null
    name: Assistance Coordination Unit (ACU)
    url: https://data.humdata.org/dataset/syria-earthquake-impact
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/syria-earthquake-impact
creator:
  affiliation: null
  email: null
  name: Assistance Coordination Unit
  url: https://data.humdata.org/dataset/syria-earthquake-impact
dataset_id: rdls_lss-syr_acu_earthquakeimpact_2023
description: 'On February 6, 2023, at dawn, a strong earthquake hit southern Turkey
  and northern Syria with a magnitude of 7.8 on the Richter scale, resulting in thousands
  of casualties and thousands of injured in Turkey and North-West Syria. The Assistance
  Coordination Unit (ACU), through its field team network represented by the following
  departments: Early Warning Alert and Response Network, WASH, Polio Team, Immunization
  Program, Information Management Unit, DPU, and M&E conducted a needs and damage
  assessment following the devastating earthquake.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/syria-earthquake-impact]'
details: 'Glide: EQ-2023-000015-TUR'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event damage and needs assessment data collected through direct
    field observations by the Assistance Coordination Unit's multi-departmental team
    network in northwest Syria following the February 6, 2023 magnitude 7.8 earthquake.
    Data includes casualty figures, injury counts, affected population estimates,
    and shelter-related impact records compiled from ground-truth assessments.
  sources:
  - id: source_1
    license: null
    name: Assistance Coordination Unit (ACU)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/syria-earthquake-impact
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct casualties from earthquake impact in Syria
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Direct injuries from earthquake impact in Syria
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
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake impact in Syria
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Affected population from earthquake impact in Syria
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_4
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Syria: Earthquake Impact (Syria Earthquake Impact 20 March 2023.xlsx)'
  download_url: https://data.humdata.org/dataset/a42fc77f-e0a9-4412-857f-18ec11cd4a80/resource/8bc69c39-4a65-4abf-9437-6d8bd7b21cb6/download/syria-earthquake-impact-20-march-2023.xlsx
  format: null
  id: resource_8bc69c39
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Syria Earthquake Impact 20 March 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Syria: Earthquake Impact (Shelters Dataset 20 March 2023.xlsx)'
  download_url: https://data.humdata.org/dataset/a42fc77f-e0a9-4412-857f-18ec11cd4a80/resource/dd8476e8-e127-4851-925f-e4ca3cb90070/download/shelters-dataset-20-march-2023.xlsx
  format: null
  id: resource_dd8476e8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Shelters Dataset 20 March 2023.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_acu_earthquakeimpact_2023
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
  end: '2023-03-20'
  start: '2023-02-15'
temporal_resolution: null
title: 'Syria: Earthquake Impact'
version: null
vulnerability: null
---
