---
attributions:
- entity:
    affiliation: null
    email: null
    name: GRFC partners
    url: https://data.humdata.org/dataset/fsin-grfc
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Food Security Information Network
  url: https://data.humdata.org/dataset/fsin-grfc
creator:
  affiliation: null
  email: null
  name: Food Security Information Network
  url: https://data.humdata.org/dataset/fsin-grfc
dataset_id: rdls_lss-fsin_globalreportcrises2025_2016
description: 'The Global Report on Food Crises (GRFC) 2025 provides a global assessment
  of the world''s food and nutrition crises. Data are available from 2017 to 2025
  as in the latest GRFC edition. Data in the various GRFC editions refer more specifically
  to a subset of the world''s identified food and nutrition crises for which data
  was available and meeting the GRFC partnership consensus. The GRFC aims at responding
  to conflicting information derived from different sources and based on different
  methodologies that lack a consensus-based standard by providing information based
  on a rigorous methodology and a highly consultative process.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/fsin-grfc]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The GRFC aggregates food security assessments from multiple partner
    organizations using standardized IPC methodology to classify populations into
    food insecurity phases (1-5). Data are compiled from 2017-2025 across countries
    experiencing identified food and nutrition crises, with population counts stratified
    by IPC phase and crisis drivers (drought, conflict, economic shocks, etc.). The
    dataset provides consensus-based impact estimates addressing methodological inconsistencies
    across disparate food security information sources.
  sources:
  - id: source_1
    license: null
    name: Food Security Information Network
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: GRFC partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fsin-grfc
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population in food insecurity phases (IPC Phase 3+) due to food crises
      driven by drought and other hazards
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Global Report on Food Crises (GRFC) 2025 September Update provides
    the latest data on acute food insecurity and acute malnutrition as of August 2025.
  download_url: https://data.humdata.org/dataset/9fbae50f-9f74-4946-bd2b-a779af116ba4/resource/82ec0f74-db68-4b49-b300-3f469eff2a0d/download/grfc_afi_database_2016-2025_september_update.xlsx
  format: null
  id: resource_82ec0f74
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: grfc_afi_database_2016-2025_september_update.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Report on Food Crises 2025 (Acute malnutrition database from
    2022 to 2024.)
  download_url: https://data.humdata.org/dataset/9fbae50f-9f74-4946-bd2b-a779af116ba4/resource/e85fa452-4f7e-4c12-b95f-387b7e2ad564/download/grfc_amn_database_2022-2024.xlsx
  format: null
  id: resource_e85fa452
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: grfc_amn_database_2022-2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Global Report on Food Crises (GRFC) 2024 Mid-Year Update is an
    update of the GRFC 2024 and provides the latest data on acute food insecurity
    and acute malnutrition as of August 2024.
  download_url: https://data.humdata.org/dataset/9fbae50f-9f74-4946-bd2b-a779af116ba4/resource/434a224b-9996-4ed2-8228-7ff05e7a4147/download/grfc_database_2016-2024-myu.xlsx
  format: null
  id: resource_434a224b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRFC_Database_2017-2024-MYU.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Report on Food Crises 2025 (Acute food insecurity database from
    2016 to 2024.)
  download_url: https://data.humdata.org/dataset/9fbae50f-9f74-4946-bd2b-a779af116ba4/resource/0f1e5a5d-c12d-4de5-b8c0-6102a6833b0c/download/grfc_afi_database_2016-2024.xlsx
  format: null
  id: resource_0f1e5a5d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: grfc_afi_database_2016-2024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-fsin_globalreportcrises2025_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-22'
  start: '2016-01-01'
temporal_resolution: null
title: Global Report on Food Crises 2025
version: null
vulnerability: null
---
