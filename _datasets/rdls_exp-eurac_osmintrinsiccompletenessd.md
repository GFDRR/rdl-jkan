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
dataset_id: rdls_exp-eurac_osmintrinsiccompletenessd
description: 'OpenStreetMap intrinsic complete analysis by discrete classification
  of its collines using terrain ruggedness and gridded population estimates as auxiliary
  predictors. [Source: This metadata record was automatically extracted from the GeoNode
  portal eurac]'
details: '''High'' and ''low'' in the data mean either greater than 3rd quartile or
  lower than 1st quartile of the sample data.'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: OSM data intrinsic calculation from GMTED terrain ruggedness and population
    estimates from 2008 census.
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
- href: https://maps.eurac.edu/catalogue/#/dataset/1286
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: Identify areas with potential missing roads in the OpenStreetMap database
  in Burundi.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_osm_discr_class&outputFormat=json&srs=EPSG%3A32635&srsName=EPSG%3A32635
  format: null
  id: resource_0
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
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (Zipped
    Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_osm_discr_class&outputFormat=SHAPE-ZIP&srs=EPSG%3A32635&format_options=charset%3AUTF-8
  format: null
  id: resource_1
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
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (GML
    3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_osm_discr_class&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A32635
  format: null
  id: resource_2
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
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_osm_discr_class&outputFormat=csv&srs=EPSG%3A32635
  format: null
  id: resource_3
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
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_osm_discr_class&outputFormat=excel&srs=EPSG%3A32635
  format: null
  id: resource_4
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
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (GML
    2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_osm_discr_class&outputFormat=gml2&srs=EPSG%3A32635
  format: null
  id: resource_5
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_osm_discr_class
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (OGC
    WMS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:bdi_osm_discr_class&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_osm_discr_class
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:32635
  description: 'BURUNDI: OSM intrinsic completeness by discrete classification (OGC
    WFS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:bdi_osm_discr_class&outputFormat=application%2Fjson
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
slug: rdls_exp-eurac_osmintrinsiccompletenessd
spatial:
  bbox:
  - 722371.492097485
  - -494652.202679492
  - 928181.147383067
  - -255677.883198066
  centroid: null
  countries:
  - AGO
  - BDI
  - BEN
  - BFA
  - BWA
  - CAF
  - CIV
  - CMR
  - COD
  - COG
  - COM
  - CPV
  - DJI
  - DZA
  - EGY
  - ERI
  - ETH
  - GAB
  - GHA
  - GIN
  - GMB
  - GNB
  - GNQ
  - KEN
  - LBR
  - LBY
  - LSO
  - MAR
  - MDG
  - MLI
  - MOZ
  - MRT
  - MUS
  - MWI
  - NAM
  - NER
  - NGA
  - RWA
  - SDN
  - SEN
  - SLE
  - SOM
  - SSD
  - STP
  - SWZ
  - SYC
  - TCD
  - TGO
  - TUN
  - TZA
  - UGA
  - ZAF
  - ZMB
  - ZWE
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: 2023
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'BURUNDI: OSM intrinsic completeness by discrete classification'
version: null
vulnerability: null
---
