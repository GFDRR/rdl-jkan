---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Luis Rua
  url: https://geonode.pacificdata.org/catalogue/#/dataset/1032
creator:
  affiliation: null
  email: null
  name: Luis Rua
  url: https://geonode.pacificdata.org/catalogue/#/dataset/1032
dataset_id: rdls_exp-plw_pacificdata_palaupopulationgrid2020
description: 'Data Input: Household locations from 2015 Household listing and population
  at Enumeration Area level extracted from 2015 Population and Housing Census conducted
  by Palau''s Bureau of Budget & Planning Year Population Growth Rate of 0.6 % has
  been applied to update population up to 2020 Household locations vector layer transformed
  into a 100m resolution raster. [Source: This metadata record was automatically extracted
  from the GeoNode portal pacificdata]'
details: null
exposure:
- asset_type: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-NC-SA-4.0
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: Luis Rua
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/1032
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Luis Rua
  url: https://geonode.pacificdata.org
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Palau Population Grid 2020
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__plw_rastpop2020rps_100m&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: https://geonode.pacificdata.org/datasets/geonode:plw_rastpop2020rps_100m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Palau Population Grid 2020 (OGC WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:plw_rastpop2020rps_100m&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:plw_rastpop2020rps_100m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Palau Population Grid 2020 (OGC WCS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__plw_rastpop2020rps_100m
  format: null
  id: resource_2
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
slug: rdls_exp-plw_pacificdata_palaupopulationgrid2020
spatial:
  bbox:
  - 130.5060880383668
  - 2.891895762302966
  - 135.37708803836682
  - 8.195895762302966
  centroid: null
  countries:
  - PLW
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Palau Population Grid 2020
version: null
vulnerability: null
---
