---
attributions:
- entity:
    affiliation: null
    email: null
    name: Indonesia National Disaster Management Agency (BNPB)
    url: https://data.humdata.org/dataset/indonesia-monthly-humanitarian-update
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Indonesia (inactive)
  url: https://data.humdata.org/dataset/indonesia-monthly-humanitarian-update
creator:
  affiliation: null
  email: null
  name: OCHA Indonesia (inactive)
  url: https://data.humdata.org/dataset/indonesia-monthly-humanitarian-update
dataset_id: rdls_lss-idn_ochaidn_monthlyhumanitarianupdate_20191118
description: 'Monthly humanitarian update on disasters event in Indonesia (period
  September - January 2019). [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-monthly-humanitarian-update]'
details: Updates on monthly basis based on information availability
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Monthly humanitarian impact data compiled by OCHA Indonesia from reports
    submitted by Provincial Governments to the National Disaster Management Agency
    (BNPB), documenting affected populations and disaster events across Indonesia
    from September 2018 to January 2019.
  sources:
  - id: source_1
    license: null
    name: Indonesia National Disaster Management Agency (BNPB)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indonesia-monthly-humanitarian-update
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood disasters in Indonesia
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake disasters in Indonesia
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by strong wind/cyclone disasters in Indonesia
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslide disasters in Indonesia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
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
  description: 'Indonesia: Monthly Humanitarian Update (Indonesia Monthly humanitarian
    update (period January 2018 - July 2019))'
  download_url: https://data.humdata.org/dataset/dcad1a8c-74d6-42e5-940c-f3d739f8e0c5/resource/6594f8a0-25f9-48cf-9e2a-bc47213f7cf7/download/mhu-jan-dec2018-idn.xlsx
  format: null
  id: resource_6594f8a0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MHU-Jan-Dec2018-IDN.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: Monthly Humanitarian Update (with HXL-tag)'
  download_url: https://data.humdata.org/dataset/dcad1a8c-74d6-42e5-940c-f3d739f8e0c5/resource/b08078d9-2e5c-4d32-a430-733e1e9e6ed2/download/mhu-jan-dec2019-idn-hxl.csv
  format: null
  id: resource_b08078d9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhu-jan-dec2019-idn-hxl.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idn_ochaidn_monthlyhumanitarianupdate_20191118
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-18'
temporal_resolution: null
title: 'Indonesia: Monthly Humanitarian Update'
version: null
vulnerability: null
---
