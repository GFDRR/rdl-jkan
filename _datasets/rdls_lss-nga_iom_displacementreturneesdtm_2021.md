---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/nigeria-displacements-returnees-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/nigeria-displacements-returnees-iom-dtm
dataset_id: rdls_lss-nga_iom_displacementreturneesdtm_2021
description: 'This dataset is the result of Displacement Tracking Matrix (DTM) assessments
  carried out by the International Organization for Migration (IOM), aims to improve
  the understanding of the scope of return movements in north-east Nigeria.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/nigeria-displacements-returnees-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM field assessments conducted across multiple rounds (Round 41
    and 43) in north-east Nigeria using standardized DTM methodology to track returnee
    populations, household counts, and geographic locations. Data collected through
    direct surveys at return locations with GPS coordinates and administrative hierarchies.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nigeria-displacements-returnees-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement and return movements tracked through DTM
      assessments in north-east Nigeria
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In Round 43, 2,100,180 returnees were recorded in the assessment. This
    number represents an increase of 117,050 individuals or more than six per cent
    compared to Round 41 when 1,983,130 returnees were recorded in June 2022.
  download_url: https://data.humdata.org/dataset/1a37c13c-59cb-42a6-a5e2-4c66f6dae580/resource/e5f334a8-23a6-4e4c-b08b-a48f3ffb3787/download/hdx_dtm_nigeria_r43_master_list_returnees_updated.xlsx
  format: null
  id: resource_e5f334a8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Nigeria Baseline Assessment Round 43
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In Round 41, 1,983,130 returnees were recorded in the assessment. This
    number represents an increase of 22,572 individuals or more than one per cent
    compared to Round 40 when 1,960,558 returnees were recorded in (March 2022).
  download_url: https://data.humdata.org/dataset/1a37c13c-59cb-42a6-a5e2-4c66f6dae580/resource/4cea97e7-d483-4979-a38d-1ecd8836ac17/download/hdx_nigeria_baseline_assessement_r41.xlsx
  format: null
  id: resource_4cea97e7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Nigeria Baseline Assessment Round 41
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nga_iom_displacementreturneesdtm_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-11-09'
  start: '2021-01-05'
temporal_resolution: null
title: Nigeria Displacement - [Returnees] - [IOM DTM]
version: null
vulnerability: null
---
