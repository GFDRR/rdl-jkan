---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_idn_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_idn_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_idn_buildings
dataset_id: rdls_exp-idn_hotosm_buildingsexport_20240603
description: 'OpenStreetMap contains roughly 41.7 million buildings in this region.
  Based on AI-mapped estimates, this is approximately 56% of the total buildings.The
  average age of data for this region is 3 years ( Last edited 3 days ago ) and 1%
  buildings were added or updated in the last 6 months. Read about what this summary
  means : indicators , metrics OpenStreetMap exports for use in GIS applications.
  This theme includes all OpenStreetMap features in this area matching ( Learn what
  tags means here ) : tags[''building''] IS NOT NULL Features may have these attributes:
  name name:en building building:levels building:materials addr:full addr:housenumber
  addr:street addr:city office source name:id This dataset is one of many OpenStreetMap
  exports on HDX . See the Humanitarian OpenStreetMap Team website for more information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_idn_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and structure inventory across Indonesia from
      OpenStreetMap
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
  description: Building footprints were extracted from OpenStreetMap for Indonesia,
    representing approximately 41.7 million structures. Data quality is assessed through
    AI-mapped estimates indicating 56% coverage of total buildings, with average data
    age of 3 years and 1% recent updates. Exports are provided in multiple GIS-compatible
    formats (GeoJSON, KML, GeoPackage).
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
- href: https://data.humdata.org/dataset/hotosm_idn_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/IDN/buildings/polygons/hotosm_idn_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Indonesia Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_c9f1f381
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_idn_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/IDN/buildings/polygons/hotosm_idn_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Indonesia Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_572136e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_idn_buildings_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/IDN/buildings/polygons/hotosm_idn_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Indonesia Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b43be2b0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_idn_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-idn_hotosm_buildingsexport_20240603
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-06-03'
temporal_resolution: null
title: Indonesia Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
