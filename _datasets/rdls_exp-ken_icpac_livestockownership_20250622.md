---
attributions:
- entity:
    affiliation: null
    email: null
    name: DHS 2022
    url: https://data.humdata.org/dataset/icpac-geonode-kenya-livestock-ownership
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-kenya-livestock-ownership
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-kenya-livestock-ownership
dataset_id: rdls_exp-ken_icpac_livestockownership_20250622
description: 'This is Kenya , livestock ownership with a resolution of 0.05 , approximately
  5000 metres Source : DHS 2022. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-kenya-livestock-ownership]'
details: Time period is set to publication date rather than the date the data covers
exposure:
- asset_type:
    description: Spatial distribution of livestock ownership across Kenya at 5 km
      resolution
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
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Livestock ownership data from the 2022 Demographic and Health Survey
    was spatially interpolated and gridded to a 0.05-degree resolution (approximately
    5 km) to create a continuous raster surface of livestock distribution across Kenya
    for exposure assessment.
  sources:
  - id: source_1
    license: null
    name: DHS 2022
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-kenya-livestock-ownership
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__Livestock_OwnershipNorm_Copy0&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'GeoTIFF file. This is Kenya , livestock ownership with a resolution
    of 0.05 , approximately 5000 metres Source : DHS 2022'
  download_url: null
  format: null
  id: resource_b1469d11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kenya Livestock_Ownership GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ken_icpac_livestockownership_20250622
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
  start: '2025-06-22'
temporal_resolution: null
title: Kenya Livestock_Ownership
version: null
vulnerability: null
---
