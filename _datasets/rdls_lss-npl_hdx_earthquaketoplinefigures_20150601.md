---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN RCO (Nepal)
    url: https://data.humdata.org/dataset/nep-earthquake-topline-figure
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/nep-earthquake-topline-figure
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/nep-earthquake-topline-figure
dataset_id: rdls_lss-npl_hdx_earthquaketoplinefigures_20150601
description: 'Topline figures dataset for the Nepal Earthquake crisis page. Figures
  for Number of People in Need of Assistance are sourced from the UN RCO (Nepal) situation
  reports .. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nep-earthquake-topline-figure]'
details: This dataset contains data about an ongoing situation.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Topline figures aggregated from UN RCO situation reports documenting
    humanitarian needs and impacts from the Nepal earthquake crisis. Data represents
    direct observational records of affected populations requiring assistance.
  sources:
  - id: source_1
    license: null
    name: UN RCO (Nepal)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nep-earthquake-topline-figure
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Number of people in need of assistance following the Nepal earthquake
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal Earthquake Topline Figures (Flat CSV file.)
  download_url: https://docs.google.com/spreadsheets/d/1V8cK8LJnRHS1BIx34KzG8z1Z4mR7hE_R-PW-wTFj4hI/export?format=csv
  format: null
  id: resource_a699046b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: topline_figures.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_hdx_earthquaketoplinefigures_20150601
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-06-01'
temporal_resolution: null
title: Nepal Earthquake Topline Figures
version: null
vulnerability: null
---
