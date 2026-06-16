---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP database
    url: https://data.humdata.org/dataset/somalia-road-network-and-access-constraints
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Logistics Cluster Road Access Constraints map
    url: https://data.humdata.org/dataset/somalia-road-network-and-access-constraints
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/somalia-road-network-and-access-constraints
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/somalia-road-network-and-access-constraints
dataset_id: rdls_exp-som_wfp_roadnetworkaccessconstrai_20170411
description: 'This dataset is an extraction of the WFP database following UNSDI-T
  standards. See ''Attributes'' tab for more information on the data structure. Roads
  are displayed here according to their functional class (fclass). It contains as
  well information on current status of the roads, as per latest Road Access Constraints
  map from Logistics Cluster. The dataset was updated on 11 April 2017. For more information
  on attributes, please go check the layer on WFP geonode:. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-road-network-and-access-constraints]'
details: null
exposure:
- asset_type:
    description: Road network with functional classification, surface conditions,
      and access constraints
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
  description: Road network data extracted from WFP database following UNSDI-T standards,
    with functional classification (fclass), surface conditions, and current access
    constraints from Logistics Cluster integrated as attributes. The dataset represents
    the spatial infrastructure inventory for Somalia as of April 2017.
  sources:
  - id: source_1
    license: null
    name: WFP database
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Logistics Cluster Road Access Constraints map
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-road-network-and-access-constraints
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: https://ogcserver.gis.wfp.org/geoserver/ows?&version=1.0.0&service=WFS&request=GetFeature&typename=geonode:som_trs_roads_osm&outputFormat=SHAPE-ZIP
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Somalia - road network and access constraints (Shapefile)
  download_url: null
  format: null
  id: resource_007d05cc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SOM_trs_roads_wfp
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_wfp_roadnetworkaccessconstrai_20170411
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-11'
temporal_resolution: null
title: Somalia - road network and access constraints
version: null
vulnerability: null
---
