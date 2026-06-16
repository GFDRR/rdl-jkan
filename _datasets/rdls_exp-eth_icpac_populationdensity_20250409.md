---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-population-density
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-population-density
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-population-density
dataset_id: rdls_exp-eth_icpac_populationdensity_20250409
description: 'This dataset represents the estimated population density of Ethiopia
  in the year 2020 , expressed as the number of people per square kilometer. It is
  intended to support spatial analysis and decision-making in areas such as disaster
  risk reduction, resource allocation, development planning, and vulnerability assessment
  Source - WORLDPOP Relationship to Exposure- (Positive)- The higher the population,
  the higher the exposure. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-ethiopia-population-density]'
details: Time period is set to publication date rather than the date the data covers
exposure:
- asset_type:
    description: Gridded population density of Ethiopia in 2020, expressed as people
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
  description: Population density estimates for Ethiopia in 2020 were sourced from
    WorldPop, a global gridded population dataset. The data was processed into a GeoTIFF
    raster format to support spatial analysis for disaster risk reduction, resource
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
- href: https://data.humdata.org/dataset/icpac-geonode-ethiopia-population-density
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__Normalized_Population_Density&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. This dataset represents the estimated population density
    of Ethiopia in the year 2020 , expressed as the number of people per square kilometer.
    It is intended to support spatial analysis and decision-making in areas such as
    disaster risk reduction, resource allocation, development planning, and vulnerability
    assessment Source - WORLDPOP Relationship to Exposure- (Positive)- The higher
    the population, the higher the exposure
  download_url: null
  format: null
  id: resource_811f629a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia population Density - GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eth_icpac_populationdensity_20250409
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-09'
temporal_resolution: null
title: Ethiopia population Density
version: null
vulnerability: null
---
