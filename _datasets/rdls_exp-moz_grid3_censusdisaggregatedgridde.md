---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Research Group
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-mozambique-2017-census-v1-1
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Mozambique Census 2017
    url: https://data.humdata.org/dataset/gridded-population-estimates-for-mozambique-2017-census-v1-1
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-mozambique-2017-census-v1-1
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/gridded-population-estimates-for-mozambique-2017-census-v1-1
dataset_id: rdls_exp-moz_grid3_censusdisaggregatedgridde
description: 'These data were produced by the WorldPop Research Group at the University
  of Southampton. This work is part of the GRID3 (Geo-Referenced Infrastructure and
  Demographic Data for Development) project funded by the Bill and Melinda Gates Foundation
  (BMGF) and the United Kingdom Foreign, Commonwealth & Development Office (OPP1182425).
  Project partners include WorldPop at the University of Southampton, the United Nations
  Population Fund ( UNFPA ), Center for International Earth Science Information Network
  ( CIESIN ) in the Earth Institute at Columbia University, and the Flowminder Foundation.
  This work provides an estimate of the geographic distribution of the population
  of Mozambique in 2017. The outputs are intended as an interim population product
  to support ongoing development and operations work until such time as the official
  2017 Population and Housing Census results are available in a spatial gridded format.
  At that time, this interim gridded population layer will be superseded and users
  will be advised to use the official gridded population release from INE . For further
  details, please, read MOZ_population_v1_1_README.pdf Recommended citation Bondarenko
  M, Jones P, Leasure D, Lazar AN, Tatem AJ. 2020. Census disaggregated gridded population
  estimates for Mozambique (2017), version 1.1. WorldPop, University of Southampton.
  doi:10.5258/SOTON/WP00672. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/gridded-population-estimates-for-mozambique-2017-census-v1-1]'
details: Census disaggregated gridded population estimates for Mozambique (2017),
  version 1.1. Contact release@worldpop.org for more information. __Recommended citation__
  _Bondarenko M, Jones P, Leasure D, Lazar AN, Tatem AJ. 2020. Census disaggregated
  gridded population estimates for Mozambique (2017), version 1.1. WorldPop, University
  of Southampton. doi:10.5258/SOTON/WP00672_
exposure:
- asset_type:
    description: Gridded population estimates disaggregated by age and sex derived
      from 2017 census data
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
  description: Census population counts from Mozambique's 2017 national census were
    spatially disaggregated using WorldPop's gridding methodology to produce high-resolution
    (approximately 100m) gridded population estimates stratified by age and sex groups.
    The resulting dataset provides baseline population exposure data suitable for
    disaster risk assessment applications.
  sources:
  - id: source_1
    license: null
    name: WorldPop Research Group
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Mozambique Census 2017
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gridded-population-estimates-for-mozambique-2017-census-v1-1
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Top-down gridded population estimates (~100m) for Mozambique. A geotiff
    raster with estimates of total population size for each approximately 100 m grid
    cell across the study area.
  download_url: https://wopr.worldpop.org/download/237
  format: null
  id: resource_05aa308d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_population_v1_1_gridded.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Top-down gridded population estimates (~100m) for specific age-sex
    groups. This zip file contains geotiff rasters with estimates of population sizes
    for individual age-sex groups for each approximately 100 m grid cell across the
    study area.
  download_url: https://wopr.worldpop.org/download/241
  format: null
  id: resource_60e5de16
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_population_v1_1_agesex.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mastergrid for gridded population estimates. This geotiff raster contains
    the mastergrid used to define where population estimates were made. It contains
    a value of 1 where population estimates were made and a value of 0 or NA everywhere
    else. Cell IDs from the mastergrid can be used to lookup values in the SQL database.
  download_url: https://wopr.worldpop.org/download/245
  format: null
  id: resource_c1a3d5ef
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_population_v1_1_mastergrid.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'README: MOZ Population v1.0 (English + Portuguese). This README file
    (English + Protuguese) provides information about the data included in the data
    release, how it was produced, source data that were used, and known assumptions
    and limitations of the results.'
  download_url: https://wopr.worldpop.org/download/242
  format: null
  id: resource_423179ce
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_population_v1_1_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: SQL database with population predictions for each 100 m grid cell.
    This SQLite database contains estimates of population size in each grid cell.
    The database can be used to develop applications that query the population estimates.
    It is used for WorldPop's woprVision web application.
  download_url: https://wopr.worldpop.org/download/243
  format: SQL
  id: resource_3e837293
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_population_v1_1_sql.sql
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Image tiles for gridded population estimates. These image tiles (XYZ
    format) allow for rapid display of the 100 m gridded population estimates across
    the study area in web applications.
  download_url: https://wopr.worldpop.org/download/244
  format: PNG
  id: resource_2b3f64a2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_population_v1_1_tiles.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-moz_grid3_censusdisaggregatedgridde
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Census disaggregated gridded population estimates for Mozambique (2017), version
  1.1
version: null
vulnerability: null
---
