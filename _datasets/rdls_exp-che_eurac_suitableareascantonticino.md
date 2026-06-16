---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: samuele.zilio@eurac.edu
  name: Samuele Zilio
  url: https://maps.eurac.edu/api/v2/users/1052
creator:
  affiliation: null
  email: valentina.dalonzo@eurac.edu
  name: Valentina D'Alonzo
  url: https://maps.eurac.edu/api/v2/users/1021
dataset_id: rdls_exp-che_eurac_suitableareascantonticino
description: 'Layer to represent the most suitable locations for installing charging
  infrastructure for e-bikes in Canton Ticino (Switzerland). [Source: This metadata
  record was automatically extracted from the GeoNode portal eurac]'
details: For more information see the Interreg IT-CH project Mobster (https://www.progettomobster.eu/en/home-page-en/)
exposure:
- asset_type: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: The raster layer is the output of a weighted sum analysis considering
    several Points of Interests (POIs) related to the possible locations for charging
    points for e-bikes in Canton Ticino.
  sources:
  - id: source_1
    license: null
    name: Valentina D'Alonzo
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/336
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Samuele Zilio
  url: https://maps.eurac.edu
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32632
  description: Suitable areas in Canton Ticino for e-bike chargers (X-Gzip)
  download_url: https://maps.eurac.edu/geoserver/wcs?service=WCS&request=GetCoverage&coverageid=geonode__TI_weighted_sum_bike&format=application%2Fx-gzip&version=2.0.1&srs=EPSG%3A32632&bbox=452864.886584027700000%2C5074002.404656375000000%2C504944.886584027700000%2C5158842.404656375000000
  format: X-Gzip
  id: resource_0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GZIP
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32632
  description: Suitable areas in Canton Ticino for e-bike chargers
  download_url: https://maps.eurac.edu/geoserver/wcs?service=WCS&request=GetCoverage&coverageid=geonode__TI_weighted_sum_bike&format=image%2Ftiff&version=2.0.1&srs=EPSG%3A32632&bbox=452864.886584027700000%2C5074002.404656375000000%2C504944.886584027700000%2C5158842.404656375000000
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:TI_weighted_sum_bike
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:32632
  description: 'Suitable areas in Canton Ticino for e-bike chargers (OGC WCS: geonode
    Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:TI_weighted_sum_bike
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:TI_weighted_sum_bike
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32632
  description: 'Suitable areas in Canton Ticino for e-bike chargers (OGC WMS: geonode
    Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:TI_weighted_sum_bike&format=image%2Fpng
  format: null
  id: resource_3
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-che_eurac_suitableareascantonticino
spatial:
  bbox:
  - 452864.8865840277
  - 5074002.404656375
  - 504944.8865840277
  - 5158842.404656375
  centroid: null
  countries:
  - CHE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2021
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Suitable areas in Canton Ticino for e-bike chargers
version: Updated to March 2021
vulnerability: null
---
