---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/humanitarian-response-plan-2015-need-index
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/humanitarian-response-plan-2015-need-index
dataset_id: rdls_lss-afg_ochaafg_2015humanitarianresponsep_2011
description: 'The dataset includes the provincial level indicators, index scores and
  caseloads of the need and vulnerability analysis carried out for the Afghanistan
  2015 Humanitarian Response Plan. The full methodology and detailed data can be downloaded
  via the following URL: https://www.humanitarianresponse.info/operations/afghanistan/document/onvi-guidance-note-afghanistan-hrp-2015.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/humanitarian-response-plan-2015-need-index]'
details: This data must be interpreted and used in accordance with the Afghanistan
  2015 Humanitarian Response Plan (HRP) and the Overall Need and Vulnerability Index
  (ONVI) Guidance Note. Publication of this data is subject to the approval of the
  data provider (source).
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Provincial-level vulnerability and needs indicators were compiled from
    multiple sources through sample survey methodology and aggregated into composite
    index scores and caseloads to inform the 2015 Afghanistan Humanitarian Response
    Plan prioritization.
  sources:
  - id: source_1
    license: null
    name: OCHA Afghanistan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/humanitarian-response-plan-2015-need-index
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population vulnerability and humanitarian needs assessment from drought
      and food insecurity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  description: Expanded metadata and description of the analysis process are provided
    in the attached guidance note.
  download_url: https://data.humdata.org/dataset/0a581d61-5cca-432e-838a-4edb64a74853/resource/4c32bdfa-9532-4c9e-a1c9-cbe864c518b7/download/afg-hrp2015-onvi-indicator-data-index-caseloads.xlsx
  format: null
  id: resource_4c32bdfa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ONVI Indicators, Index Scores and Caseloads - Afghanistan HRP 2015
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_2015humanitarianresponsep_2011
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2014-08-31'
  start: '2011-09-01'
temporal_resolution: null
title: Afghanistan 2015 Humanitarian Response Plan - Need & Vulnerability Index
version: null
vulnerability: null
---
