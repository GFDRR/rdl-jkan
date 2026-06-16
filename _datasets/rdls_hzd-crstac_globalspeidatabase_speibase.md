---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Spanish National Research Council (CSIC)
  url: https://spei.csic.es/spei_database
creator:
  affiliation: null
  email: null
  name: Spanish National Research Council (CSIC)
  url: https://spei.csic.es/spei_database
dataset_id: rdls_hzd-crstac_globalspeidatabase_speibase
description: 'The SPEIbase is based on the FAO-56 Penman-Monteith estimation of potential
  evapotranspiration. This is a major difference with respect to the SPEI Global Drought
  Monitor, that uses the Thornthwaite PET estimation [Source: This metadata record
  was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
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
license: https://spdx.org/licenses/ODbL-1.0.html
lineage:
  description: The Global SPEI database, SPEIbase, offers long-time, robust information
    about drought conditions at the global scale, with a 0.5 degrees spatial resolution
    and a monthly time resolution. It has a multi-scale character, providing SPEI
    time-scales between 1 and 48 months. It is based on monthly precipitation and
    potential evapotranspiration data from the Climatic Research Unit of the University
    of East Anglia, starting in January 1901, and it is updated as soon as new data
    becomes available.
  sources:
  - id: source_underlying_1
    license: null
    name: NOAA
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
    url: https://doi.org/10.5281/zenodo.834461
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Spanish National Research Council (CSIC)
  url: https://spei.csic.es/spei_database
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1002/joc.3887
  id: ref_doi
  name: null
  url: https://doi.org/10.1002/joc.3887
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/precipitation-related/global-spei-database/speibase/speibase.json
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
  title: 'STAC Item: Global SPEI database - SPEIbase'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global SPEI database - SPEIbase - data file
  download_url: https://digital.csic.es/bitstream/10261/332007/3/spei01.nc
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global SPEI database - SPEIbase - data file
- access_url: https://doi.org/10.1002/joc.3887
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global SPEI database - SPEIbase (Web reference)
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
- access_url: https://doi.org/10.5281/zenodo.834461
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global SPEI database - SPEIbase (Code link)
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
slug: rdls_hzd-crstac_globalspeidatabase_speibase
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
  end: '2022'
  start: '1901'
temporal_resolution: P1M
title: Global SPEI database - SPEIbase
version: null
vulnerability: null
---
