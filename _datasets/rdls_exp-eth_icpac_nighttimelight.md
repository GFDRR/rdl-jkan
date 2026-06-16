---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
creator:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
dataset_id: rdls_exp-eth_icpac_nighttimelight
description: 'This dataset presents high-resolution satellite-derived Nighttime Lights
  (NTL) imagery of Ethiopia,a resolution of approximately 5000 mettres , acquired
  from NASA''s Visible Infrared Imaging Radiometer Suite (VIIRS). NTL data captures
  the intensity and distribution of artificial lighting, serving as a proxy for human
  settlements, infrastructure development, and economic activity. [Source: This metadata
  record was automatically extracted from the GeoNode portal icpac]'
details: null
exposure:
- asset_type: null
  category: economic_indicator
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: currency
      unit: USD
hazard: null
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: IGAD DRM Team
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/Normalized_Night.Time.Light:geonode:Normalized_Night_Time_Light
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net
purpose: 'component : Exposure Source : NASA Relationship to component : Positive
  Night time light ( NTL) data serves as a powerful proxy for human activity ,development
  and economic status , making it highly useful in vulnerability assements for Drought'
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:Normalized_Night_Time_Light
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Ethiopia NightTime Light (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:Normalized_Night_Time_Light&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:Normalized_Night_Time_Light
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Ethiopia NightTime Light (OGC WCS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:Normalized_Night_Time_Light
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eth_icpac_nighttimelight
spatial:
  bbox:
  - 33.083
  - 3.433
  - 47.933
  - 14.833
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2025
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Ethiopia NightTime Light
version: null
vulnerability: null
---
