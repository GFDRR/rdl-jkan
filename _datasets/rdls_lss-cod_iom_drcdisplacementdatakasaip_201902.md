---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/drc-displacement-data-kasai-province-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-data-kasai-province-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/drc-displacement-data-kasai-province-baseline-assessment-iom-dtm
dataset_id: rdls_lss-cod_iom_drcdisplacementdatakasaip_201902
description: 'The dataset contains number of people displaced and returnees at village
  level in Kasai province. The dataset also contains needs of the displaced and returned
  people, reason and time of displacement.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/drc-displacement-data-kasai-province-baseline-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM baseline assessments conducted across multiple rounds (May
    2018 to February 2019) in Kasai Province using standardized DTM methodology to
    enumerate displaced and returned populations at village level, document displacement
    reasons and timing, and assess humanitarian needs.
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
- href: https://data.humdata.org/dataset/drc-displacement-data-kasai-province-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displacement counts of affected population in Kasai Province
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
    description: Returnee population counts in Kasai Province
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
  description: DRC Displacement Data - Kasai Province - Baseline Assessment [IOM DTM]
    (DTM DRC BA Kasai Feb2019 R4)
  download_url: https://data.humdata.org/dataset/d014687b-b1d6-4964-a0c1-c13e8469c48c/resource/688d02d1-8b57-49e2-a838-bfc571eb3708/download/dtm-drc-ba-kasai-feb2019-r4.xlsx
  format: null
  id: resource_688d02d1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Feb2019 R4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Province - Baseline Assessment [IOM DTM]
    (DTM DRC BA Kasai Nov2018 R3)
  download_url: https://data.humdata.org/dataset/d014687b-b1d6-4964-a0c1-c13e8469c48c/resource/06bc01ff-5d35-486a-8225-5cf62792c035/download/dtm-drc-ba-kasai-nov2018-r3.xlsx
  format: null
  id: resource_06bc01ff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Nov2018 R3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Province - Baseline Assessment [IOM DTM]
    (DTM DRC BA Kasai Jul2018 R2)
  download_url: https://data.humdata.org/dataset/d014687b-b1d6-4964-a0c1-c13e8469c48c/resource/62deb054-bac6-4b2a-b076-f40bc5f49834/download/dtm-drc-ba-kasai-jul2018-r2.xlsx
  format: null
  id: resource_62deb054
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai Jul2018 R2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DRC Displacement Data - Kasai Province - Baseline Assessment [IOM DTM]
    (DTM DRC BA Kasai May2018 R1)
  download_url: https://data.humdata.org/dataset/d014687b-b1d6-4964-a0c1-c13e8469c48c/resource/557fbcac-1db7-472a-acd0-cd235651773f/download/dtm-drc-ba-kasai-may2018-r1.xlsx
  format: null
  id: resource_557fbcac
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM DRC BA Kasai May2018 R1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_iom_drcdisplacementdatakasaip_201902
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
  end: '2019-02-19'
  start: '2019-02-01'
temporal_resolution: null
title: DRC Displacement Data - Kasai Province - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
