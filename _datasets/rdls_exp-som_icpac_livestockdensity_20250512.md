---
attributions:
- entity:
    affiliation: null
    email: null
    name: GLW 4 (Global Livestock of the World version 4)
    url: https://data.humdata.org/dataset/icpac-geonode-somalia-livestock-density
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-livestock-density
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-livestock-density
dataset_id: rdls_exp-som_icpac_livestockdensity_20250512
description: 'This dataset contains the most up to date version of GLW 4 for the reference
  year 2020 for the following species: buffalo, cattle, sheep, goats, pigs and chicken.
  The individual species datasets are available at global extent and 5 minutes of
  arc resolution (approx. 10 km at the equator). The fourth version of GLW, compared
  to the previous ones, reflects the most recently compiled and harmonized subnational
  livestock distribution data and much more detailed metadata. The layers contain
  the density of animals per km&sup2;, with weight estimated by the Random Forest
  model. The livestock species modelled include: buffaloes, cattle, chickens, goats,
  pigs and sheep. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-livestock-density]'
details: Time period is set to publication date rather than the date the data covers
exposure:
- asset_type:
    description: "Livestock density (animals per km\xB2) for six species: buffalo,\
      \ cattle, sheep, goats, pigs, and chicken"
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "GLW 4 integrates recently compiled and harmonized subnational livestock\
    \ distribution data for six species at 5-minute arc resolution. Animal density\
    \ per km\xB2 was estimated using Random Forest modeling for the 2020 reference\
    \ year, providing the most detailed livestock exposure inventory available."
  sources:
  - id: source_1
    license: null
    name: GLW 4 (Global Livestock of the World version 4)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-livestock-density
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__SOM_livestock_density1_normalized&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'GeoTIFF file. This dataset contains the most up to date version of
    GLW 4 for the reference year 2020 for the following species: buffalo, cattle,
    sheep, goats, pigs and chicken. The individual species datasets are available
    at global extent and 5 minutes of arc resolution (approx. 10 km at the equator).
    The fourth version of GLW, compared to the previous ones, reflects the most recently
    compiled and harmonized subnational livestock distribution data and much more
    detailed metadata. The layers contain the density of animals per km&sup2;, with
    weight estimated by the Random Forest model. The livestock species modelled include:
    buffaloes, cattle, chickens, goats, pigs and sheep'
  download_url: null
  format: null
  id: resource_02cc61e5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia livestock density GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_icpac_livestockdensity_20250512
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
  start: '2025-05-12'
temporal_resolution: null
title: Somalia livestock density
version: null
vulnerability: null
---
