---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_mar_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_mar_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_mar_buildings
dataset_id: rdls_exp-mar_hotosm_buildingsexport_20260102
description: 'OpenStreetMap contains roughly 1.5 million buildings in this region.
  Based on AI-mapped estimates, this is approximately 19% of the total buildings.The
  average age of data for this region is 5 years ( Last edited 3 months ago ) and
  2% buildings were added or updated in the last 6 months. Read about what this summary
  means : indicators , metrics This theme includes all OpenStreetMap features in this
  area matching ( Learn what tags means here ) : tags[''building''] IS NOT NULL Features
  may have these attributes: name name:en building building:levels building:materials
  addr:full addr:housenumber addr:street addr:city office source name:ar name:ber
  This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_mar_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and stock inventory across Morocco from OpenStreetMap
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
license: ODbL-1.0/
lineage:
  description: Building footprints were extracted from OpenStreetMap volunteered geographic
    information for Morocco. The dataset represents approximately 19% of estimated
    total buildings based on AI-mapping validation. Data were exported in multiple
    geospatial formats (SHP, GeoJSON, GeoPackage, KML, CSV) for accessibility.
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
- href: https://data.humdata.org/dataset/hotosm_mar_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MAR/buildings/polygons/hotosm_mar_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Morocco Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_2ff3fc86
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mar_buildings_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Morocco Buildings (OpenStreetMap Export) (Geopackage, SQLite compatible)
  download_url: https://export.hotosm.org/downloads/1e95db86-a36b-44d9-b0fc-3d6853b4fe15/hotosm_mar_buildings_gpkg.zip
  format: null
  id: resource_ad630c9c
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mar_buildings_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MAR/buildings/polygons/hotosm_mar_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Morocco Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_e5e81266
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mar_buildings_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Morocco Buildings (OpenStreetMap Export) (.IMG for Garmin GPS Devices
    (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/1e95db86-a36b-44d9-b0fc-3d6853b4fe15/hotosm_mar_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_6f88b7a1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mar_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MAR/buildings/polygons/hotosm_mar_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Morocco Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_4eb9094b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mar_buildings_polygons_geojson.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Morocco Buildings (OpenStreetMap Export) (CSV Output along with centroid
    of feature)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_mar_buildings_polygons_csv_csv_uid_9571ff9c-4462-48cc-abee-86ef0c692a1a.zip
  format: null
  id: resource_b601c04d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mar_buildings_polygons_csv.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MAR/buildings/polygons/hotosm_mar_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Morocco Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_bb29cab8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mar_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mar_hotosm_buildingsexport_20260102
spatial:
  bbox: null
  centroid: null
  countries:
  - MAR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-02'
temporal_resolution: null
title: Morocco Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
