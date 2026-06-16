---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: kathrin.renner@eurac.edu
  name: Kathrin Renner
  url: https://maps.eurac.edu/api/v2/users/1042
creator:
  affiliation: null
  email: kathrin.renner@eurac.edu
  name: Kathrin Renner
  url: https://maps.eurac.edu/api/v2/users/1042
dataset_id: rdls_exp-bdi_eurac_grid3settlementextentssma
description: 'A small settlement (SSA) is a settled area of permanently inhabited
  structures and compounds of roughly a few hundred to a few thousand inhabitants.
  The housing pattern in SSAs is an assemblage of family compounds adjoining other
  similar habitations. Small settlement areas are characterized by having 50 or more
  buildings and are not a BUA. [Source: This metadata record was automatically extracted
  from the GeoNode portal eurac]'
details: 'Data Use Constraints Users are free to use, copy, distribute, transmit,
  and adapt the work for commercial and non-commercial purposes, without restriction,
  as long as clear attribution of the source is provided. Copyright 2020. The Trustees
  of Columbia University in the City of New York. The data and accompanying document
  is licensed under a Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0)
  and specified in legal code (http://creativecommons.org/licenses/by/4.0/legalcode).
  The Shapefile contains the following fields: OBJECTID ArcGIS Unique ID for each
  row SHAPE Geometry type mgrs_code Unique name generated using the Military Grid
  Reference System type The settlement type as defined by a BUA, SSA, or hamlet Shape_Length
  The shape length in geographic coordinates Shape_Area The shape area in geographic
  coordinates GlobalID Universal unique identifier'
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
license: CC-BY-4.0
lineage:
  description: Known data limitations and disclaimer The GRID3 settlement extents
    have not been visually inspected for false negatives. A settlement may exist for
    a location where there is no polygon. This may lead to settlements not being identified.
    Likewise, the GRID3 settlement extents have not been visually inspected for false
    positives. A settlement polygon may have been falsely identified as an actual
    settlement. These data are part of ongoing work and is not guaranteed to be accurate
    and clean. If users encounter apparent errors or misstatements in the data, they
    should contact GRID3 at data.queries@grid3.org.
  sources:
  - id: source_1
    license: null
    name: Kathrin Renner
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/563
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Kathrin Renner
  url: https://maps.eurac.edu
purpose: The settlement extents and classification are derived solely from the building
  footprints, and no ancillary datasets are used. The centerpoints of building footprint
  features are converted to a 3 arc-second raster grid of building densities. Shell-up
  contours are then generated using the building density grid to delineate settled
  vs non-settled areas.
referenced_by:
- author_names: null
  date_published: null
  doi: https://doi.org/10.7916/d8-963j-wp65
  id: ref_doi
  name: null
  url: https://doi.org/10.7916/d8-963j-wp65
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (Zipped
    Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_small_settlement_area_pol&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_small_settlement_area_pol&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_1
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
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_small_settlement_area_pol&outputFormat=csv&srs=EPSG%3A4326
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
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_small_settlement_area_pol&outputFormat=excel&srs=EPSG%3A4326
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
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_small_settlement_area_pol&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_4
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
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_small_settlement_area_pol&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_5
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_settl_extents_small_settlement_area_pol
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (OGC WMS:
    EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:bdi_settl_extents_small_settlement_area_pol&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_settl_extents_small_settlement_area_pol
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Burundi: GRID3 Settlement Extents - small settlement areas (OGC WFS:
    EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:bdi_settl_extents_small_settlement_area_pol&outputFormat=application%2Fjson
  format: null
  id: resource_7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: EO_CDR Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bdi_eurac_grid3settlementextentssma
spatial:
  bbox:
  - 29.0200309753418
  - -4.46833992004395
  - 30.8530731201172
  - -2.3096296787262
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2020
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'Burundi: GRID3 Settlement Extents - small settlement areas'
version: null
vulnerability: null
---
