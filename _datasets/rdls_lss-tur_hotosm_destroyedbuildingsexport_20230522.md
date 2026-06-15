---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus EMS
    url: https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Istanbul Technical University CSCRS
    url: https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings
dataset_id: rdls_lss-tur_hotosm_destroyedbuildingsexport_20230522
description: 'In response to Turkey Syria Earthquake 2023, Source data includes aerial
  imagery from Copernicus EMS and Istanbul Technical University, Implementation and
  Research Center for Satellite Communications and Remote Sensing (CSCRS). Destroyed
  buildings were derived by users of OSM and Map Roulette. OpenStreetMap exports for
  use in GIS applications. This theme includes all OpenStreetMap features in this
  area matching: destroyed:building = ''yes'' AND damage:date = ''2023-02-06'' Features
  may have these attributes: addr:housenumber addr:full damage:event source damage:type
  damage:date building destroyed:building addr:street name addr:city This dataset
  is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure: []
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Destroyed buildings were identified by OpenStreetMap volunteers and
    Map Roulette contributors using aerial imagery from Copernicus EMS and Istanbul
    Technical University CSCRS. Building polygons were tagged with destroyed:building='yes'
    and damage:date='2023-02-06' to document direct structural damage from the February
    2023 earthquake. The dataset was exported in multiple GIS formats for humanitarian
    response and damage assessment.
  sources:
  - id: source_1
    license: null
    name: Copernicus EMS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Istanbul Technical University CSCRS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OpenStreetMap contributors
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm_tur_destroyed_buildings
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage (destruction) from the 2023 Turkey-Syria earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: HOTOSM Turkey Destroyed Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_tur_destroyed_buildings_polygons_geojson_geojson_uid_12c31136-ec56-4c83-bdd9-f37b1cd7fc08.zip
  format: null
  id: resource_fb8297e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tur_destroyed_buildings_polygons_geojson.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Turkey Destroyed Buildings (OpenStreetMap Export) (CSV Output
    along with centroid of feature)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_tur_destroyed_buildings_polygons_csv_csv_uid_447d931d-bfba-4e57-9c17-c335e146c471.zip
  format: null
  id: resource_d542acc4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tur_destroyed_buildings_polygons_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Turkey Destroyed Buildings (OpenStreetMap Export) (Geopackage,
    SQLite compatible)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_tur_destroyed_buildings_polygons_gpkg_gpkg_uid_9ca77aea-a2d5-4c7b-8ff0-f9aff1df04eb.zip
  format: null
  id: resource_978e04c7
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tur_destroyed_buildings_polygons_gpkg.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Turkey Destroyed Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_tur_destroyed_buildings_polygons_shp_shp_uid_219a2888-3687-4a55-a7fc-458955b1c498.zip
  format: null
  id: resource_5c157a71
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tur_destroyed_buildings_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Turkey Destroyed Buildings (OpenStreetMap Export) (Google Earth
    .KML)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_tur_destroyed_buildings_polygons_kml_kml_uid_0bc795c3-2589-495d-b8b1-249734a7aa61.zip
  format: null
  id: resource_bc1b9dd9
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tur_destroyed_buildings_polygons_kml.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tur_hotosm_destroyedbuildingsexport_20230522
spatial:
  bbox: null
  centroid: null
  countries:
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-22'
temporal_resolution: null
title: HOTOSM Turkey Destroyed Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
