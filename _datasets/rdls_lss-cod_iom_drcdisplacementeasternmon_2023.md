---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/drc-displacement-eastern-monitoring-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-eastern-monitoring-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-eastern-monitoring-baseline-assessment-iom-dtm
dataset_id: rdls_lss-cod_iom_drcdisplacementeasternmon_2023
description: 'This dataset presents compiled data from the most recent round of DTM
  DRC''s mobility tracking assessments, currently conducted in the provinces of Ituri,
  North Kivu, South Kivu, and Tanganyika.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/drc-displacement-eastern-monitoring-baseline-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM collected displacement and mobility data through standardized
    key informant interviews and community assessments across Ituri, North Kivu, South
    Kivu, and Tanganyika provinces. Data were compiled into mobility tracking atlases
    documenting IDP populations in host families, CCCM-covered sites, and spontaneous
    sites, as well as returnee populations, disaggregated by households and individuals
    at administrative division 2 level.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/drc-displacement-eastern-monitoring-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (households and individuals) from conflict-driven
      displacement in eastern DRC provinces
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
  - asset_category: population
    asset_dimension: population
    description: Returnee populations (households and individuals) who have returned
      within 36-month period in eastern DRC
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
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In the four eastern provinces of the DRC, comprising Ituri, North Kivu,
    South Kivu, and Tanganyika, during this assessment DTM identified 5,647,465 internally
    displaced people (IDPs) and 3,525,590 returnees, present in 71 percent of assessed
    villages. DTM estimates that the highest proportion (45%) of IDPs (2,561,136 individuals)
    are hosted in North Kivu, followed by 25 percent (1,395,604) in South Kivu, 24
    percent (1,360,577) in Ituri and 6 percent (330,148) in Tanganyika. The most frequently
    reported reasons for displacement among displaced populations living in host families
    are attacks by armed groups (87%), inter-community conflict (10%) and natural
    disasters (3%). An estimated 2,026,086 individuals were displaced by the M23 crisis
    at the time of the most recently produced DTM crisis analysis.
  download_url: https://data.humdata.org/dataset/69c01da6-e999-41d2-9529-e8f3941246c7/resource/a09bfd93-ead3-497d-9214-804a2d2a37d7/download/20240827_atlas_mt_2024_r1_cl.xlsx
  format: null
  id: resource_a09bfd93
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DRC - Mobility Tracking Atlas - Round 4 - April 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset presents compiled data from the most recent round of DTM
    DRC's mobility tracking assessments, currently conducted in the provinces of Ituri,
    North Kivu, South Kivu, and Tanganyika.
  download_url: https://data.humdata.org/dataset/69c01da6-e999-41d2-9529-e8f3941246c7/resource/60bd6057-4df7-462a-9712-900c3d75d39e/download/dtm_drc_disp_atlas_r2_2023_db_public_20231106.xlsx
  format: null
  id: resource_60bd6057
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DRC - Mobility Tracking Atlas - Round 3 - October 2023
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_iom_drcdisplacementeasternmon_2023
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
  end: '2024-05-20'
  start: '2023-08-03'
temporal_resolution: null
title: DRC Displacement - Eastern Monitoring - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
