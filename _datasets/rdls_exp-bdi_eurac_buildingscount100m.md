---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: kathrin.renner@eurac.edu
  name: Kathrin Renner
  url: https://maps.eurac.edu/api/v2/users/1042
creator:
  affiliation: null
  email: kathrin.renner@eurac.edu
  name: Kathrin Renner
  url: https://maps.eurac.edu/api/v2/users/1042
dataset_id: rdls_exp-bdi_eurac_buildingscount100m
description: 'This layer shows gridded buildings with 100m resolution for Burundi.
  It was extracted from Gridded maps of building patterns throughout sub-Saharan Africa,
  version 2.0. This raster contains counts of buildings that fall within a grid cell.
  Each buildings was counted in the grid cell that contained the centroid of its building
  footprint [Source: This metadata record was automatically extracted from the GeoNode
  portal eurac]'
details: null
exposure:
- asset_type: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: None.
  sources:
  - id: source_1
    license: null
    name: Kathrin Renner
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/496
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Kathrin Renner
  url: https://maps.eurac.edu
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.5258/SOTON/WP00712
  id: ref_doi
  name: null
  url: https://doi.org/10.5258/SOTON/WP00712
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Burundi: Buildings count (100m)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__bdi_bldgs_buildings_Worldpop_v2_0_count_ras_100m&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Burundi: Buildings count (100m)'
  download_url: https://maps.eurac.edu/geoserver/wcs?service=WCS&request=GetCoverage&coverageid=geonode__bdi_bldgs_buildings_Worldpop_v2_0_count_ras_100m&format=image%2Ftiff&version=2.0.1&srs=EPSG%3A4326&bbox=29.000416566000000%2C-4.469583114000000%2C30.850416559000000%2C-2.308749789000000
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Burundi: Buildings count (100m) (X-Gzip)'
  download_url: https://maps.eurac.edu/geoserver/wcs?service=WCS&request=GetCoverage&coverageid=geonode__bdi_bldgs_buildings_Worldpop_v2_0_count_ras_100m&format=application%2Fx-gzip&version=2.0.1&srs=EPSG%3A4326&bbox=29.000416566000000%2C-4.469583114000000%2C30.850416559000000%2C-2.308749789000000
  format: X-Gzip
  id: resource_2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GZIP
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:bdi_bldgs_buildings_Worldpop_v2_0_count_ras_100m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Burundi: Buildings count (100m) (OGC WMS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:bdi_bldgs_buildings_Worldpop_v2_0_count_ras_100m&format=image%2Fpng
  format: null
  id: resource_3
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:bdi_bldgs_buildings_Worldpop_v2_0_count_ras_100m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Burundi: Buildings count (100m) (OGC WCS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:bdi_bldgs_buildings_Worldpop_v2_0_count_ras_100m
  format: null
  id: resource_4
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
slug: rdls_exp-bdi_eurac_buildingscount100m
spatial:
  bbox:
  - 29.000416566
  - -4.469583114
  - 30.850416559
  - -2.308749789
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2021
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'Burundi: Buildings count (100m)'
version: V2
vulnerability: null
---
