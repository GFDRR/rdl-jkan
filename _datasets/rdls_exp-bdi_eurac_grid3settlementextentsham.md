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
dataset_id: rdls_exp-bdi_eurac_grid3settlementextentsham
description: 'A hamlet is a collection of several compounds or sleeping houses in
  isolation from small settlements or urban areas. Hamlets are characterized as a
  collection of lowdensity settlements between one and 50 buildings and falls within
  65 meters of one another. [Source: This metadata record was automatically extracted
  from the GeoNode portal eurac]'
details: 'The settlement extents and classification are derived solely from the building
  footprints, and no ancillary datasets are used. The centerpoints of building footprint
  features are converted to a 3 arc-second raster grid of building densities. Shell-up
  contours are then generated using the building density grid to delineate settled
  vs non-settled areas. The shell-up method includes contours that start at the lower
  bounds, but includes all grid cells with building densities to the upper bounds
  of the grid. For example, a shell up contour of 10 would include all grid cells
  with a building density of 10 or more. Contours with a building density of one or
  more are used to create the settlement extent polygons. The GRID3 Burundi settlement
  extents characterised building density into three (3) classes: built-up areas (bua_extents),
  small settlement areas (ssa_extents), and hamlets (hamlet_extents)'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: 4. Known data limitations and disclaimer The GRID3 settlement extents
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
- href: https://maps.eurac.edu/catalogue/#/dataset/562
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Kathrin Renner
  url: https://maps.eurac.edu
purpose: 'The Shapefile contains the following fields: OBJECTID ArcGIS Unique ID for
  each row SHAPE Geometry type mgrs_code Unique name generated using the Military
  Grid Reference System type The settlement type as defined by a BUA, SSA, or hamlet
  Shape_Length The shape length in geographic coordinates Shape_Area The shape area
  in geographic coordinates GlobalID Universal unique identifier'
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
  description: 'Burundi: GRID3 Settlement Extents - hamlets (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_hamlets_pol&outputFormat=gml2&srs=EPSG%3A4326
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
  description: 'Burundi: GRID3 Settlement Extents - hamlets (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_hamlets_pol&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
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
  description: 'Burundi: GRID3 Settlement Extents - hamlets (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_hamlets_pol&outputFormat=csv&srs=EPSG%3A4326
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
  description: 'Burundi: GRID3 Settlement Extents - hamlets (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_hamlets_pol&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_3
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Burundi: GRID3 Settlement Extents - hamlets (Zipped Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_hamlets_pol&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_4
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
  description: 'Burundi: GRID3 Settlement Extents - hamlets (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_settl_extents_hamlets_pol&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_settl_extents_hamlets_pol
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Burundi: GRID3 Settlement Extents - hamlets (OGC WMS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:bdi_settl_extents_hamlets_pol&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_settl_extents_hamlets_pol
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Burundi: GRID3 Settlement Extents - hamlets (OGC WFS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:bdi_settl_extents_hamlets_pol&outputFormat=application%2Fjson
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
slug: rdls_exp-bdi_eurac_grid3settlementextentsham
spatial:
  bbox:
  - 28.9923496246338
  - -4.47444295883179
  - 30.8565845489502
  - -2.30216836929321
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
title: 'Burundi: GRID3 Settlement Extents - hamlets'
version: Version 01 Alpha
vulnerability: null
---
