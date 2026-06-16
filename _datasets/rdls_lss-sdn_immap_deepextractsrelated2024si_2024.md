---
attributions:
- entity:
    affiliation: null
    email: null
    name: DFS (Displacement and Food Security)
    url: https://data.humdata.org/dataset/deep-extracts-sudan-2024-situational-analyses
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/deep-extracts-sudan-2024-situational-analyses
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/deep-extracts-sudan-2024-situational-analyses
dataset_id: rdls_lss-sdn_immap_deepextractsrelated2024si_2024
description: 'Monthly DEEP extracts related to the Sudan Situational Analyses conducted
  by DFS and iMMAP Inc. They are provided by sector and operational environment themes.
  DOCX files contain the screenshot of the visuals used as DEEP entries. XLSX files
  contain links to the screenshots stored in the DEEP platform.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/deep-extracts-sudan-2024-situational-analyses]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: DFS analysts and Information Management Officers collate available
    information daily from multiple sources into the DEEP platform, tagging entries
    according to the DFS/iMMAP Sudan Crisis Framework based on JIAF pillars. Monthly
    extracts are organized by sector (agriculture, casualties, displacement, food
    security, health, etc.) and operational environment themes, with source verification
    and reliability assessments included.
  sources:
  - id: source_1
    license: null
    name: DFS (Displacement and Food Security)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: iMMAP Inc.
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/deep-extracts-sudan-2024-situational-analyses
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Casualty figures from conflict-related incidents in Sudan
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement from conflict and insecurity in Sudan
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
  description: DEEP January Extract, Agriculture, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/49581913-4d38-4cd0-9ed3-5d83613abca5/download/sdn_deep_extracts_2024-01_agriculture_immap_dfs.xlsx
  format: null
  id: resource_49581913
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Agriculture_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Casualties, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/52a251a2-5bed-4a0f-84da-c33250434590/download/sdn_deep_extracts_2024-01_casualties_immap_dfs.xlsx
  format: null
  id: resource_52a251a2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Casualties_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Conflict, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/3579bff2-8589-4aba-8927-0441b36f677b/download/sdn_deep_extracts_2024-01_conflict_immap_dfs.xlsx
  format: null
  id: resource_3579bff2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Conflict_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Context, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/2e1d28c2-f9d3-4d9f-87ed-26356604eb3c/download/sdn_deep_extracts_2024-01_context_immap_dfs.xlsx
  format: null
  id: resource_2e1d28c2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Context_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Cross, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/0b29abab-2601-43a4-a0ca-4ff8afb7bd73/download/sdn_deep_extracts_2024-01_cross_immap_dfs.xlsx
  format: null
  id: resource_0b29abab
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Cross_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Displacement, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/900eefe7-af65-4c93-a2a1-be2271ef0040/download/sdn_deep_extracts_2024-01_displacement_immap_dfs.xlsx
  format: null
  id: resource_900eefe7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Displacement_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Education, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/a1688f1a-a41c-4912-bd89-294246197ba0/download/sdn_deep_extracts_2024-01_education_immap_dfs.xlsx
  format: null
  id: resource_a1688f1a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Education_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Food, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/22c1533b-7e5d-448f-ba4f-069519c3e4d9/download/sdn_deep_extracts_2024-01_food_immap_dfs.xlsx
  format: null
  id: resource_22c1533b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Food_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Health, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/506544e8-0a7b-4b14-bce9-19a72b00486f/download/sdn_deep_extracts_2024-01_health_immap_dfs.xlsx
  format: null
  id: resource_506544e8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Health_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Humanitarian Access, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/43cd6e3f-e061-46f7-a115-043455b6b1ee/download/sdn_deep_extracts_2024-01_humanitarian_access_immap_dfs.xlsx
  format: null
  id: resource_43cd6e3f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Humanitarian_Access_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Information and Communication, 1 Jan. 2024 -
    31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/fead6c44-a94d-4bbf-ba77-548fb44cfd38/download/sdn_deep_extracts_2024-01_information_and_communication_immap_dfs.xlsx
  format: null
  id: resource_fead6c44
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Information_and_Communication_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Livelihood, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/bd68a2a5-f766-4cea-8e4f-e8bf768be2cd/download/sdn_deep_extracts_2024-01_livelihood_immap_dfs.xlsx
  format: null
  id: resource_bd68a2a5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Livelihood_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Logistic, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/804741ef-d68a-47a0-a7e3-860990459f20/download/sdn_deep_extracts_2024-01_logistic_immap_dfs.xlsx
  format: null
  id: resource_804741ef
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Logistic_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Nutrition, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/1a62e9d7-db28-4809-94ba-9be5a1c4e4e5/download/sdn_deep_extracts_2024-01_nutrition_immap_dfs.xlsx
  format: null
  id: resource_1a62e9d7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Nutrition_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Protection, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/f67330d0-0301-4984-aefa-149d76a44465/download/sdn_deep_extracts_2024-01_protection_immap_dfs.xlsx
  format: null
  id: resource_f67330d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Protection_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Shelter, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/0e48fa88-9839-461c-bf13-29bca37dd1d3/download/sdn_deep_extracts_2024-01_shelter_immap_dfs.xlsx
  format: null
  id: resource_0e48fa88
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Shelter_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, Shock, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/b692e36c-e9f2-43c2-ac36-d64acf33bff0/download/sdn_deep_extracts_2024-01_shock_immap_dfs.xlsx
  format: null
  id: resource_b692e36c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_Shock_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP January Extract, WASH, 1 Jan. 2024 - 31 Jan. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/299cb413-a7d2-4a25-8bfa-eb24d04a2587/download/sdn_deep_extracts_2024-01_wash_immap_dfs.xlsx
  format: null
  id: resource_299cb413
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-01_WASH_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Agriculture, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/309bd9b7-2ae8-4e9e-b950-a24e7c60ac58/download/sdn_deep_extracts_2024-02_agriculture_immap_dfs.xlsx
  format: null
  id: resource_309bd9b7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Agriculture_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Casualties, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/076d0a26-36e5-48ef-8b9d-05371887bece/download/sdn_deep_extracts_2024-02_casualties_immap_dfs.xlsx
  format: null
  id: resource_076d0a26
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Casualties_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Conflict, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/bca0930b-81c8-4242-915e-64c5520572fe/download/sdn_deep_extracts_2024-02_conflict_immap_dfs.xlsx
  format: null
  id: resource_bca0930b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Conflict_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Context, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/ff969f80-e294-4b9e-8dbd-a493982fbb7a/download/sdn_deep_extracts_2024-02_context_immap_dfs.xlsx
  format: null
  id: resource_ff969f80
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Context_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Cross, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/a06d7565-6899-4709-8491-49137c7f59ff/download/sdn_deep_extracts_2024-02_cross_immap_dfs.xlsx
  format: null
  id: resource_a06d7565
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Cross_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Displacement, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/fbf0ab43-0d57-4f6f-bae9-7098e2a9e822/download/sdn_deep_extracts_2024-02_displacement_immap_dfs.xlsx
  format: null
  id: resource_fbf0ab43
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Displacement_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Education, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/f2a70b27-a1eb-4966-907b-fd3f01dfbffb/download/sdn_deep_extracts_2024-02_education_immap_dfs.xlsx
  format: null
  id: resource_f2a70b27
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Education_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Event and Shock, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/3d0dc895-7b5b-49b3-b1bf-37dd674875f5/download/sdn_deep_extracts_2024-02_event-and-shock_immap_dfs.xlsx
  format: null
  id: resource_3d0dc895
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Event and Shock_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Food, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/d5bfb732-a300-4a57-8451-5f88d94d8aaa/download/sdn_deep_extracts_2024-02_food_immap_dfs.xlsx
  format: null
  id: resource_d5bfb732
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Food_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Health, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/f7b9f44f-f35d-49fe-8929-e207b4fa94ec/download/sdn_deep_extracts_2024-02_health_immap_dfs.xlsx
  format: null
  id: resource_f7b9f44f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Health_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Humanitarian Access, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/d5c433d1-4cce-4fac-8c51-bac763308160/download/sdn_deep_extracts_2024-02_humanitarian-access_immap_dfs.xlsx
  format: null
  id: resource_d5c433d1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Humanitarian Access_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Information and Communication, 1 Feb. 2024 -
    29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/779b31b1-da29-49eb-9366-db1b838c68e0/download/sdn_deep_extracts_2024-02_information-and-communication_immap_dfs.xlsx
  format: null
  id: resource_779b31b1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Information and Communication_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Livelihood, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/686bb8cf-f754-478e-9cc9-6f5a9d6fe11a/download/sdn_deep_extracts_2024-02_livelihood_immap_dfs.xlsx
  format: null
  id: resource_686bb8cf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Livelihood_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Logistics, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/34b89339-124d-48c3-84fe-2bca33b43c4b/download/sdn_deep_extracts_2024-02_logistics_immap_dfs.xlsx
  format: null
  id: resource_34b89339
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Logistics_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Nutrition, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/17e0cf4d-cd19-4071-8060-9cf7396a0e63/download/sdn_deep_extracts_2024-02_nutrition_immap_dfs.xlsx
  format: null
  id: resource_17e0cf4d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Nutrition_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Protection, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/038815c6-a558-46ae-873c-8d58d144ef5c/download/sdn_deep_extracts_2024-02_protection_immap_dfs.xlsx
  format: null
  id: resource_038815c6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Protection_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, Shelter, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/88b3cc7a-b5c5-4df0-9771-93ee8f785b3f/download/sdn_deep_extracts_2024-02_shelter_immap_dfs.xlsx
  format: null
  id: resource_88b3cc7a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_Shelter_immap_dfs.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DEEP February Extract, WASH, 1 Feb. 2024 - 29 Feb. 2024
  download_url: https://data.humdata.org/dataset/9f81de68-4bba-4a66-9c77-10658f6d4f69/resource/eebc2247-680f-452f-aed5-b0fb2a452722/download/sdn_deep_extracts_2024-02_wash_immap_dfs.xlsx
  format: null
  id: resource_eebc2247
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_DEEP_extracts_2024-02_WASH_immap_dfs.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_immap_deepextractsrelated2024si_2024
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
  end: '2024-02-29'
  start: '2024-01-01'
temporal_resolution: null
title: DEEP extracts related to the Sudan 2024 Situational Analyses
version: null
vulnerability: null
---
