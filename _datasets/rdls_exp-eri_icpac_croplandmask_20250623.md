---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-eritrea-cropland-mask
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-eritrea-cropland-mask
dataset_id: rdls_exp-eri_icpac_croplandmask_20250623
description: 'The dataset contains global crop at 0.0089286 deg resolution (about
  1 squared kilometer).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-eritrea-cropland-mask]'
details: Time period is set to publication date rather than the date the data covers
exposure:
- asset_type:
    description: "Cropland spatial extent and distribution in Eritrea at ~1 km\xB2\
      \ resolution"
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
  description: "Global cropland mask derived from satellite or remote sensing data,\
    \ resampled to 0.0089286 degree resolution (~1 km\xB2), and extracted for Eritrea\
    \ administrative boundary to create a national-scale agricultural exposure dataset."
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-eritrea-cropland-mask
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__Eri_cropland_Normalized&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. The dataset contains global crop at 0.0089286 deg resolution
    (about 1 squared kilometer).
  download_url: null
  format: null
  id: resource_7555d5a8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Eritrea Cropland Mask GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eri_icpac_croplandmask_20250623
spatial:
  bbox: null
  centroid: null
  countries:
  - ERI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-06-23'
temporal_resolution: null
title: Eritrea Cropland Mask
version: null
vulnerability: null
---
