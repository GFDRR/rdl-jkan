---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/vanuatu-cyclone-1000966
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-cyclone-1000966
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-cyclone-1000966
dataset_id: rdls_hel-vut_wfpadam_cyclonecategory2mar2023_202303
description: 'ADAM ID: 1000966_3 Cyclone (category 2) during the period Mar 01 2023-Mar
  05 2023 in Vanuatu. It impacted 142418 people.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/vanuatu-cyclone-1000966]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone hazard in affected areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected observed tropical cyclone track geometry,
    classification (Category 2), wind speed measurements, and population exposure
    data for the March 2023 cyclone event in Vanuatu. Geospatial data was processed
    into shapefile format with population impact metrics aggregated by affected administrative
    areas.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/vanuatu-cyclone-1000966
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Category 2 tropical cyclone in Vanuatu
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
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: 'Vanuatu: Cyclone - Category 2 - Mar 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/8653835f-4b3e-4bb4-afa9-28e4a928d5b9/resource/fbd900c8-f606-4dbd-af54-92a31ec6ef32/download/1000966-14-adam-ts-1000966-14-shp.zip
  format: null
  id: resource_fbd900c8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000966-14-adam-ts-1000966-14-shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vut_wfpadam_cyclonecategory2mar2023_202303
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-05'
  start: '2023-03-01'
temporal_resolution: null
title: 'Vanuatu: Cyclone - Category 2 - Mar 2023'
version: null
vulnerability: null
---
