---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Zenodo
  url: https://zenodo.org/doi/10.5281/zenodo.7768533
creator:
  affiliation: null
  email: null
  name: Zenodo
  url: https://zenodo.org/doi/10.5281/zenodo.7768533
dataset_id: rdls_hzd-crstac_dailyevapotranspirationdeficitindexdedi_dedi19792022
description: 'A global daily drought index dataset named as daily evapotranspiration
  deficit index (DEDI) is constructed using daily actual evapotranspiration and potential
  evapotranspiration data provided by European Centre for Medium-Range Weather Forecasts
  Reanalysis v5 (ERA5) [Source: This metadata record was automatically extracted from
  the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
  type: drought
license: CC-BY-4.0
lineage:
  description: A global daily drought index dataset named as daily evapotranspiration
    deficit index (DEDI) is constructed using daily actual evapotranspiration and
    potential evapotranspiration data provided by European Centre for Medium-Range
    Weather Forecasts Reanalysis v5 (ERA5).
  sources:
  - id: source_underlying_1
    license: null
    name: ERA5
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
    url: https://github.com/XiaZhang1113/Daily-drought-index--DEDI
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Zenodo
  url: https://zenodo.org/doi/10.5281/zenodo.7768533
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41597-023-02756-1
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41597-023-02756-1
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/precipitation-related/daily-evapotranspiration-deficit-index-dedi/dedi-1979-2022/dedi-1979-2022.json
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
  title: 'STAC Item: Daily Evapotranspiration Deficit Index (DEDI) - DEDI 1979-2022'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily Evapotranspiration Deficit Index (DEDI) - DEDI 1979-2022 - data
    file
  download_url: https://zenodo.org/doi/10.5281/zenodo.7768533
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily Evapotranspiration Deficit Index (DEDI) - DEDI 1979-2022 - data file
- access_url: https://doi.org/10.1038/s41597-023-02756-1
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily Evapotranspiration Deficit Index (DEDI) - DEDI 1979-2022 (Web
    reference)
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
- access_url: https://github.com/XiaZhang1113/Daily-drought-index--DEDI
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily Evapotranspiration Deficit Index (DEDI) - DEDI 1979-2022 (Code
    link)
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
slug: rdls_hzd-crstac_dailyevapotranspirationdeficitindexdedi_dedi19792022
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
spatial_resolution: 27750
temporal:
  central_year: null
  duration: null
  end: '2022'
  start: '1979'
temporal_resolution: P1D
title: Daily Evapotranspiration Deficit Index (DEDI) - DEDI 1979-2022
version: null
vulnerability: null
---
