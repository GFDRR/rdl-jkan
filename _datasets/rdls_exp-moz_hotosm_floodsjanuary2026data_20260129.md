---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/moz-floods-january-2026-openstreetmap-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Copernicus Emergency Management Service (EMSR857)
    url: https://data.humdata.org/dataset/moz-floods-january-2026-openstreetmap-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/moz-floods-january-2026-openstreetmap-data
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/moz-floods-january-2026-openstreetmap-data
dataset_id: rdls_exp-moz_hotosm_floodsjanuary2026data_20260129
description: 'This dataset contains OpenStreetMap data exported from the HOTOSM disaster
  mapping in response to flooding events in the Gaza, Maputo and Maputo City Provinces
  of Mozambique (GLIDE: FL-2026-000004-MOZ) in early 2026. Severe flooding in Mozambique
  has affected more than half a million people following heavy rains in the first
  weeks of the new year. Gaza province has been hit hardest, alongside Maputo and
  Sofala provinces. The OSM extract below is based on Copernicus'' flood extend from
  29 January 2026. The first disaster response mapping project focuses on settlements
  around Chicumbane in the Province of Gaza. The data has been contributed by volunteers
  through the Humanitarian OpenStreetMap Team''s Tasking Manager and represents buildings
  and roads in the affected area. It is updated once a week as mapping progresses.
  Subscribe to this dataset to be notified of any new updates. This dataset includes
  all OpenStreetMap features in the area of interest for this event, covering: - Buildings
  - Roads See the list of projects in the Tasking Manager here . Fro more information
  see the HOTOSM activation page . As of 29 January: 296 contributors.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/moz-floods-january-2026-openstreetmap-data]'
details: null
exposure:
- asset_type:
    description: Building footprints mapped via crowdsourced OpenStreetMap disaster
      mapping in flood-affected areas
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network geometry and attributes in flood-affected provinces
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: OpenStreetMap building and road features were extracted and exported
    by the Humanitarian OpenStreetMap Team following activation EMSR857 in response
    to January 2026 flooding in Mozambique. The extraction was spatially bounded by
    Copernicus flood extent mapping from 29 January 2026 covering Gaza, Maputo, and
    Maputo City provinces. Data were crowdsourced and compiled into standardized GeoJSON
    and Shapefile formats for humanitarian response.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap contributors
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Copernicus Emergency Management Service (EMSR857)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/moz-floods-january-2026-openstreetmap-data
  rel: source
loss:
  losses: []
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
  description: 'Buildings (GeoJSON): OpenStreetMap buildings data in the Gaza, Maputo
    and Maputo City Provinces, Mozambique, including updates from the January 2026
    flood disaster mapping activation (as of 29 January 2026).'
  download_url: https://data.humdata.org/dataset/a5c814cf-a98b-479d-a679-d390e325bf59/resource/589e663e-c32a-4e8b-937a-45d235909699/download/moz_floods_buildings_glide_fl_2026_000004_moz_29jan2026_geojson.zip
  format: null
  id: resource_589e663e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_Floods_Buildings_GLIDE_FL_2026_000004_MOZ_29Jan2026_geojson.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Buildings (Shapefile): OpenStreetMap buildings data in the Gaza, Maputo
    and Maputo City Provinces, Mozambique, including updates from the January 2026
    flood disaster mapping activation (as of 29 January 2026).'
  download_url: https://data.humdata.org/dataset/a5c814cf-a98b-479d-a679-d390e325bf59/resource/21307846-7c49-41b3-8c05-b1c685444611/download/moz_floods_buildings_glide_fl_2026_000004_moz_29jan2026_shp.zip
  format: null
  id: resource_21307846
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_Floods_Buildings_GLIDE_FL_2026_000004_MOZ_29Jan2026_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Roads (GeoJSON): OpenStreetMap roads data in the Gaza, Maputo and
    Maputo City Provinces, Mozambique, including updates from the January 2026 flood
    disaster mapping activation (as of 29 January 2026).'
  download_url: https://data.humdata.org/dataset/a5c814cf-a98b-479d-a679-d390e325bf59/resource/506ccee5-b53f-4a02-87b0-bc25c116062b/download/moz_floods_roads_glide_fl_2026_000004_moz_29jan2026_geojson.zip
  format: null
  id: resource_506ccee5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_Floods_Roads_GLIDE_FL_2026_000004_MOZ_29Jan2026_geojson.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Roads (Shapefile): OpenStreetMap roads data in the Gaza, Maputo and
    Maputo City Provinces, Mozambique, including updates from the January 2026 flood
    disaster mapping activation (as of 29 January 2026).'
  download_url: https://data.humdata.org/dataset/a5c814cf-a98b-479d-a679-d390e325bf59/resource/dcb3150a-13ca-47e8-b8b3-ad01479fb80b/download/moz_floods_roads_glide_fl_2026_000004_moz_29jan2026_shp.zip
  format: null
  id: resource_dcb3150a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_Floods_Roads_GLIDE_FL_2026_000004_MOZ_29Jan2026_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-moz_hotosm_floodsjanuary2026data_20260129
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-29'
temporal_resolution: null
title: Mozambique - Floods - January 2026 - OpenStreetMap Data
version: null
vulnerability: null
---
