---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2019-data
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2019-data
dataset_id: rdls_lss-unhcr_globaltrendsforceddisplac_20200618
description: 'This dataset contains 22 data tables on global trends in forced displacement
  in 2019. The data provide trends, national level summaries and the demographic composition
  of refugees, asylum-seekers, Venezuelans displaced abroad, internally displaced
  persons (IDPs), returnees (refugees and IDPs), stateless persons, and other persons
  of concern to UNHCR.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2019-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: National governments report forced displacement statistics to UNHCR
    using their own definitions and data collection methodologies. UNHCR aggregates
    these reports into 22 data tables providing global trends, national summaries,
    and demographic composition of displaced populations and persons of concern for
    2019.
  sources:
  - id: source_1
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2019-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and refugees displaced by various hazards
      and conflicts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
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
  - asset_category: population
    asset_dimension: population
    description: Asylum seekers, returnees, stateless persons and other persons of
      concern
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains 22 data tables on global trends in forced displacement
    in 2019. The data provide trends, national level summaries and the demographic
    composition of refugees, asylum-seekers, Venezuelans displaced abroad, internally
    displaced persons (IDPs), returnees (refugees and IDPs), stateless persons, and
    other persons of concern to UNHCR.
  download_url: https://data.humdata.org/dataset/76a164ce-c1c1-4a76-aa47-8a510a65108f/resource/4fdfca50-3e4a-4c7d-a25e-cda569ae5a55/download/19-wrd-tables_v10.xlsx
  format: null
  id: resource_4fdfca50
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 19-WRD-tables_v10.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-unhcr_globaltrendsforceddisplac_20200618
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
  end: null
  start: '2020-06-18'
temporal_resolution: null
title: 'UNHCR Global Trends: Forced Displacement in 2019 Data'
version: null
vulnerability: null
---
