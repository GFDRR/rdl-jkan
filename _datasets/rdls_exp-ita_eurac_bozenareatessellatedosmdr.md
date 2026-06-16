---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
creator:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
dataset_id: rdls_exp-ita_eurac_bozenareatessellatedosmdr
description: 'Drivable roads from OpenStreetMap over the area of Bozen (South Tyrol)
  onto an hexagonal tessellation of ~250m. [Source: This metadata record was automatically
  extracted from the GeoNode portal eurac]'
details: 'An edge in the roads network exist when at least 1 road in the original
  OSM network intersects with the underlying hexagonal tessellation. The ''count''
  field registers the number of such roads per each edge. The type and number of roads
  intersecting with the cells borders both participate in the definition of the ''weight''.
  The more important the road, the higher the weight. Python packages used: NetworkX,
  Shapely, GeoPandas.'
exposure:
- asset_type: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: Data derived from original OSM data.
  sources:
  - id: source_1
    license: null
    name: Piero Campalani
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/1013
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: Simplify the OSM roads network onto a regular tessellation for more flexible
  use in risk analysis and reduction.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_tran_rds_ln_s4_osm_pp_drive_250tess_bz&outputFormat=excel&srs=EPSG%3A25832
  format: null
  id: resource_0
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
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_tran_rds_ln_s4_osm_pp_drive_250tess_bz&outputFormat=json&srs=EPSG%3A25832&srsName=EPSG%3A25832
  format: null
  id: resource_1
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
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (Zipped Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_tran_rds_ln_s4_osm_pp_drive_250tess_bz&outputFormat=SHAPE-ZIP&srs=EPSG%3A25832&format_options=charset%3AUTF-8
  format: null
  id: resource_2
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
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_tran_rds_ln_s4_osm_pp_drive_250tess_bz&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A25832
  format: null
  id: resource_3
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:st_tran_rds_ln_s4_osm_pp_drive_250tess_bz
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (OGC WMS: EO_CDR
    Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:st_tran_rds_ln_s4_osm_pp_drive_250tess_bz&format=image%2Fpng
  format: null
  id: resource_4
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:st_tran_rds_ln_s4_osm_pp_drive_250tess_bz
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (OGC WFS: EO_CDR
    Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:st_tran_rds_ln_s4_osm_pp_drive_250tess_bz&outputFormat=application%2Fjson
  format: null
  id: resource_5
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: EO_CDR Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_tran_rds_ln_s4_osm_pp_drive_250tess_bz&outputFormat=gml2&srs=EPSG%3A25832
  format: null
  id: resource_6
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
  coordinate_system: EPSG:25832
  description: 'BOZEN AREA: tessellated OSM drivable roads (~250m) (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_tran_rds_ln_s4_osm_pp_drive_250tess_bz&outputFormat=csv&srs=EPSG%3A25832
  format: null
  id: resource_7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ita_eurac_bozenareatessellatedosmdr
spatial:
  bbox:
  - 674645.25
  - 5145954.5
  - 685402.0
  - 5155715.0
  centroid: null
  countries:
  - ITA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2022
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'BOZEN AREA: tessellated OSM drivable roads (~250m)'
version: null
vulnerability: null
---
