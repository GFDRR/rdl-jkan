---
attributions:
- entity:
    affiliation: null
    email: null
    name: MERIT DEM (Multi-Error-Removed Improved-Terrain Digital Elevation Model)
    url: https://data.humdata.org/dataset/mimu-geonode-myanmar-low-lying-areas
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-myanmar-low-lying-areas
creator:
  affiliation: null
  email: null
  name: Myanmar Information Management Unit (MIMU)
  url: https://data.humdata.org/dataset/mimu-geonode-myanmar-low-lying-areas
dataset_id: rdls_exp-mmr_mimu_lowlyingareas_20190827
description: 'Low-lying Areas below 5 meters elevation. This dataset is derived from
  the Multi-Error-Removed Improved-Terrain / MERIT DEM.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/mimu-geonode-myanmar-low-lying-areas]'
details: "This product has been prepared for operational purposes only, to support\
  \ humanitarian and development activities in Myanmar. Copyright \xC2\xA92020 Myanmar\
  \ Information Management Unit. MIMU geospatial datasets cannot be used on online\
  \ platform unless with prior written agreement from MIMU. MIMU products are not\
  \ for sale and can be used free of charge with attribution. For more information\
  \ see http://themimu.info/mimu-terms-conditions."
exposure:
- asset_type:
    description: Low-lying terrain areas below 5 meters elevation derived from digital
      elevation model
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Low-lying areas below 5 meters elevation were identified and delineated
    from the MERIT DEM, a global high-resolution digital elevation model. The dataset
    represents terrain susceptibility to inundation based on topographic position
    and is provided as vector geometries (shapefile and GeoJSON) for Myanmar.
  sources:
  - id: source_1
    license: null
    name: MERIT DEM (Multi-Error-Removed Improved-Terrain Digital Elevation Model)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mimu-geonode-myanmar-low-lying-areas
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
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?format_options=charset%3AUTF-8&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature&typename=geonode:below5m_shp
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile. Low-lying Areas below 5 meters elevation.
  download_url: null
  format: null
  id: resource_e06462b9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Myanmar Low-Lying Areas shapefile
- access_url: https://geonode.themimu.info/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=application%2Fjson&typeName=geonode:below5m_shp
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. Low-lying Areas below 5 meters elevation.
  download_url: null
  format: null
  id: resource_5f23af69
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Myanmar Low-Lying Areas geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mmr_mimu_lowlyingareas_20190827
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
  end: null
  start: '2019-08-27'
temporal_resolution: null
title: Myanmar Low-Lying Areas
version: null
vulnerability: null
---
