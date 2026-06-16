---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/reach-car-2022-msna-results-table
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach-car-2022-msna-results-table
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/reach-car-2022-msna-results-table
dataset_id: rdls_lss-caf_reach_2022multisectoralneedsass_2022
description: 'The 2022 Multi-Sectoral Needs Assessment (MSNA), conducted by the REACH
  Initiative in close collaboration with the United Nations Office for the Coordination
  of Humanitarian Affairs (OCHA) and mandated by the Inter-cluster Coordination Group
  (ICCG), aims to understand the multi-sectoral and sector-specific needs, circumstances,
  and vulnerabilities of households across the entire territory of the Central African
  Republic. It also aims to understand specific needs and vulnerabilities of population
  groups, namely non-displaced households, returnees, internally displaced persons
  (IDPs) living in host communities, and IDPs living at sites. The needs assessment
  covers protection, health, mental health, WASH, Shelter and NFI, Education, food
  security, livelihoods and disabilities, as well as the perception of and satisfaction
  with humanitarian aid (AAP). The 2022 MSNA was conducted through a statistically
  representative household survey across 66 accessible sub-prefectures (admin2) out
  of the 72 sub-prefectures of the country. The inaccessible sub-prefectures were
  evaluated using a Key Informant survey. In consultation with key humanitarian partners
  and actors, a joint set of indicators, questions, and answer choices were developed
  for the assessment of needs in the context of the Central African Republic. All
  surveys were conducted through face-to-face interviews, using the tablet-based Kobo
  Collect Open Data Kit (ODK) app. Household data collection took place from July
  20 to September 18, 2022. A total of 12,347 households were assessed after data
  cleaning. Data is statistically representative at a 92% confidence level and a +/-
  10% margin of error with a buffer of 10% for the entire population on the level
  of sub-prefectures (admin2) and higher levels, and for specific population groups
  on the level of prefectures (admin1) and higher levels.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/reach-car-2022-msna-results-table]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The 2022 MSNA was conducted through sample survey methodology across
    Central African Republic's entire territory by REACH Initiative in collaboration
    with OCHA and the Inter-cluster Coordination Group. Survey data captures multi-sectoral
    needs, vulnerabilities, and circumstances of households stratified by displacement
    status (non-displaced, returnees, IDPs), generating impact metrics on food security,
    health, education, shelter, WASH, protection, and NFI needs.
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
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/reach-car-2022-msna-results-table
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multi-sectoral needs and vulnerabilities of households affected by
      food insecurity and humanitarian crisis
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
  - asset_category: economic_indicator
    asset_dimension: index
    description: Food security, livelihoods, and economic vulnerability indicators
      across population groups
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
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
  description: REACH Central African Republic 2022 Multi-Sectoral Needs Assessment
    (MSNA), Results table (Results table of REACH CAR 2022 MSNA)
  download_url: https://data.humdata.org/dataset/4e3887ee-803f-4b73-8e57-248c3e4d2089/resource/3ee43006-ed9e-420a-91d1-e7db306c6b55/download/reach_car_msna2022_final_results.xlsx
  format: null
  id: resource_3ee43006
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: REACH_CAR_MSNA2022_final_results.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_reach_2022multisectoralneedsass_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-09-18'
  start: '2022-07-20'
temporal_resolution: null
title: REACH Central African Republic 2022 Multi-Sectoral Needs Assessment (MSNA),
  Results table
version: null
vulnerability: null
---
