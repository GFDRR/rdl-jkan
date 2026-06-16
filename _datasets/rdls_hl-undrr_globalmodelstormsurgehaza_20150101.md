---
attributions:
- entity:
    affiliation: null
    email: null
    name: CIMNE
    url: https://data.humdata.org/dataset/storm-surge-hazard-10-years
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Ingeniar
    url: https://data.humdata.org/dataset/storm-surge-hazard-10-years
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/storm-surge-hazard-10-years
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/storm-surge-hazard-10-years
dataset_id: rdls_hl-undrr_globalmodelstormsurgehaza_20150101
description: 'The tropical cyclonic strong wind and storm surge model use information
  from 2594 historical tropical cyclones, topography, terrain roughness, and bathymetry.
  The risk assessment was also conducted by CIMNE and Ingeniar to produced AAL and
  PML values for cyclone risk.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/storm-surge-hazard-10-years]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 1
      events:
      - calculation_method: simulated
        description: Probabilistic storm surge hazard model derived from 2594 historical
          tropical cyclones with inundation depths at 10-year return period
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_flood
          intensity_measure: wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: event_10yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.1
            probability: null
            return_period: 10
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Historical tropical cyclone data from five oceanic basins (2594 events)
    were integrated with topographic, bathymetric, and terrain roughness datasets
    to simulate probabilistic storm surge inundation using CIMNE's cyclone hazard
    model. Risk metrics (AAL and PML) were subsequently calculated by Ingeniar using
    the modeled hazard outputs to quantify expected losses from coastal flooding.
  sources:
  - id: source_1
    license: null
    name: CIMNE
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Ingeniar
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/storm-surge-hazard-10-years
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Annual Average Loss (AAL) and Probable Maximum Loss (PML) from cyclone-driven
      storm surge
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Global model of storm surge hazard 10 years return period (Zipped shapefiles
    of storm surge hazard (7,230 kb))
  download_url: https://data.humdata.org/dataset/87ce9e07-4914-49e6-81cc-3e4913d1ea02/resource/9d30760e-292f-4e81-9f5f-8a526977aa68/download/ss-world.zip
  format: null
  id: resource_9d30760e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SS-world.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global model of storm surge hazard 10 years return period (Geojson
    of storm surge hazard (37,509 kb))
  download_url: https://data.humdata.org/dataset/87ce9e07-4914-49e6-81cc-3e4913d1ea02/resource/db1e1d99-6724-450c-8c2a-271524588f0e/download/ss-world.json
  format: null
  id: resource_db1e1d99
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SS-World.json
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-undrr_globalmodelstormsurgehaza_20150101
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
  start: '2015-01-01'
temporal_resolution: null
title: Global model of storm surge hazard 10 years return period
version: null
vulnerability: null
---
