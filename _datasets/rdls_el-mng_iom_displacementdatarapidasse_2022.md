---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/mongolia-displacement-idps-rapid-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/mongolia-displacement-idps-rapid-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/mongolia-displacement-idps-rapid-assessment-iom-dtm
dataset_id: rdls_el-mng_iom_displacementdatarapidasse_2022
description: 'The datasets provide an overview of key thematic areas covered by the
  Ulaanbaatar city-wide rapid assessment on population, migration and needs from June
  to August 2022. The datasets explore eight primary themes across Ulaanbaatar, namely,
  population baseline figures, registration, internal arrivals and departures (migration),
  employment, financial situation, mobility-related challenges, and services and infrastructure.
  Data are collected through key informant interviews with kheseg leaders , who are
  well-informed about their communities, resources and local context.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mongolia-displacement-idps-rapid-assessment-iom-dtm]'
details: null
exposure:
- asset_type:
    description: Population baseline figures disaggregated by age groups (0-5, 6-17,
      18-59, 60+) and gender across Ulaanbaatar districts
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population and migration data collected through key informant interviews
    with kheseg leaders across Ulaanbaatar districts during June-August 2022 (Round
    3) and prior rounds. Data captures baseline population demographics, internal
    arrivals/departures, vulnerability classifications (single-parent households,
    elderly-headed households, pregnant women, disabilities, child separation), employment
    status, and financial situation. Multiple rounds enable temporal tracking of displacement
    and mobility patterns.
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
- href: https://data.humdata.org/dataset/mongolia-displacement-idps-rapid-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by internal displacement and migration due to
      drought-related livelihood stress and herding/mining labor migration
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
  - asset_category: population
    asset_dimension: population
    description: Internal arrivals and departures (migration) with vulnerability indicators
      including single-parent households, elderly-headed households, and persons with
      disabilities
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
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: 'At the time of the round 3 assessment, there were 1,640,758 individuals
    and 474,198 households living in Ulaanbaatar city. Fifty-three per cent were women
    and 47 per cent were men. A significant 35 per cent of the population registered
    as minors: 12 per cent aged 0-5 years, and 23 per cent aged 6-17 years. Adults
    aged 18-59 years accounted for 56 per cent of the population, whereas the elderly
    aged 60 years and above accounted for nine per cent.'
  download_url: https://data.humdata.org/dataset/8c8423f4-e69a-4fb6-b5c3-25b0203390df/resource/ebf434c1-56e9-49c6-baff-4b9ab1a67cec/download/mub_phase-3_data_hdx.xlsx
  format: null
  id: resource_ebf434c1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mongolia - Rapid Assessment - Migration, Population and Needs - Round
    3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset covers 1,640 baghs in 21 provinces of Mongolia. 504,554
    households and 1, 779,600 individuals were identified. 36.5 percent of the population
    (649,000 individuals) were registered as minors below the age of 18; 55.6 percent
    (988,700 individuals) were registered as adults aged 18-59 years, and 141,900
    (7.9%) were counted as elderly aged 60 and above.
  download_url: https://data.humdata.org/dataset/8c8423f4-e69a-4fb6-b5c3-25b0203390df/resource/c9834e49-521d-4ffd-ad46-55ee0be34eb6/download/data-analysis_nw_mng_nso_july12_hdx.xlsx
  format: null
  id: resource_c9834e49
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mongolia - Rapid Assessment - Migration, Population and Needs - Nationwide
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset provides an overview of key thematic areas covered by
    the Ulaanbaatar city-wide rapid assessment on population, migration and needs
    between June and August 2022. Current data collection is the second phase of the
    Displacement Tracking Matrix Mobility (DTM) tracking assessment done by IOM Mongolia
    in Ulaanbaatar. Similar to phase one, this study explores eight primary themes
    across Ulaanbaatar, namely, population baseline figures, registration, internal
    arrivals and departures (migration), employment, financial situation, mobility-related
    challenges, and services and infrastructure. Data are collected through key informant
    interviews with kheseg leaders , who are well-informed about their communities,
    resources and local context.
  download_url: https://data.humdata.org/dataset/8c8423f4-e69a-4fb6-b5c3-25b0203390df/resource/953772cb-55eb-4088-8661-37394d8a0a9a/download/dtm_mub-city_-data_cleaned_private_may4-hdx.xlsx
  format: null
  id: resource_953772cb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mongolia - Rapid Assessment - Migration, Population and Needs - Round
    2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'This dataset explores eight primary themes across Ulaanbaatar city:
    namely, population baseline figures, arrivals and departures (migration), employment,
    financial situation, challenges and security, services and infrastructure, parks
    and green areas, and children and education. Data is captured via key informant
    interviews with kheseg leaders, who have been chosen due to their in-depth knowledge
    of their communities, their resources and local contacts.'
  download_url: https://data.humdata.org/dataset/8c8423f4-e69a-4fb6-b5c3-25b0203390df/resource/8cfabf47-d736-4bd1-8dc1-477648d82484/download/final-ub-data_rvd_phase1-hdx.xlsx
  format: null
  id: resource_8cfabf47
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mongolia - Rapid Assessment - Migration, Population and Needs - Round
    1
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mng_iom_displacementdatarapidasse_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - MNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-02-28'
  start: '2022-06-01'
temporal_resolution: null
title: Mongolia Displacement Data - Rapid Assessment [IOM DTM]
version: null
vulnerability: null
---
