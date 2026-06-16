---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Havard Dataverse
  url: https://dataverse.harvard.edu/dataverse/geospatial_human_dimensions_data
creator:
  affiliation: null
  email: null
  name: Havard Dataverse
  url: https://dataverse.harvard.edu/dataverse/geospatial_human_dimensions_data
dataset_id: rdls_exp-crstac_urbanlandprojections_18degreenetcdf
description: 'Urban land projections under the Shared Socioeconomic Pathways (SSPs)
  until 2100 at 1/8 degree resolution and in netcdf format. Climate scenarios (as
  published): "SSPs" [Source: This metadata record was automatically extracted from
  the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: urban/built-up footprints
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: CC0-1.0
lineage:
  description: Urban land projections based on the Shared Socioeconomic Pathways (SSPs)
    developed by Gao Lab
  sources:
  - id: source_underlying_1
    license: null
    name: based on GHSL
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_2
    license: null
    name: population projections from Jones & O'Neill 2016
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_underlying_3
    license: null
    name: and other input data
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
  name: Havard Dataverse
  url: https://dataverse.harvard.edu/dataverse/geospatial_human_dimensions_data
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41467-020-15788-7
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41467-020-15788-7
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/urban-land-projections/18-degree-netcdf/18-degree-netcdf.json
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
  title: 'STAC Item: Urban land projections - 1/8 degree netcdf'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Urban land projections - 1/8 degree netcdf - data file
  download_url: https://dataverse.harvard.edu/file.xhtml?persistentId=doi:10.7910/DVN/ZHMI1L/Q4S9QA&version=1.0
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Urban land projections - 1/8 degree netcdf - data file
- access_url: https://doi.org/10.1038/s41467-020-15788-7
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Urban land projections - 1/8 degree netcdf (Web reference)
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
slug: rdls_exp-crstac_urbanlandprojections_18degreenetcdf
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
spatial_resolution: 13889
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '2010'
temporal_resolution: P10Y
title: Urban land projections - 1/8 degree netcdf
version: null
vulnerability: null
---
