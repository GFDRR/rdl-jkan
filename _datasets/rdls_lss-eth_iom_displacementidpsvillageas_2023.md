---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/ethiopia-displacement-northern-region-tigray-idps-village-assessment-survey-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/ethiopia-displacement-northern-region-tigray-idps-village-assessment-survey-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/ethiopia-displacement-northern-region-tigray-idps-village-assessment-survey-iom-dtm
dataset_id: rdls_lss-eth_iom_displacementidpsvillageas_2023
description: 'Ethiopia village assessment survey (VAS) is a sub-component of mobility
  tracking. It collects data on returning IDPs, IDPs, returned migrants and host community
  members. VAS evaluates the absorption capacity of villages to receive returning
  IDPs with a focus on accessibility of services, livelihoods and reintegration..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-displacement-northern-region-tigray-idps-village-assessment-survey-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted village assessment surveys (VAS) across Tigray region
    following standardized DTM methodology to track displacement and mobility patterns.
    Data collection involved enumeration of returning IDP households and individuals
    at village level, with documentation of displacement triggers (conflict, drought,
    climate), duration categories, and temporal arrival patterns to assess village
    reintegration capacity.
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
- href: https://data.humdata.org/dataset/ethiopia-displacement-northern-region-tigray-idps-village-assessment-survey-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returning IDPs with displacement
      duration and arrival timing
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
  url: https://displacement.iom.int/system/tdf/Methodological%20Framework%20used%20in%20DTM%20Operations%20for%20Quantifying%20Displacement%20and%20Mobility.pdf?file=1&type=node&id=2389
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In Tigray village assessment survey round 16, 963 villages were covered.
    1,256,297 returning IDPs and 296,229 returning IDP households were identified.
  download_url: https://data.humdata.org/dataset/19d2f36c-6425-4676-b4b0-875c4a253c1b/resource/878e400c-17ad-4806-b755-b1aa983ad8a2/download/dtm-ethiopia-tigray-region-village-assessment-survey-round-16-april-june-2023_new.xlsx
  format: null
  id: resource_878e400c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Ethiopia - VAS - Tigray - R16
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_iom_displacementidpsvillageas_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-06-29'
  start: '2023-04-27'
temporal_resolution: null
title: Ethiopia Displacement - [IDPs] - Village Assessment Survey - Tigray - [IOM
  DTM]
version: null
vulnerability: null
---
