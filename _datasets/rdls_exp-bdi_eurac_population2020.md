---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
creator:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
dataset_id: rdls_exp-bdi_eurac_population2020
description: 'Estimated total number of people per grid-cell at a resolution of 3
  arc seconds. [Source: This metadata record was automatically extracted from the
  GeoNode portal eurac]'
details: Building footprints were provided by the Digitize Africa project of Ecopia.AI
  and Maxar Technologies (2020) and gridded building patterns derived from the datasets
  produced by Dooley et al. 2020. Geospatial covariates representing factors related
  to population distribution, were obtained from the 'Global High Resolution Population
  Denominators Project' (OPP1134076).
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: This dataset was produced based on the 2020 population census/projection-based
    estimates for 2020
  sources:
  - id: source_1
    license: null
    name: Piero Campalani
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/495
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.5258/SOTON/WP00683
  id: ref_doi
  name: null
  url: https://doi.org/10.5258/SOTON/WP00683
resources:
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:bdi_pop_ppp_2020_UNadj_constrained_Worldpop_ras_12092020
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Burundi Population 2020 (OGC WMS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:bdi_pop_ppp_2020_UNadj_constrained_Worldpop_ras_12092020&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:bdi_pop_ppp_2020_UNadj_constrained_Worldpop_ras_12092020
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Burundi Population 2020 (OGC WCS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:bdi_pop_ppp_2020_UNadj_constrained_Worldpop_ras_12092020
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Burundi Population 2020 (X-Gzip)
  download_url: https://maps.eurac.edu/geoserver/wcs?service=WCS&request=GetCoverage&coverageid=geonode__bdi_pop_ppp_2020_UNadj_constrained_Worldpop_ras_12092020&format=application%2Fx-gzip&version=2.0.1&srs=EPSG%3A4326&bbox=29.000416566000000%2C-4.469583114000000%2C30.850416559000000%2C-2.308749789000000
  format: X-Gzip
  id: resource_2
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
  coordinate_system: EPSG:4326
  description: Burundi Population 2020
  download_url: https://maps.eurac.edu/geoserver/wcs?service=WCS&request=GetCoverage&coverageid=geonode__bdi_pop_ppp_2020_UNadj_constrained_Worldpop_ras_12092020&format=image%2Ftiff&version=2.0.1&srs=EPSG%3A4326&bbox=29.000416566000000%2C-4.469583114000000%2C30.850416559000000%2C-2.308749789000000
  format: null
  id: resource_3
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
  description: Burundi Population 2020
  download_url: https://maps.eurac.edu/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__bdi_pop_ppp_2020_UNadj_constrained_Worldpop_ras_12092020&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bdi_eurac_population2020
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
  central_year: null
  duration: null
  end: '2020'
  start: '2019'
temporal_resolution: null
title: Burundi Population 2020
version: null
vulnerability: null
---
