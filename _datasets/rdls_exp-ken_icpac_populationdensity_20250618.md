---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/icpac-geonode-kenya-population-density
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-kenya-population-density
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-kenya-population-density
dataset_id: rdls_exp-ken_icpac_populationdensity_20250618
description: 'This dataset represents the estimated population density of Kenya in
  the year 2020 , expressed as the number of people per square kilometer. It is intended
  to support spatial analysis and decision-making in areas such as disaster risk reduction,
  resource allocation, development planning, and vulnerability assessment Source -
  WORLDPOP Relationship to Exposure- (Positive)- The higher the population, the higher
  the exposure. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-kenya-population-density]'
details: Time period is set to publication date rather than the date the data covers
exposure:
- asset_type:
    description: Gridded population density of Kenya in 2020, expressed as people
      per square kilometer
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: WorldPop gridded population density data for Kenya was processed and
    distributed by ICPAC as a GeoTIFF raster to support disaster risk reduction, resource
    allocation, and vulnerability assessment applications.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-kenya-population-density
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__Normalized_popdensityNorm_Copy&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. This dataset represents the estimated population density
    of Kenya in the year 2020 , expressed as the number of people per square kilometer.
    It is intended to support spatial analysis and decision-making in areas such as
    disaster risk reduction, resource allocation, development planning, and vulnerability
    assessment Source - WORLDPOP Relationship to Exposure- (Positive)- The higher
    the population, the higher the exposure
  download_url: null
  format: null
  id: resource_b89f40b3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kenya Population Density GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ken_icpac_populationdensity_20250618
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-06-18'
temporal_resolution: null
title: Kenya Population Density
version: null
vulnerability: null
---
