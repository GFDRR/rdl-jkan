---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/18
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/18
dataset_id: rdls_exp-slb_pacificdata_populationenumerationarea
description: 'The population was compiled from available census reports and validated
  using other available datasets. For each country, population counts from the finest
  resolution was trended to 2010 using a country-specific annual growth rate assumptions.
  Underlying vector geometry comes from regional sources, primarily SPC. Primary Data
  Source(s): PopGIS, Solomon Islands National Statistics Office Secondary Data Source(s):
  SPC (GPS Points), DIGO Geographical Resolutions Available (with count): 1. Province
  (10) 2. Ward (183) 3. Enumeration Area (1,143) Additional Comments: 1. This population
  database is misaligned due to the source data provided in the SPC?s PopGIS data
  set. This misalignment is not linear and the largest measured misalignment in a
  significantly populated region is approximately 600 meters. Complied by AIR Worldwide
  [Source: This metadata record was automatically extracted from the GeoNode portal
  pacificdata]'
details: Exposure Population
exposure:
- asset_type: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-NC-SA-4.0
lineage:
  description: 'Geographical Resolutions Available (with count): 1. Province (10)
    2. Ward (183) 3. Enumeration Area (1,143)'
  sources:
  - id: source_1
    license: null
    name: Earth and Oceans Observations Team Pacific Community
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/18
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Population by Enumeration Area in 2010 in Solomon Islands (GML 2.0)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Asb_enumeration_area&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_0
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Population by Enumeration Area in 2010 in Solomon Islands (GML 3.1.1)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Asb_enumeration_area&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_1
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Population by Enumeration Area in 2010 in Solomon Islands (CSV)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Asb_enumeration_area&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Population by Enumeration Area in 2010 in Solomon Islands (Excel)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Asb_enumeration_area&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Population by Enumeration Area in 2010 in Solomon Islands (JSON)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Asb_enumeration_area&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: https://geonode.pacificdata.org/datasets/geonode:sb_enumeration_area
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Population by Enumeration Area in 2010 in Solomon Islands (OGC WMS:
    geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:sb_enumeration_area&format=image%2Fpng
  format: null
  id: resource_5
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Population by Enumeration Area in 2010 in Solomon Islands (Zipped Shapefile)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Asb_enumeration_area&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: https://geonode.pacificdata.org/datasets/geonode:sb_enumeration_area
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Population by Enumeration Area in 2010 in Solomon Islands (OGC WFS:
    geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:sb_enumeration_area&outputFormat=application%2Fjson
  format: null
  id: resource_7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-slb_pacificdata_populationenumerationarea
spatial:
  bbox:
  - 155.51184800008502
  - -12.308583999751818
  - 168.84784000011587
  - -6.582871999942824
  centroid: null
  countries:
  - SLB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2020
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Population by Enumeration Area in 2010 in Solomon Islands
version: null
vulnerability: null
---
