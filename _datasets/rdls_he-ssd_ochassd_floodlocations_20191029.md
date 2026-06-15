---
attributions:
- entity:
    affiliation: null
    email: null
    name: DTM (Displacement Tracking Matrix)
    url: https://data.humdata.org/dataset/south-sudan-flood-locations
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ICWG - Malakal
    url: https://data.humdata.org/dataset/south-sudan-flood-locations
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IRNA - Warrap
    url: https://data.humdata.org/dataset/south-sudan-flood-locations
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: RRC - Aweil
    url: https://data.humdata.org/dataset/south-sudan-flood-locations
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: RRC - Rumbek
    url: https://data.humdata.org/dataset/south-sudan-flood-locations
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/south-sudan-flood-locations
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-flood-locations
creator:
  affiliation: null
  email: null
  name: OCHA South Sudan
  url: https://data.humdata.org/dataset/south-sudan-flood-locations
dataset_id: rdls_he-ssd_ochassd_floodlocations_20191029
description: 'South Sudan flood locations as per end of October 2019. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-flood-locations]'
details: null
exposure:
- asset_type:
    description: Populated places and settlements affected by or located in flood
      areas
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
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood locations were compiled from direct field observations and anecdotal
    reports collected by multiple humanitarian organizations (DTM, ICWG, IRNA, RRC,
    OCHA) across South Sudan as of October 29, 2019. Data represents observed flood
    extents at populated settlements and locations, aggregated from regional assessments
    and humanitarian coordination mechanisms.
  sources:
  - id: source_1
    license: null
    name: DTM (Displacement Tracking Matrix)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: ICWG - Malakal
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: IRNA - Warrap
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: RRC - Aweil
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_5
    license: null
    name: RRC - Rumbek
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_6
    license: null
    name: OCHA
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-flood-locations
  rel: source
loss:
  losses: []
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
  description: 'South Sudan : Flood Locations (South sudan flood locations as per
    end of October 2019)'
  download_url: https://data.humdata.org/dataset/a0a190d5-09af-49a8-87ba-83d91bfdab30/resource/7c454f75-ea6e-4361-98ab-e12baa31cb20/download/20191029_dtm_floods_locations.xlsx
  format: null
  id: resource_7c454f75
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sudan 20191029_DTM_floods_locations.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-ssd_ochassd_floodlocations_20191029
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-29'
temporal_resolution: null
title: 'South Sudan : Flood Locations'
version: null
vulnerability: null
---
