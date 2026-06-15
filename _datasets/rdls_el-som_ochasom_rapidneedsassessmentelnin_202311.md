---
attributions:
- entity:
    affiliation: null
    email: null
    name: REACH
    url: https://data.humdata.org/dataset/reach_som_clean-dataset-baardheere_rna-flooding_november-2023-xlsx
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Inter-Cluster Coordination Group (ICCG)
    url: https://data.humdata.org/dataset/reach_som_clean-dataset-baardheere_rna-flooding_november-2023-xlsx
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/reach_som_clean-dataset-baardheere_rna-flooding_november-2023-xlsx
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/reach_som_clean-dataset-baardheere_rna-flooding_november-2023-xlsx
dataset_id: rdls_el-som_ochasom_rapidneedsassessmentelnin_202311
description: 'Baardheere district in Jubaland State also experienced extreme flash
  flooding in March 2023, which caused 14 deaths, displaced thousands, and destroyed
  property. The Inter-Cluster Coordination Group (ICCG) emergency response and preparedness
  plan anticipated that this cycle of flooding will affect nearly 400,000 - 500,000
  people in Jowhar and Belet Weyne, and approximately 42,305 people in Baardheere.
  REACH''s rapid needs assessment of key informants (KIs) in Belet Weyne and Baardheere
  districts focuses on locations with high influx of displaced people evacuating their
  flooded communities, aiming to cover all evacuation sites with affected populations,
  dependent on accessibility.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/reach_som_clean-dataset-baardheere_rna-flooding_november-2023-xlsx]'
details: null
exposure:
- asset_type:
    description: "Displaced and host populations in Baardheere and Belet Weyne districts\
      \ affected by El Ni\xF1o flooding"
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
    description: Shelter types occupied by flood-affected households including solid
      buildings, makeshift shelters, and open-air arrangements
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Post-event rapid needs assessment data collected via key informant\
    \ interviews in November 2023 in Baardheere and Belet Weyne districts following\
    \ March 2023 El Ni\xF1o-induced flooding. Survey methodology captured displacement\
    \ status, population demographics, shelter conditions, and humanitarian needs\
    \ across host communities and IDP settlements. Data was compiled and cleaned by\
    \ REACH in coordination with OCHA Somalia and humanitarian partners to inform\
    \ response strategy and resource allocation."
  sources:
  - id: source_1
    license: null
    name: REACH
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Inter-Cluster Coordination Group (ICCG)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/reach_som_clean-dataset-baardheere_rna-flooding_november-2023-xlsx
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Direct fatalities from El Ni\xF1o flooding in Baardheere district\
      \ (14 deaths recorded)"
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement from flood-affected communities in Baardheere
      and Belet Weyne districts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: buildings
    asset_dimension: structure
    description: "Property destruction from El Ni\xF1o flooding in assessed locations"
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
        metric: loss
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
  description: Somalia - Rapid Needs Assessment for El Nino Flooding in Baardheere
    District (Excel)
  download_url: https://data.humdata.org/dataset/e855c8d8-93c8-4a86-a2c6-3bd9dc10b8b1/resource/b44d3aba-c2c1-4a06-a841-9e69b78df55c/download/02.-reach_som_clean-dataset-baardheere_rna-flooding_november-2023.xlsx
  format: null
  id: resource_b44d3aba
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 02. REACH_SOM_Clean-dataset-Baardheere_RNA-Flooding_November-2023.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_ochasom_rapidneedsassessmentelnin_202311
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-11-30'
  start: '2023-11-01'
temporal_resolution: null
title: Somalia - Rapid Needs Assessment for El Nino Flooding in Baardheere District
version: null
vulnerability: null
---
