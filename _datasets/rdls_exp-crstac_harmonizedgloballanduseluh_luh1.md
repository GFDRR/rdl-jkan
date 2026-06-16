---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: ORNL DAAC
  url: https://doi.org/10.3334/ORNLDAAC/1248
creator:
  affiliation: null
  email: null
  name: ORNL DAAC
  url: https://doi.org/10.3334/ORNLDAAC/1248
dataset_id: rdls_exp-crstac_harmonizedgloballanduseluh_luh1
description: 'These data represent fractional land use and land cover patterns annually
  for the years 1500 - 2100 for the globe at 0.5-degree (~50-km) spatial resolution.
  Land use categories of cropland, pasture, primary land, secondary (recovering) land,
  and urban land, and underlying annual land-use transitions, are included. Annual
  data on age and biomass density of secondary land, as well as annual wood harvest,
  are included for each grid cell. Climate scenarios (as published): "SSP-RCP combinations"
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: land use/land cover footprints
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC0-1.0.html
lineage:
  description: These data represent fractional land use and land cover patterns annually
    for the years 1500 - 2100 for the globe at 0.5-degree (~50-km) spatial resolution.
    Land use categories of cropland, pasture, primary land, secondary (recovering)
    land, and urban land, and underlying annual land-use transitions, are included.
    Annual data on age and biomass density of secondary land, as well as annual wood
    harvest, are included for each grid cell.
  sources:
  - id: source_underlying_1
    license: null
    name: Several data sources (see publication for further details)
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
  name: ORNL DAAC
  url: https://doi.org/10.3334/ORNLDAAC/1248
purpose: user account needed
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1007/s10584-011-0153-2
  id: ref_doi
  name: null
  url: https://doi.org/10.1007/s10584-011-0153-2
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/harmonized-global-land-use-luh/luh1/luh1.json
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
  title: 'STAC Item: Harmonized Global Land Use (LUH) - LUH1'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Harmonized Global Land Use (LUH) - LUH1 - data file
  download_url: https://doi.org/10.3334/ORNLDAAC/1248
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Harmonized Global Land Use (LUH) - LUH1 - data file
- access_url: https://doi.org/10.1007/s10584-011-0153-2
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Harmonized Global Land Use (LUH) - LUH1 (Web reference)
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
slug: rdls_exp-crstac_harmonizedgloballanduseluh_luh1
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
spatial_resolution: 55500
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '1500'
temporal_resolution: null
title: Harmonized Global Land Use (LUH) - LUH1
version: null
vulnerability: null
---
