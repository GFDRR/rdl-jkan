---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA MODIS
    url: https://data.humdata.org/dataset/nigeria-flood-extents-nov-2012-fod
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Nigeria
  url: https://data.humdata.org/dataset/nigeria-flood-extents-nov-2012-fod
creator:
  affiliation: null
  email: null
  name: OCHA Nigeria
  url: https://data.humdata.org/dataset/nigeria-flood-extents-nov-2012-fod
dataset_id: rdls_hzd-nga_ochanga_floodextentsnov2012_20121101
description: 'The dataset represents the extent of floods in Nigeria from July to
  November 2012.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nigeria-flood-extents-nov-2012-fod]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: MODIS satellite imagery from NASA was analyzed to delineate flood extent
    boundaries across Nigeria during the July-November 2012 flood event. The 250-meter
    resolution imagery was processed to identify inundated areas and vectorized into
    spatial polygons representing the observed flood footprint.
  sources:
  - id: source_1
    license: null
    name: NASA MODIS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nigeria-flood-extents-nov-2012-fod
  rel: source
loss: null
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
  description: Nigeria - Flood Extents Nov 2012 (Shapefile)
  download_url: https://data.humdata.org/dataset/bd3b4ef6-0a96-4346-b229-2c410d9c6c6d/resource/3c6a77da-be1a-4437-b04f-9e1a47a601a7/download/nga-floods-2012-shp.zip
  format: null
  id: resource_3c6a77da
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nga_floods_2012.shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-nga_ochanga_floodextentsnov2012_20121101
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2012-11-01'
temporal_resolution: null
title: Nigeria - Flood Extents Nov 2012
version: null
vulnerability: null
---
