---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-msna-2021
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/sudan-msna-2021
dataset_id: rdls_lss-sdn_iom_2021multisectorneedsanaly_20210831
description: 'This is the 2021 multisector needs analysis data (MSNA) - a comprehensive
  household-level analysis covering all states in Sudan.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/sudan-msna-2021]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The 2021 MSNA was conducted by IOM using DTM (Displacement Tracking
    Matrix) standard methodology as a comprehensive household-level survey across
    all Sudanese states. The dataset aggregates multisector needs data (education,
    health, nutrition, WASH) to assess humanitarian impacts and sectoral vulnerabilities
    at the population level.
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
- href: https://data.humdata.org/dataset/sudan-msna-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Multisector needs assessment capturing affected populations across
      health, nutrition, WASH, and education sectors
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
  description: Sudan - 2021 Multisector Needs Analysis(MSNA) (SUD_MSNA_Data Tables)
  download_url: https://data.humdata.org/dataset/952c64c3-2d94-4471-9d45-fd6ff49a6a27/resource/3bcec4e8-96ef-4c84-90c1-b88ba22bf601/download/sud_msna_data-tables_ext.xlsx
  format: null
  id: resource_3bcec4e8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SUD_MSNA_Data Tables
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_iom_2021multisectorneedsanaly_20210831
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
  end: null
  start: '2021-08-31'
temporal_resolution: null
title: Sudan - 2021 Multisector Needs Analysis(MSNA)
version: null
vulnerability: null
---
