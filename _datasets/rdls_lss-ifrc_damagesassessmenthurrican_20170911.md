---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/damages-assessment-for-hurricane-irma
creator:
  affiliation: null
  email: null
  name: International Federation of Red Cross and Red Crescent Societies (IFRC)
  url: https://data.humdata.org/dataset/damages-assessment-for-hurricane-irma
dataset_id: rdls_lss-ifrc_damagesassessmenthurrican_20170911
description: 'Includes information from several data sources about Damages and needs
  assessment. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damages-assessment-for-hurricane-irma]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Damages assessment data compiled by IFRC from multiple sources documenting
    post-event impacts of Hurricane Irma. The registry aggregates damage observations
    and needs assessments across affected areas to quantify direct losses to buildings
    and infrastructure.
  sources:
  - id: source_1
    license: null
    name: International Federation of Red Cross and Red Crescent Societies (IFRC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damages-assessment-for-hurricane-irma
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Hurricane Irma
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage and losses from Hurricane Irma
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damages assessment for Hurricane Irma. (Damage assessment)
  download_url: https://docs.google.com/spreadsheets/d/1AGTArx8wiI33xwgmYOgrbcL9foCc_TMYv8JgzZK_dTk/edit?usp=sharing
  format: null
  id: resource_985498a3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hurricane_IRMA_DANA
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ifrc_damagesassessmenthurrican_20170911
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  - ATG
  - BHS
  - BRB
  - CUB
  - DMA
  - DOM
  - GRL
  - HTI
  - JAM
  - MAF
  - PRI
  - KNA
  - LCA
  - VCT
  - TCA
  - VGB
  - VIR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-11'
temporal_resolution: null
title: Damages assessment for Hurricane Irma.
version: null
vulnerability: null
---
