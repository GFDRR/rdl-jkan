---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/drc-displacement-data-kasai-central-province-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-data-kasai-central-province-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-data-kasai-central-province-baseline-assessment-iom-dtm
dataset_id: rdls_lss-cod_iom_drcdisplacementdatakasaic_202012
description: 'The dataset contains number of people displaced and returnees at village
  level in Kasai Central province. The dataset also contains needs of the displaced
  and returned people, reason and time of displacement.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/drc-displacement-data-kasai-central-province-baseline-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted baseline assessments at village level in Kasai Central
    Province across multiple rounds (Sep2017-Dec2020) using standardized DTM methodology
    to enumerate internally displaced persons, returnees from Angola and other areas,
    and associated humanitarian needs. Data aggregated by administrative units (province,
    territoire, health zone) with population coverage metrics.
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
- href: https://data.humdata.org/dataset/drc-displacement-data-kasai-central-province-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict in Kasai Central Province
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
    description: Returnees from Angola and other areas in Kasai Central Province
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Central Province - Baseline Assessment
    [IOM DTM] (DTM DRC BA Kasai Central Dec2020 R7)
  download_url: https://data.humdata.org/dataset/61d97b52-55f3-4553-b2fa-276dcac360f2/resource/62a5dbd5-ecd5-476e-8cfc-6225331e1377/download/hdx_oim_dtm_rdc_bd_mt_trd_kasai_centrale.xlsx
  format: null
  id: resource_62a5dbd5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Central Dec2020 R7
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Central Province - Baseline Assessment
    [IOM DTM] (DTM DRC BA Kasai Central Feb2019 R6)
  download_url: https://data.humdata.org/dataset/61d97b52-55f3-4553-b2fa-276dcac360f2/resource/1285f36a-616e-448e-b912-d2fa117393f9/download/dtm-drc-ba-kasai-central-feb2019-r6.xlsx
  format: null
  id: resource_1285f36a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Central Feb2019 R6
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Central Province - Baseline Assessment
    [IOM DTM] (DTM DRC BA Kasai Central Nov2018 R5)
  download_url: https://data.humdata.org/dataset/61d97b52-55f3-4553-b2fa-276dcac360f2/resource/74293a91-010a-4d09-8c2a-00549b1ec4ce/download/dtm-drc-ba-kasai-central-nov2018-r5.xlsx
  format: null
  id: resource_74293a91
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Central Nov2018 R5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Central Province - Baseline Assessment
    [IOM DTM] (DTM DRC BA Kasai Central Jul2018 R4)
  download_url: https://data.humdata.org/dataset/61d97b52-55f3-4553-b2fa-276dcac360f2/resource/2b702091-6596-45a0-819f-1303bc0e4d96/download/dtm-drc-ba-kasai-central-jul2018-r4.xlsx
  format: null
  id: resource_2b702091
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Central Jul2018 R4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Central Province - Baseline Assessment
    [IOM DTM] (DTM DRC BA Kasai Central Mar2018 R3)
  download_url: https://data.humdata.org/dataset/61d97b52-55f3-4553-b2fa-276dcac360f2/resource/e9545895-b50c-436d-87e8-78cc26abcb53/download/dtm-drc-ba-kasai-central-mar2018-r3.xlsx
  format: null
  id: resource_e9545895
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Central Mar2018 R3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Central Province - Baseline Assessment
    [IOM DTM] (DTM DRC BA Kasai Central Nov2017 R2)
  download_url: https://data.humdata.org/dataset/61d97b52-55f3-4553-b2fa-276dcac360f2/resource/f8dc4658-2fd3-4d1b-abf9-a692c7d133f4/download/dtm-drc-ba-kasai-central-nov2017-r2.xlsx
  format: null
  id: resource_f8dc4658
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Central Nov2017 R2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Central Province - Baseline Assessment
    [IOM DTM] (DTM DRC BA Kasai Central Sep2017 R1)
  download_url: https://data.humdata.org/dataset/61d97b52-55f3-4553-b2fa-276dcac360f2/resource/6a156466-ada1-4d7a-ae29-4d76deb5b70d/download/dtm-drc-ba-kasai-central-sep2017-r1.xlsx
  format: null
  id: resource_6a156466
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Central Sep2017 R1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_iom_drcdisplacementdatakasaic_202012
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
  end: '2020-12-31'
  start: '2020-12-01'
temporal_resolution: null
title: DRC Displacement Data - Kasai Central Province - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
