---
attributions:
- entity:
    affiliation: null
    email: null
    name: Demographic and Health Surveys (DHS) 2016
    url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-household-members-per-clusters
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-household-members-per-clusters
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-household-members-per-clusters
dataset_id: rdls_exp-eth_icpac_householdmemberspercluste_20250414
description: 'Ethiopia household members per cluster entails the average household
  members per cluster (645 Clusters According to the 2016 DHS data - with a Spatial
  Resolution of 0.05 pixels about 5000 metres. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-ethiopia-household-members-per-clusters]'
details: Time period is set to publication date rather than the date the data covers
exposure:
- asset_type:
    description: Average household members per cluster derived from 2016 DHS survey
      data at 5 km spatial resolution
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
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Household member counts from the 2016 Ethiopia DHS survey were spatially
    aggregated to 645 clusters and gridded at 0.05-degree resolution (~5 km pixels)
    to create a rasterized population exposure layer suitable for disaster risk assessment.
  sources:
  - id: source_1
    license: null
    name: Demographic and Health Surveys (DHS) 2016
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-ethiopia-household-members-per-clusters
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__eTH_hOUSEHOLD_MEMBERS&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. Ethiopia household members per cluster entails the average
    household members per cluster (645 Clusters According to the 2016 DHS data - with
    a Spatial Resolution of 0.05 pixels about 5000 metres
  download_url: null
  format: null
  id: resource_91368893
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia Household Members -Per Clusters GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eth_icpac_householdmemberspercluste_20250414
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
  start: '2025-04-14'
temporal_resolution: null
title: Ethiopia Household Members -Per Clusters
version: null
vulnerability: null
---
