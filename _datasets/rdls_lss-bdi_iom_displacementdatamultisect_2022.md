---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burundi-displacement-data-multi-sectoral-location-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/burundi-displacement-data-multi-sectoral-location-assessment-iom-dtm
dataset_id: rdls_lss-bdi_iom_displacementdatamultisect_2022
description: 'The dataset aims to collect data on population presence, living conditions
  and needs in a particular displacement location or community.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/burundi-displacement-data-multi-sectoral-location-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted repeated multi-sectoral location assessments (4 rounds)
    across Burundi displacement sites using standardized key informant interview methodology.
    Data collection captured internally displaced population counts disaggregated
    by age and gender, displacement reasons (natural disasters, socio-political, other),
    and arrival periods. The dataset documents post-displacement impact on populations
    across multiple assessment rounds from 2013-2024.
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
- href: https://data.humdata.org/dataset/burundi-displacement-data-multi-sectoral-location-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood and natural disaster events
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
    description: Population affected by natural disasters in displacement locations
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
  url: https://displacement.iom.int/sites/default/files/public/Methodological%20Framework%20used%20in%20DTM%20Operations%20for%20Quantifying%20Displacement%20and%20Mobility.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The DTM identified 102,824 internally displaced persons (IDPs) in 21,979
    displaced households in Burundi in May 2024. Of those identified, 93% were displaced
    due to disasters and climate change while 7% were the result of other reasons.
  download_url: https://data.humdata.org/dataset/d54f46a8-03f8-4678-8ed2-94c14fda5fe0/resource/393ef733-589a-41f7-bde1-3dc1a05380d1/download/v2_dtm_burundi_msla-datasets_may_2024_public_hdx.xlsx
  format: null
  id: resource_393ef733
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Multi Sectoral Location Assessment Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM identified 76,987 Internally Displaced Persons (IDPs) in 17,819
    displaced households in the 18 provinces of Burundi during the month of May 2023.
    Among those identified, 89 per cent were displaced due to environment-related
    disasters while 11 per cent were a result of other reasons. A little more than
    half (54%) of IDPs are children, 18 years old and under.
  download_url: https://data.humdata.org/dataset/d54f46a8-03f8-4678-8ed2-94c14fda5fe0/resource/cbe79019-9c98-498c-bf2a-ea720cb4ebdd/download/dtm_burundi_dataset_msla_kii_mai_2023_brutes_public-hdx.xlsx
  format: null
  id: resource_cbe79019
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Multi Sectoral Location Assessment Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: As of October 2022, the main cause of displacement was natural disasters
    (89%). Most IDPs (46%) were hosted in the provinces of Rumonge (19%), Cibitoke
    (14%), and Cankuzo (13%). Even though natural disasters were the main displacement
    reason, a considerable share of IDPs in the provinces of Mwaro (56%), Ruyigi (36%),
    Bujumbura Mairie (28%), Gitega (27%) and Muyinga (27%) were displaced due to other
    reasons.
  download_url: https://data.humdata.org/dataset/d54f46a8-03f8-4678-8ed2-94c14fda5fe0/resource/11d6d4ea-7ac8-48ea-8530-6357594e20d6/download/r2_dtm_burundi_fiche_colline_msla_kii_october_2022_brute_public-hdx.xlsx
  format: null
  id: resource_11d6d4ea
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Multi Sectoral Location Assessment Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM identified 84,791 Internally Displaced Persons (IDPs) in 19,407
    displaced households in the 18 provinces of Burundi during the month of April
    2022. Among those identified, 91 per cent were displaced due to environment-related
    disasters while nine per cent were a result of other reasons. A little more than
    half (56%) of IDPs are children, 18 years old and under. The number of IDPs Individuals
    and Households in this summary are from the latest Baseline Assessment report
    (https://displacement.iom.int/reports/burundi-internal-displacement-dashboard-april-2022?close=true)
  download_url: https://data.humdata.org/dataset/d54f46a8-03f8-4678-8ed2-94c14fda5fe0/resource/c21acc48-af77-4b16-bf6e-de8c76957b79/download/r1_hdx_dtm_burundi_msla_data_avril2022_to_be_shared.xlsx
  format: null
  id: resource_c21acc48
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Burundi Multi Sectoral Location Assessment Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bdi_iom_displacementdatamultisect_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-05-17'
  start: '2022-04-11'
temporal_resolution: null
title: Burundi Displacement Data - Multi Sectoral Location Assessment [IOM DTM]
version: null
vulnerability: null
---
