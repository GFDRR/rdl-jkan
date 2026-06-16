---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-guyana-age-and-gender-structures
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-guyana-age-and-gender-structures
dataset_id: rdls_exp-guy_worldpop_agegenderstructures_2019
description: 'Age and gender structures: WorldPop produces different types of gridded
  population count datasets, depending on the methods used and end application. An
  overview of the data can be found in Tatem et al , and a description of the modelling
  methods used found in Tatem et al and Pezzulo et al . The '' Global per country
  2000-2020 '' datasets represent the outputs from a project focused on construction
  of consistent 100m resolution population count datasets for all countries of the
  World for each year 2000-2020 structured by male/female and 5-year age classes (plus
  a <1 year class). These efforts necessarily involved some shortcuts for consistency.
  The '' individual countries '' datasets represent older efforts to map population
  age and gender counts for each country separately, using a set of tailored geospatial
  inputs and differing methods and time periods. The '' whole continent '' datasets
  are mosaics of the individual countries datasets. WorldPop (www.worldpop.org - School
  of Geography and Environmental Science, University of Southampton; Department of
  Geography and Geosciences, University of Louisville; Departement de Geographie,
  Universite de Namur) and Center for International Earth Science Information Network
  (CIESIN), Columbia University (2018). Global High Resolution Population Denominators
  Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-guyana-age-and-gender-structures]'
details: null
exposure:
- asset_type:
    description: Gridded population counts of women of child-bearing age (15-49 years)
      at approximately 1 km resolution for Guyana in 2015
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: WorldPop applied spatial modeling methods (Pezzulo et al.) to census
    and geospatial data to estimate the distribution of women of child-bearing age
    (15-49 years) across Guyana at 1 km grid resolution for 2015, producing a GeoTIFF
    raster dataset.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-guyana-age-and-gender-structures
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
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guyana - Age and gender structures (Women of child bearing age (15-49
    years old) in 2015 , Guyana)
  download_url: ftp://ftp.worldpop.org.uk/GIS/AgeSex_structures/Women_of_child_bearing_age/15_49_years_old/2015/GUY/guy_f_15_49_2015_1km.tif
  format: null
  id: resource_e56e30f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_f_15_49_2015_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-guy_worldpop_agegenderstructures_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - GUY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: Guyana - Age and gender structures
version: null
vulnerability: null
---
