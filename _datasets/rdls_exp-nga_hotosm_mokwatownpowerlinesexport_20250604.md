---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_nga_mka_power_lines
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_nga_mka_power_lines
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_nga_mka_power_lines
dataset_id: rdls_exp-nga_hotosm_mokwatownpowerlinesexport_20250604
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''power''] IN (''tower'', ''line'') Features
  may have these attributes: name amenity power source operator:type addr:full addr:city
  building This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_nga_mka_power_lines]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Power transmission lines (towers and line segments) in Mokwa Town
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Power infrastructure features were extracted from OpenStreetMap using
    tag-based filtering (power=tower and power=line) for Mokwa Town, Nigeria. Data
    were provided by Humanitarian OpenStreetMap Team (HOT) in multiple geospatial
    formats (SHP, GeoJSON, KML, GeoPackage) representing both point features (towers)
    and line features (transmission lines).
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap contributors
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm_nga_mka_power_lines
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/points/hotosm_nga_mka_power_lines_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_640536e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/points/hotosm_nga_mka_power_lines_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_038edf4e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/points/hotosm_nga_mka_power_lines_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_891c8e1b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/points/hotosm_nga_mka_power_lines_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_c366ae8a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/lines/hotosm_nga_mka_power_lines_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_b386901f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/lines/hotosm_nga_mka_power_lines_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3360cc4c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/lines/hotosm_nga_mka_power_lines_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f9d83046
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_nga_mka/power_lines/lines/hotosm_nga_mka_power_lines_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f465bb81
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nga_mka_power_lines_lines_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nga_hotosm_mokwatownpowerlinesexport_20250604
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
  start: '2025-06-04'
temporal_resolution: null
title: Mokwa Town, Nigeria Power Lines (OpenStreetMap Export)
version: null
vulnerability: null
---
