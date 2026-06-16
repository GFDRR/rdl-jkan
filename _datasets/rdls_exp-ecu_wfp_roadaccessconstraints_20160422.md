---
attributions:
- entity:
    affiliation: null
    email: null
    name: Government of Ecuador
    url: https://data.humdata.org/dataset/ecuador-road-access-constraints
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/ecuador-road-access-constraints
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/ecuador-road-access-constraints
dataset_id: rdls_exp-ecu_wfp_roadaccessconstraints_20160422
description: 'This dataset shows road access constraints in Ecuador after the earthquake
  that occurred on 17 April 2016. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ecuador-road-access-constraints]'
details: null
exposure:
- asset_type:
    description: Road network with access constraints and disruptions following the
      2016 earthquake
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Road network data was compiled by WFP Logistics Cluster partners and
    Government of Ecuador following the 17 April 2016 earthquake in Ecuador. The dataset
    documents spatial constraints on road accessibility for humanitarian logistics
    operations, derived from post-event field assessments and partner reports.
  sources:
  - id: source_1
    license: null
    name: WFP - World Food Programme
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Government of Ecuador
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ecuador-road-access-constraints
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
- access_url: http://geonode.wfp.org/geoserver/wfs?format_options=charset%3AUTF-8&typename=geonode%3Aecu_trs_roadaccess_wfp_1&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Ecuador, Road Access Constraints (zipped shapefile)
  download_url: null
  format: null
  id: resource_ccdb83b3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zipped shapefile
- access_url: http://geonode.wfp.org/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Aecu_trs_roadaccess_wfp_1&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Ecuador, Road Access Constraints (GeoJSON)
  download_url: null
  format: null
  id: resource_4f0baf56
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ecu_wfp_roadaccessconstraints_20160422
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-22'
temporal_resolution: null
title: Ecuador, Road Access Constraints
version: null
vulnerability: null
---
