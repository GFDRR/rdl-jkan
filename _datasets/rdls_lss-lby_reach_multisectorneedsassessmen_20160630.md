---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/libya-multi-sector-needs-assessment-update-june-2016
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/libya-multi-sector-needs-assessment-update-june-2016
dataset_id: rdls_lss-lby_reach_multisectorneedsassessmen_20160630
description: 'In June 2016, a third round of the MSNA updates was initiated by REACH,
  supported by ECHO, following the February 2016 update to the MSNA baseline. This
  assessment draws on community level data, collected from ''People with Knowledge''
  (PwK). Findings indicate that the situation of some population groups remains challenging,
  with prevalent threats to personal safety and security reported in certain locations
  in addition to unaffordable basic needs, weakened WASH infrastructure, and restricted
  access to livelihoods and liquidity in some areas.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/libya-multi-sector-needs-assessment-update-june-2016]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Community-level data collected by REACH Initiative through People with
    Knowledge (PwK) surveys in June 2016 as the third round of the Multi-Sector Needs
    Assessment (MSNA) for Libya. The assessment synthesizes qualitative and quantitative
    findings on population needs, security conditions, WASH infrastructure status,
    and livelihood access across multiple sectors to inform humanitarian response
    prioritization.
  sources:
  - id: source_1
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/libya-multi-sector-needs-assessment-update-june-2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by security threats and unmet basic needs across
      multiple sectors
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Weakened WASH infrastructure and restricted access to livelihoods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: indirect
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
  description: Libya - Multi-Sector Needs Assessment Update (June 2016) (Excel)
  download_url: https://data.humdata.org/dataset/7146f721-087b-448f-9414-df49013e13f1/resource/c02c104d-a152-4d3b-a6d2-f7c4e8d91f54/download/reach_lby_msna_update_dataset_june_2016.xlsx
  format: null
  id: resource_c02c104d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_LBY_MSNA_Update_Dataset_June_2016.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Multi-Sector Needs Assessment Update (June 2016) (Questionnaire
    formatted for KOBO)
  download_url: https://data.humdata.org/dataset/7146f721-087b-448f-9414-df49013e13f1/resource/2c11ba00-01f3-4e17-96d7-8547f9adffeb/download/reach_lby_msna_update_xlsform_june_2016.xlsx
  format: null
  id: resource_2c11ba00
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_LBY_MSNA_Update_xlsForm_June_2016.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lby_reach_multisectorneedsassessmen_20160630
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-06-30'
temporal_resolution: null
title: Libya - Multi-Sector Needs Assessment Update (June 2016)
version: null
vulnerability: null
---
