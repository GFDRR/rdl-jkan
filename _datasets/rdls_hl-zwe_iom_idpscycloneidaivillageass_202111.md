---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/zimbabwe-idps-cyclone-idai-village-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/zimbabwe-idps-cyclone-idai-village-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/zimbabwe-idps-cyclone-idai-village-assessment-iom-dtm
dataset_id: rdls_hl-zwe_iom_idpscycloneidaivillageass_202111
description: 'The data contains number of IDPs dis-aggregated by gender, age at village
  level.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zimbabwe-idps-cyclone-idai-village-assessment-iom-dtm]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted village-level assessments in Matabeleland South and
    Masvingo Provinces following Cyclone IDAI, enumerating internally displaced persons
    and disaggregating counts by gender and age groups using standardized DTM methodology
    to document post-event displacement impacts.
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
- href: https://data.humdata.org/dataset/zimbabwe-idps-cyclone-idai-village-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from Cyclone IDAI disaggregated by gender
      and age at village level
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Electronic questionnaires were used to collect the data and purposive
    sampling was used for sample selection. Eighty-nine enumerators were trained on
    the multisectoral village assessment questionnaires as well as data collection
    techniques. Multi-sectoral village assessments were conducted through focus group
    discussions with key informants in villages identified through baseline assessments
    which were conducted during the same period to capture population estimates, multi-sectoral
    needs, vulnerabilities and livelihood opportunities. The key informants included
    village heads, village health workers, childcare workers, village secretaries,
    chiefs, religious leaders, community members, education officers.
  download_url: https://data.humdata.org/dataset/62bc7aff-287a-4426-a63d-6c322989357a/resource/5e42b51e-8395-40ec-90dc-fa4d20d90307/download/3-hdx_bha_livelihood_msva_pulicdataset_rev-final.xlsx
  format: null
  id: resource_5e42b51e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Zimbabwe Village Assessment - Matabeleland South and Masvingo Provinces
    (November 2021)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zimbabwe - [IDPs] - Cyclone IDAI - Village Assessment - [IOM DTM] (DTM
    Zimbabwe IDAI Village Round 4)
  download_url: https://data.humdata.org/dataset/62bc7aff-287a-4426-a63d-6c322989357a/resource/09bf1d18-5541-4b1d-aa81-45ad9f7a5813/download/dtm-zimbabwe-idai-village-round-4.xlsx
  format: null
  id: resource_09bf1d18
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Zimbabwe IDAI Village Round 4
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-zwe_iom_idpscycloneidaivillageass_202111
spatial:
  bbox: null
  centroid: null
  countries:
  - ZWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-11-30'
  start: '2021-11-12'
temporal_resolution: null
title: Zimbabwe - [IDPs] - Cyclone IDAI - Village Assessment - [IOM DTM]
version: null
vulnerability: null
---
