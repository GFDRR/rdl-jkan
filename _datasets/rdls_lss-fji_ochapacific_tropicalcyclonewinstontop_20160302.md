---
attributions:
- entity:
    affiliation: null
    email: null
    name: Fiji Government
    url: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Fiji NEOC/NDMO
    url: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: PHT Partners
    url: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NGO Community
    url: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Office of the Pacific Islands
  url: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures
creator:
  affiliation: null
  email: null
  name: OCHA Office of the Pacific Islands
  url: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures
dataset_id: rdls_lss-fji_ochapacific_tropicalcyclonewinstontop_20160302
description: 'Topline figures dataset for the Fiji Tropical Cyclone Winston disaster.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Topline figures aggregated from multiple sources including Fiji Government,
    NEOC/NDMO, and NGO partners documenting post-event impacts from Tropical Cyclone
    Winston. Data compiled by OCHA Pacific Islands office to provide consolidated
    impact metrics across affected populations and infrastructure.
  sources:
  - id: source_1
    license: null
    name: Fiji Government
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Fiji NEOC/NDMO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: PHT Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: NGO Community
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fiji-tropical-cyclone-winston-topline-figures
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone winds
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone Winston
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displaced by tropical cyclone Winston
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
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
    description: Fatalities from tropical cyclone Winston
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_4
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
  description: Fiji Tropical Cyclone Winston Topline Figures (Flat CSV file)
  download_url: https://docs.google.com/spreadsheets/d/1ObwjZNS8y_mdjNXjhPLSqi-YGtQxkCDIW3Vg2kpwjgs/export?format=csv&id=1ObwjZNS8y_mdjNXjhPLSqi-YGtQxkCDIW3Vg2kpwjgs&gid=0
  format: null
  id: resource_bfa6b55f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Fiji Tropical Cyclone Winston Topline Figures.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-fji_ochapacific_tropicalcyclonewinstontop_20160302
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-03-02'
temporal_resolution: null
title: Fiji Tropical Cyclone Winston Topline Figures
version: null
vulnerability: null
---
