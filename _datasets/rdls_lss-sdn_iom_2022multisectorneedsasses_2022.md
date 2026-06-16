---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-2022-multisector-needs-assessment-msna-data-analysis
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-2022-multisector-needs-assessment-msna-data-analysis
dataset_id: rdls_lss-sdn_iom_2022multisectorneedsasses_2022
description: 'This is the 2022 multisector needs analysis data (MSNA) - a comprehensive
  household-level analysis covering all states in Sudan.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/sudan-2022-multisector-needs-assessment-msna-data-analysis]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Household-level survey data collected by IOM across all Sudanese states
    using DTM (Displacement Tracking Matrix) standard methodology. The assessment
    captures multisector humanitarian needs and impacts across health, shelter, WASH,
    and NFI sectors, representing post-event or ongoing crisis impact documentation
    rather than hazard or exposure inventories.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-2022-multisector-needs-assessment-msna-data-analysis
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multisector needs assessment capturing flood-affected populations
      across Sudan
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
  - asset_category: population
    asset_dimension: population
    description: Multisector needs assessment capturing drought-affected populations
      across Sudan
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
  description: Sudan - 2022 Multisector Needs Assessment (MSNA) - Analysis Data (SUD_MSNA__2022_Data
    Tables_with refugee_external.xlsx)
  download_url: https://data.humdata.org/dataset/74a84e17-ca2c-4450-ae0c-0bf6f86e9896/resource/5786cca2-b797-4fc1-9489-3e8d2b6fedb6/download/sud_msna__2022_data-tables_with-refugee_external.xlsx
  format: null
  id: resource_5786cca2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SUD_MSNA__2022_Data Tables_with refugee_external.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_iom_2022multisectorneedsasses_2022
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
  end: '2022-07-31'
  start: '2022-06-01'
temporal_resolution: null
title: Sudan - 2022 Multisector Needs Assessment (MSNA) - Analysis Data
version: null
vulnerability: null
---
