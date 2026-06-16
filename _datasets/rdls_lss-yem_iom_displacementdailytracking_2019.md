---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/yemen-displacement-daily-tracking-idps-returnees-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/yemen-displacement-daily-tracking-idps-returnees-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/yemen-displacement-daily-tracking-idps-returnees-iom-dtm
dataset_id: rdls_lss-yem_iom_displacementdailytracking_2019
description: 'DTM''s Displacement Tracking tool collects and reports on displaced
  numbers of households on a daily basis, allowing for regular reporting of new displacements
  in terms of numbers, geography and needs. More than 3.6 million people are displaced
  as per August 2018 assessment.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-displacement-daily-tracking-idps-returnees-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM collects weekly displacement data through field assessments
    across Yemen governorates, recording household counts of newly displaced persons
    and returnees by origin/destination location, displacement reason, and humanitarian
    needs. Data is aggregated by week and governorate to produce regular tracking
    reports for humanitarian response monitoring.
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
- href: https://data.humdata.org/dataset/yemen-displacement-daily-tracking-idps-returnees-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (households) tracked weekly by displacement
      event and governorate
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
    description: Returnee households tracked weekly by return event and governorate
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
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1 January to 14 June 2025, IOM Yemen DTM tracked 1,323 households
    (HH) (7,938 Individuals) who experienced displacement at least once. Between 8
    and 14 June 2025, IOM Yemen DTM tracked 30 households (180 individuals) displaced
    at least once. The majority of people moved into/within the following governorates
    and districts: - Ma''rib (19 HHs) - Ma''rib City (13 HHs), Ma''rib (6 HHs) districts.
    Most displacements in the governorate originated from Dhamar and Ta''iz. - Ta''iz
    (6 HHs) - Mawza (6 HHs) district. All displacements in the governorate were internal.
    - Al Hodeidah (5 HHs) - Hays (5 HHs) district. All displacements in the governorate
    were internal.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/6d7a3ae1-7b9c-44dd-aa19-98044cbecc95/download/20250615_rdt-dataset-08-june-2025-14-june-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_6d7a3ae1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 08 - 14 June 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 7 June 2025, IOM Yemen DTM tracked 1,274 households
    (HH) (7,644 Individuals) who experienced displacement at least once. Between 1
    and 7 June 2025, IOM Yemen DTM tracked 25 households (150 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/81e3d8ff-25a4-4f34-98e3-e71ac258c267/download/20250608_rdt-dataset-01-june-2025-07-june-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_81e3d8ff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 - 07 June 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 31 May 2025, IOM Yemen DTM tracked 1,245 households
    (HH) (7,470 Individuals) who experienced displacement at least once. Between 25
    and 31 May 2025, IOM Yemen DTM tracked 44 households (264 individuals) displaced
    at least once. This dataset includes the data from Jan to May 31, 2025.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/22a0a5eb-4446-4244-9af0-32d4162ed23d/download/20250601_rdt-dataset-apr-2025-31-may-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_22a0a5eb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 06 April - 31 May 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 5 April 2025, IOM Yemen DTM tracked 527 households
    (HH) (3,162 Individuals) who experienced displacement at least once. Between 30
    March and 5 April 2025, IOM Yemen DTM tracked 20 households (120 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/42d79d91-3afb-4043-a3a5-af1b0b483935/download/20250406_rdt-dataset-30-mar-2025-05-apr-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_42d79d91
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 30 March - 05 April Mar 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 29 March 2025, IOM Yemen DTM tracked 505 households
    (HH) (3,030 Individuals) who experienced displacement at least once. Between 23
    and 29 March 2025, IOM Yemen DTM tracked 38 households (228 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/3ba26209-587d-4fa2-a8d2-5dc860047834/download/20250401_rdt-dataset-23-mar-2025-29-mar-2025-external-district-list_hdx.xlsx
  format: null
  id: resource_3ba26209
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 23 - 29 Mar 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 22 March 2025, IOM Yemen DTM tracked 458 households
    (HH) (2,748 Individuals) who experienced displacement at least once. Between 16
    and 22 March 2025, IOM Yemen DTM tracked 25 households (150 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/7e3a1fa2-2ed6-4801-b81f-88b825e7e3ff/download/20250323_rdt-dataset-16-mar-2025-22-mar-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_7e3a1fa2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 16 - 22 Mar 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 15 March 2025, IOM Yemen DTM tracked 423 households
    (HH) (2,538 Individuals) who experienced displacement at least once. Between 9
    and 15 March 2025, IOM Yemen DTM tracked 17 households (102 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/c88f7296-855d-4f86-9d91-771c3a593821/download/20250316_rdt-dataset-09-mar-2025-15-mar-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_c88f7296
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 09 - 15 Mar 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 8 March 2025, IOM Yemen DTM tracked 384 households
    (HH) (2,304 Individuals) who experienced displacement at least once. Between 2
    and 8 March 2025, IOM Yemen DTM tracked 15 households (90 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/1f8c9158-d130-4c12-a56c-2209b9ddf996/download/20250309_rdt-dataset-02-mar-2025-08-mar-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_1f8c9158
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 02 Mar - 08 Mar 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 1 March 2025, IOM Yemen DTM tracked 365 households
    (HH) (2,190 Individuals) who experienced displacement at least once. Between 23
    February and 1 March 2025, IOM Yemen DTM tracked 14 households (84 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/5669b5e5-58c8-468a-837c-23ed16e909d9/download/20250302_rdt-dataset-23-feb-2025-01-mar-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_5669b5e5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 23 Feb - 01 Mar 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 22 February 2025, IOM Yemen DTM tracked 337 households
    (HH) (2,022 Individuals) who experienced displacement at least once. Between 16
    and 22 February 2025, IOM Yemen DTM tracked 23 households (138 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/7c260a11-1f66-4807-85fe-acc8538c4fef/download/20250223_rdt-dataset-16-feb-2025-22-feb-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_7c260a11
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 16 - 22 Feb 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 9 and 15 February 2025, IOM Yemen DTM tracked 36 households
    (HHs) (216 individuals) who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 53 per cent (19 HHs) of the total followed by economic reasons
    related to conflict, accounting for 47 per cent (17 HHs).
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/3ac907b5-b06a-4279-9bf6-6a1383aadba4/download/20250216_rdt-dataset-09-feb-2025-15-feb-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_3ac907b5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 09 - 15 Feb 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 8 February 2025, IOM Yemen DTM tracked 216 households
    (HH) (1,296 Individuals) who experienced displacement at least once. Between 2
    and 8 February 2025, IOM Yemen DTM tracked 25 households (150 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/09ee6692-3bfe-496a-b895-99d742c23df5/download/20250209_rdt-dataset-02-feb-2025-09-feb-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_09ee6692
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 02 - 08 Feb 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 1 February 2025, IOM Yemen DTM tracked 183 households
    (HH) (1,098 Individuals) who experienced displacement at least once. Between 26
    January and 1 February 2025, IOM Yemen DTM tracked 34 households (204 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/02a1168d-4b3c-4b67-9262-8a8a6372dbb5/download/20250202_rdt-dataset-26-jan-2025-01-feb-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_02a1168d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 26 Jan - 01 Feb 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January 2024 to 4 January 2025, IOM Yemen DTM tracked 3,678
    households (HH) (22,068 Individuals) who experienced displacement at least once.
    Between 29 December 2024 and 4 January 2025, IOM Yemen DTM tracked 19 households
    (114 individuals) displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/01f6944f-254d-4e9f-bdfc-bb77cfbdef1b/download/20250105_rdt-dataset-29-dec-2024-04-jan-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_01f6944f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 28 December 2024 - 04 Jan 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 28 December 2024, IOM Yemen DTM tracked 3,649 households
    (HH) (21,894 Individuals) who experienced displacement at least once. Between
    22 and 28 December 2024, IOM Yemen DTM tracked 32 households (192 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/805324ab-8396-4740-a961-f150779f47e9/download/20241229_rdt-dataset-22-dec-2024-28-dec-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_805324ab
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 22 - 28 December 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 21 December 2024, IOM Yemen DTM tracked 3,589 households
    (HH) (21,534 Individuals) who experienced displacement at least once. Between
    15 and 21 December 2024, IOM Yemen DTM tracked 38 households (228 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/d6ddbf06-7abe-4918-a7e0-73cbca9ad3f3/download/20241222_rdt-dataset-15-dec-2024-21-dec-2024-external-district-list_hdx.xlsx
  format: null
  id: resource_d6ddbf06
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 15 - 21 December 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 14 December 2024, IOM Yemen DTM tracked 3,511 households
    (HH) (21,066 Individuals) who experienced displacement at least once. Between
    8 and 14 December 2024, IOM Yemen DTM tracked 36 households (216 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/9671bb70-a130-477d-9bd3-6ca3a4580191/download/20241215_rdt-dataset-08-dec-2024-14-dec-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_9671bb70
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 8 - 14 December 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1 January to 7 December 2024, IOM Yemen DTM tracked 3,456 households
    (HH) (20,736 Individuals) who experienced displacement at least once. The majority
    of people moved into/within the following governorates and districts: Ma''rib
    (32 HH) - Ma''rib City (25 HHs), Harib (4 HHs), Ma''rib (3 HHs) districts. Most
    displacements in the governorate originated from Dhamar and Ibb. Ta''iz (8 HHs)
    - Al Makha (5 HHs), Al Misrakh (3 HHs) districts. All displacements in the governorate
    were internal. Al Hodeidah (4 HH) - Hays (4 HHs) district. Most displacements
    in the governorate originated from Al Hodeidah and Ta''iz.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/67d2ee3a-09de-4bf0-80aa-86d1b246b2cf/download/20241208_rdt-dataset-01-dec-2024-07-dec-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_67d2ee3a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 1 - 7 December 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1 January to 30 November 2024, IOM Yemen DTM tracked 3,411 households
    (HH) (20,466 Individuals) who experienced displacement at least once. Between
    24 and 30 November 2024, IOM Yemen DTM tracked 71 households (426 individuals)
    displaced at least once. The majority of people moved into/within the following
    governorates and districts: Ma''rib (49 HH) - Ma''rib City (34 HHs), Ma''rib (15
    HHs) districts. Most displacements in the governorate originated from Ta''iz and
    Al Hodeidah. Al Hodeidah (20 HHs) - Hays (15 HHs), Al Khukhah (5 HHs) districts.
    Most displacements in the governorate were internal. Ad Dali (1 HH) - Al Azariq
    (1 HH) district. All displacements in the governorate originated from Ta''iz.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/8b9acba6-5491-4091-b653-b1ecc3e69556/download/20241201_rdt-dataset-24-nov-2024-30-nov-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_8b9acba6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 24 - 30 November 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 23 November 2024, IOM Yemen DTM tracked 3,297 households
    (HH) (19,782 Individuals) who experienced displacement at least once. Between
    17 and 23 November 2024, IOM Yemen DTM tracked 59 households (354 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/39928d09-755e-45e8-b2b6-c25f6aebbd46/download/20241124_rdt-dataset-17-nov-2024-23-nov-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_39928d09
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 17 - 23 November 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 16 November 2024, IOM Yemen DTM tracked 3,177 households
    (HH) (19,062 Individuals) who experienced displacement at least once. Between
    10 and 16 November 2024, IOM Yemen DTM tracked 35 households (210 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/3691de7d-e0c1-4719-aa27-337a7f158efb/download/20241117_rdt-dataset-10-nov-2024-16-nov-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_3691de7d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 10 - 16 November 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 9 November 2024, IOM Yemen DTM tracked 3,112 households
    (HH) (18,672 Individuals) who experienced displacement at least once. Between
    3 and 9 November 2024, IOM Yemen DTM tracked 30 households (180 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/3940a53c-afec-424f-b5f3-f6f81a794cbe/download/20241110_rdt-dataset-03-nov-2024-09-nov-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_3940a53c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 03 - 09 November 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 2 November 2024, IOM Yemen DTM tracked 3,060 households
    (HH) (18,360 Individuals) who experienced displacement at least once. Between
    27 October and 2 November 2024, IOM Yemen DTM tracked 31 households (186 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/9a640ac7-c4ac-41d2-a9b0-bb7d348cbf81/download/20241102_rdt-dataset-27-oct-2024-02-nov-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_9a640ac7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 27 October - 02 November 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 26 October 2024, IOM Yemen DTM tracked 2,982 households
    (HH) (17,892 Individuals) who experienced displacement at least once. Between
    20 and 26 October 2024, IOM Yemen DTM tracked 31 households (186 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/b4e8025f-ca4d-447f-a39e-87da8844083e/download/20241027_rdt-dataset-20-oct-2024-26-oct-2024-external-district-list_hdx.xlsx
  format: null
  id: resource_b4e8025f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 20 - 26 October 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 19 October 2024, IOM Yemen DTM tracked 2,904 households
    (HH) (17,424 Individuals) who experienced displacement at least once. Between
    13 and 19 October 2024, IOM Yemen DTM tracked 34 households (204 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/52a8d222-698f-44cc-bd63-e8c5b17f59c4/download/20241020_rdt-dataset-13-oct-2024-19-oct-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_52a8d222
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 13 - 19 October 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 12 October 2024, IOM Yemen DTM tracked 2,856 households
    (HH) (17,136 Individuals) who experienced displacement at least once. Between
    6 and 12 October 2024, IOM Yemen DTM tracked 22 households (132 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/b79f3c39-4a07-4a77-887b-fd4aa605c329/download/20241013_rdt-dataset-06-oct-2024-12-oct-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_b79f3c39
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 06 - 12 October 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 5 October 2024, IOM Yemen DTM tracked 2,819 households
    (HH) (16,914 Individuals) who experienced displacement at least once. Between
    29 September and 5 October 2024, IOM Yemen DTM tracked 24 households (144 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/fa7e0550-275d-45bf-8191-103323d5e874/download/20241005_rdt-dataset-29-sep-2024-05-oct-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_fa7e0550
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 29 September - 05 October 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 28 September 2024, IOM Yemen DTM tracked 2,725 households
    (HH) (16,350 Individuals) who experienced displacement at least once. Between
    22 and 28 September 2024, IOM Yemen DTM tracked 23 households (138 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/270ff455-26c1-4ff7-8d23-11ec48846963/download/20240929_rdt-dataset-22-sep-2024-29-sep-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_270ff455
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 22 - 28 September 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 21 September 2024, IOM Yemen DTM tracked 2,679 households
    (HH) (16,074 Individuals) who experienced displacement at least once. Between
    15 and 21 September 2024, IOM Yemen DTM tracked 28 households (168 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/5e02defa-ec3f-4349-90e2-a8cdfa213c88/download/20240922_rdt-dataset-15-sep-2024-21-sep-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_5e02defa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 15 - 21 September 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 14 September 2024, IOM Yemen DTM tracked 2,633 households
    (HH) (15,798 Individuals) who experienced displacement at least once. Between
    8 and 14 September 2024, IOM Yemen DTM tracked 86 households (516 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/c756fb47-1a3d-420b-a5da-530893365b4e/download/20240915_rdt-dataset-08-sep-2024-14-sep-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_c756fb47
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 08 - 14 September 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 7 September 2024, IOM Yemen DTM tracked 2,361 households
    (HH) (14,166 Individuals) who experienced displacement at least once. Between
    1 and 7 September 2024, IOM Yemen DTM tracked 26 households (156 individuals)
    displaced at least once
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/f4fb4415-cea1-4892-b032-4689a469ee54/download/20240908_rdt-dataset-01-sep-2024-07-sep-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_f4fb4415
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 - 07 September 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 31 August 2024, IOM Yemen DTM tracked 2,319 households
    (HH) (13,914 Individuals) who experienced displacement at least once. Between
    25 and 31 August 2024, IOM Yemen DTM tracked 40 households (240 individuals) displaced
    at least once
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/18d29fe0-7eee-452f-8a69-94e2272da042/download/20240901_rdt-dataset-25-aug-2024-31-aug-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_18d29fe0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 25 - 31 August 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 24 August 2024, IOM Yemen DTM tracked 2,234 households
    (HH) (13,404 Individuals) who experienced displacement at least once. Between
    18 and 24 August 2024, IOM Yemen DTM tracked 51 households (306 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/7b9e78e4-b313-4a4e-ad1a-3a9ce90a8c6f/download/20240825_rdt-dataset-18-aug-2024-24-aug-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_7b9e78e4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 18 - 24 August 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 17 August 2024, IOM Yemen DTM tracked 2,156 households
    (HH) (12,936 Individuals) who experienced displacement at least once. Between
    11 and 17 August 2024, IOM Yemen DTM tracked 40 households (240 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/053be349-16c2-4859-a49b-0a1349587a90/download/20240818_rdt-dataset-11-aug-2024-17-aug-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_053be349
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 11 - 17 August 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 10 August 2024, IOM Yemen DTM tracked 2,077 households
    (HH) (12,462 Individuals) who experienced displacement at least once. Between
    4 and 10 August 2024, IOM Yemen DTM tracked 55 households (330 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/723f9d83-b8cc-4dc4-8a0c-36d01a9339ab/download/20240811_rdt-dataset-04-aug-2024-10-aug-2024-external-district-level.xlsx
  format: null
  id: resource_723f9d83
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 04 - 10 August 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 3 August 2024, IOM Yemen DTM tracked 1,981 households
    (HH) (11,886 Individuals) who experienced displacement at least once. Between
    28 July and 3 August 2024, IOM Yemen DTM tracked 70 households (420 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/deb90fab-a479-4346-92e4-33c1062c8b2e/download/20240804_rdt-dataset-28-july-2024-03-aug-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_deb90fab
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 28 July - 3 August 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 27 July 2024, IOM Yemen DTM tracked 1,881 households
    (HH) (11,286 Individuals) who experienced displacement at least once. Between
    21 and 27 July 2024, IOM Yemen DTM tracked 28 households (168 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/8c12390b-6edd-4a88-9cb8-d244708e05ab/download/20240728_rdt-dataset-21-july-2024-27-july-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_8c12390b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 21 - 27 July 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 20 July 2024, IOM Yemen DTM tracked 1,821 households
    (HH) (10,926 Individuals) who experienced displacement at least once. Between
    14 and 20 July 2024, IOM Yemen DTM tracked 57 households (342 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/102d0c41-5e93-43b1-80e8-3a3f9f10c292/download/20240721_rdt-dataset-14-july-2024-20-july-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_102d0c41
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 14 - 20 July 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 13 July 2024, IOM Yemen DTM tracked 1,745 households
    (HH) (10,470 Individuals) who experienced displacement at least once. Between
    7 and 13 July 2024, IOM Yemen DTM tracked 29 households (174 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/ca1ba545-5019-4be2-9ecb-4326b2555ccf/download/20240714_rdt-dataset-07-july-2024-13-july-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_ca1ba545
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 07 - 13 July 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 6 July 2024, IOM Yemen DTM tracked 1,688 households
    (HH) (10,128 Individuals) who experienced displacement at least once. Between
    30 June and 6 July 2024, IOM Yemen DTM tracked 44 households (264 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/d9385f7e-9316-41cd-8bc6-5bb6b11aed32/download/20240708_rdt-dataset-30-june-2024-06-july-2024-external-district-level_hdx.xlsx
  format: null
  id: resource_d9385f7e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 30 June - 06 July 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 29 June 2024, IOM Yemen DTM tracked 1,622 households
    (HH) (9,732 Individuals) who experienced displacement at least once. Between 23
    and 29 June 2024, IOM Yemen DTM tracked 43 households (258 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/2892d650-02af-4cdd-8830-83715b7e08ae/download/20240630_rdt-dataset-23-june-2024-29-june-2024-external-district-level.xlsx
  format: null
  id: resource_2892d650
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 23 - 29 June 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 22 June 2024, IOM Yemen DTM tracked 1,564 households
    (HH) (9,384 Individuals) who experienced displacement at least once. Between 16
    and 22 June 2024, IOM Yemen DTM tracked 7 households (42 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/12a0bcdc-4c1c-40a4-9d39-515d46db22d5/download/20240623_rdt-dataset-16-june-2024-22-june-2024-external-district-level.xlsx
  format: null
  id: resource_12a0bcdc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 16 - 22 June 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 15 June 2024, IOM Yemen DTM tracked 1,557 households
    (HH) (9,342 Individuals) who experienced displacement at least once. Between 9
    and 15 June 2024, IOM Yemen DTM tracked 15 households (90 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/74f93cd9-ade3-4912-a21b-dab46a945755/download/20240619_rdt-dataset-09-june-2024-15-june-2024-external-district-level.xlsx
  format: null
  id: resource_74f93cd9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 09 - 15 June 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 8 June 2024, IOM Yemen DTM tracked 1,530 households
    (HH) (9,180 Individuals) who experienced displacement at least once. Between 2
    and 8 June 2024, IOM Yemen DTM tracked 38 households (228 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/5a3b62da-6ac1-4504-ada5-50d27b9db79a/download/20240609_rdt-dataset-02-june-2024-08-june-2024-external-district-level.xlsx
  format: null
  id: resource_5a3b62da
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 - 08 June 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 1 June 2024, IOM Yemen DTM tracked 1,465 households
    (HH) (8,790 Individuals) who experienced displacement at least once. Between 26
    May and 1 June 2024, IOM Yemen DTM tracked 57 households (342 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/df4147bf-400a-4aa5-ad4d-400e51231139/download/20240602_rdt-dataset-26-may-2024-01-june-2024-external-district-level.xlsx
  format: null
  id: resource_df4147bf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 26 May - June 01 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 25 May 2024, IOM Yemen DTM tracked 1,358 households
    (HH) (8,148 Individuals) who experienced displacement at least once. Between 19
    and 25 May 2024, IOM Yemen DTM tracked 41 households (246 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/2fa9e76d-d94b-48f6-9695-a86e08f9c5f9/download/20240526_rdt-dataset-19-may-2024-25-may-2024-external-district-level.xlsx
  format: null
  id: resource_2fa9e76d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 19 - 25 May 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 18 May 2024, IOM Yemen DTM tracked 1,300 households
    (HH) (7,800 Individuals) who experienced displacement at least once . Between
    12 and 18 May 2024, IOM Yemen DTM tracked 48 households (288 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/cb6d5a8c-cc1d-4b3a-9978-782d9c8d3ed5/download/20240519_rdt-dataset-12-may-2024-18-may-2024-external-district-level.xlsx
  format: null
  id: resource_cb6d5a8c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 12 - 18 May 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 11 May 2024, IOM Yemen DTM tracked 1,233 households
    (HH) (7,398 Individuals) who experienced displacement at least once. Between 5
    and 11 May 2024, IOM Yemen DTM tracked 47 households (282 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/9cde0c84-d19b-4601-b18a-692579f908f8/download/20240512_rdt-dataset-05-may-2024-11-may-2024-external-district-level.xlsx
  format: null
  id: resource_9cde0c84
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 05 - 11 May 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 4 May 2024, IOM Yemen DTM tracked 1,159 households
    (HH) (6,954 Individuals) who experienced displacement at least once. Between 28
    April and 4 May 2024, IOM Yemen DTM tracked 32 households (192 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/de99211d-ca4e-435c-be9a-11d9cdb8e73e/download/20240504_rdt-dataset-28-april-2024-04-mayl-2024-external-district-level.xlsx
  format: null
  id: resource_de99211d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 28 April - 04 May 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 27 April 2024, IOM Yemen DTM tracked 1,067 households
    (HH) (6,402 Individuals) who experienced displacement at least once. Between 21
    and 27 April 2024, IOM Yemen DTM tracked 39 households (234 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/31084d2c-52f9-4251-b124-d1583a515466/download/20240428_rdt-dataset-21-april-2024-27-april-2024-external-district-level.xlsx
  format: null
  id: resource_31084d2c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 21 - 27 April 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 20 April 2024, IOM Yemen DTM tracked 1,019 households
    (HH) (6,114 Individuals) who experienced displacement at least once. Between 14
    and 20 April 2024, IOM Yemen DTM tracked 44 households (264 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/14053de1-2752-4363-9d1a-29edeb6e48b6/download/20240421_rdt-dataset-14-april-2024-20-april-2024-external-district-level.xlsx
  format: null
  id: resource_14053de1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 14 - 20 April 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 13 April 2024, IOM Yemen DTM tracked 961 households
    (HH) (5,766 Individuals) who experienced displacement at least once. Between 7
    and 13 April 2024, IOM Yemen DTM tracked 7 households (42 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/0e1c6b40-fe9d-4e41-a487-873f6dece437/download/20240415_rdt-dataset-07-april2024-13-april-2024-external-district-level.xlsx
  format: null
  id: resource_0e1c6b40
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 07 - 13 April 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 6 April 2024, IOM Yemen DTM tracked 947 households
    (HH) (5,682 Individuals) who experienced displacement at least once. Between 31
    March and 6 April 2024, IOM Yemen DTM tracked 34 households (204 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/c65e857f-fddc-4d84-9a26-1cc4d81091fa/download/20240407_rdt-dataset-31-march-2024-06-april-2024-external-district-level.xlsx
  format: null
  id: resource_c65e857f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 31 March 2024 - 06 April 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 30 March 2024, IOM Yemen DTM tracked 904 households
    (HH) (5,424 Individuals) who experienced displacement at least once. Between 24
    and 30 March 2024, IOM Yemen DTM tracked 18 households (108 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/13eecbd4-9713-4ef9-81a6-eb1ef4f1ad86/download/20240331_rdt-dataset-24-march-2024-30-march-2024-external-district-level_0.xlsx
  format: null
  id: resource_13eecbd4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 24 - 30 March 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 23 March 2024, IOM Yemen DTM tracked 879 households
    (HH) (5,274 Individuals) who experienced displacement at least once. Between 17
    and 23 March 2024, IOM Yemen DTM tracked 34 households (204 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/afa45fbc-407a-4ced-8f7b-839d03136cc3/download/20240324_rdt-dataset-17-march-2024-23-march-2024-external-district-level.xlsm
  format: null
  id: resource_afa45fbc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 17 - 23 March 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 16 March 2024, IOM Yemen DTM tracked 830 households
    (HH) (4,980 Individuals) who experienced displacement at least once. Between 10
    and 16 March 2024, IOM Yemen DTM tracked 32 households (192 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/19064ec1-41c6-4770-afb1-3967abb92dbb/download/20240317_rdt-dataset-10-march-2024-16-march-2024-external-district-level.xlsx
  format: null
  id: resource_19064ec1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 10 - 16 March 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 9 March 2024, IOM Yemen DTM tracked 782 households
    (HH) (4,692 Individuals) who experienced displacement at least once. Between 3
    and 9 March 2024, IOM Yemen DTM tracked 31 households (186 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/ed7cf43f-17c6-4675-9f80-c9a0bada271b/download/20240310_rdt-dataset-03-march-2024-09-march-2024-external-district-level_1.xlsx
  format: null
  id: resource_ed7cf43f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 03 - 09 March 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 2 March 2024, IOM Yemen DTM tracked 637 households
    (HH) (3,822 Individuals) who experienced displacement at least once. Between 25
    February and 2 March 2024, IOM Yemen DTM tracked 50 households (300 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/442b8255-2440-4a51-b8fa-a54f59b61365/download/20240302_rdt-dataset-25-february-2024-02-march-2024-external-district-level.xlsx
  format: null
  id: resource_442b8255
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 25 February - 02 March 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 24 February 2024, IOM Yemen DTM tracked 552 households
    (HH) (3,312 Individuals) who experienced displacement at least once. Between 18
    and 24 February 2024, IOM Yemen DTM tracked 21 households (126 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/a0441d58-e0e9-414b-ad26-cd0f6e110754/download/20240225_rdt-dataset-18-february-2024-24-february-2024-external-district-level.xlsx
  format: null
  id: resource_a0441d58
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 18 - 24 February 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 17 February 2024, IOM Yemen DTM tracked 496 households
    (HH) (2,976 Individuals) who experienced displacement at least once. Between 11
    and 17 February 2024, IOM Yemen DTM tracked 36 households (216 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/697c656a-684c-4ae1-9849-0db4d6b732ad/download/20240218_rdt-dataset-11-february-2024-17-february-2024-external-district-level.xlsx
  format: null
  id: resource_697c656a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 11 - 17 February 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 10 February 2024, IOM Yemen DTM tracked 404 households
    (HH) (2,424 Individuals) who experienced displacement at least once. Between 4
    and 10 February 2024, IOM Yemen DTM tracked 19 households (114 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/6827b8c0-e24d-4740-b230-9747b821cf15/download/20240211_rdt-dataset-04-february-2024-10-february-2024-external-district-level.xlsx
  format: null
  id: resource_6827b8c0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 04 - 10 February 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 10 February 2024, IOM Yemen DTM tracked 404 households
    (HH) (2,424 Individuals) who experienced displacement at least once. Between 4
    and 10 February 2024, IOM Yemen DTM tracked 19 households (114 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/17ea4c49-d4cf-4668-9986-8749cae96e08/download/20240203_rdt-dataset-28-january-2024-03-february-2024-external-district-level.xlsx
  format: null
  id: resource_17ea4c49
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 28 January 2024 - 03 February 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 to 27 January 2024, IOM Yemen DTM tracked 255 households (HH)
    (1,530 Individuals) who experienced displacement at least once. Between 21 and
    27 January 2024, IOM Yemen DTM tracked 21 households (126 individuals) displaced
    at least once. The majority of people moved into/within the following governorates
    and districts.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/724f4b65-b22d-4528-8aaf-9a361f9048b0/download/20240128_rdt-dataset-21-january-2024-27-january-2024-district-level.xlsx
  format: null
  id: resource_724f4b65
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 21 - 27 January 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 20 January 2024, IOM Yemen DTM tracked 194 households
    (HH) (1,164 Individuals) who experienced displacement at least once. Between 14
    and 20 January 2024, IOM Yemen DTM tracked 52 households (312 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/c1480281-f76a-4f67-8df6-09bbf837a85e/download/20240121_rdt-dataset-14-january-2024-20-january-2024-district-level.xlsx
  format: null
  id: resource_c1480281
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 14 - 20 January 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 13 January 2024, IOM Yemen DTM tracked 70 households
    (HH) (420 Individuals) who experienced displacement at least once. Between 7 and
    13 January 2024, IOM Yemen DTM tracked 23 households (138 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/ae3ecedd-24ba-4039-ba20-37f8758b3bd2/download/20240114_rdt-dataset-07-january-2024-13-january-2024-external-district-level.xlsx
  format: null
  id: resource_ae3ecedd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 07 - 13 January 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January 2023 to 6 January 2024, IOM Yemen DTM tracked 9,977
    households (HH) (59,862 Individuals) who experienced displacement at least once.
    Between 31 December 2023 and 6 January 2024, IOM Yemen DTM tracked 21 households
    (126 individuals) displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/53bcdd8c-b71f-4ba1-aaea-22e789d9e6f4/download/20240107_rdt-dataset-31-december-2023-06-january-2024-external-district-level.xlsx
  format: null
  id: resource_53bcdd8c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 31 December 2023 - 06 January 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 30 December 2023, IOM Yemen DTM tracked 9,928 households
    (HH) (59,568 Individuals) who experienced displacement at least once. Between
    24 and 30 December 2023, IOM Yemen DTM tracked 12 households (72 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/f53c754f-1c0d-42a5-aba0-f94d7bee9d02/download/20231231_rdt-dataset-24-december-2023-30-december-2023-external-district-level.xlsx
  format: null
  id: resource_f53c754f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 24 - 30 December 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 23 December 2023, IOM Yemen DTM tracked 9,896 households
    (HH) (59,376 Individuals) who experienced displacement at least once. Between
    17 and 23 December 2023, IOM Yemen DTM tracked 33 households (198 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/f083be02-b6b7-45d6-bc0c-97be2fa2b547/download/20231224_rdt-dataset-17-december-2023-23-december-2023-external-district-level.xlsx
  format: null
  id: resource_f083be02
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 17 - 23 December 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 16 December 2023, IOM Yemen DTM tracked 9,836 households
    (HH) (59,016 Individuals) who experienced displacement at least once. Between
    10 and 16 December 2023, IOM Yemen DTM tracked 50 households (300 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/38c9b16d-a0e9-4c0d-912c-0ddb089f9c28/download/20231217_rdt-dataset-10-december-2023-16-december-2023-external-district-level.xlsx
  format: null
  id: resource_38c9b16d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 10 - 16 December 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Yemen DTM's Rapid Displacement Tracking (RDT) tool collects data
    on estimated numbers of households forced to flee on a daily basis from their
    locations of habitual residence or displacement, allowing for regular reporting
    of new displacements1 in terms of estimated numbers, causes of displacement, geography
    and needs. It also tracks IDP returnees who returned to their location of habitual
    residence. Between 3 and 9 December 2023, IOM Yemen DTM tracked 45 households
    (HHs) (270 individuals)2 who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 60 per cent (27 HHs) of the total followed by economic reasons
    related to conflict, accounting for 40 per cent (18 HHs). From 1 January to 9
    December 2023, IOM Yemen DTM tracked 9,744 households3 (58,464 Individuals) who
    experienced displacement at least once. IOM DTM also recorded 6 returnee households
    in governorates of Ma'rib (4 HHs) and Ta'iz (2 HHs) returning to their locations
    of origin during the reporting period
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/76c4aaa8-3a32-4a36-8e7c-b00014c1ebb6/download/20231209_rdt-dataset-03-december-2023-09-december-2023-external-district-level.xlsx
  format: null
  id: resource_76c4aaa8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 03 - 09 December 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1 January to 2 December 2023, IOM Yemen DTM tracked 9,643 households
    (HH) (57,858 Individuals) who experienced displacement at least once. Between
    26 November and 2 December 2023, IOM Yemen DTM tracked 47 households (282 individuals)
    displaced at least once. The majority of people moved into/within the following
    governorates and districts: Ta''iz (22 HHs) - Al Makha (12 HHs), Mawza (6 HHs),
    Al Maafer (4 HHs) districts. Most displacements in the governorate originated
    from Taiz and Al Hodeidah. Ma''rib (19 HHs) - Marib (9 HHs), Marib City (5 HHs),
    Harib (5 HHs) districts. Most displacements in the governorate originated from
    Taiz and Al Hodeidah. Al Hodeidah (6 HHs) - Al Khukhah (5 HHs), Hays (1 HHs) districts.
    Most displacements in the governorate were internal. The majority of people moved
    from the following governorates and districts: Al Hodeidah (14 HHs) - At Tuhayta
    (3 HHs), Hays (3 HHs), Al Hawak (3 HHs) districts. Ta''iz (11 HHs) - Maqbanah
    (8 HHs), Al Maafer (3 HHs) districts. Ma''rib (5 HHs) - Harib (5 HHs) district.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/c5786ea5-5135-4803-a990-ec20c99b50c9/download/20231203_rdt-dataset-26-november-2023-02-december-2023-external-district-level.xlsx
  format: null
  id: resource_c5786ea5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 26 November 2023 - 02 December 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1 January to 25 November 2023, IOM Yemen DTM tracked 9,571 households
    (HH) (57,426 Individuals) who experienced displacement at least once. Between
    19 and 25 November 2023, IOM Yemen DTM tracked 42 households (252 individuals)
    displaced at least once. The majority of people moved into/within the following
    governorates and districts: Al Hodeidah (26 HHs) - Al Khukhah (13 HHs), and Hays
    (13 HHs) districts. Most displacements in the governorate were internal. Ma''rib
    (10 HHs), Ma''rib City (7 HHs), and Ma''rib (3 HHs) districts. Most displacements
    in the governorate originated from Al Hodeidah and Ma''rib. Ta''iz (5 HHs) - Al
    Makha (5 HHs) district. Most displacements in the governorate originated from
    Al Hodeidah and Hadramawt. The majority of people moved from the following governorates
    and districts: Al Hodiedah (31 HHs) - At Tuhayta (15 HHs), Al Jarrahi (9 HHs),
    Ad Durayhimi (3 HHs) districts. Ta''iz (5 HHs) - Maqbanah (3 HHs), At Taiziyah
    (2 HHs) districts. Ma''rib (2 HHs) - Madghal Al Jidan (2 HHs) district.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/01604393-24ff-4c44-ac36-a3b0a6a13591/download/20231126_rdt-dataset-19-november-2023-25-november-2023-external-district-level.xlsx
  format: null
  id: resource_01604393
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 19 - 25 November 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Yemen DTM's Rapid Displacement Tracking (RDT) tool collects data
    on estimated numbers of households forced to flee on a daily basis from their
    locations of habitual residence or displacement, allowing for regular reporting
    of new displacements1 in terms of estimated numbers, causes of displacement, geography
    and needs. It also tracks IDP returnees who returned to their location of habitual
    residence. Between 12 and 18 November 2023, IOM Yemen DTM tracked 37 households
    (HHs) (222 individuals) who experienced displacement at least once. Economic reasons
    related to the conflict were the main reason for displacement, accounting for
    65 per cent (24 HHs) of the total followed by safety and security reasons as a
    result of the conflict, accounting for 35 per cent (13 HHs). From 1 January to
    18 November 2023, IOM Yemen DTM tracked 9,405 households3 (56,430 Individuals)
    who experienced displacement at least once. IOM DTM also recorded 6 returnee households
    in Ma'rib (4 HHs) and Ta'iz (2 HHs) governorates returning to their locations
    of origin during the reporting period
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/98d72a0f-fb78-4161-b39a-f526b001201d/download/20231119_rdt-dataset-12-november-2023-18-november-2023-external-district-level.xlsx
  format: null
  id: resource_98d72a0f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 12 - 18 November 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Yemen DTM's Rapid Displacement Tracking (RDT) tool collects data
    on estimated numbers of households forced to ?ee on a daily basis from their locations
    of habitual residence or displacement, allowing for regular reporting of new displacements1
    in terms of estimated numbers, causes of displacement, geography and needs. It
    also tracks IDP returnees who returned to their location of habitual residence.
    Between 5 and 11 November 2023, IOM Yemen DTM tracked 29 households (HHs) (174
    individuals) who experienced displacement at least once. Safety and security concerns
    as a result of the conflict were the main reason for displacement, accounting
    for 55 per cent (16 HHs) of the total followed by economic reasons related to
    conflict, accounting for 45 per cent (13 HHs). From 1 January to 11 November 2023,
    IOM Yemen DTM tracked 9,343 households3 (56,058 Individuals) who experienced displacement
    at least once. IOM DTM also recorded 272 returnee households in Hadramawt governorate
    returning to their locations of origin during the reporting period.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/938e0c2e-384c-46df-a17a-5785d61623a1/download/20231112_rdt-dataset-05-november-2023-11-november-2023-external-district-level.xlsx
  format: null
  id: resource_938e0c2e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 05 - 11 November 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Yemen DTM's Rapid Displacement Tracking (RDT) tool collects data
    on estimated numbers of households forced to flee on a daily basis from their
    locations of habitual residence or displacement, allowing for regular reporting
    of new displacements1 in terms of estimated numbers, causes of displacement, geography
    and needs. It also tracks IDP returnees who returned to their location of habitual
    residence. Between 29 October and 4 November 2023, IOM Yemen DTM tracked 15 households
    (HHs) (90 individuals)2 who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 67 per cent (10 HHs) of the total followed by economic reasons
    related to conflict, accounting for 33 per cent (5 HHs). From 1 January to 4 November
    2023, IOM Yemen DTM tracked 9,273 households3 (55,638 Individuals) who experienced
    displacement at least once. IOM DTM also recorded 1,683 returnee households who
    were displaced by cyclone Tej last week in the governorates of Al Maharah (1,415HHs),
    Hadramawt (262 HHs), and Ma'rib (6 HHs) returning to their locations of origin
    during the reporting period.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/95a1b7dd-1a1c-4537-ba31-0e1734cccc0f/download/20231105_rdt-dataset-29-october-2023-04-november-2023-external-district-level.xlsx
  format: null
  id: resource_95a1b7dd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 29 October 2023 - 04 November 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IOM Yemen DTM's Rapid Displacement Tracking (RDT) tool collects data
    on estimated numbers of households forced to ?ee on a daily basis from their locations
    of habitual residence or displacement, allowing for regular reporting of new displacements1
    in terms of estimated numbers, causes of displacement, geography and needs. It
    also tracks IDP returnees who returned to their location of habitual residence.
    Between 22 and 28 October 2023, IOM Yemen DTM tracked 4,392 households (HHs) (26,352
    individuals)2 who experienced displacement at least once. Cyclone Tej (Natural
    disaster) is the main reason for displacement, accounting for 99 per cent (4,356
    HHs) of the total followed by security concerns as a result of the conflict accounting
    for (0.41%; 18 HHs), and economic reasons related to conflict (0.41%; 18 HHs).
    From 1 January to 28 October 2023, IOM Yemen DTM tracked 9,187 households3 (55,122
    Individuals) who experienced displacement at least once. IOM DTM also recorded
    22 returnee households in the governorates of Al Maharah (17 HHs) and Ta'iz (5
    HHs) returning to their locations of origin during the reporting period.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/11c3397a-a945-4c5c-b02a-2971fd3f2d81/download/20231029_rdt-dataset-22-october-2023-28-october-2023-external-district-level-1.xlsx
  format: null
  id: resource_11c3397a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 22 - 28 October 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 15 and 21 October 2023, IOM Yemen DTM tracked 32 households
    (HHs) (192 individuals) who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 72 per cent (23 HHs) of the total followed by economic reasons
    related to conflict, accounting for 28 per cent (9 HHs). From 1 January to 21
    October 2023, IOM Yemen DTM tracked 4,767 households3 (28,602 Individuals) who
    experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/ab63af1c-4806-4c6b-8bda-e8124153a5d1/download/20231022_rdt-dataset-15-october-2023-21-october-2023-external-district-level.xlsx
  format: null
  id: resource_ab63af1c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 15 - 21 October 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 8 and 14 October 2023, IOM Yemen DTM tracked 24 households
    (HHs) (144 individuals) who experienced displacement at least once. Economic reasons
    related to the conflict were the main reason for displacement, accounting for
    54 per cent (13 HHs) of the total followed by safety and security reasons, accounting
    for 46 per cent (11 HHs). From 1 January to 14 October 2023, IOM Yemen DTM tracked
    4,716 households3 (28,296 Individuals) who experienced displacement at least once.
    IOM DTM also recorded seven returnee households in the governorate of Ma'rib returning
    to their locations of origin during the reporting period.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/30603e07-226e-4a56-ba3a-1fd295aa7268/download/20231015_rdt-dataset-08-october-2023-14-october-2023_district-level.xlsm
  format: null
  id: resource_30603e07
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 08 October 2023 - 14 October 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 1 and 7 October 2023, IOM Yemen DTM tracked 35 households (HHs)
    (210 individuals) who experienced displacement at least once. Safety and security
    concerns as a result of the conflict were the main reason for displacement, accounting
    for 69 per cent (24 HHs) of the total followed by economic reasons related to
    conflict, accounting for 31 per cent (11 HHs). From 1 January to 7 October 2023,
    IOM Yemen DTM tracked 4,652 households3 (27,912 Individuals) who experienced displacement
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/3aabde62-3081-4c4c-8d65-2e49593370c7/download/20231008_rdt-dataset-01-october-2023-07-october-2023-external-district-level.xlsx
  format: null
  id: resource_3aabde62
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 October 2023 - 07 October 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: During the reporting period, between 1 July and 30 September 2023,
    IOM Yemen DTM tracked 1,089 households (HHs) (6,534 individuals) who experienced
    displacement at least once. This compares to 1,016 households (6,096 individuals)
    in the second quarter 2023 representing an seven per cent increase. Since the
    beginning of April 2022, the number of tracked new instances of displacement has
    been declining with a truce held between conflicting parties until October 2022.
    However, the number began to light rise in the first quarter of the year 2023
    (2,495 HHs) due to the renewed conflict in Harib (Ma'rib) and heavy rains and
    floods in Shabwah governorate. The monthly average of household displacements
    in 2023 so far has been 511 with a high of 1,079 in January 2023 compared to an
    average of 845 in 2022 with a maximum of 2,453 in January 2022.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/cf43ff51-dcae-4ead-bc0f-93b4c3b40057/download/20231002_rdt-dataset-01-july-30-september-2023_district-level.xlsm
  format: null
  id: resource_cf43ff51
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking Third Quarter Report (July - September 2023)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 24 and 30 September 2023, IOM Yemen DTM tracked 49 households
    (HHs) (294 individuals) who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 78 per cent (38 HHs) of the total followed by economic reasons
    related to conflict, accounting for 22 per cent (11 HHs). From 1 January to 30
    September 2023, IOM Yemen DTM tracked 4,600 households (27,600 Individuals) who
    experienced displacement at least once. IOM DTM also recorded three returnee households
    in the governorate of Ma'rib returning to their locations of origin during the
    reporting period.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/d05ddc2e-926e-4943-b347-7d6a1dabd8ec/download/rdt-dataset-24-september-2023-30-september-2023.xlsx
  format: null
  id: resource_d05ddc2e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 24 - 30 September 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 17 and 23 September 2023, IOM Yemen DTM tracked 111 households
    (HHs) (666 individuals) who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 92 per cent (102 HHs) of the total followed by economic reasons
    related to conflict, accounting for eight per cent (9 HHs). From 1 January to
    23 September 2023, IOM Yemen DTM tracked 4,478 households (26,868 Individuals)
    who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/bb37ac62-209f-4317-a205-d4bad801a444/download/20230924_rdt-dataset-17-september-2023-23-september-2023-external-district-level.xlsx
  format: null
  id: resource_bb37ac62
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 17 - 23 September 2023 External District
    Level.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 10 and 16 September 2023, IOM Yemen DTM tracked 36 households
    (HHs) (216 individuals) who experienced displacement at least once. Safety and
    security concerns as a result of the confliict were the main reason for displacement,
    accounting for 69 per cent (25 HHs) of the total followed by economic reasons
    related to conflict, accounting for 31 per cent (11 HHs). From 1 January to 16
    September 2023, IOM Yemen DTM tracked 4,311 households (25,866 Individuals) who
    experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/774fd737-3265-435f-8319-ecb35155a7e0/download/20230917_rdt-dataset-10-september-2023-16-september-2023-external-district-level.xlsx
  format: null
  id: resource_774fd737
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 10 - 16 September 2023 External District
    Level.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 3 and 9 September 2023, IOM Yemen DTM tracked 26 households
    (HHs) (156 individuals) who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 58 per cent (15 HHs) of the total followed by economic reasons
    related to conflict, accounting for 42 per cent (11 HHs). From 1 January to 9
    September 2023, IOM Yemen DTM tracked 4,231 households (25,386 Individuals) who
    experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/da0f513c-35a4-421d-ba1d-9f5b29c6c6bf/download/20230910_rdt-dataset-03-september-2023-09-september-2023-external-district-level.xlsx
  format: null
  id: resource_da0f513c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 03 - 09 September 2023 External District
    Level
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Between 27 August and 2 September 2023, IOM Yemen DTM tracked 30 households
    (180 individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts: Marib (21 HHs) - Marib (10 HHs), Marib
    City (9 HHs), Harib (2 HHs) districts. Most displacements in the governorate originated
    from Marib and Taiz. Al Hodeidah (6 HHs) - Hays (5 HHs), Al Khukhah (1 HH) districts.
    Most displacements in the governorate originated from Taiz and Al Hodeidah. Taiz
    (2 HHs) - Al Mudhaffar (2 HHs) district. All displacements in the governorate
    were internal. The majority of people moved from the following governorates and
    districts: Taiz (9 HHs) - Maqbanah (6 HHs), Al Qahirah (1 HH), Sharab As Salam
    (1 HH) districts. Marib (9 HHs) - Harib (7 HHs), Al Jubah (2 HHs) districts. Al
    Hodeidah (5 HHs) - Al Jarrahi (3 HHs), Al Marawiah (1 HH), Bajil (1 HH) districts.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/df7c1d94-8896-4b3a-82bf-c9d122102c30/download/rdt-dataset-27aug2023-02sep2023-district-level.xlsx
  format: null
  id: resource_df7c1d94
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 27 Aug - 02 Sep 2023 - District Level
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 20 and 26 August 2023, IOM Yemen DTM tracked 41 households
    (HH) (246 individuals)2 who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 80 per cent (33 HHs) of the total followed by economic reasons
    related to conflict, accounting for 20 per cent (8 HHs). From 1 January to 26
    August 2023, IOM Yemen DTM tracked 4,141 households3 (24,846 Individuals) who
    experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/bd633a1a-ae7b-49e0-9010-3358fb049a6a/download/rdt-dataset-20-26-august-2023.xlsx
  format: null
  id: resource_bd633a1a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 20 - 26 August 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 13 and 19 August 2023, IOM Yemen DTM tracked 21 households
    (HH) (126 individuals)2 who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 76 per cent (16 HHs) of the total followed by economic reasons
    related to conflict, accounting for 24 per cent (5 HHs). From 1 January to 19
    August 2023, IOM Yemen DTM tracked 4,078 households3 (24,468 Individuals) who
    experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/62f7f3e2-d18c-4405-96d7-919d44df67a3/download/rdt-dataset-13-august-2023-19-august-2023.xlsx
  format: null
  id: resource_62f7f3e2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 13 August 2023 - 19 August 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 6 and 12 August 2023, IOM Yemen DTM tracked 60 households (HH)
    (360 individuals)2 who experienced displacement at least once. Safety and security
    concerns as a result of the conflict were the main reason for displacement, accounting
    for 97 per cent (58 HHs) of the total followed by economic reasons related to
    conflict, accounting for 3 per cent (2 HHs). From 1 January to 12 August 2023,
    IOM Yemen DTM tracked 4,050 households3 (24,300 Individuals) who experienced displacement
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/b69823d1-66b5-4d8b-8d33-14d3271a7a0a/download/rdt-dataset-06-12-august-2023.xlsm
  format: null
  id: resource_b69823d1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 06 - 12 August 2023.xlsm
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 30 July and 5 August 2023, IOM Yemen DTM tracked 28 households
    (HH) (168 individuals)2 who experienced displacement at least once. Safety and
    security concerns as a result of the conflict were the main reason for displacement,
    accounting for 61 per cent (17 HHs) of the total followed by economic reasons
    related to conflict, accounting for 39 per cent (11 HHs). From 1 January to 5
    August 2023, IOM Yemen DTM tracked 3,964 households3 (23,784 Individuals) who
    experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/d934e026-ff9c-4852-aa79-e4dd80e6c9da/download/rdt-dataset-30-july-2023-05-august-2023.xlsm
  format: null
  id: resource_d934e026
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 30 July 2023 - 05 August 2023.xlsm
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 23 and 29 July 2023, IOM Yemen DTM tracked 48 households (HH)
    (288 individuals)2 who experienced displacement at least once. Safety and security
    concerns as a result of the conflict were the main reason for displacement, accounting
    for 69 per cent (33 HHs) of the total followed by economic reasons related to
    conflict, accounting for 31 per cent (15 HHs). From 1 January to 29 July 2023,
    IOM Yemen DTM tracked 3,882 households3 (23,292 Individuals) who experienced displacement
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/54d06b75-cf07-4028-95e3-f1ca219d6cc3/download/20230730_rdt-dataset-23-29-july-2023.xlsx
  format: null
  id: resource_54d06b75
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 23-29 July 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: During the reporting period, between 1 April and 30 June 2023, IOM
    Yemen DTM tracked 1,016 households (HHs) (6,096 individuals)1 who experienced
    displacement at least once. This represents a 59 per cent drop from the 2,495
    households (14,970 individuals) in the first quarter of 2023. The number of tracked
    new instances of displacement has been declining since the beginning of April
    2022 when a truce began ending in October 2022. The monthly average of household
    displacements in 2023 so far has been 585 with a high of 1,079 in January 2023
    compared to an average of 854 in 2022 with a maximum of 2,453 in January 2022.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/3df49209-f464-4da2-8ed6-96dd57e3adc3/download/20230713_rdt-dataset-01-april-2023-30-june-2023.xlsx
  format: null
  id: resource_3df49209
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking Q2 April to June 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 16 and 22 July 2023, IOM Yemen DTM tracked 61 households (HH)
    (366 individuals)2 who experienced displacement at least once. Safety and security
    concerns as a result of the con?ict were the main reason for displacement, accounting
    for 82 per cent (50 HHs) of the total followed by economic reasons related to
    con?ict, accounting for 18 per cent (11 HHs). From 1 January to 22 July 2023,
    IOM Yemen DTM tracked 3,805 households3 (22,830 Individuals) who experienced displacement
    at least once. DISPLACED
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/0c131b58-035b-4e7f-bcd5-11e70ecc956b/download/20230723_rdt-dataset-16-july-2023-22-july-2023.xlsx
  format: null
  id: resource_0c131b58
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 16 - 22 July 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 09 and 15 July 2023, IOM Yemen DTM tracked 83 households (498
    individuals)2 who experienced displacement at least once. Safety and security
    concerns as a result of the conflict were the main reason for displacement, accounting
    for 84 per cent (70 HHs) of the total and followed by economic reasons related
    to conflict, accounting for 16 per cent (13 HH). From 1 January to 15 July 2023,
    IOM Yemen DTM tracked 3,675 households (HH) (22,050 Individuals) who experienced
    displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/c18b5b0e-1c3c-4f26-8848-e0628fdc3cb5/download/20230716_rdt-dataset-09-july-2023-15-july-2023.xlsx
  format: null
  id: resource_c18b5b0e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 09 - 15 July 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Between 2 and 8 July 2023, IOM Yemen DTM tracked 34 households (204
    individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts: Al Hodeidah (13 HHs) - Hays (13 HHs)
    district. Most displacements in the governorate were internal. Ma''rib (12 HHs)
    - Ma''rib (8 HHs), Harib (3 HHs), Ma''rib City (1 HH) districts. Most displacements
    in the governorate originated from Ma''rib and Al Bayda. Ta''iz (6 HHs) - Jabal
    Habashi (3 HHs), Ash Shamayatayn (3 HHs) districts. All displacements in the governorate
    were internal.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/e820498f-9c98-4eb7-982d-528b4d60c25a/download/20230709_rdt-dataset-02-08july2023external.xlsx
  format: null
  id: resource_e820498f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 02-08July2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Between 25 June and 1 July 2023, IOM Yemen DTM tracked 07 households
    (042 individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts: Al Hodeidah (3 HHs) - Al Khukhah (3
    HHs) district. All displacements in the governorate were internal. Ma''rib (2
    HHs) - Ma''rib (2 HHs) district. Most displacements in the governorate originated
    from Ibb and Dhamar. Ta''iz (1 HH) - Al Misrakh (1 HH) district. All displacements
    in the governorate originated from Amran.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/0a9554ff-b248-41d9-a6de-d6f610691d91/download/20230704_rdt-dataset-25-june-2023-01-july-2023.xlsx
  format: null
  id: resource_0a9554ff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 25 June - 01 July 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Between 18 and 24 June 2023, IOM Yemen DTM tracked 24 households (144
    individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts: Ma''rib (15 HHs) - Ma''rib (6 HHs),
    Ma''rib City (5 HHs), Harib (4 HHs) districts. Most displacements in the governorate
    originated from Ma''rib and Ibb. Al Hodeidah (4 HHs) -Hays (4 HHs) district. All
    displacements in the governorate were internal. Ad Dali (3 HHs) - Ad Dali (3 HHs)
    district. All displacements in the governorate were internal.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/a1e76e90-5c31-46fa-98cf-847dd7527107/download/20230625_rdt-dataset-18-june-2023-24-june-2023.xlsx
  format: null
  id: resource_a1e76e90
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 18 - 24 June 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Between 11 and 17 June 2023, IOM Yemen DTM tracked 37 households (222
    individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts: Ta''iz (17 HHs) - Maqbanah (10 HHs),
    Al Maafer (7 HHs) districts. Most displacements in the governorate were internal.
    Al Hodeidah (12 HHs) - Hays (7 HHs), Al Khukhah (5 HHs) districts. Most displacements
    in the governorate were internal. Ma''rib (7 HHs) - Ma''rib City (5 HHs), Ma''rib
    (2 HHs) districts. Most displacements in the governorate originated from Al Bayda
    and Ta''iz. The majority of people moved from the following governorates and districts:
    Ta''iz (19 HHs) - Maqbanah (18 HHs), Al Mudhaffar (1 HH) districts. Al Hodeidah
    (12 HHs) - At Tuhayta (4 HHs), Jabal Ras (4 HHs), Al Jarrahi (2 HHs) districts.
    Al Bayda (2 HHs) - Dhi Naim (2 HHs) district.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/8b9a0712-724e-41d3-a88a-cb110759e6f4/download/hdx_20230618_rdt-dataset-11-june-2023-17-june-2023.xlsx
  format: null
  id: resource_8b9a0712
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 11 - 17 June 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 10 June 2023, IOM Yemen DTM tracked 3,339 households
    (HH) (20,034 Individuals) who experienced displacement at least once. Between
    4 and 10 June 2023, IOM Yemen DTM tracked 23 households (138 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/edf6c45f-739d-463e-ac5b-f75b02fcccba/download/hdx_rdt-dataset-04-june-2023-10-june-2023-external-district-level.xlsx
  format: null
  id: resource_edf6c45f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 06 - 09 June 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1 January to 3 June 2023, IOM Yemen DTM tracked 3,303 households
    (HH) (19,818 Individuals) who experienced displacement at least once. Between
    28 May and 3 June 2023, IOM Yemen DTM tracked 33 households (198 individuals)
    displaced at least once. The majority of people moved into/within the following
    governorates and districts: Al Hodeidah (23 HHs) - Hays (16 HHs), Al Khukhah (7
    HHs) districts. Most displacements in the governorate originated from Al Hodeidah
    and Ta''iz. Ma''rib (9 HHs) - Ma''rib City (7 HHs), Ma''rib (2 HHs) districts.
    Most displacements in the governorate originated from Sanaa and Hajjah. Ta''iz
    (1 HH) - Sabir Al Mawadim (1 HH) district. All displacements in the governorate
    were internal. The majority of people moved from the following governorates and
    districts: Al Hodeidah (16 HHs) - At Tuhayta (7 HHs), Jabal Ras (4 HHs), Hays
    (4 HHs) districts. Ta''iz (10 HHs) - Maqbanah (8 HHs), Salah (1 HH), Sabir Al
    Mawadim (1 HH) districts. Sanaa (2 HHs) - Bani Matar (1 HH), Nihm (1 HH) districts.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/dc91c658-3cfa-4e4b-af9e-cd244a41eddb/download/20230604_rdt-dataset-28-may-2023-03-june-2023-external-district-level.xlsx
  format: null
  id: resource_dc91c658
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 28 May - 03 June 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 21 and 27 May 2023, IOM Yemen DTM tracked 19 households (114
    individuals) displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/f3946ae2-686d-4f02-895c-62a5d5bd32f2/download/hdx_rdt-dataset-21-may-2023-27-may-2023-external-district-level.xlsx
  format: null
  id: resource_f3946ae2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 21 -27 May 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 14 and 20 May 2023, IOM Yemen DTM tracked 30 households (180
    individuals) displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/8abb0a58-17e8-42da-bfb9-c66c0423361f/download/hdx_20230521_rdt-dataset-14-may-2023-20-may-2023-external-district-level.xlsx
  format: null
  id: resource_8abb0a58
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 14 -20 May 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 7 and 13 May 2023, IOM Yemen DTM tracked 78 households (468
    individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/2c52304d-d421-4e21-9c71-fddd9a05c351/download/hdx_rdt-dataset-07-may-2023-13-may-2023-external-district-level.xlsx
  format: null
  id: resource_2c52304d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 07 -13 May 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 16 and 29 April 2023, IOM Yemen DTM tracked 75 households (450
    individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/c04294f4-49e0-470f-a206-d33188792834/download/hdx_0230430_rdt-dataset-16-april-2023-29-april-2023-external-district-level.xlsx
  format: null
  id: resource_c04294f4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 16 April 2023 - 29 April 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 9 and 15 April 2023, IOM Yemen DTM tracked 103 households (618
    individuals) displaced at least once. The majority of people moved into/within
    the following governorates and districts.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/e878ca2a-e2e9-418a-8563-3eae1d0875dd/download/hdx_20230416_rdt-dataset-09-april-2023-15-april-2023-external-district-level.xlsx
  format: null
  id: resource_e878ca2a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 09 April 2023 - 15A pril 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 2 and 8 April 2023, IOM Yemen DTM tracked 219 households (1,314
    individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/2d0b1718-9f1a-45fa-8930-cd78c7fa3848/download/dtm-yemen-displacement-tracking-02-april-2023-08-april-2023.xlsx
  format: null
  id: resource_2d0b1718
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 02 April 2023 - 08 April 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 26 March and 1 April 2023, IOM Yemen DTM tracked 373 households
    (3,238 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/777c806a-c275-4836-8713-2520988af509/download/dtm-yemen-displacement-tracking-26-march-2023-01-april-2023.xlsx
  format: null
  id: resource_777c806a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 26 March 2023 - 01 April 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 19 and 25 March 2023, IOM Yemen DTM tracked 235 households
    (1,410 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/da15f82f-f9a2-4fac-a953-dd44d5c0c622/download/dtm-yemen-displacement-tracking-19-march-2023-25-march-2023.xlsx
  format: null
  id: resource_da15f82f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 19 March 2023 - 25 March 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 12 and 18 March 2023, IOM Yemen DTM tracked 28 households (168
    individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/0e242ce1-6951-43a6-aa50-75edb4179a63/download/dtm-yemen-displacement-tracking-12-march-2023-18-march-2023.xlsx
  format: null
  id: resource_0e242ce1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 12 March 2023 - 18 March 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 5 and 11 March 2023, IOM Yemen DTM tracked 57 households (342
    individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/15c22224-eb4e-4afa-aaf5-ad330be5e255/download/dtm-yemen-displacement-tracking-05-march-2023-11-march-2023.xlsx
  format: null
  id: resource_15c22224
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 05 March 2023 - 11 March 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 26 February and 4 March 2023, IOM Yemen DTM tracked 78 households
    (468 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/603dfdb8-7035-430e-830b-e5f822b545d8/download/dtm-yemen-displacement-tracking-26-february-2023-04-march-2023.xlsx
  format: null
  id: resource_603dfdb8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 26 February 2023 - 04 March 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 19 and 25 February 2023, IOM Yemen DTM tracked 42 households
    (252 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/e4461410-8e31-4333-97c5-fd78fe1dea4e/download/dtm-yemen-displacement-tracking-19-february-2023-25-february-2023.xlsx
  format: null
  id: resource_e4461410
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 19 February 2023 - 25 February 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 12 and 18 February 2023, IOM Yemen DTM tracked 79 households
    (474 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/9448628d-fb3d-46fb-bdc2-6d7c1495dafb/download/dtm-yemen-displacement-tracking-12-february-2023-18-february-2023.xlsx
  format: null
  id: resource_9448628d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 12 February 2023 - 18 February 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 5 and 11 February 2023, IOM Yemen DTM tracked 84 households
    (504 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/5595da25-5117-46ae-a157-0f529e69fb3e/download/dtm-yemen-displacement-tracking-05-february-2023-11-february-2023.xlsx
  format: null
  id: resource_5595da25
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 05 February 2023 - 11 February 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 29 January and 4 February 2023, IOM Yemen DTM tracked 66 households
    (396 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/52563ecb-ceb6-4431-afab-d9fe9f3ba4ee/download/dtm-yemen-displacement-tracking-29-january-2023-04-february-2023.xlsx
  format: null
  id: resource_52563ecb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 29 January 2023 - 04 February 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 22 and 28 January 2023, IOM Yemen DTM tracked 160 households
    (960 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/489e03ca-6376-4e0f-aa0a-3c86f2c1be94/download/dtm-yemen-displacement-tracking-22-january-2023-28-january-2023.xlsx
  format: null
  id: resource_489e03ca
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 22 January 2023 - 28 January 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 15 and 21 January 2023, IOM Yemen DTM tracked 77 households
    (462 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/f0ee1b11-f54e-420b-8f04-f2a3405d6918/download/dtm-yemen-displacement-tracking-15-january-2023-21-january-2023.xlsx
  format: null
  id: resource_f0ee1b11
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 15 January 2023 - 21 January 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 8 and 14 January 2023, IOM Yemen DTM tracked 115 households
    (690 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/da01cf08-7acf-418c-8c5f-e7fc6f9ea0fe/download/dtm-yemen-displacement-tracking-08-14-january-2023.xlsx
  format: null
  id: resource_da01cf08
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 08-14 January 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between 1 and 7 January 2023, IOM Yemen DTM tracked 353 households
    (2,118 individuals) who experienced displacement at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/ea380f24-3e07-4094-bbeb-4660135dc92e/download/dtm-yemen-displacement-tracking-01-07-january-2023.xlsx
  format: null
  id: resource_ea380f24
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01-07 January 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 1 January to 31 December 2022, IOM Yemen DTM tracked 10,135 households
    (HH) (60,810 Individuals) who experienced displacement at least once. Between
    25 and 31 December 2022, IOM Yemen DTM tracked 35 households (210 individuals)
    displaced at least once. The majority of people moved into/within the following
    governorates and districts: Marib (24 HHs) - Marib City (12 HHs), Marib (9 HHs),
    Harib (3 HHs) districts. Most displacements in the governorate originated from
    Dhamar and Marib. Al Hodeidah (6 HHs) - Hays (4 HHs), Al Khukhah (2 HHs) districts.
    Most displacements in the governorate originated from Taiz and Sanaa. Abyan (5
    HHs) - Khanfar (4 HHs), Zinjibar (1 HHs) districts. Most displacements in the
    governorate originated from Al Hodeidah. The majority of people moved from the
    following governorates and districts: - Taiz (8 HHs) - Al Misrakh (3 HHs), Maqbanah
    (3 HHs), Al Maafer (1 HHs) districts. - Dhamar (6 HHs) - Maghrib Ans (3 HHs),
    Wusab Al Aali (1 HHs), Al Hada (1 HHs) districts. - Al Hodeidah (5 HHs) - Hays
    (3 HHs), Al Jarrahi (1 HHs), Zabid (1 HHs) districts.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/cb9e7228-1e75-4a4b-987f-e38757d700e6/download/20230102_rdt-dataset-25-december-2022-31-december-2022-external-district-level_hdx.xlsx
  format: null
  id: resource_cb9e7228
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 Jan - 31 Dec 2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'From 01 January 2021 to 25 December 2021, IOM Yemen DTM estimates
    that 25,591 households (HH) (153,546 Individuals) have experienced displacement
    at least once. Since the beginning of 2021, DTM also identified 4,440 displaced
    households who left their locations of displacement and either moved back to their
    place of origin or another location. Between 19 and 25 December 2021, IOM Yemen
    DTM tracked 1,164 households (6,984 individuals) displaced at least once. The
    top three governorates and districts where people moved into/within are: - Al
    Jawf (600 HH) - Khab wa Ash Shaf (600 HH) district. All displacements in the governorate
    were internal. - Marib (362 HH) - Marib City (218 HH), Marib (144 HH) districts.
    Most displacements in the governorate were internal. - Al Hodeidah (83 HH) - Al
    Khukhah (83 HH) district. Most displacements in the governorate originated from
    Taiz and Al Hodeidah. Most displacements resulted from the increased conflict
    in the following governorates and districts. - Al Jawf (640 HH) - Barat Al Anan
    (628 HH), Khab wa Ash Shaf (7 HH), Rajuzah (5 HH) districts. - Marib (315 HH)
    - Marib (147 HH), Marib City (125 HH), Al Jubah (28 HH) districts. - Taiz (87
    HH) - Maqbanah (44 HH), Al Makha (41 HH), Sabir Al Mawadim (1 HH) districts.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/b262b64a-827b-4d82-8e43-d8f8c8745a3b/download/20211227_rdt_weekly-update-19-december-25-december-2021-external-district-level_hdx.xlsx
  format: null
  id: resource_b262b64a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 Jan - 25 Dec 2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'In the first eleven months of 2020, conflict (82%) and natural disasters
    (13%) have resulted most of displacements, particularly in Marib, Al Hudaydah,
    Al Dhale''e, Tiaz, Al Jawf, and Hadramaut governorates. Economic conditions, Health,
    COVID-19 and other factors caused rest of 5% displacements. From 01 January 2020
    to 5 December 2020, IOM Yemen DTM estimates that 27,930 Households (167,580 Individuals)
    have experienced displacement at least once. Since the beginning of 2020, DTM
    also identified other 1,319 previously displaced households who left the displaced
    location and moved to either their place of origin or some other displaced location.
    Between 29 November 2020 and 05 December 2020, IOM Yemen DTM tracked 204 Households
    (1,224 individuals) displaced at least once. The highest number of displacements
    were seen in: Taizz (74 HH) - Mawza (18 HH), Al Mudhaffar (10 HH), Al Mukha (9
    HH) districts. Most displacements in the governorate originated from Taizz and
    Al Hudaydah. Marib (74 HH) - Raghwan (50 HH), Marib City (17 HH), Al Jubah (6
    HH) districts. Most displacements in the governorate were internal. Al Dhale''e
    (26 HH) - Ad Dhale''e (17 HH), Al Hussein (5 HH), Ash Shu''ayb (2 HH) districts.
    Most displacements in the governorate originated from Al Dhale''e and Lahj. Most
    displacement resulted from increased conflict in the following governorates and
    districts. Marib (62 HH) - Majzar (50 HH), Rahabah (6 HH), Raghwan (4 HH) districts.
    Taizz (50 HH) - Maqbanah (20 HH), Al Mudhaffar (6 HH), Jabal Habashy (6 HH) districts.
    Al Hudaydah (33 HH) - Ad Durayhimi (13 HH), Al Hali (6 HH), Hays (4 HH) districts.'
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/edd50957-0803-47f6-95bf-e47bf3d6281d/download/yemen-rapid-displacement-tracking-dataset-01-january-05-dec-2020_hdx.xlsx
  format: null
  id: resource_edd50957
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 Jan - 05 Dec 2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In the first Eleven months of 2019, conflict activities have resulted
    in new patterns of displacement, particularly in within Hajjah, Al Dhale'e, Al
    Hudaydah and Taizz governorates. IOM estimates that 65,089 displaced households
    from 01 Jan to 30 Nov 2019 in addition to 6,406 returnee households during 01
    Jul to 30 Nov 2019.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/8c81c4a5-6835-42df-9f58-a312bbd2ac6a/download/dtm-yemen_-rapid-displacement-tracking-rdt-dataset-_01-jan-to-30-nov-2019_hdx.xlsx
  format: null
  id: resource_8c81c4a5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 01 Jan - 30 Nov 2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 25 January 2025, IOM Yemen DTM tracked 127 households
    (HH) (762 Individuals) who experienced displacement at least once. Between 19
    and 25 January 2025, IOM Yemen DTM tracked 23 households (138 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/39bcde9a-9f1c-4978-9420-d1754eff089d/download/20250126_rdt-dataset-19-jan-2025-25-jan-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_39bcde9a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 19 - 25 January 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 18 January 2025, IOM Yemen DTM tracked 101 households
    (HH) (606 Individuals) who experienced displacement at least once. Between 12
    and 18 January 2025, IOM Yemen DTM tracked 29 households (174 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/f58bc821-b04d-4e75-95a5-dddf8a84fa3b/download/20250119_rdt-dataset-12-jan-2025-18-jan-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_f58bc821
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 12 - 18 January 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 11 January 2025, IOM Yemen DTM tracked 063 households
    (HH) (378 Individuals) who experienced displacement at least once. Between 5 and
    11 January 2025, IOM Yemen DTM tracked 33 households (198 individuals) displaced
    at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/b43dd5f7-0f13-4d19-99a5-55a2b87c700e/download/20250112_rdt-dataset-05-jan-2025-11-jan-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_b43dd5f7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 05 - 11 January 2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 1 January to 5 April 2025, IOM Yemen DTM tracked 527 households
    (HH) (3,162 Individuals) who experienced displacement at least once. Between 30
    March and 5 April 2025, IOM Yemen DTM tracked 20 households (120 individuals)
    displaced at least once.
  download_url: https://data.humdata.org/dataset/62cc626a-39c4-431d-964b-7a5600a4684b/resource/f91d8aea-7201-43d2-b553-439083c9e093/download/20250406_rdt-dataset-30-mar-2025-05-apr-2025-external-district-level_hdx.xlsx
  format: null
  id: resource_f91d8aea
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen Displacement Tracking 30 Mar - 05 Apr2025
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_iom_displacementdailytracking_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-14'
  start: '2019-01-01'
temporal_resolution: null
title: Yemen Displacement - Daily Tracking - [IDPs, Returnees] - [IOM DTM]
version: null
vulnerability: null
---
