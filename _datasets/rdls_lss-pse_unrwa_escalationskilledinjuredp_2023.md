---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ministry of Health in Gaza
    url: https://data.humdata.org/dataset/escalations-in-gaza-key-figures
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations Relief and Works Agency for Palestine Refugees in the Near
      East (UNRWA)
    url: https://data.humdata.org/dataset/escalations-in-gaza-key-figures
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Relief and Works Agency for Palestine Refugees in the Near
    East
  url: https://data.humdata.org/dataset/escalations-in-gaza-key-figures
creator:
  affiliation: null
  email: null
  name: United Nations Relief and Works Agency for Palestine Refugees in the Near
    East
  url: https://data.humdata.org/dataset/escalations-in-gaza-key-figures
dataset_id: rdls_lss-pse_unrwa_escalationskilledinjuredp_2023
description: 'Dataset containing data on killed & injured Persons in Gaza.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/escalations-in-gaza-key-figures]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Casualty data collected through direct observation and anecdotal reporting
    by the Ministry of Health in Gaza and compiled by UNRWA. Records document killed
    and injured persons resulting from the 2023 escalation in Gaza, aggregated from
    health facility reports and field assessments.
  sources:
  - id: source_1
    license: null
    name: Ministry of Health in Gaza
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: United Nations Relief and Works Agency for Palestine Refugees in the Near
      East (UNRWA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/escalations-in-gaza-key-figures
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct fatalities from conflict-violence escalation in Gaza
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
    description: Direct injuries from conflict-violence escalation in Gaza
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Escalations in Gaza - Killed & Injured Persons in Gaza
    (Data on killed & injured Persons in Gaza.)
  download_url: https://docs.google.com/spreadsheets/d/1TNL1kx13vPC6KmpB8CFeEqjjj-ea7DP6X4BFOGsD_ew/edit?https://docs.google.com/spreadsheets/d/1TNL1kx13vPC6KmpB8CFeEqjjj-ea7DP6X4BFOGsD_ew/edit?usp=sharing
  format: null
  id: resource_b87bbff0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Data on Killed and Injured Persons - Gaza 2023
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_unrwa_escalationskilledinjuredp_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-03-15'
  start: '2023-10-07'
temporal_resolution: null
title: Palestine - Escalations in Gaza - Killed & Injured Persons in Gaza
version: null
vulnerability: null
---
