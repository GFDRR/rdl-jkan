---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-crop-mask
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-crop-mask
dataset_id: rdls_exp-som_icpac_cropmask_20250512
description: 'The dataset contains global crop at 0.0089286 deg resolution (about
  1 squared kilometer). Each pixel represents the area fraction of the specific cover
  (i.e. percentage of the pixel with rangelands). [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/icpac-geonode-somalia-crop-mask]'
details: Time period is set to publication date rather than the date the data covers
exposure:
- asset_type:
    description: "Crop area fraction per pixel at 1 km\xB2 resolution showing percentage\
      \ of land cover classified as cropland"
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
  description: "Global crop mask generated from remote sensing data at approximately\
    \ 1 km\xB2 resolution, with each pixel representing the fractional area of cropland\
    \ cover. The dataset provides agricultural exposure information for Somalia and\
    \ globally, enabling assessment of crop-based assets at risk to hazards."
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
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-crop-mask
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__SOM_crop_negative1_normalized&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. The dataset contains global crop at 0.0089286 deg resolution
    (about 1 squared kilometer). Each pixel represents the area fraction of the specific
    cover (i.e. percentage of the pixel with rangelands)
  download_url: null
  format: null
  id: resource_2ec6c1cd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Crop Mask GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_icpac_cropmask_20250512
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
title: Somalia Crop Mask
version: null
vulnerability: null
---
