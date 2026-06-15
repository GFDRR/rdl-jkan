---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/drc-displacement-countrywide-monitoring-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-countrywide-monitoring-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-countrywide-monitoring-baseline-assessment-iom-dtm
dataset_id: rdls_lss-cod_iom_drcdisplacementcountrywid_2023
description: 'The Democratic Republic of the Congo (DRC) has a complex internal displacement
  situation with a diverse set of drivers and impacts. In the country''s eastern provinces,
  armed conflict and insecurity have long been the primary drivers of the large-scale
  protracted displacement that the region experiences. This has been compounded, since
  mid-2022, by a resurgence in armed group activity in the provinces of North Kivu
  and Ituri leading to internal unrest, regional instability, and widespread acute
  displacement. On top of the large-scale humanitarian crisis in the east of the country,
  other regions of the DRC have experienced conflict, insecurity, and disasters such
  as floods and landslides. A complete understanding of the displacement situation
  across the entire DRC is vital to inform both near-term humanitarian assistance,
  as well as engaging a wider array of stakeholders involved in long-term programming.
  The Displacement Tracking Matrix (DTM) is IOM''s system for collecting and analysing
  primary data concerning population movement and has been deployed over 90 humanitarian
  operations globally. DTM has conducted large-scale population mobility monitoring
  in the country''s eastern part since 2018.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/drc-displacement-countrywide-monitoring-baseline-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM collected displacement baseline data through countrywide monitoring
    across multiple rounds (2023-2025) using standardized methodology applied at health
    zone and province administrative levels. Data captures internally displaced individuals
    disaggregated by displacement driver (conflict, natural disasters, epidemics,
    other reasons) and settlement location (host communities, CCCM-covered sites,
    spontaneous sites), with returnee populations tracked over 18-month periods. The
    dataset serves as a foundational loss assessment for understanding protracted
    displacement dynamics in DRC.
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
- href: https://data.humdata.org/dataset/drc-displacement-countrywide-monitoring-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from armed conflict and insecurity
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
    description: Internally displaced persons from natural disasters including flooding
      and landslides
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from natural disasters including flooding
      and landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: 'DTM DRC found a total of 4,915,515 IDPs across the country, including
    3,511,295 in the eastern region. By province, there are: 903,282 displaced individuals
    in Ituri (26% of IDPs in the region, or 18% nationally); 1,152,383 displaced individuals
    in North Kivu (33% of IDPs regionally, or 23% nationally); 1,201,673 displaced
    individuals in South Kivu (34% of IDPs regionally, or 24% nationally); 253,957
    displaced individuals in Tanganyika (7% of IDPs regionally, or 5% nationally).'
  download_url: https://data.humdata.org/dataset/e29a8f6f-94b5-4182-a028-f5b09c21668f/resource/041a1926-6369-486e-8665-320ea0752b17/download/20251015_iom_dtm_drc_national_overview_update_oct2025_3_hdx.xlsx
  format: null
  id: resource_041a1926
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Baseline Assessment - Countrywide Displacement Overview 2025 - Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "DTM DRC found a total of 5,039,256 IDPs across the country's eastern\
    \ region. By province, there are: 903,282 displaced individuals in Ituri (25%\
    \ of IDPs in the region, or 18% nationally); 1,011,335 displaced individuals in\
    \ North Kivu (28% of IDPs in the region, or 20% nationally); 1,466,462 displaced\
    \ individuals in South Kivu (40% of IDPs in the region, or 29% nationally); 253,957\
    \ displaced individuals in Tanganyika (7% of IDPs in the region, or 5% nationally).\
    \ DTM DRC found a total of 201,787 returnees across the country's western region.\
    \ By province, there are: 97,118 returnees in Ma\u221A\xD8-Ndombe (48% of returnees\
    \ in the region, or 2% nationally); 66,818 returnees in Kinshasa (33% of returnees\
    \ in the region, or 1% nationally); 21,220 returnees in Kwilu (11% of returnees\
    \ in the region, or <1% nationally); 16,631 returnees in Kwango (8% of returnees\
    \ in the region, or <1% of nationally)."
  download_url: https://data.humdata.org/dataset/e29a8f6f-94b5-4182-a028-f5b09c21668f/resource/904bd740-dd10-4a88-850e-d1f95b450257/download/drc_national_overview_2025_final_v2_hdx.xlsx
  format: null
  id: resource_904bd740
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Baseline Assessment - Countrywide Displacement Overview 2025 - Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset provides an updated country-level displacement overview
    in the DRC and combines data from targeted Mobility Tracking (MT) in the country's
    four eastern provinces (conducted between July and August 2024) as well as from
    a separate exercise (known as MT light), covering the remaining 22 provinces,
    for which data was collected between June and July 2024. A total number of 6,917,478
    internally displaced persons (IDPs) and 5,433,548 internal returnees were reported.
  download_url: https://data.humdata.org/dataset/e29a8f6f-94b5-4182-a028-f5b09c21668f/resource/e40ef081-07c8-4e39-aa8e-88a55adab3d2/download/dtm_drc_nationaldisplacementoverview_sep24_hxl.xlsx
  format: null
  id: resource_e40ef081
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Baseline Assessment - Countrywide Displacement Overview 2024 - Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset represents the first country level displacement overview
    produced by DTM in the DRC and combines data from conventional Mobility Tracking
    (MT) in the country's four east provinces (conducted between August and September
    2023) as well as from a new exercise launched covering the remaining 22 provinces
    for which data was collected in May and June 2023.
  download_url: https://data.humdata.org/dataset/e29a8f6f-94b5-4182-a028-f5b09c21668f/resource/fa72f791-d515-4be7-b355-dbb0cfa3572f/download/hdx_dtm_drc_db_public_nationaldisplacementover-copy.xlsx
  format: null
  id: resource_fa72f791
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Baseline Assessment - Countrywide Displacement Overview 2023 - Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_iom_drcdisplacementcountrywid_2023
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
  end: '2025-09-30'
  start: '2023-08-01'
temporal_resolution: null
title: DRC Displacement - Countrywide Monitoring - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
