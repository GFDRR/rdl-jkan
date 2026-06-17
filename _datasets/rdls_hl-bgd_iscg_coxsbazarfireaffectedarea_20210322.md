---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Inter Sector Coordination Group
  url: https://data.humdata.org/dataset/cox-s-bazar-fire-incident-area-at-rohingya-refugee-camps-in-march-2021
creator:
  affiliation: null
  email: null
  name: Inter Sector Coordination Group
  url: https://data.humdata.org/dataset/cox-s-bazar-fire-incident-area-at-rohingya-refugee-camps-in-march-2021
dataset_id: rdls_hl-bgd_iscg_coxsbazarfireaffectedarea_20210322
description: 'A massive fire swept through three IOM-managed sites on 22 March 2021
  displacing Rohingya refugees and causing catastrophic damage in the world''s largest
  refugee camp, Cox''s Bazar, Bangladesh.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cox-s-bazar-fire-incident-area-at-rohingya-refugee-camps-in-march-2021]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: wildfire
license: CC-BY-4.0
lineage:
  description: Fire extent was mapped through direct observational data collection
    following the 22 March 2021 wildfire event at three IOM-managed sites in Cox's
    Bazar refugee camps. The resulting shapefile delineates the spatial extent of
    fire-affected areas, enabling quantification of displaced populations and damaged
    shelter infrastructure.
  sources:
  - id: source_1
    license: null
    name: Inter Sector Coordination Group
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cox-s-bazar-fire-incident-area-at-rohingya-refugee-camps-in-march-2021
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from wildfire at refugee camp shelters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
    description: Rohingya refugees displaced by the wildfire event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
  description: 'Bangladesh - Cox''s Bazar: Fire Affected Area at Rohingya Refugee
    Camps (The source of the data is IOM Cox''s Bazar)'
  download_url: https://data.humdata.org/dataset/302060fa-b0b2-41af-8c82-ec12979f8f20/resource/834dc826-4a6d-4d72-9498-1d2980531bfb/download/fire_extent_shapefile.zip
  format: null
  id: resource_834dc826
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Fire_Extent_shapefile.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-bgd_iscg_coxsbazarfireaffectedarea_20210322
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-03-22'
temporal_resolution: null
title: 'Bangladesh - Cox''s Bazar: Fire Affected Area at Rohingya Refugee Camps'
version: null
vulnerability: null
---
