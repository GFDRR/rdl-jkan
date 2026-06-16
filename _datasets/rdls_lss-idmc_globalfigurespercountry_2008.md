---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/world-internal-displacement-figures-per-country
creator:
  affiliation: null
  email: null
  name: Internal Displacement Monitoring Centre (IDMC)
  url: https://data.humdata.org/dataset/world-internal-displacement-figures-per-country
dataset_id: rdls_lss-idmc_globalfigurespercountry_2008
description: 'Internal displacement figures per country. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/world-internal-displacement-figures-per-country]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDMC collects and aggregates internal displacement data from multiple
    sources including government reports, humanitarian assessments, and field monitoring
    across countries. Data is compiled into a global database tracking displacement
    figures by country and triggering hazard type, providing post-event impact records
    for disaster risk analysis.
  sources:
  - id: source_1
    license: null
    name: Internal Displacement Monitoring Centre (IDMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/world-internal-displacement-figures-per-country
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internal displacement figures resulting from various hazards including
      floods
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internal displacement figures resulting from earthquakes
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internal displacement figures resulting from wildfires
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
    description: Internal displacement figures resulting from storms and cyclones
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.internal-displacement.org/database/methodology
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global Internal Displacement Figures Per Country (Excel)
  download_url: https://data.humdata.org/dataset/23c87a9e-22e0-4b7d-9ca0-43a532913ba3/resource/cbbb2b0e-c6b2-4d12-826c-213cc0d0fdb4/download/idmc_displacement_all_dataset2.xlsx
  format: null
  id: resource_cbbb2b0e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: idmc_displacement_all_dataset2.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idmc_globalfigurespercountry_2008
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
  end: '2018-12-31'
  start: '2008-01-01'
temporal_resolution: null
title: Global Internal Displacement Figures Per Country
version: null
vulnerability: null
---
