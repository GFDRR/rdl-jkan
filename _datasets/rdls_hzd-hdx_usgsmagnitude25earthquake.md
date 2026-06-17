---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS
    url: https://data.humdata.org/dataset/usgs-magnitude-2-5-earthquakes
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/usgs-magnitude-2-5-earthquakes
creator:
  affiliation: null
  email: null
  name: USGS
  url: https://data.humdata.org/dataset/usgs-magnitude-2-5-earthquakes
dataset_id: rdls_hzd-hdx_usgsmagnitude25earthquake
description: 'This data lists events with magnitude 2.5+ which have been located by
  the USGS and contributing agencies within the last day and last week. To see these
  events in an interactive map, see the USGS map . For more information, see the USGS
  site .. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/usgs-magnitude-2-5-earthquakes]'
details: These events should not be considered to be complete lists of all events
  in the U.S. and adjacent areas and especially should not be considered to be complete
  lists of all events M4.5+ in the world.
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
      intensity_measure: mag:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-4.0
lineage:
  description: USGS and contributing agencies detect and locate earthquake events
    in real-time using seismic networks. Events with magnitude 2.5 and above are compiled
    into near-real-time catalogs updated daily, with derived intensity metrics (Community
    Decimal Intensity, Modified Mercalli Intensity) calculated from felt reports and
    instrumental data.
  sources:
  - id: source_1
    license: null
    name: USGS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/usgs-magnitude-2-5-earthquakes
  rel: source
loss: null
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
  description: USGS Magnitude 2.5+ Earthquakes, Past Day (geojson)
  download_url: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson
  format: null
  id: resource_d32557f8
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USGS Magnitude 2.5+ Earthquakes, Past Day (geojson)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: USGS Magnitude 2.5+ Earthquakes, Past Day (csv)
  download_url: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.csv
  format: null
  id: resource_80dd31c5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USGS Magnitude 2.5+ Earthquakes, Past Day (csv)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: USGS Magnitude 2.5+ Earthquakes, Past Week (geojson)
  download_url: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson
  format: null
  id: resource_e9ec6d6a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USGS Magnitude 2.5+ Earthquakes, Past Week (geojson)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: USGS Magnitude 2.5+ Earthquakes, Past Week (csv)
  download_url: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv
  format: null
  id: resource_169aafca
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: USGS Magnitude 2.5+ Earthquakes, Past Week (csv)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hdx_usgsmagnitude25earthquake
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: USGS Magnitude 2.5+ Earthquakes
version: null
vulnerability: null
---
