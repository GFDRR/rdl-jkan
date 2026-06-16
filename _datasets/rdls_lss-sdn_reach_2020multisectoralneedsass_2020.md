---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/2020-multi-sectoral-needs-assessment-analysis-results-of-household-data-sudan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/2020-multi-sectoral-needs-assessment-analysis-results-of-household-data-sudan
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/2020-multi-sectoral-needs-assessment-analysis-results-of-household-data-sudan
dataset_id: rdls_lss-sdn_reach_2020multisectoralneedsass_2020
description: 'This inaugural round of Sudan''s Multi-Sector Needs Assessment (MSNA),
  conducted by REACH and OCHA in close collaboration with the Inter-Sectoral Coordination
  Group (ISCG), seeks to understand multi-sectoral priority humanitarian needs of
  populations across the whole of Sudan. The findings from this assessment are presented
  in this document and are intended to provide timely updates on key sectoral needs
  and priorities in order to inform humanitarian response and strategic programming
  for non-displaced, IDP and refugee households across the country.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/2020-multi-sectoral-needs-assessment-analysis-results-of-household-data-sudan]'
details: More information on the methodology can be found in the readme (first sheet
  of the spreadsheet).
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Household survey data collected by REACH and OCHA across Sudan to assess
    multi-sectoral humanitarian needs of non-displaced, IDP, and refugee populations.
    Analysis results synthesize priority needs across sectors to inform humanitarian
    response programming and strategic planning.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2020-multi-sectoral-needs-assessment-analysis-results-of-household-data-sudan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sectoral humanitarian needs assessment capturing population
      affected by flooding and other crises
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
        metric: exposure
        modelling: observed
        type: total
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
  description: 2020 Multi-Sectoral Needs Assessment, Analysis results of household
    data, Sudan (Excel)
  download_url: https://data.humdata.org/dataset/25b3977b-add7-4ce9-b632-feac44c1b7e2/resource/9c812a9a-c912-4fb5-9336-fbc6f04f2eac/download/reach_sdn_analysis_msna2020hhdata_january2021.xlsx
  format: null
  id: resource_9c812a9a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_SDN_Analysis_MSNA2020HHdata_January2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_reach_2020multisectoralneedsass_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-11-26'
  start: '2020-08-16'
temporal_resolution: null
title: 2020 Multi-Sectoral Needs Assessment, Analysis results of household data, Sudan
version: null
vulnerability: null
---
