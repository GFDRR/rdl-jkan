---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-myanmar-road-network
creator:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-myanmar-road-network
dataset_id: rdls_exp-mmr_mimu_roadnetwork_2022
description: 'Road network with main, secondary and tertiary roads. This network-based
  connectivity approach mainly uses population centres, such as, Union capital, State/Region
  capital, Main town, other town and village location, as the bases to road network.
  Main Road links ST/R Capital to Main Towns and to Neighbouring countries. Secondary
  Road links a Major Road to another Main Road. Tertiary Road links main town to other-town
  and other-town to other-town. Original dataset title: Myanmar Road Network 2022.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mimu-geonode-myanmar-road-network]'
details: "This product has been prepared for operational purposes only, to support\
  \ humanitarian and development activities in Myanmar. Copyright \xC2\xA92020 Myanmar\
  \ Information Management Unit. MIMU geospatial datasets cannot be used on online\
  \ platform unless with prior written agreement from MIMU. MIMU products are not\
  \ for sale and can be used free of charge with attribution. For more information\
  \ see http://themimu.info/mimu-terms-conditions."
exposure:
- asset_type:
    description: Road network classified by functional hierarchy (main, secondary,
      tertiary roads) connecting population centres and international borders
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
  description: Road network data compiled by MIMU from available sources and classified
    into functional categories (main, secondary, tertiary) based on connectivity to
    population centres including Union capital, State/Region capitals, main towns,
    and villages. Data provided as shapefile and GeoJSON formats for reference purposes.
  sources:
  - id: source_1
    license: null
    name: Myanmar Information Management Unit (MIMU)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mimu-geonode-myanmar-road-network
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?format_options=charset%3AUTF-8&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature&typename=geonode:mmr_rdsl_mimu_250k
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile. Road network with main, secondary and tertiary roads.
    This network-based connectivity approach mainly uses population centres, such
    as, Union capital, State/Region capital, Main town, other town and village location,
    as the bases to road network.
  download_url: null
  format: null
  id: resource_4809cbe5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Myanmar Road Network shapefile
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=application%2Fjson&typeName=geonode:mmr_rdsl_mimu_250k
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. Road network with main, secondary and tertiary roads.
    This network-based connectivity approach mainly uses population centres, such
    as, Union capital, State/Region capital, Main town, other town and village location,
    as the bases to road network.
  download_url: null
  format: null
  id: resource_e47f2ba7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Myanmar Road Network geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mmr_mimu_roadnetwork_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: Myanmar Road Network
version: null
vulnerability: null
---
