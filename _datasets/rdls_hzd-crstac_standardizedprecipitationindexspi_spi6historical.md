---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Copernicus Climate Data Store
  url: https://doi.org/10.24381/cds.5292a2b0
creator:
  affiliation: null
  email: null
  name: Copernicus Climate Data Store
  url: https://doi.org/10.24381/cds.5292a2b0
dataset_id: rdls_hzd-crstac_standardizedprecipitationindexspi_spi6historical
description: '6-Month Standardized Precipitation Index 1970-2005 [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: spi:dimensionless
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: This catalogue entry provides gridded data from CMIP6 projections included
    in the IPCC Interactive Atlas, a novel contribution from Working Group I (WGI)
    to the IPCC Sixth Assessment Report (AR6).
  sources:
  - id: source_underlying_1
    license: null
    name: CMIP6
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/IPCC-WG1/Atlas/blob/main/datasets-interactive-atlas/01_index_calculation_SPI.R
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Copernicus Climate Data Store
  url: https://doi.org/10.24381/cds.5292a2b0
purpose: data download via interface or API
referenced_by:
- author_names: null
  date_published: null
  doi: 10.24381/cds.5292a2b0
  id: ref_doi
  name: null
  url: https://doi.org/10.24381/cds.5292a2b0
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/precipitation-related/standardized-precipitation-index-spi/spi6-historical/spi6-historical.json
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
  title: 'STAC Item: Standardized precipitation index (SPI) - SPI6 Historical'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Standardized precipitation index (SPI) - SPI6 Historical - data file
  download_url: https://doi.org/10.24381/cds.5292a2b0
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Standardized precipitation index (SPI) - SPI6 Historical - data file
- access_url: https://github.com/IPCC-WG1/Atlas/blob/main/datasets-interactive-atlas/01_index_calculation_SPI.R
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Standardized precipitation index (SPI) - SPI6 Historical (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_standardizedprecipitationindexspi_spi6historical
spatial:
  bbox:
  - -180.0
  - -60.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 111000
temporal:
  central_year: null
  duration: null
  end: '2014'
  start: '1850'
temporal_resolution: P1M
title: Standardized precipitation index (SPI) - SPI6 Historical
version: null
vulnerability: null
---
