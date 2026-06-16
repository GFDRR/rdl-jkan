---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: NASA
  url: https://doi.org/10.7927/H46M34XX
creator:
  affiliation: null
  email: null
  name: NASA
  url: https://doi.org/10.7927/H46M34XX
dataset_id: rdls_exp-crstac_griddedpopulationoftheworldgpwv4_population30arcminutesascii
description: 'Population count from 2000-2020 in 30 arc minutes resolution in ascii
  format [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: population number
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
  description: The Gridded Population of the World (GPW) collection, now in its fourth
    version (GPWv4), models the distribution of human population (counts and densities)
    on a continuous global raster surface.
  sources:
  - id: source_underlying_1
    license: null
    name: Census and population registers
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: NASA
  url: https://doi.org/10.7927/H46M34XX
purpose: 'free user account needed; GPW is assembled from different census data and
  time steps per country, which align roughly with the year 2010. More details can
  be found in the documentation: https://sedac.ciesin.columbia.edu/binaries/web/sedac/collections/gpw-v4/gpw-v4-documentation-rev11.pdf'
referenced_by:
- author_names: null
  date_published: null
  doi: 10.7927/H4JW8BX5
  id: ref_doi
  name: null
  url: https://doi.org/10.7927/H4JW8BX5
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/gridded-population-of-the-world-gpw-v4/population-30-arc-minutes-ascii/population-30-arc-minutes-ascii.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Gridded Population of the World (GPW v4) - Population 30 arc
    minutes ascii'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Gridded Population of the World (GPW v4) - Population 30 arc minutes
    ascii - data file
  download_url: https://data.earthdata.nasa.gov/nasa-earth/human-dimensions/sedac-root/downloads/data/gpw-v4/gpw-v4-population-count-rev11/gpw-v4-population-count-rev11_2000_30_min_asc.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gridded Population of the World (GPW v4) - Population 30 arc minutes ascii
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Gridded Population of the World (GPW v4) - Population 30 arc minutes
    ascii - data file
  download_url: https://data.earthdata.nasa.gov/nasa-earth/human-dimensions/sedac-root/downloads/data/gpw-v4/gpw-v4-population-count-rev11/gpw-v4-population-count-rev11_2005_30_min_asc.zip
  format: null
  id: resource_data-file_2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gridded Population of the World (GPW v4) - Population 30 arc minutes ascii
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Gridded Population of the World (GPW v4) - Population 30 arc minutes
    ascii - data file
  download_url: https://data.earthdata.nasa.gov/nasa-earth/human-dimensions/sedac-root/downloads/data/gpw-v4/gpw-v4-population-count-rev11/gpw-v4-population-count-rev11_2010_30_min_asc.zip
  format: null
  id: resource_data-file_3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gridded Population of the World (GPW v4) - Population 30 arc minutes ascii
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Gridded Population of the World (GPW v4) - Population 30 arc minutes
    ascii - data file
  download_url: https://data.earthdata.nasa.gov/nasa-earth/human-dimensions/sedac-root/downloads/data/gpw-v4/gpw-v4-population-count-rev11/gpw-v4-population-count-rev11_2015_30_min_asc.zip
  format: null
  id: resource_data-file_4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gridded Population of the World (GPW v4) - Population 30 arc minutes ascii
    - data file
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Gridded Population of the World (GPW v4) - Population 30 arc minutes
    ascii - data file
  download_url: https://data.earthdata.nasa.gov/nasa-earth/human-dimensions/sedac-root/downloads/data/gpw-v4/gpw-v4-population-count-rev11/gpw-v4-population-count-rev11_2020_30_min_asc.zip
  format: null
  id: resource_data-file_5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gridded Population of the World (GPW v4) - Population 30 arc minutes ascii
    - data file
- access_url: https://doi.org/10.7927/H4JW8BX5
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded Population of the World (GPW v4) - Population 30 arc minutes
    ascii (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_griddedpopulationoftheworldgpwv4_population30arcminutesascii
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 55556
temporal:
  central_year: null
  duration: null
  end: '2020'
  start: '2000'
temporal_resolution: P5Y
title: Gridded Population of the World (GPW v4) - Population 30 arc minutes ascii
version: null
vulnerability: null
---
