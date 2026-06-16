---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Luis Rua
  url: https://geonode.pacificdata.org/catalogue/#/dataset/1040
creator:
  affiliation: null
  email: null
  name: Luis Rua
  url: https://geonode.pacificdata.org/catalogue/#/dataset/1040
dataset_id: rdls_exp-slb_pacificdata_populationgrid2020
description: 'Data Input: Household locations from 2008 household listing, Population
  extracted from 2009 Population and Housing Census at enumeration area level. Year
  Population Growth Rate of 3.05% has been applied to update population up to 2020
  Household locations vector layer has been transformed into a 100m resolution raster.
  [Source: This metadata record was automatically extracted from the GeoNode portal
  pacificdata]'
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
license: ODbL-1.0/
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
- href: https://geonode.pacificdata.org/catalogue/#/dataset/1040
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
  description: Solomon Islands Population Grid 2020
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__slb_rastpop2020rps_100m&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: https://geonode.pacificdata.org/datasets/geonode:slb_rastpop2020rps_100m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Solomon Islands Population Grid 2020 (OGC WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:slb_rastpop2020rps_100m&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:slb_rastpop2020rps_100m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Solomon Islands Population Grid 2020 (OGC WCS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__slb_rastpop2020rps_100m
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
slug: rdls_exp-slb_pacificdata_populationgrid2020
spatial:
  bbox:
  - 155.54613672
  - -12.30738404
  - 169.85213672
  - -5.09338404000002
  centroid: null
  countries:
  - SLB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Solomon Islands Population Grid 2020
version: null
vulnerability: null
---
