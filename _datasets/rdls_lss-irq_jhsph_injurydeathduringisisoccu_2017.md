---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Johns Hopkins School of Public Health
  url: https://data.humdata.org/dataset/injury-and-death-during-the-isis-occupation-of-mosul-and-its-liberation
creator:
  affiliation: null
  email: null
  name: Johns Hopkins School of Public Health
  url: https://data.humdata.org/dataset/injury-and-death-during-the-isis-occupation-of-mosul-and-its-liberation
dataset_id: rdls_lss-irq_jhsph_injurydeathduringisisoccu_2017
description: 'This is the minimal underlying dataset for a forthcoming manuscript
  presenting results from a cross-sectional survey aimed at measuring deaths, injuries,
  and kidnapping in Mosul households during the 29 months of ISIS control and the
  8 months of Iraqi military action during the liberation.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/injury-and-death-during-the-isis-occupation-of-mosul-and-its-liberation]'
details: Please disregard the 'expected update frequency.' This was a cross sectional
  survey and will not be conducted again.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Cross-sectional household survey conducted in Mosul to measure mortality,
    morbidity, and kidnapping outcomes during the ISIS occupation (29 months) and
    subsequent Iraqi military liberation operations (8 months). Survey data were compiled
    into a minimal dataset for epidemiological analysis of conflict-related health
    impacts.
  sources:
  - id: source_1
    license: null
    name: Johns Hopkins School of Public Health
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/injury-and-death-during-the-isis-occupation-of-mosul-and-its-liberation
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Deaths among Mosul households during ISIS occupation and military
      liberation operations
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
    description: Injuries among Mosul households during ISIS occupation and military
      liberation operations
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Minimal underlying dataset for assessment of mortality in and injuries
    in Mosul from mid-2014 through mid-2017
  download_url: https://data.humdata.org/dataset/7a0ba837-2798-4bae-a0cf-525a297c0033/resource/b2c9a14a-91c3-47e0-afa5-44ba9e033f77/download/mosul_deaths_injuries_min_dataset_21jan2018.xls
  format: null
  id: resource_b2c9a14a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mosul_Deaths_Injuries_Min_Dataset
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_jhsph_injurydeathduringisisoccu_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-07-31'
  start: '2017-03-01'
temporal_resolution: null
title: Iraq - Injury and death during the ISIS occupation of Mosul and its liberation
version: null
vulnerability: null
---
