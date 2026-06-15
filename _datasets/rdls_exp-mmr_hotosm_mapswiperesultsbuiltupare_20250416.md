---
attributions:
- entity:
    affiliation: null
    email: null
    name: MapSwipe
    url: https://data.humdata.org/dataset/mapswipe_myanmar_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/mapswipe_myanmar_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/mapswipe_myanmar_buildings
dataset_id: rdls_exp-mmr_hotosm_mapswiperesultsbuiltupare_20250416
description: 'MapSwipe results focusing on areas with at least one building. This
  data is collected through the MapSwipe platform, whereby humans visually check for
  the presence of buildings using satellite imagery (Esri World Imagery for Myanmar).
  It combines results from several MapSwipe projects listed below. In the download
  files below the ''results_yes_maybe'' are the results and the original input areas
  are ''aois''. Source MapSwipe Projects Myanmar: Find - Buildings - Earthquake Response
  (2) Myanmar: Find - Buildings - Earthquake Response (3) Myanmar: Find - Buildings
  - Earthquake Response (4) Myanmar: Find - Buildings - Earthquake Response (5) Myanmar:
  Find - Buildings - Earthquake Response (6) Myanmar: Find - Buildings - Earthquake
  Response (7) Myanmar: Find - Buildings - Earthquake Response (8). [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mapswipe_myanmar_buildings]'
details: null
exposure:
- asset_type:
    description: Building footprints and locations identified through human validation
      of satellite imagery in Myanmar
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
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Building locations were identified through crowdsourced visual inspection
    of Esri World Imagery satellite data via the MapSwipe platform. Results from multiple
    MapSwipe projects focused on Myanmar were aggregated and validated by human contributors.
    The final dataset contains confirmed building presence locations (yes/maybe classifications)
    distributed as vector geometries in GeoJSON, GeoPackage, and KML formats.
  sources:
  - id: source_1
    license: null
    name: MapSwipe
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Humanitarian OpenStreetMap Team (HOT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mapswipe_myanmar_buildings
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
  description: 'MapSwipe Results: Myanmar Built Up Areas (Combined results from MapSwipe
    projects in GeoJSON format)'
  download_url: https://data.humdata.org/dataset/f6a1beaa-1f4f-4dc0-bdd2-d7ad3591545d/resource/1e1983db-63ad-426e-b63c-7c45260068b2/download/mapswipe_myanmar_buildings_geojson.zip
  format: null
  id: resource_1e1983db
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mapswipe_myanmar_buildings_results_yes_maybe.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'MapSwipe Results: Myanmar Built Up Areas (Combined results from MapSwipe
    projects in GeoPackage format)'
  download_url: https://data.humdata.org/dataset/f6a1beaa-1f4f-4dc0-bdd2-d7ad3591545d/resource/97c06616-3a54-4cec-aea0-e78f104412a0/download/mapswipe_myanmar_buildings_gpkg.zip
  format: null
  id: resource_97c06616
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mapswipe_myanmar_buildings_results_yes_maybe.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'MapSwipe Results: Myanmar Built Up Areas (Combined results from MapSwipe
    projects in KML format)'
  download_url: https://data.humdata.org/dataset/f6a1beaa-1f4f-4dc0-bdd2-d7ad3591545d/resource/b6c0809e-ed58-41f7-980e-a80befd8ff7e/download/mapswipe_myanmar_buildings_kml.zip
  format: null
  id: resource_b6c0809e
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mapswipe_myanmar_buildings_results_yes_maybe.kml
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mmr_hotosm_mapswiperesultsbuiltupare_20250416
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-16'
temporal_resolution: null
title: 'MapSwipe Results: Myanmar Built Up Areas'
version: null
vulnerability: null
---
